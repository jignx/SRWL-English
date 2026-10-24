"""Write a plain CHECKSUMS.txt for a base ROM and its patched build.

Usage:
    python tools/make_release_checksums.py rom/game.nds releases/v309/game_en.nds
    python tools/make_release_checksums.py rom/game.nds build/game_en.nds \
        --build-name "SRW L English v309" --out dist/CHECKSUMS.txt

The output records the build name, then size, MD5 and SHA-1 for both files.
Hashes are streamed, so this works on multi-hundred-megabyte ROMs.
"""
import argparse
import hashlib
import pathlib
import sys

CHUNK = 1024 * 1024


def digest(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as handle:
        while True:
            block = handle.read(CHUNK)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def build_checksums(base, patched, out=None, build_name=None):
    """Write the checksum manifest and return its path.

    `out` may be a directory (CHECKSUMS.txt is created inside it) or a file path.
    The build name defaults to the patched ROM's stem.
    """
    base = pathlib.Path(base)
    patched = pathlib.Path(patched)
    for label, path in (("base ROM", base), ("patched ROM", patched)):
        if not path.is_file():
            raise FileNotFoundError(f"{label} is not a file: {path}")
    if build_name is None:
        build_name = patched.stem
    if out is None:
        out = patched.parent / "CHECKSUMS.txt"
    else:
        out = pathlib.Path(out)
        if out.is_dir():
            out = out / "CHECKSUMS.txt"

    lines = [f"Build: {build_name}", ""]
    for label, path in (("Base", base), ("Patched", patched)):
        lines.extend([
            f"{label} ROM: {path.name}",
            f"{label} size: {path.stat().st_size} bytes",
            f"{label} MD5: {digest(path, 'md5')}",
            f"{label} SHA-1: {digest(path, 'sha1')}",
            "",
        ])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("base", help="original, unpatched ROM")
    parser.add_argument("patched", help="patched build")
    parser.add_argument("--build-name", help="name recorded in the manifest (default: patched ROM stem)")
    parser.add_argument("--out", help="output file or directory (default: CHECKSUMS.txt beside the patched ROM)")
    args = parser.parse_args(argv)
    try:
        out = build_checksums(args.base, args.patched, args.out, args.build_name)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
