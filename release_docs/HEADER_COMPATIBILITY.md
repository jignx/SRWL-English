# v1.0.1 source headers and patch

v1.0.1 ships **one patch** for both supported clean dumps: `SRWL_English_v1.0.1.xdelta`.

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
| Patched size | 128,485,436 bytes |
| Patched SHA-256 | `648b7b6c918e10cc62e6dc7fbe690b71bb24d011acc2b18d4f6e7177fa4e9031` |
| Patched CRC32 | `EF8329B6` |

The patch was reapplied to both supported clean dumps; both outputs match the release hash.

Patch values:

| Property | Value |
| --- | --- |
| Patch | `SRWL_English_v1.0.1.xdelta` |
| Size | 7,043,158 bytes |
| SHA-256 | `61aaa5880eec76c25086888da95236180b2291de2ec0b6a5981859f45327284e` |
| CRC32 | `C86F802B` |

Because the patch has no whole-file source checksum, **check the patched output hash** against
`CHECKSUMS.txt` after applying it. If a patcher offers an option to ignore checksum errors, do not
use it. If a mismatch appears on a dump whose SHA-256 is one of the two above, redownload the patch
and re-check both hashes.
