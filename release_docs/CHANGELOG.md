# Changelog

Release packets are cumulative: each one contains every earlier text and engine
change unless the entry says otherwise. Only the versions listed here as releases
were handed out; the other builds were private test builds.

## v1.5 - 2026-11-25

- **Screens.** Blank or cut-off Spirit and Skill names on pilot screens fixed; HIT label on stat and weapon lists; menu labels no longer blank or clipped; Rei and Rey name plates fixed.
- **Text.** Chang Wufei name order, honorifics removed, official Dancouga Nova attack names, Crow's Machine Gun, Roo Riruri, typo and term fixes, smoother story line breaks, safer battle text fitting.
- **Patches:** `SRWL_English_v1.5.html`, 134,217,728 bytes, SHA-256 `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f`; `SRWL_English_v1.5.bps`, 134,217,728 bytes, SHA-256 `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`. Patched ROM: 128,465,980 bytes, SHA-1 `3fb18fe8422812f11c0b90e30b0c038876b49278`, SHA-256 `61f7c3102d3110471bc56b66a4aa941f90966a9a6704be6cda756df869b26467`, CRC32 `A9B5A749`.
- **BGM add-ons:** none for v1.5 yet. Earlier add-ons don't fit v1.5.

## v1.4 - 2026-11-21

