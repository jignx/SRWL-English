## v1.0 — Battle art and crash fix
**Super Robot Wars L English reaches v1.0.** This update redraws the battle pop-ups in English and fixes a battle crash caused by long weapon names.

**What's new:**
- **Redrawn battle pop-up art.** Critical hits, Support Attack and Support Defense badges and banners, map battle results and the common battle labels now use clean English artwork that matches the original style and colours.
- **Battle crash fixed.** The game could crash when Daiku-Maryu used Zolmanium Piercing Shell, because the English name was too long for the battle screen. This crash is fixed, and other long weapon, unit and pilot names on battle screens are now protected the same way: they are shortened safely instead of overflowing. The names themselves are unchanged in the game text.
- **One patch for both dumps.** `SRWL_English_v1.0.xdelta` works on both known clean Japanese dumps and gives the same English ROM.

Everything from v0.91, v0.92 and the v0.92.1 hotfix is included: anti-piracy disabled, the help-text font fix, corrected unit names, English ending credits, JIT/dynarec support on melonDS Android and WatermelonDS, the smaller 128.5 MB ROM and all earlier text and menu fixes.

**How to patch:**
1. Get your own clean Japanese dump of Super Robot Taisen L (134,217,728 bytes). Its SHA-256 should match one of the two hashes below.
2. Download `SRWL_English_v1.0.xdelta` from this release.
3. Apply it to a copy of your dump with Delta Patcher or xdelta3, keeping checksum validation on:
   `xdelta3 -d -s clean-jp.nds SRWL_English_v1.0.xdelta SRWL_English_v1.0.nds`
4. Check that the patched ROM is 128,484,412 bytes with the SHA-256 below.
5. Back up your save and cold boot the game. Old save states won't work, but normal in-game saves carry over.

**Known issues:**
- The weapon Type line shows an extra comma for combination attacks and a few other types, for example `CQB, Combo,`. It's cosmetic only and will be fixed in the next update.
- Very long weapon, unit and pilot names are cut short on battle screens. This is on purpose and is what prevents the crash.
- The game hasn't been played start to finish on every route yet, so some late-game lines, rare menus or long names may still overflow.
- Tested mainly in DeSmuME. Real DS/3DS hardware hasn't been fully checked.

**Found a bug?** Please [open an issue](https://github.com/jignx/SRWL-English/issues) and include the patch version, your emulator or hardware, where it happened (stage, menu or battle), the steps to make it happen again and a screenshot of both screens. A normal in-game save near the problem helps a lot. See [PLAYTESTING.md](https://github.com/jignx/SRWL-English/blob/main/release_docs/PLAYTESTING.md) for the full checklist. Please don't upload ROMs.

### Verification

- Canonical source SHA-256: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- Alternate-header source SHA-256: `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f`
- Patch SHA-256: `45612d2a4fef472b5d3bc85de91e95bdb2abc4e727f1cada7ee3088e0c0ced98`
- Patched output SHA-256 (both sources): `f183ea1562c794e0ac5e39eda0c5fe335f0ed81e20596b15511d55e55a0d2643`

Only the translation patch and checksums are attached. Supply your own clean Japanese dump.
