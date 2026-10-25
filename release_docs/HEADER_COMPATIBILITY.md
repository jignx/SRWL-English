# v0.91 source headers and patches

v0.91 ships **two header-specific patches**. They are not interchangeable with the single v0.9
patch, and the v0.9 patch reproduces the old 234 MB build, not this one.

| Source dump | Size | SHA-256 | CRC32 | Use this patch |
| --- | --- | --- | --- | --- |
| Canonical Japanese revision-0 | 134217728 | `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f` | `1D040BE8` | `SRWL_English_v0.91_standard.xdelta` |
| Zeroed extended-header metadata | 134217728 | `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f` | `82804748` | `SRWL_English_v0.91_alt-header.xdelta` |

Only 188 bytes differ between the two dumps: offsets `0x33C`-`0x34F`, `0x378`-`0x39F` and
`0xF80`-`0xFFF`. The normal DS header, secure area, executable and all game data after the first
4 KiB are identical.

Both patches were created with xdelta3 3.2.2 and its default **source checksum** (whole-file
BLAKE3) checking enabled. Each patch stores the hash of the exact dump it was built from, so:

- applied to its own dump, it produces the same English ROM and verifies cleanly;
- applied to the other dump, it is **refused** with `source file BLAKE3 mismatch` instead of
  producing a wrong or broken image. Do not disable checksum validation to force it through.

Verify the output against `CHECKSUMS.txt`:

| Property | Value |
| --- | --- |
| Patched size | 128,551,996 bytes |
| Patched SHA-256 | `0c3cda0339ca583fbd7b08b8503588eafba65e4267e45f318d27ea389ac2ea1b` |
| Patched CRC32 | `193D992D` |

The 200-byte-range differences above mean the v0.9 "one patch for both headers" technique is no
longer used: with source checking on, a header-agnostic patch would have to hide the source hash,
which defeats the check. Pick the patch that matches your dump.

Apply with xdelta3 3.2.2 or later (or a patcher that supports the xdelta3 3.2 source checksum).
Older decoders that predate that checksum may reject the patch's application header; update the
patcher rather than turning checksum validation off.
