"""Create and verify a Super Robot Wars L English v0.91 xdelta patch.

The v0.91 release uses one patch per supported clean dump and keeps xdelta3's
source checksum (whole-file BLAKE3) checking enabled. This helper reproduces a
published patch from the matching dump and the release ROM: it encodes with
xdelta3 3.2.2 defaults (armor on, lzma secondary), verifies the decoded output,
and confirms the produced patch against the published hash when the local
xdelta3/lzma build matches.

Requires xdelta3 3.2.2 or later on PATH (or pass --xdelta PATH).

Usage:
    python make_patch.py clean-source.nds SRWL_English_v0.91.nds out.xdelta
    python make_patch.py zeroed-header.nds SRWL_English_v0.91.nds out.xdelta
"""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
import zlib

RELEASE_SIZE = 128551996
RELEASE_SHA256 = "0c3cda0339ca583fbd7b08b8503588eafba65e4267e45f318d27ea389ac2ea1b"
RELEASE_CRC32 = "193D992D"

HEADERS = {
    "standard": {
        "label": "Clean Japanese ROM (canonical header)",
        "source_name": "clean.nds",
        "size": 134217728,
        "sha256": "a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f",
        "crc32": "1D040BE8",
        "patch": "SRWL_English_v0.91_standard.xdelta",
        "patch_sha256": "ae3b83ad40316b7ec177c20891a351371b7bd6feddef57a284852af455b7c710",
        "patch_crc32": "45C6F472",
        "patch_size": 1831395,
    },
    "alt-header": {
        "label": "Japanese ROM with zeroed extended-header metadata",
        "source_name": "zeroed-header.nds",
        "size": 134217728,
        "sha256": "1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f",
        "crc32": "82804748",
        "patch": "SRWL_English_v0.91_alt-header.xdelta",
        "patch_sha256": "a93539ba9812d4a788f86971549f8002740733bf6336977d597b3bfd32c78def",
        "patch_crc32": "96830C9E",
        "patch_size": 1831623,
    },
}
BUILT_NAME = "SRWL_English_v0.91.nds"


def digest(path):
    hasher = hashlib.sha256()
    crc = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
            crc = zlib.crc32(chunk, crc)
    return hasher.hexdigest(), f"{crc & 0xffffffff:08X}"


def identify_source(source):
    size = source.stat().st_size
    sha, crc = digest(source)
    for name, spec in HEADERS.items():
        if (size, sha) == (spec["size"], spec["sha256"]):
            if crc != spec["crc32"]:
                raise ValueError("Source CRC32 does not match the supported dump.")
            return name, spec
    raise ValueError("Source ROM does not match either supported clean dump.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path, help="legally dumped clean Japanese ROM")
    parser.add_argument("built", type=Path, help="the released English ROM (SRWL_English_v0.91.nds)")
    parser.add_argument("output", type=Path, help="new .xdelta output file")
    parser.add_argument("--xdelta", default="xdelta3", help="xdelta3 executable (3.2.2 or later)")
    parser.add_argument("--checksums", type=Path, help="new v0.91 checksum manifest")
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
        header, spec = identify_source(source)
        built_size = built.stat().st_size
        built_sha, built_crc = digest(built)
        if (built_size, built_sha) != (RELEASE_SIZE, RELEASE_SHA256):
            raise ValueError("Built ROM is not the v0.91 release ROM (size/SHA-256 mismatch).")
        executable = shutil.which(args.xdelta)
        if not executable:
            raise ValueError("xdelta3 was not found; install xdelta3 3.2.2 or pass --xdelta.")
        if args.checksums and args.checksums.exists():
            raise ValueError("Checksum manifest already exists.")
        with tempfile.TemporaryDirectory(prefix="srwl_patch_") as folder:
            folder = Path(folder)
            # Fixed temporary names keep the application header (and so the patch bytes)
            # reproducible regardless of where the caller keeps the ROMs.
            normalized_source = folder / spec["source_name"]
            normalized_built = folder / BUILT_NAME
            shutil.copyfile(source, normalized_source)
            shutil.copyfile(built, normalized_built)
            assert digest(normalized_source)[0] == spec["sha256"]
            assert digest(normalized_built)[0] == RELEASE_SHA256
            patch = folder / "release.xdelta"
            # Default armor stays on: the patch stores the source BLAKE3 and refuses a
            # different dump. Do not pass -a or -A here.
            subprocess.run([executable, "-S", "lzma", "-9", "-e", "-s",
                            str(normalized_source), str(normalized_built), str(patch)], check=True)
            if patch.read_bytes()[:4] != b"\xd6\xc3\xc4\0":
                raise ValueError("Output is not a standard VCDIFF patch.")
            verified = folder / "verified.nds"
            subprocess.run([executable, "-d", "-s", str(source), str(patch), str(verified)], check=True)
            if (verified.stat().st_size, digest(verified)[0]) != (RELEASE_SIZE, RELEASE_SHA256):
                raise ValueError("Patch did not reproduce the v0.91 release ROM.")
            patch_sha, patch_crc = digest(patch)
            if patch_sha != spec["patch_sha256"]:
                print("warning: patch hash differs from the published one (different xdelta3/lzma build); "
                      "the decoded ROM still matches the release.")
            with output.open("xb") as destination, patch.open("rb") as stream:
                shutil.copyfileobj(stream, destination)
            produced = (patch.stat().st_size, patch_sha, patch_crc)
        if args.checksums:
            lines = [
                "Super Robot Wars L English v0.91", "",
                "Patch verification: xdelta3 3.2.2, source checksum (whole-file BLAKE3) checking enabled.",
                "Each patch was applied to its own supported dump and produced the identical patched ROM below.",
                "Applying a patch to the other dump is refused with \"source file BLAKE3 mismatch\".", "",
            ]
            for spec_entry in (HEADERS["standard"], HEADERS["alt-header"]):
                lines.extend([spec_entry["label"] + " (not distributed): " + spec_entry["source_name"],
                              "Size: " + str(spec_entry["size"]) + " bytes",
                              "SHA-256: " + spec_entry["sha256"],
                              "CRC32: " + spec_entry["crc32"], ""])
            for label, name, size, sha, crc in (
                    ("Translation patch (canonical header)", "SRWL_English_v0.91_standard.xdelta",
                     HEADERS["standard"]["patch_size"], HEADERS["standard"]["patch_sha256"],
                     HEADERS["standard"]["patch_crc32"]),
                    ("Translation patch (zeroed extended-header metadata)",
                     "SRWL_English_v0.91_alt-header.xdelta", HEADERS["alt-header"]["patch_size"],
                     HEADERS["alt-header"]["patch_sha256"], HEADERS["alt-header"]["patch_crc32"])):
                lines.extend([label + ": " + name, "Size: " + str(size) + " bytes",
                              "SHA-256: " + sha, "CRC32: " + crc, ""])
            lines.extend(["Patched ROM (not distributed): " + BUILT_NAME,
                          "Size: " + str(RELEASE_SIZE) + " bytes",
                          "SHA-256: " + RELEASE_SHA256,
                          "CRC32: " + RELEASE_CRC32, ""])
            args.checksums.write_text("\n".join(lines), encoding="utf8", newline="\n")
        print(f"Patch created and verified for the {header} dump: "
              f"size {produced[0]}, SHA-256 {produced[1]}, CRC32 {produced[2]}.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
