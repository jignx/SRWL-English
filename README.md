# Super Robot Taisen L -- English v0.92.1

An unofficial English fan translation for **Super Robot Taisen L** on Nintendo DS. This is a public playtesting release. Only xdelta patches, checksums and documentation are distributed; supply your own clean Japanese cartridge dump.

## Introduction
Hello,
I was curious about using AI as a tool in order to translate a SRW game (been a fan for a long time now) and I kept having too much fun working on it while throwing deepseek, Claude, Chatgpt at it to push through every bug and fixes I could find.
In my opinion, using AI to help translate a game is far harder than I thought. While AI makes it easier, a lot of work is just figuring things out and applying solutions and waiting. I spent the past few weeks wrestling with SRW L and seeing bugs and issues crop up one over another.
After playing through it a bit and fixing all the bugs I could spot, I feel like this is good enough for a public release and something I'm proud of putting out into the world. Please do let me know if you find any bugs or issues while playing the game. I would be happy to fix them.

## What’s new in v0.92.1
- Fixed garbage font tiles below Skills, Spirits and Abilities descriptions, including Shield Defense in map Search. The cache allocation fix also prevents the resulting graphics damage after leaving help.
- Corrected unit identity data: Jack Smith no longer displays Takeminakata; Gaiking no longer displays Godannar. Heavyarms Kai, Dancouga Nova Max God and Quadran with Super Pack also use their correct names. Gaiking the Great retains its correct name.
- The Kills/Support Defense fix is retained.

This cumulative hotfix includes all v0.92 changes. It passed 640 automated tests and cold-boot emulator checks, including full-roster list selections. The remaining broad menu and route sweeps are deferred; this is still a public playtesting release.

## Included from v0.92
- **Anti-piracy game over fixed on DS/3DS and flashcarts.** Anti-piracy checks are fully disabled in the patch; no cheat file is needed.
- **English ending credits**, including the Story Outline heading.
- **Weapon and name fixes**, including the Katana/Laser Blade and Ken/Sword splits, Dancou Dangai Sword, Zankitou, Tachi Combo Slash and Heavy Sword.
- **Translated map pop-ups and Iczer graphics**, terrain icons on formation/sortie screens, aligned pilot-stat columns with Hit visible, and corrected sort-heading highlights.
- **Kills/Support Defense pages stay readable** while cycling stats.

### Included from v0.91
- **JIT/dynarec on now works.** The prologue-intro freeze on melonDS Android and WatermelonDS is fixed. There is no emulator setting to disable for this patch.
- **The ROM is 128.5 MB instead of 234 MB.** The English build is tightly repacked; the game content is unchanged, the file is smaller and it loads faster.
- **The remaining Japanese names are translated.** 26 picture-cell/pilot name sources that no text scan could reach now have English names, and Macross Quarter reads exactly "Macross Quarter" in both its fortress and assault states.
- **Enemy and speaker fixes.** The Katou soldier name box is one line, `KATOU ORG. SOLDIER`, and the stray glyph that appeared before Kouichi's speaker name is gone.
- **Cartridge-menu title:** ROM lists show **Super Robot Wars L** in all six banner languages.

## Disclaimer
The game has been translated, including the ending credits, but has not been played from beginning to end on every route. There may still be late-game bugs, rare-menu issues or text overflow. Please report problems with an in-game save and reproduction steps. This remains a public playtesting release; a complete route-by-route hardware playthrough is not claimed.

## Features
- Full English translation of the story, battle quotes, and unit, weapon, pilot and ability descriptions, with a story-wide consistency audit
- Translation has been checked to consistently keep within each series setting, lore and personality to ensure that the writing consistently captured the personality of the characters in the game.
- Official English name spellings for series, characters and mechs where they exist using Akurasu, Fansubs and Wiki as a source
- Terms familiar from other official SRW games like VTX30Y: Will, Valor, Spirit, CQB / RNG / SKL
- Menus and UI fitted to the screen, with labels sized and aligned to match the original layout
- Translated graphics: title and copyright screens, terrain icons, battle badges such as Support Attack
- English cartridge-menu title: **Super Robot Wars L** in all six banner languages
- Battle menu cleaned up: full Action / Counter / Defend / Evade tabs
- JIT/dynarec on is supported on melonDS Android, WatermelonDS and other DS emulators
- 128.5 MB ROM (down from 234 MB), so it loads faster from storage
- All remaining Japanese picture-cell names translated, including Macross Quarter; one-line `KATOU ORG. SOLDIER` label; stray speaker glyph before Kouichi fixed
- Distributed as an .xdelta patch: apply it to your own clean Japanese ROM

