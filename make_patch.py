"""Create and verify the Super Robot Wars L English v0.92.1 xdelta patch.

v0.92.1 uses one patch for both supported clean dump variants. The 188 bytes that
differ between the canonical dump and the zeroed-extended-header dump are replaced
with deterministic junk in the encoding reference, so xdelta cannot copy those
regions and emits the target bytes as literals there. Whole-file source
verification (armor) is off; VCDIFF target-window checksums stay on; -B is set
large enough to cover the whole ROM. The finished patch is then applied to fresh
copies of both real dumps and each output is checked against the release ROM.

Requires xdelta3 on PATH (or pass --xdelta PATH).

Usage:
    python make_patch.py clean-source.nds SRWL_English_v0.92.1.nds SRWL_English_v0.92.1.xdelta
"""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
import zlib

SOURCE_SIZE = 134217728
SOURCE_SHA256 = "a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f"
ALTERNATE_SHA256 = "1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f"
EXTENDED_METADATA = ((0x33c, 0x350), (0x378, 0x3a0), (0xf80, 0x1000))
RELEASE_SIZE = 128499260
RELEASE_SHA256 = "35cdc6aab4b7dc82885a845712c250590f4a533f7ed7f2ddba6352490547fbbe"
RELEASE_CRC32 = "0396A124"
SOURCE_WINDOW = 268435456


def digest(path):
    hasher = hashlib.sha256()
    crc = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
            crc = zlib.crc32(chunk, crc)
    return hasher.hexdigest(), f"{crc & 0xffffffff:08X}"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path, help="legally dumped clean Japanese ROM (canonical header)")
    parser.add_argument("built", type=Path, help="the released English ROM (SRWL_English_v0.92.1.nds)")
    parser.add_argument("output", type=Path, help="new .xdelta output file")
    parser.add_argument("--xdelta", default="xdelta3", help="xdelta3 executable")
    parser.add_argument("--checksums", type=Path, help="new v0.92.1 checksum manifest")
    parser.add_argument("--secondary", choices=("none", "djw", "lzma"), default="lzma",
                        help="standard xdelta secondary compression (default: lzma)")
    args = parser.parse_args(argv)
    source, built, output = (p.resolve() for p in (args.source, args.built, args.output))
    try:
        if not source.is_file() or not built.is_file():
            raise ValueError("Both input ROM files must exist.")
        if source == built or output in (source, built):
            raise ValueError("Source, built ROM and output must be different files.")
        if output.suffix.lower() != ".xdelta" or output.exists():
            raise ValueError("Output must be a new .xdelta file.")
        if not output.parent.is_dir():
            raise ValueError("Output directory must already exist.")
        if source.stat().st_size != SOURCE_SIZE or digest(source)[0] != SOURCE_SHA256:
            raise ValueError("Source ROM is not the supported canonical clean dump.")
        if (built.stat().st_size, digest(built)[0]) != (RELEASE_SIZE, RELEASE_SHA256):
            raise ValueError("Built ROM is not the v0.92.1 release ROM (size/SHA-256 mismatch).")
        executable = shutil.which(args.xdelta)
        if not executable:
            raise ValueError("xdelta3 was not found; install it or pass --xdelta.")
        if args.checksums and args.checksums.exists():
            raise ValueError("Checksum manifest already exists.")
        help_text = subprocess.run([executable, "-h"], capture_output=True, text=True).stdout
        help_text += subprocess.run([executable, "-h"], capture_output=True, text=True).stderr
        # xdelta 3.2 defaults to armor. Disable it: one patch must work for both
        # headers, so the whole-file source checksum cannot be used. Target-window
        # checksums stay enabled (no -n). -A keeps the patch friendly to legacy
        # VCDIFF patchers and -B covers the whole ROM in one source window.
        legacy = ["-a"] if "disable armor" in help_text else []
        with tempfile.TemporaryDirectory(prefix="srwl_patch_") as folder:
            folder = Path(folder)
            patch = folder / "release.xdelta"
            clean = bytearray(source.read_bytes())
            built_raw = built.read_bytes()
            clean_copy = folder / "clean.nds"
            clean_copy.write_bytes(clean)
            alternate = folder / "zeroed-header.nds"
            alt = bytearray(clean)
            for start, end in EXTENDED_METADATA:
                alt[start:end] = bytes(end - start)
            alternate.write_bytes(alt)
            if digest(alternate)[0] != ALTERNATE_SHA256:
                raise ValueError("Known alternate-header source guard failed.")
            # Replace every differing header byte with junk that matches neither
            # supported dump nor the release ROM, so those regions become literals.
            encoding = bytearray(clean)
            for start, end in EXTENDED_METADATA:
                for i in range(start, end):
                    for k in range(1, 256):
                        value = (clean[i] + k) & 0xFF
                        if value not in (clean[i], alt[i], built_raw[i]):
                            encoding[i] = value
                            break
                    else:
                        raise ValueError(f"No safe junk byte for header offset {i:#x}.")
            encoding_source = folder / "encoding-source.nds"
            encoding_source.write_bytes(encoding)
            subprocess.run([executable, *legacy, "-A", "-B", str(SOURCE_WINDOW),
                            "-S", args.secondary, "-9", "-e", "-s",
                            str(encoding_source), str(built), str(patch)], check=True)
            if patch.read_bytes()[:4] != b"\xd6\xc3\xc4\0":
                raise ValueError("Output is not a standard VCDIFF patch.")
            for index, candidate in enumerate((clean_copy, alternate)):
                verified = folder / f"verified-{index}.nds"
                subprocess.run([executable, "-d", "-s", str(candidate), str(patch), str(verified)], check=True)
                if (verified.stat().st_size, digest(verified)[0]) != (RELEASE_SIZE, RELEASE_SHA256):
                    raise ValueError("Patch verification failed for a supported source header.")
            with output.open("xb") as destination, patch.open("rb") as stream:
                shutil.copyfileobj(stream, destination)
            patch_sha, patch_crc = digest(output)
            patch_size = output.stat().st_size
        if args.checksums:
            lines = [
                "Super Robot Wars L English v0.92.1", "",
                "One patch for both supported source headers (header-neutral encoding).",
                "Patch reapplication: PASS on both dumps; identical output hash below.", "",
            ]
            for label, name, sha, crc in (
                    ("Clean Japanese ROM (canonical header, not distributed)", "clean.nds",
                     SOURCE_SHA256, "1D040BE8"),
                    ("Japanese ROM with zeroed extended-header metadata (not distributed)",
                     "zeroed-header.nds", ALTERNATE_SHA256, "82804748")):
                lines.extend([label + ": " + name, "Size: " + str(SOURCE_SIZE) + " bytes",
                              "SHA-256: " + sha, "CRC32: " + crc, ""])
            lines.extend(["Translation patch: " + output.name,
                          "Size: " + str(patch_size) + " bytes",
                          "SHA-256: " + patch_sha, "CRC32: " + patch_crc, ""])
            lines.extend(["Patched ROM (not distributed): SRWL_English_v0.92.1.nds",
                          "Size: " + str(RELEASE_SIZE) + " bytes",
                          "SHA-256: " + RELEASE_SHA256, "CRC32: " + RELEASE_CRC32, ""])
            args.checksums.write_text("\n".join(lines), encoding="utf8", newline="\n")
        print(f"Patch created and verified against both supported headers: "
              f"size {patch_size}, SHA-256 {patch_sha}, CRC32 {patch_crc}.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
