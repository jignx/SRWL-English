# Changelog

Release packets are cumulative: each one contains every earlier text and engine
change unless the entry says otherwise. Only the versions listed here as releases
were handed out; the other builds were private test builds.

## v0.92.1 - 2026-10-27

- Fixed the shared Skills/Spirits/Abilities help cache allocation, including Shield Defense in map Search and the graphics damage that could follow it.
- Corrected Jack Smith's full-name aliases and the Gaiking, Heavyarms Kai, Dancouga Nova Max God and Quadran (Super Pack) identity data.
- Retained the Kills/Support Defense correction. No general font-cache or rendering rewrite.
- Validated with 640 automated tests, cold boots and three full-roster list sweeps. Broader menu/route sweeps remain for a later session.
- Patch from a clean supported Japanese dump, then cold boot and load an in-game save. Do not apply over v0.92 or load an old emulator savestate.

## v0.92 - 2026-10-26

- **Anti-piracy is fully disabled in the ROM itself.** The eight checks the Action Replay
  code used to neutralise live in overlay 0 (FAT file 0, loaded at `0x021AE4C0`); all eight
  bytes are now patched permanently at build time, so the game runs without a cheat file or a
  patched flashcard loader. The patch is byte-identical to the community AAP bypass and needs no
  recompression.
- **English staff credits.** All 23 credit pages are English and ship enabled in the normal
  build (the roll was previously withheld behind a build flag). The page-4 heading reads
  **"Story Outline"**.
- **Weapon-name fixes.** Shared weapon strings are now split per unit where the official name
  differs: Blade Gainer's plain katana reads **Katana** while Celleblader keeps **Laser Blade**,
  and the pilot 剣 stays **Ken** while the four 剣 weapons read **Sword**. Blade Gainer's
  Gottfried-style pun attacks are corrected to **Hell's Wind** and **Hell's Hurricane**, its
  follow-up reads **Death Strash**, and the sword it swings is **Celleblade**. Four further
  sword names were reviewed against licensed sources and updated: **Dancou Dangai Sword**,
  **Zankitou**, **Tachi Combo Slash** and **Heavy Sword**. Everything else keeps its approved
  wording (including "Breaker Shoot" and both Blade Gainer forms sharing "Death Strash").
- **Text fixes:** the three Japanese series titles now read Gundam Seed Destiny, Gundam Wing EW
  and Godannar!! 2nd Season, the Dancouga unit name is R-Daigun, 博士の家 is Prof's House, and the
  remaining playtest text corrections are in.
- **Graphics and UI alignment:** six map ability pop-ups (Steel Power, Ammo Refill, Mazin Power,
  Zero System, Link and Unlink) and nine Iczer skill picture cells are installed with their native
  palettes and positions; the pilot-stat page uses the native six-column alignment including the
  Hit column; hidden list tiles are reused so the Kills and Support Defense pages no longer
  corrupt; the sort headings have measured frames including Support Attack and Support Defense;
  and the formation and sortie screens show the native terrain icons with their inline headers.
- **One patch for both dumps**, as in v0.91: `SRWL_English_v0.92.xdelta` applies to the canonical
  dump (`a2b666a2...`) and to the zeroed extended-header dump (`1bc8e2e0...`), and both produce the
  same patched ROM. Check the patched ROM hash in `CHECKSUMS.txt`.

## v0.91 - 2026-10-25

- **JIT/dynarec on is supported.** The engine's five ARMv6K `nop` hints
  (`0xE320F000`, decoded as an MSR on the ARM9) were replaced with the ARMv5
  `mov r0, r0`, and the assembler now rejects the hint encoding. The prologue-intro
  freeze on melonDS Android and WatermelonDS is fixed; no emulator setting needs to
  be disabled. This supersedes the v0.9 JIT-off workaround.
- **ROM is 128.5 MB instead of 234 MB.** The final packer repacks the image tightly
  (234,292,908 -> 128,551,996 bytes, below the clean 128 MiB Japanese image) and
  loads faster. All 108 FAT payloads and the ARM9/ARM7/FNT/banner blobs are
  byte-identical to the pre-shrink build; only layout offsets, size/capacity fields
  and the header checksum changed. Game content is unchanged.
- **v0.9 player fixes:** Macross Quarter unit names (fortress and assault states),
  one-line `KATOU ORG. SOLDIER` enemy label, and the speaker-plate overhang glyph
  fix.
- **26 leftover Japanese names translated:** 16 unit picture-cell names, 8 weapon
  picture-cell names and 2 Shift-JIS pilot full names that no text scan could
  reach (`Remaining_Text/name_source_catalog.json`, with a catalog test).
