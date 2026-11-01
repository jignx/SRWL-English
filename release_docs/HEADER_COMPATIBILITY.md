# v1.0 source headers and patch

v1.0 ships **one patch** for both supported clean dumps: `SRWL_English_v1.0.xdelta`.

| Source dump | Size | SHA-256 | CRC32 |
| --- | --- | --- | --- |
| Canonical Japanese revision-0 | 134217728 | `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f` | `1D040BE8` |
| Zeroed extended-header metadata | 134217728 | `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f` | `82804748` |

Only 188 bytes differ between the two dumps: offsets `0x33C`-`0x34F`, `0x378`-`0x39F` and
`0xF80`-`0xFFF`. The normal DS header, secure area, executable and all game data after the first
4 KiB are identical, so one patch can serve both.

## How the single patch works

The encoding reference is the canonical dump with those **188 differing bytes filled with unique
junk** (a value that matches neither dump and not the release ROM). xdelta therefore cannot copy
those regions from the source and writes the target bytes as literals in the patch. The source
window (`-B`) is large enough to cover the whole ROM.

That construction means neither source header is embedded in the patch, so it applies to both. A
single file cannot also carry xdelta3's whole-file source checksum (that identifies exactly one
source file), so whole-file source verification (armor) is off. VCDIFF **target-window checksums
stay on**, and validation must stay enabled: a corrupted or different source is normally caught
with `target window checksum mismatch` rather than producing a broken ROM.

During release verification the finished patch was applied to a fresh copy of **both** real dumps
and each produced exactly:

| Property | Value |
| --- | --- |
| Patched size | 128,484,412 bytes |
| Patched SHA-256 | `f183ea1562c794e0ac5e39eda0c5fe335f0ed81e20596b15511d55e55a0d2643` |
| Patched CRC32 | `9C705A37` |

The patch was reapplied to both supported clean dumps; both outputs match the release hash.

Patch values:

| Property | Value |
| --- | --- |
| Patch | `SRWL_English_v1.0.xdelta` |
| Size | 7,054,495 bytes |
| SHA-256 | `45612d2a4fef472b5d3bc85de91e95bdb2abc4e727f1cada7ee3088e0c0ced98` |
| CRC32 | `3263A740` |

Because the patch has no whole-file source checksum, **check the patched output hash** against
`CHECKSUMS.txt` after applying it. If a patcher offers an option to ignore checksum errors, do not
use it. If a mismatch appears on a dump whose SHA-256 is one of the two above, redownload the patch
and re-check both hashes.
