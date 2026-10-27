# v0.92.1 source headers and patch

v0.92.1 ships **one patch** for both supported clean dumps: `SRWL_English_v0.92.1.xdelta`.

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
| Patched size | 128,499,260 bytes |
| Patched SHA-256 | `35cdc6aab4b7dc82885a845712c250590f4a533f7ed7f2ddba6352490547fbbe` |
| Patched CRC32 | `0396A124` |

The patch was reapplied to both supported clean dumps; both outputs match the release hash.

Patch values:

| Property | Value |
| --- | --- |
| Patch | `SRWL_English_v0.92.1.xdelta` |
| Size | 7,010,029 bytes |
| SHA-256 | `ec5a63b215a9e483ee74e7320b2993d8d32e5f69d30f884b89e5824cabcf75a4` |
| CRC32 | `594A8171` |

Because the patch has no whole-file source checksum, **check the patched output hash** against
`CHECKSUMS.txt` after applying it. If a patcher offers an option to ignore checksum errors, do not
use it. If a mismatch appears on a dump whose SHA-256 is one of the two above, redownload the patch
and re-check both hashes.
