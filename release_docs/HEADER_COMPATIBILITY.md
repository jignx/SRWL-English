# v0.9 source-header compatibility correction

The first v0.9 patch assumed one exact extended ROM header. A second dump has identical game data but zeroes three extended-header regions. Applying the original patch to that dump produced `target window checksum mismatch`, including error `-17712` in the published xdelta-wasm web patcher.

The updated **SRWL_English_v0.9.xdelta** accepts both known source hashes. Redownload the patch and its matching checksum attachment together. Checksum validation stays enabled; do not bypass the error on the old patch.

| Source | Size | SHA-256 | CRC32 |
| --- | --- | --- | --- |
| Canonical header | 134217728 | a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f | 1D040BE8 |
| Zeroed extended-header regions | 134217728 | 1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f | 82804748 |

Only 188 bytes differ: offsets 0x33C--0x34F, 0x378--0x39F and 0xF80--0xFFF. The normal DS header, secure area, executable and all game data after the first 4 KiB are identical.

The patch generator now avoids depending on the source's first 4 KiB. Its private encoding reference uses a distinct first page; it then applies the finished patch independently to fresh copies of both real supported headers and checks the complete output. That temporary reference is not distributed or required for applying the patch.

## Regression verification

| Decoder | Canonical source | Alternate source | Checksums |
| --- | --- | --- | --- |
| Native xdelta 3.2.2 | PASS | PASS | enabled |
| Published xdelta-wasm web decoder | PASS | PASS | enabled |

The old patch reproduces the reported `-17712` failure on the alternate source in the web decoder. The updated generator reproduces the independently tested compatibility patch exactly.

The independent decoder check is reproducible with `tools/verify_web_patch.mjs` and the upstream [xdelta-wasm](https://github.com/kotcrab/xdelta-wasm) decoder. Supply its JavaScript/WASM files, your source ROM, the patch and the expected output SHA-256. The helper keeps checksum validation enabled and hashes the streamed output; no decoder binaries or ROMs are bundled.

Updated patch SHA-256: `e68811e68b23aff42bb66eadf8ac9fc2cb82b6c7c58bb3e881eb0be09b4e98d3`.

Both inputs produce the unchanged approved English ROM, 234292908 bytes:

- SHA-256: `8caaa39d45c18d532a2b5cb0115bb3dbc0f8487d6fa1d4fca22493b3fab762b2`
- CRC32: `0F0E3042`

This correction changes patch packaging and source compatibility only. Translation, graphics, game code and saves are unchanged. No ROM or standalone game assets are distributed.