- **Original-game bugs fixed.** Aoi Hidaka's A.Combo was one level low on maps (never reached level 3). The Great Booster showed 4/6 instead of 6/6 with B-Save on the Great Mazinger and lost shots. Soul, Hot Blood, Direct Hit, Mercy, Luck and Effort stayed active after boosting a support attack. Pressing X on a Combo weapon's target list could start a battle that hit nothing or froze. The Dannar Combination cut-in showed Goh instead of Shizuru when Anna or Mira started it.
- **Other fixes.** Enemy info screen pilot labels "Nuke Missile" and "Stray Mach." no longer cut off, with extra checks against the v1.3.2 kind of crash. BGM add-on: no more horizontal line in battle scenes. Counter Settings: blank button now reads "Counter", help lines not clipped. Upgrade screen: "Fund" not clipped, weapon header reads "Atk". Weapon list: stray pink dot removed. Script unchanged from v1.3.2.
- **Patches:** `SRWL_English_v1.4.html`, 41,035,086 bytes, SHA-256 `f500ab4a98fe537a7efbb2f3be7dacbaeb1d05f304d3e39dc39ffc0614ab463c`; `SRWL_English_v1.4.bps`, 30,762,920 bytes, SHA-256 `2ac84747abf64cf26c985ddc790bbc98c53d77d3ab87cc261b25dbae0ebda4fb`. Patched ROM: 128,465,468 bytes, SHA-1 `b689c17c185e61850a08b9c9300d594c4b5a51e0`, SHA-256 `cc7969fd4e6eeeb39c709d30219a3a89f959b9569f39a0f0fb94022501f0bc08`, CRC32 `59EEF226`.
- **BGM add-ons (downloaded separately):** `SRWL_English_v1.4_StereoBGM_addon.bps`, 164,731,107 bytes, SHA-256 `f2040026ae62f552d963ff01f027687d4e2084616950b11e1677ed39e404faf1` (result 265,797,184 bytes, SHA-256 `efd428750a6d46b93710955bff859e80cc68e6acb0871c2087315714d386a682`); `SRWL_English_v1.4_MonoBGM_addon.bps`, 94,723,405 bytes, SHA-256 `53cf58a727675e69f6fc385b80843c386b6d6546ab959cc3000bb16ecd952be3` (result 197,139,008 bytes, SHA-256 `04a5eab315b86c012bbad041318070989887e286a9b7f7e4e43a5504178a10d1`). Earlier add-ons don't fit v1.4.
- **BGM mirrors:** Stereo: [Gofile](https://gofile.io/d/fdHC3rB8) · [1fichier](https://1fichier.com/?7dc46khps1cskb7unzoe) · [MEGA](https://mega.nz/file/DfphyLjS#5h93ZXpTBrfJTXP1d7G4oqPPgDFWRcCOsCw4EJxKOhk); Mono: [Gofile](https://gofile.io/d/KuRgBefu) · [1fichier](https://1fichier.com/?6l4xw2s40hs1pe9ufoxn) · [MEGA](https://mega.nz/file/KOBEyazY#6Ckc5Xhla47knCPnzYqN7zj1XPxvIubOwl6Q3s7eCbQ)

## v1.3.2 - 2026-11-21

- **Crash fix.** Stage 12 could crash or freeze when the info screen of the ARMA enemy unit was opened. Its pilot's shortened name label was written to the wrong place in the text buffer, so the text renderer ran past its memory. Text and graphics otherwise unchanged from v1.3.1.
- **Patches:** `SRWL_English_v1.3.2.html`, 41,280,379 bytes, SHA-256 `31cf1f3bbf9c155a965c47699c08a1e24f63b2923c03accb2921263e7cee853f`; `SRWL_English_v1.3.2.bps`, 30,946,868 bytes, SHA-256 `eed96d08e6474fb1ebcc33d90e970ee18e8c0ea868f3917239468725af9b4f77`. Patched ROM: 128,465,468 bytes, SHA-1 `4b39867136cec8bf37fe594bdd01f9b2cd66e901`, SHA-256 `d727da13ebe78a9da22ff3e4f8584565f406218e5eac579675032e60cea09797`, CRC32 `53E9E761`.
- **BGM add-ons (downloaded separately):** `SRWL_English_v1.3.2_StereoBGM_addon.bps`, 163,746,754 bytes, SHA-256 `394eaa0bbefd99c0ec91483859c548ea705d5a30fbd26e6164a046bfce5ddd27` (result 265,797,184 bytes, SHA-256 `4c1bdcf5cd12fc1695b38ba0a5da47c6c7c173f8027cb78e57610687777569b3`); `SRWL_English_v1.3.2_MonoBGM_addon.bps`, 93,739,020 bytes, SHA-256 `6bf61b94506b2895dcb75b2f0b65bfda9d5d424346df03a16c7c0b80c1f2ddf2` (result 197,139,008 bytes, SHA-256 `9f7646da0e9bbb83836bb398c246f5ccec7156c4b27fe5dfc85e255634963858`). Same music and player as v1.3.1; the v1.3.1 add-ons don't fit v1.3.2.

## v1.3.1 - 2026-11-20

- **BGM add-on save fix.** With the Stereo or Mono BGM add-on, saving on a map could freeze on "Saving... Do not power off." (the save itself was written). The music player now waits while the game writes the save. Main patch and patched ROM unchanged from v1.3.
- **Patches:** `SRWL_English_v1.3.1.html`, 41,280,379 bytes, SHA-256 `48452d46a15962f1a98b1d27a5136d38f9b01a9ec424147951c41d02be68327e`; `SRWL_English_v1.3.1.bps` (same bytes as v1.3), 30,946,868 bytes, SHA-256 `39215bf4fb8dbccfc8cbcadb1dac07b882482566a2f879112e6a7f6b1a487203`. Patched ROM unchanged: SHA-256 `6ca621dd431f71a26ef8870161262e0c656c09b26729af0d9ab1f4b21607cdc0`.
- **BGM add-ons:** `SRWL_English_v1.3.1_StereoBGM_addon.bps`, 163,746,754 bytes, SHA-256 `c1885c46950f52038be6d3bba6c19c324b7e2e9fca953061d8bf1c12b70a269d` (result 265,797,184 bytes, SHA-256 `00cde860141abbe08bac6b4f844afe3583134b44fb2ed46b63633c3495b981d3`); `SRWL_English_v1.3.1_MonoBGM_addon.bps`, 93,739,020 bytes, SHA-256 `9be2a8204c9ab1dd8efc358250f3cbd97ad9f379a0df3b0b17bfa17f31e12a05` (result 197,139,008 bytes, SHA-256 `f1345a89129d59a302ad7354534833a0227473afb1f3868cbb31a47fe7680c85`).

## v1.3 - 2026-11-20

- **Dialogue.** About 185 lines corrected for meaning and about 380 polished for flow.
- **Names.** Full names on map locations and area titles; Mission Objectives name the pilot they need.
- **Fixes.** *Gundam Wing Endless Waltz* series title, consistent CIWS names, more room for menu button shortcuts.
- **Vocal BGM add-on (optional).** Stereo (tested on 3DS) with a mono fallback. The HTML patcher can build the BGM ROM in one go from the Japanese ROM or the patched v1.3 ROM; Flips works too.
- **Patches:** `SRWL_English_v1.3.html`, 41,280,351 bytes, SHA-256 `96645ee1b7cba94ba45cd029255448c11f4570353ebd01a65aff763f14db7c79`; `SRWL_English_v1.3.bps`, 30,946,868 bytes, SHA-256 `39215bf4fb8dbccfc8cbcadb1dac07b882482566a2f879112e6a7f6b1a487203`. Patched ROM: 128,465,468 bytes, SHA-1 `07a1f95e7ad4d897c489c18a524f75cea43e06c4`, SHA-256 `6ca621dd431f71a26ef8870161262e0c656c09b26729af0d9ab1f4b21607cdc0`, CRC32 `40E00BDD`.
- **BGM add-ons:** `SRWL_English_v1.3_StereoBGM_addon.bps`, 163,746,566 bytes, SHA-256 `92b291c221abc1f08d3aa4cc81954cdd4fc16c5571de1d46937dcac230e90363` (result 265,797,184 bytes, SHA-256 `85ca36eff5216dc68a4fc3f43ae908e7c067ef828dcf5d0b4dacb0a0388685a1`); `SRWL_English_v1.3_MonoBGM_addon.bps`, 93,738,600 bytes, SHA-256 `809744b6594be041c230a2961272ec82230883e39feb63837c99923c72389c92` (result 197,138,496 bytes, SHA-256 `8bf651bf69d4bf491a935a248d896b93eaecffecf027892cf6ecf4844ca94d8f`).
- **BGM add-ons withdrawn:** they could freeze on the Saving screen; replaced by v1.3.1.

## v1.2 - 2026-11-17

- **Meaning fixes.** 143 lines that drifted from the Japanese corrected, plus 74 more found in a later cross-check.
- **Voice pass.** About 2,200 story lines reworked so each character sounds like themselves; trailing-off lines restored where the Japanese trails off.
- **Consistent names and terms.** Alliance, NUNS and S.M.S. standardised; names of characters, units and weapons made to match across story, menus and battles.
- **Battle quotes.** More than 200 battle lines corrected for meaning or voice, hesitation pauses restored, and the remaining rows over the box edge re-broken to fit.
- **Map labels.** About 40 location labels widened so place names show in full.
- **Mission Objective hints.** Cyan hints for secret conditions and route splits.
- **Battle forecast.** Pilot names in mixed case.
- **BGM.** Titles updated; one title strip redrawn.
- **Nagisa fix.** Restarting a stage no longer drops Nagisa from Iczer-1's crew.
- **UI.** Spirit buttons and the Aid label centred.
- Header version byte stays 1 (DSpico fix from v1.1.2); game code BRWJ.
- **Patches:** `SRWL_English_v1.2.html`, 27,348,919 bytes, SHA-256 `be69b111989e7f67893c68b060e9ecf0f1e5fd807b92d53700a46b52cee48502`; `SRWL_English_v1.2.bps`, 20,502,515 bytes, SHA-256 `70a63f6cf2ec66f39e66964af3c9c4d33d23928e5b6bce16f737bed083c95715`. Patched ROM: 128,463,420 bytes, SHA-1 `201fab8613eb586e8a6192f047d34143b7eb4f8d`, SHA-256 `164570786f29e70785e23f0837437c966c90de068241bcae4e6c8f4936993f52`, CRC32 `C3C460E6`.

## v1.1.2 - 2026-11-14

- **DSpico white screen fixed.** The ROM header's version byte is now 1 instead of the Japanese game's 0. Pico Loader (DSpico) looks up its anti-piracy patches by game code and version and patched SRW L's anti-piracy code on top of ours, which left the game on a white screen. With version 1 it skips that patch. The game code stays BRWJ, so save-type detection is unchanged. No text or graphics changed.
- **Patches:** `SRWL_English_v1.1.2.html`, 40,941,901 bytes, SHA-256 `0c864bb0df5ea27e3b632a6f811d0742558f8c54c10e6adb38de5b55a591f938`; `SRWL_English_v1.1.2.bps`, 30,697,247 bytes, SHA-256 `cb86e11a3e72cdb9f5662ab8d838126a4334970e04ce119d91eda9d33f5b7e46`. Patched ROM: 128,452,668 bytes, SHA-256 `b7d13764e408ddd2048f4aa87ad8ccf0c68f733413d59a5010f8b74c80da3fac`, CRC32 `BE95E7D7`.

## v1.1.1 - 2026-11-13

- **Font polish.** Redrew W, M, Y and T in the narrow story/battle font, made capitals, digits and tall lowercase letters one pixel shorter, and tidied g, a, s, j, K, N, S, X and 0. Every letter keeps its width, so no line breaks changed.
- **Battle quotes past the box edge fixed.** Battle quote rows now leave room for the box's 4-pixel indent; about 170 pages that spilled a letter onto the next row are re-broken, including Daiya's "We're giving it everything we've got!" in a Gaiking battle.
- **Known issue (cosmetic):** the weapon Type line still keeps a trailing comma, e.g. `CQB, Combo,`.
- **Patches:** `SRWL_English_v1.1.1.html`, 40,941,897 bytes, SHA-256 `a17fd39d5e1cec388d478065a360aade266d5a13df89795592dc4346c52a3c0d`; `SRWL_English_v1.1.1.bps`, 30,697,245 bytes, SHA-256 `73b7dd1bd2a086caf8bc9dec3ca031160cb693bf30526d07485ce9e46e658f96`, CRC32 `2144DF1C`. Patched ROM: 128,452,668 bytes, SHA-256 `dd9f3b4424c0ec531e4093d57b65bbae8517425087cf1439b3b4f8b37dcb2dfd`, CRC32 `73FDBF3D`.

## v1.1 - 2026-11-13

- **More text per line.** A narrower story/battle font and engine changes let story and battle text use the full width of the text box. Lines that had been trimmed to fit the old width are restored to their full wording.
- **Flow pass.** About 2,600 story and battle lines reworked against the Japanese using the extra room; forms of address made consistent and leftover battle "-san" honorifics removed.
- **Battle quote fixes**, including Saruwatari's taunt and the "War of the Giants" line break.
- **Name pass.** Another pass so character and speaker names match the Japanese more closely.
- **Restored ellipses** in about 800 lines.
- **Pilot Stats:** Intuition and Resupply Spirit slots no longer blank.
- **Known issue:** a few long battle lines can still run past the edge of the box, e.g. Daiya's "Take a good look! We're giving it everything we've got!" in a Gaiking battle.
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
