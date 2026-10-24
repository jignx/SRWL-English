"""Create and verify an xdelta patch using user-supplied ROM paths.

Requires xdelta3 on PATH (or pass --xdelta PATH).
Usage: python make_patch.py clean-source.nds built.nds release.xdelta
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


def digest(path):
    hasher = hashlib.sha256()
    crc = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
            crc = zlib.crc32(chunk, crc)
    return hasher.hexdigest(), f"{crc & 0xffffffff:08X}"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="legally dumped clean Japanese ROM")
    parser.add_argument("built", type=Path, help="translated ROM built separately")
    parser.add_argument("output", type=Path, help="new .xdelta output file")
    parser.add_argument("--xdelta", default="xdelta3", help="xdelta3 executable")
    parser.add_argument("--checksums", type=Path, help="new checksum manifest for source, patch and output")
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
            raise ValueError("Source ROM does not match the supported clean dump.")
        if digest(source)[0] == digest(built)[0]:
            raise ValueError("Built ROM is identical to the source.")
        executable = shutil.which(args.xdelta)
        if not executable:
            raise ValueError("xdelta3 was not found; install it or pass --xdelta.")
        if args.checksums and args.checksums.exists():
            raise ValueError("Checksum manifest already exists.")
        with tempfile.TemporaryDirectory(prefix="srwl_patch_") as folder:
            patch = Path(folder) / "release.xdelta"
            clean_copy = Path(folder) / "clean.nds"
            shutil.copyfile(source, clean_copy)
            assert digest(clean_copy) == digest(source)
            alternate = Path(folder) / "zeroed-header.nds"
            raw = bytearray(source.read_bytes())
            for start, end in EXTENDED_METADATA:
                raw[start:end] = bytes(end - start)
            alternate.write_bytes(raw)
            if digest(alternate)[0] != ALTERNATE_SHA256:
                raise ValueError("Known alternate-header source guard failed.")
            # Encode without relying on either dump's header metadata.
            encoding_source = Path(folder) / "encoding-source.nds"
            raw[:4096] = bytes([0xa5]) * 4096
            encoding_source.write_bytes(raw)
            source_entries = []
            for label, path in (("Clean Japanese ROM", clean_copy),
                                ("Japanese ROM with zeroed extended-header metadata", alternate)):
                sha, crc = digest(path)
                source_entries.append((label + " (not distributed)", path.name, path.stat().st_size, sha, crc))
            help_text = subprocess.run([executable, "-h"], capture_output=True, text=True).stdout
            help_text += subprocess.run([executable, "-h"], capture_output=True, text=True).stderr
            # xdelta 3.2 defaults to armor. Disable it for legacy VCDIFF patchers.
            legacy = ["-a"] if "disable armor" in help_text else []
            subprocess.run([executable, *legacy, "-A", "-S", args.secondary, "-9", "-e", "-s",
                            str(encoding_source), str(built), str(patch)], check=True)
            if patch.read_bytes()[:4] != b"\xd6\xc3\xc4\0":
                raise ValueError("Output is not a standard VCDIFF patch.")
            for index, candidate in enumerate((clean_copy, alternate)):
                verified = Path(folder) / f"verified-{index}.nds"
                subprocess.run([executable, "-d", "-s", str(candidate), str(patch), str(verified)], check=True)
                if verified.stat().st_size != built.stat().st_size or digest(verified) != digest(built):
                    raise ValueError("Patch verification failed for a supported source header.")
            # Exclusive creation prevents overwriting an existing release.
            with output.open("xb") as destination, patch.open("rb") as stream:
                shutil.copyfileobj(stream, destination)
        if args.checksums:
            lines = ["Super Robot Taisen L English v0.9 -- header compatibility update", "", "Patch reapplication: PASS for both supported source headers; output unchanged", ""]
            entries = list(source_entries)
            for label, name, path in (("Translation patch", output.name, output),
                                      ("Patched ROM (not distributed)", "SRWL_English_v0.9.nds", built)):
                sha, crc = digest(path)
                entries.append((label, name, path.stat().st_size, sha, crc))
            for label, name, size, sha, crc in entries:
                lines.extend([label + ": " + name, "Size: " + str(size) + " bytes",
                              "SHA-256: " + sha, "CRC32: " + crc, ""])
            args.checksums.write_text("\n".join(lines), encoding="utf8", newline="\n")
        print("Patch created and verified against both supported source headers.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