- **One patch for both dumps.** `SRWL_English_v0.91.xdelta` applies to the
  canonical dump (`a2b666a2...`, CRC32 `1D040BE8`) and to the otherwise-identical
  zeroed extended-header dump (`1bc8e2e0...`, CRC32 `82804748`); both produce the
  same patched ROM. The 188 differing header bytes are filled with junk in the
  encoding reference and emitted as literals (v0.9-style header-neutral encoding);
  the source window covers the whole ROM, whole-file source verification is off
  and target-window checksums stay on, so check the patched output hash. Verified
  on both dumps. Patch: 6,829,409 bytes, SHA-256
  `052cf7e2662f501648f9f8a08016ab2a9e0e1087bfe921d57340091546bd664b`,
  CRC32 `F2B28C0E`.
  Patched ROM: 128,551,996 bytes, SHA-256
  `0c3cda0339ca583fbd7b08b8503588eafba65e4267e45f318d27ea389ac2ea1b`,
  CRC32 `193D992D`.
- Verified: 26,500 UI / 1,704 residual / 23,415 battle records, 0 insertion errors,
  engine sources verified, 12/12 overlay guards, zero-Japanese and upgrade-UI
  contract pass. Standalone suite 106 modules / 616 tests with only the three
  documented legacy exceptions; story-fit diagnostic 4,073 (baseline).
  `test_engine_nop_encoding` and `test_rom_compact` pass. Cold boot through the
  intro (DeSmuME libretro, fresh boot): 20,236 frames, 27 captures, 27/27
  byte-identical to the pre-shrink build. Both patched ROMs boot in DeSmuME.

- **Style pass on existing text**, applied through `tl revise`:
  - 17 lines that used a Unicode em dash now use `--`. A Unicode dash is
    normalized to a single hyphen in game, so these lines used to read as
    "Alto-and" or "Wha-!"; the double hyphen is the approved interruption form.
  - 18 lines that used two dots or a Unicode ellipsis now use ASCII periods:
    six periods for two Japanese ellipsis marks, three for one mark or an
    existing pause. This includes the short battle reactions that used to show
    two dots.
  - No name, name token, control code or line break was changed. Every edited
    line was re-encoded with the story or battle encoder and keeps its row count.
  - Private build only; not part of the v309 hashes. These edits are part of the
    v0.91 packet.
- Canonical character-name spellings applied across dialogue, battle lines and
  the name tables (`test_canonical_names`).
- Player name tokens (`{Ichitaka}`, `{Alice}`, `{Unit}`, `{FullName}`,
  `{Family}`) and the team token (`{Team}`) now work in story text.
- Menu fit pass: the bonus prefix reads `Barrier +` (so the game shows
  `Barrier +1000`), and the Use screen header reads `After`; the remaining
  item wording was staged for review.
- Terrain icons installed for air, land, sea, space, water and underground with
  guarded selectors and a pixel-only runtime check.
- Map Critical popup redrawn in title case, plus the map-result family art
  (HIT / EVADE / status labels).
- Short picture labels for pilots 260 and 263; Sir Violet's name picture on one
  line so the text log no longer clips it.
- Battle RESULT EXP overflow and Upgrade Units Accuracy label spill fixed.
- Objective wording and stage-title pass, Spirit marker spacing, and a
  Japanese-term variant scan.
- Added the release checksum tool, the settled-renderings/choices reports and
  this release packet.
- Short mission titles for the Clear Data line were drafted only; they are not
  installed.

## v309 - 2026-10-22

- Current release packet. Built from the cumulative working tree; no commits
  were made between v308 and v309.
- SHA-256 of the patched ROM: `527e4415c3bdb4c3f068980fb54af29cf19dc692d868d31fb052763d1412e7cb`.
- Includes the approved 2026-10-22 text package and the graphics fixes recorded
  below. Release save is a copy of the designated mission-5 save; the original
  is never modified.
- v309 is the build the hashes in this v309 section describe; v0.91 supersedes it
  and has its own hashes in `README.md` and `CHECKSUMS.txt`.

## v308 - 2026-10-22

- Green release: 78 test modules, 469 tests, 0 failures; engine-source,
  text-presence, overlay and format-slot checks passed.
- Included the Okusaer, percent/Destroy Gundam, Misato/Mihoshi and Spirit #28
  changes.
- Recorded as the last full green release before v309. v309 supersedes it for
  testing.

## v307, v305, v303

- Not recommended. These builds were red or had stale evidence and were
  superseded by v308 and v309.
- Kept only for project history; do not use them as the base for a bug report.

## v306, v304, v301, v302

- Successive text, menu and graphics passes.
- v304 supplied the previous designated save.
- v306 added the approved Lulu wording and its related checks.

## Earlier releases

- v295, v276, v273 and v267 were intermediate snapshots used for menu, battle
  and graphics QA.
- Older changes are recorded in the project's AI changelog and the per-release
  notes. Very old release folders have been removed; do not rely on their paths.

## Reporting a problem

Use `PLAYTESTING.md`. A report needs the stage or menu path, a screenshot, the
Japanese line or record ID if you know it, your suggested fix, and the `.sav`
you used. Save states are not accepted as the only evidence.
