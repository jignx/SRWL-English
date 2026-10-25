# Changelog

## v0.91 -- 2026-10-25

- **JIT/dynarec on now works.** The engine's five ARMv6K `nop` hints (`0xE320F000`, which the ARM9 decodes as an MSR) were replaced with the ARMv5 `mov r0, r0`, and the assembler now rejects the hint encoding. The prologue-intro freeze on melonDS Android and WatermelonDS is fixed; no emulator setting needs to be disabled. This supersedes the v0.9 JIT-off workaround.
- **Smaller, faster ROM.** The final packer repacks the image tightly: 234,292,908 -> 128,551,996 bytes (128.5 MB), below the clean 128 MiB Japanese image. All 108 FAT payloads and the ARM9/ARM7/FNT/banner blobs are byte-identical to the pre-shrink v1.0 build; only layout offsets, the ROM size/capacity fields and the header checksum changed. The game content is unchanged and the smaller file loads faster.
- **v0.9 player fixes merged.** Macross Quarter is exactly "Macross Quarter" for both fortress and assault states (short and full); pilot 260's two-row 104px label is one line, `KATOU ORG. SOLDIER`; the wide-header picture hook no longer draws the previous speaker's first glyph before a following text name (Katou -> Kouichi).
- **26 leftover Japanese names translated.** 16 unit picture-cell names, 8 weapon picture-cell names and 2 Shift-JIS pilot full names that no text scan could reach now have English names, pinned in `Remaining_Text/name_source_catalog.json` with a catalog test.
- **Cartridge-menu title.** ROM lists show **Super Robot Wars L** in all six banner languages (carried from v0.9).
- **Two source-specific patches.** `SRWL_English_v0.91_standard.xdelta` is for the canonical clean dump; `SRWL_English_v0.91_alt-header.xdelta` is for the otherwise-identical dump with zeroed extended-header metadata. Each was created and applied with xdelta3 3.2.2 source checksum checking on, produced the identical ROM below from its own dump, and refuses the other dump with a source mismatch.
- Patch sizes and hashes: standard patch 1,831,395 bytes, SHA-256 `ae3b83ad40316b7ec177c20891a351371b7bd6feddef57a284852af455b7c710`, CRC32 `45C6F472`; alt-header patch 1,831,623 bytes, SHA-256 `a93539ba9812d4a788f86971549f8002740733bf6336977d597b3bfd32c78def`, CRC32 `96830C9E`.
- Sources: canonical dump SHA-256 `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f` (CRC32 `1D040BE8`); zeroed-header dump SHA-256 `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f` (CRC32 `82804748`). Both are 134,217,728 bytes.
- Patched ROM: 128,551,996 bytes, SHA-256 `0c3cda0339ca583fbd7b08b8503588eafba65e4267e45f318d27ea389ac2ea1b`, CRC32 `193D992D`.
- Verified: build 26,500 UI / 1,704 residual / 23,415 battle records, 0 insertion errors, engine sources verified, 12/12 overlay guards, zero-Japanese and upgrade-UI contract pass. Standalone suite on master: 106 modules / 616 tests with only the three documented legacy exceptions (engine-source, Spirit-marker, text-presence); story-fit diagnostic 4,073 (baseline); `test_engine_nop_encoding` (built-ROM scan) and `test_rom_compact` pass. Cold boot through the intro (DeSmuME libretro, fresh boot, designated save) ran 20,236 frames / 27 captures with 27/27 captures byte-identical to the pre-shrink v1.0 build. Both patched ROMs boot in DeSmuME.

## v0.9 -- 2026-10-25

- Cartridge-menu update: all six banner language fields now display **Super Robot Wars L**. The icon, game code and game data are unchanged. Recreated the patch and checksums, verified both supported clean sources, and passed an independent browser decoder check and DeSmuME cold boot. The cumulative build has zero insertion errors and passes all 12 overlay guards; banner, title-graphics, ECD and story-fit tests pass (legacy overflow: 4,073). Existing 3DS forwarders need regeneration to show the new name. The Android JIT-off workaround still applies.

- Header-compatibility update: the patch now accepts both the canonical source (CRC32 1D040BE8) and the identical game dump with zeroed extended-header metadata (CRC32 82804748). Both produce the unchanged approved English ROM. Verified with native xdelta and the published web-patcher decoder, with checksum validation enabled. Redownload the patch and matching checksum attachment if the first v0.9 patch reported a target-window mismatch on the alternate header.

