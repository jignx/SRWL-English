# Super Robot Taisen L -- English v0.9

An unofficial English fan translation for **Super Robot Taisen L** on Nintendo DS. This is a public playtesting release. Only an xdelta patch, checksums and documentation are distributed; supply your own clean Japanese cartridge dump.

## Introduction
Hello,
I was curious about using AI as a tool in order to translate a SRW game (been a fan for a long time now) and I kept having too much fun working on it while throwing deepseek, Claude, Chatgpt at it to push through every bug and fixes I could find.
In my opinion, using AI to help translate a game is far harder than I thought. While AI makes it easier, a lot of work is just figuring things out and applying solutions and waiting. I spent the past few weeks wrestling with SRW L and seeing bugs and issues crop up one over another.
After playing through it a bit and fixing all the bugs I could spot, I feel like this is good enough for a public release and something I'm proud of putting out into the world. Please do let me know if you find any bugs or issues while playing the game. I would be happy to fix them.

## Disclaimer
While the game has been fully translated from what I could explore and find, it has not been fully played from beginning to the end. There might still be bugs or translation issues near the end so please do let me know if you spot an issue and give a save so I can fix it. Also the ending credits has been untranslated due to not having an end game save to check out if it works. Overall it's a complete game from beginning to the end and I hope you enjoy it.
It's version 0.9 right now on release, I would happily update it to version 1.0 once I hear from other people beating the game before I could confidently say it's complete at 1.0

## Features
- Full English translation of the story, battle quotes, and unit, weapon, pilot and ability descriptions, with a story-wide consistency audit
- Official English name spellings for series, characters and mechs where they exist
- Terms familiar from other SRW games: Will, Valor, Spirit, CQB / RNG / SKL
- Menus and UI fitted to the screen, with labels sized and aligned to match the original layout
- Translated graphics: title and copyright screens, terrain icons, battle badges such as Support Attack
- Battle menu cleaned up: full Action / Counter / Defend / Evade tabs
- Distributed as an .xdelta patch: apply it to your own clean Japanese ROM

## Download
Grab `SRWL_English_v0.9.xdelta` and `CHECKSUMS.txt` from the [Releases page](../../releases). No pre-patched ROMs, please don't ask.
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
A clean Japanese ROM of the game (BRWJ, revision 0, 134,217,728 bytes). Two dumps are known and both work:
- SHA-256 `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- SHA-256 `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f` (same game, only the header differs)
If yours matches neither, the patch won't apply. If you got a "target window checksum mismatch" error with an older download, grab the patch again.
## How to patch
1. Check your ROM's SHA-256 against one of the hashes above.
2. Open Delta Patcher (or any xdelta patcher). Pick your ROM as **Original file** and the .xdelta as **Patch**, and save to a new file.
3. Optional: check the patched ROM against `CHECKSUMS.txt`. It should be `8caaa39d45c18d532a2b5cb0115bb3dbc0f8487d6fa1d4fca22493b3fab762b2`.
4. Back up your save, then start the game fresh. Don't load old emulator savestates, as they can bring back old text and graphics.
Command line:
```sh
xdelta3 -d -s clean-jp.nds SRWL_English_v0.9.xdelta SRWL_English_v0.9.nds
```
## Known issues
- The ending staff credits are still in Japanese (the translation is done, it just needs an ending save to test).
- The game hasn't been played start to finish on every route yet, so some late-game lines, rare menus or long names may still overflow.
- Tested in DeSmuME. Real hardware hasn't been checked.
Found something? See [PLAYTESTING.md](release_docs/PLAYTESTING.md), and please attach a save. Changes are in the [changelog](release_docs/CHANGELOG.md).
## Credits
- Translation and testing: Jignx, with AI help from ChatGPT (Codex), Claude and DeepSeek. Every change was checked in-game by hand.
- Terminology reference: Akurasu
- Fonts: GohuFont by Hugo Chargois (WTFPL), adapted to a proportional font; Roboto Condensed by the Roboto Project Authors (SIL OFL 1.1)
- Tools: DeSmuME, xdelta
Super Robot Taisen L and all its characters, art and music belong to their respective rights holders. This project isn't affiliated with or endorsed by them. Please don't share ROMs or pre-patched games.