## Download
Grab `SRWL_English_v0.92.1.xdelta` and `CHECKSUMS.txt` from the [v0.92 release](https://github.com/jignx/SRWL-English/releases/tag/v0.92.1). The same patch works for both known clean dumps.

No pre-patched ROMs, please don't ask.

## Screenshots
Captured in DeSmuME, showing both Nintendo DS screens at their original resolution.

| Title screen | Opening narration |
| --- | --- |
| ![English title screen and main menu](screenshots/title-screen.png) | ![Original English opening narration](screenshots/opening-narration.png) |

| Scenario title | Story dialogue |
| --- | --- |
| ![English Scenario 3 title card](screenshots/scenario-title.png) | ![English story dialogue between Cobalt and Sepia](screenshots/story-dialogue.png) |

| Weapon selection | Attack dialogue |
| --- | --- |
| ![English weapon selection and Dancouga Nova stats](screenshots/weapon-selection.png) | ![Johnny calling Dancou Cannon during an attack](screenshots/attack-dialogue.png) |

| Pilot cut-in | Battle animation |
| --- | --- |
| ![Goh's pilot cut-in with English battle dialogue](screenshots/pilot-cut-in.png) | ![Alto's battle animation and English dialogue](screenshots/battle-animation.png) |

## What you need
A clean Japanese ROM of the game (BRWJ, revision 0, 134,217,728 bytes). Two dumps are known, and the one patch applies to both:

| Dump | SHA-256 | CRC32 |
| --- | --- | --- |
| Canonical | `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f` | `1D040BE8` |
| Zeroed extended-header metadata | `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f` | `82804748` |

They contain identical game data; only 188 bytes of unused extended-header metadata in the first 4 KiB differ. If your dump matches neither, the patch won't apply cleanly. Keep checksum validation enabled: the patch checks its target windows, so a corrupted or modified source is refused instead of producing a broken ROM.

## How to patch
1. Check your ROM's SHA-256 against the table above.
2. Apply the patch to a copy of your dump:
```sh
xdelta3 -d -s clean-jp.nds SRWL_English_v0.92.1.xdelta SRWL_English_v0.92.1.nds
```
3. Check the patched ROM against `CHECKSUMS.txt`. It should be 128,499,260 bytes with SHA-256 `35cdc6aab4b7dc82885a845712c250590f4a533f7ed7f2ddba6352490547fbbe`.
4. Back up your save, then start the game fresh. Don't load old emulator savestates, as they can bring back old text and graphics.

Keep checksum validation enabled in your patcher. The patch is encoded so it does not depend on the 188 bytes of extended-header metadata that differ between the two dumps, which is why one file works for both. Because one patch has to cover two sources, it does not carry a whole-file source checksum -- so **always check the patched output** against `CHECKSUMS.txt` (or the hash in step 3). If a patcher reports a target-window checksum mismatch, stop: the source or patch is damaged, so re-check the dump hash and redownload the patch.

The ROM displays the English ROM-list title. Refresh cached ROM lists after replacing the ROM. For an existing 3DS HOME Menu forwarder, recreate the forwarder from the new ROM to update its stored title.

## Known issues
- The game hasn't been played start to finish on every route yet, so some late-game lines, rare menus or long names may still overflow.
- Tested in DeSmuME. Real hardware hasn't been checked.
- Old save states are incompatible with this update; cold boot and load a normal in-game save. In-game saves carry over.

Found something? See [PLAYTESTING.md](release_docs/PLAYTESTING.md), and please attach a save. Changes are in the [changelog](release_docs/CHANGELOG.md).

## Credits
- Translation and testing: Jignx, with AI help from ChatGPT (Codex), Claude and DeepSeek. Every change was checked in-game by hand.
- Terminology reference: Akurasu
- Fonts: GohuFont by Hugo Chargois (WTFPL), adapted to a proportional font; Roboto Condensed by the Roboto Project Authors (SIL OFL 1.1)
- Tools: DeSmuME, xdelta

Super Robot Taisen L and all its characters, art and music belong to their respective rights holders. This project isn't affiliated with or endorsed by them. Please don't share ROMs or pre-patched games.