- Publishes the merged story/meaning/style, overflow, description, terminology and graphics work summarized below as a patch against the clean Japanese revision-0 ROM.
- Includes the gold support-badge correction and Iczer-1 crash fix; Action-tab and tab-ghost fixes; UI sweep 2 wording/spacing; and the all-song BGM title guard.
- Includes the newly translated Japanese-based opening narration and history graphics, approved in-game.
- Verified by standalone tests (three documented exceptions), zero insertion errors, 12 overlay guards, cold-boot smoke, and fresh-source patch reapplication with matching SHA-256/CRC32.
- Uses the v0.9 checksums at the repository root. Historical build numbers below do not identify the v0.9 patch or its output.

## Historical development notes

This summary describes recorded development work and earlier release notes. It is draft documentation, not a fresh release certification.

## Unreleased work after v309

- Completed the full story meaning/style audit across stages 1-41, including alternate routes, the ending and epilogue. Applied approved stages 1-5 and 6-10 revisions; stages 11-20 received 519 revisions, stages 21-30 received 343, and stages 31-41 received 481. Character voices, meaning, grammar, contractions, apostrophes, ranks and settled wording were reviewed. Internal test labels were excluded.
- Reviewed all 622 high-risk story overflow rows and applied their revisions. Native insertion checks report zero overflows; the older story-fit diagnostic still reports 4,073 and must not be described as a clean full-playthrough result.
- Audited all 23,415 battle-quote pages for style and meaning. Applied 55 low-risk style fixes and 268 meaning fixes; retained the canonical Glain Neidr spelling instead of one conflicting proposal. Higher-risk style proposals remain review work. Repaired spaces beside dynamic name tokens in 13 pages and checked all 165 dynamic pages without changing their controls or substitution order. The approved Ichitaka/Alice voice pass is retained; Daiya and Lulu review drafts are separate from installed work.
- Audited non-dialogue descriptions, ability/skill/part names, units, weapons, mission titles, objectives and Spirit/UI labels. Applied 132 low-risk style rows and 23 meaning revisions; nine meaning findings were already satisfied. Four route-label proposals could not be repacked safely. Unresolved fit and identity questions remain listed for playtesting.
- Settled the mechanic terms **Will**, **Valor** and **Spirit** in place of Morale, Hot Blood and Yell. Applied 14 follow-up term records, including the missed Will -20 line. Ordinary dialogue uses of morale, yelling and hot-blooded remain context-dependent.
- Standardized character-name spellings, terminology, ranks and punctuation, with regression checks and a term-variant review.
- Added player and team name-token support in story text.
- Applied short mission titles to the relevant title strings; Clear Data short-title drafts remain separate from installed changes.
- Improved menu wording and fit, including bonus and Use-screen labels, battle-result EXP and upgrade accuracy text.
- Installed approved English series plates, ability/status and Spirit banners, BGM lettering and 29 pilot-name pictures. Added all 55 English stage cards, corrected title-to-card mapping and applied the approved title wording. Full enemy labels fit the tested story/battle headers; narrow fields still need coverage.
- Added map-result graphics, including the title-case Critical popup. Installed coloured terrain silhouettes on tested Unit Stats and Weapon Power screens: cloud for air, mountains for land, waves for sea and star for space. Added separate forecast dictionary pictures without changing shared alphabet or upgrade-bar art. Natural forecast checks cover air/land; sea/space were verified with renderer fixtures and still need natural gameplay coverage. Underground remains a draft.
- Localized the title plate and boot copyright screens in separate private title-art builds. The approved English logo retains the corrected straight lower border and red glow. Larger mixed-case copyright lettering preserves all 13 complete attributions, dates and copyright symbols within the original tile budgets; cold-boot and visual checks passed for those builds. This is distinct from the deferred ending staff-credit roll.
- Centered the search grid and recorded further map-screen and title-screen findings. Leftover text under orange tabs and icon-spacing blockers remain documented issues; do not assume every menu finding is fixed.
- Refined Turns, Save Data Name/Funds alignment, Overview, Combo, All Units/Team BGM, Swap Unit, Pick Unit/Pick PU, Stat/Now/After/Parts, Barrier + and Hit wording. Corrected texture tile counting while preserving native positioning. Some labels were verified only in specific layouts; Barrier + still needs a naturally reached example.

These entries summarize development across several local branches and private test builds. They do not claim that every change is merged into one published patch. No ROM, patch or new release certification is produced by this documentation update. Latest recorded broad checks retain known test failures; focused checks and earlier runtime evidence apply only to their recorded builds.

## v309 - 2026-10-22

- Existing cumulative English patch packet, including the approved text package and recorded graphics fixes.
- Source and output checksums are documented in the existing release packet. No new ROM or patch was generated for this documentation branch.

## Earlier work

- v308 recorded a passing full test run; v309 superseded it for testing.
- Earlier builds developed dialogue, battle text, names, menus, fonts and graphics through repeated audits and runtime checks.
- Historical test counts and screenshots describe their original builds; a new release requires validation of its own artifact.
