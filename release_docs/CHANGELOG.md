# Changelog

Release packets are cumulative: each one contains every earlier text and engine
change unless the entry says otherwise. Only the versions listed here as releases
were handed out; the other builds were private test builds.

## v1.1 - 2026-11-13

- **More text per line.** A narrower story/battle font and engine changes let story and battle text use the full width of the text box. Lines that had been trimmed to fit the old width are restored to their full wording.
- **Flow pass.** About 2,600 story and battle lines reworked against the Japanese using the extra room; forms of address made consistent and leftover battle "-san" honorifics removed.
- **Battle quote fixes**, including Saruwatari's taunt and the "War of the Giants" line break.
- **Name pass.** Another pass so character and speaker names match the Japanese more closely.
- **Restored ellipses** in about 800 lines.
- **More English graphics:** 15 more pop-ups (Iczer Robo Combine/Split, Mazin Power, Steel Power, Zero System, Link/Unlink, Ammo Refill).
- **Pilot Stats:** CQB/RNG/SKL headers aligned, clearer Q glyph, Intuition and Resupply Spirit slots no longer blank.
- **New offline HTML patcher** (both dumps) alongside a standard BPS patch (canonical dump).
- **Known issue (cosmetic):** the weapon Type line still keeps a trailing comma, e.g. `CQB, Combo,`.
- **Patches:** `SRWL_English_v1.1.html`, 40,727,619 bytes, SHA-256 `6b2153126f5ead7b1435efc742a70cd5d2ba50e91c59d4d586fec34a104a8ac4`; `SRWL_English_v1.1.bps`, 30,536,539 bytes, SHA-256 `dfa59203a10abc991bb7513aa96dcfba07769131efae0b70f7df6aff967a879c`, CRC32 `2144DF1C`. Patched ROM: 128,452,668 bytes, SHA-256 `d6b89851a743d3526026fc3151df4501abeb022fd9dec5b3f2483e3cf891fcc7`, CRC32 `2D97804E`. Verified on hardware and by patching fresh copies of the clean dumps.
## v1.0.1 - 2026-11-05

- **Wrong battle quotes fixed.** At battle setup the game copied each weapon and unit name into fixed slots with no length limit. A long English name could run past the last weapon slot into the battle flags beside it, so the game picked the wrong quote situation. Steel Jeeg's Mach Drill showed Heero with an untranslated line and no Combo label; it now shows Kenji and Tsubaki with the label. Other battles with the same overrun are fixed too. These two copies now stop at the slot limit, like the ones fixed in v1.0. No translation text was changed.
- **Combo label no longer cut off.** The yellow combination label art fits its window.
- **One-line picture names.** 23 picture-drawn names no longer lose their top line in the speaker box: the numbered Angels, EVA Unit 01, SOUND ONLY, NERV Agent/Staff, Neos Gold and Darius XVII keep their wording, and seven are shortened (Unk. Soldr, Logos Man, UN Officer, UN Soldier, Vajra Q., B. Galaxy, MP Machina).
- **Godannar names.** "Go Dannar" is now Godannar, and Go-Okusaer and Neo-Okusaer match the Japanese.
- **List menus.** Short column headers that fit (S.Atk, S.Def, Arm, Hit, Left), level-less rows keep their columns aligned, and the ability column shows an English marker.
- **Known issue (cosmetic):** the weapon Type line still keeps a trailing comma, e.g. `CQB, Combo,`.
- **Patch:** `SRWL_English_v1.0.1.xdelta`, 7,043,158 bytes, SHA-256 `61aaa5880eec76c25086888da95236180b2291de2ec0b6a5981859f45327284e`, CRC32 `C86F802B`. One patch for both supported dumps. Patched ROM: 128,485,436 bytes, SHA-256 `648b7b6c918e10cc62e6dc7fbe690b71bb24d011acc2b18d4f6e7177fa4e9031`, CRC32 `EF8329B6`. Verified by applying the patch to fresh copies of both dumps.
- **Build checks:** 26,500 UI / 1,705 residual / 23,415 battle records, 0 insertion errors, engine sources verified, 12/12 overlay guards. Release-tier suite: 116 modules / 697 tests, all pass. Cold boot in DeSmuME passes.

## v1.0 - 2026-11-01

- **Approved battle pop-up artwork installed.** 95 approved round-3 resources are installed with
  predecessor, native-geometry, raw-PAT, alias and palette guards: Critical pop-ups, Support
  Attack/Defense badges and banners, map-result pop-ups and the common battle labels. Bronze Bell
  and the shipped-sans **9 PM Don't Be Late** are included. Natural support captures cover
  animations on/off, badge and banner; Critical and Accuracy Down L1 use controlled native events.
- **Battle-name buffer crash fixed.** The ov22 weapon, unit and pilot name caches and the ov10
  list-label records now use bounded copies that stop at a character boundary and always terminate.
  This fixes the crash when Daiku-Maryu used Zolmanium Piercing Shell, whose 48-byte name
  overflowed the 33-byte weapon cache and corrupted the caller's stack. The marker-1 compact form
  is not used in those caches because the battle parser treats bytes below `0x80` as tokens; long
  names are truncated on those screens instead. No catalog or translation text was changed.
- **Known issue (cosmetic):** the weapon Type line keeps a trailing comma for combination attacks
  and some other types, e.g. `CQB, Combo,`. The shared translated type fragment ends with an ASCII
  comma and the native list builder does not strip it; tracked for the next text/UI pass.
- **One patch for both dumps.** `SRWL_English_v1.0.xdelta` applies to the canonical dump
  (`a2b666a2...`, CRC32 `1D040BE8`) and to the zeroed extended-header dump (`1bc8e2e0...`,
  CRC32 `82804748`), and both produce the same patched ROM. The 188 differing header bytes are
  filled with junk in the encoding reference and emitted as literals; the source window covers the
  whole ROM, whole-file source verification is off and target-window checksums stay on.
  Patch: 7,054,495 bytes, SHA-256
  `45612d2a4fef472b5d3bc85de91e95bdb2abc4e727f1cada7ee3088e0c0ced98`, CRC32 `3263A740`.
  Patched ROM: 128,484,412 bytes, SHA-256
  `f183ea1562c794e0ac5e39eda0c5fe335f0ed81e20596b15511d55e55a0d2643`, CRC32 `9C705A37`.
  Verified by applying the patch to fresh copies of both dumps.
- **Build checks:** the final private build and the v1.0 release build are byte-identical
  (SHA-256 above); 26,500 UI / 1,705
  residual / 23,415 battle records, 0 insertion errors, engine sources verified, 12/12 overlay
  guards. Release-tier suite: 113 modules / 651 tests, all pass. Cold boot in DeSmuME passes
  (5 captures, smoke frame OK).

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
  - These edits are part of the v0.91 packet.
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

## Before v0.9

- Numbered private test builds were used for text, menu, battle and graphics QA
  before the first public release. They were never distributed; do not use them
  as the base for a bug report.

## Reporting a problem

Use `PLAYTESTING.md`. A report needs the stage or menu path, a screenshot, the
Japanese line or record ID if you know it, your suggested fix, and the `.sav`
you used. Save states are not accepted as the only evidence.
