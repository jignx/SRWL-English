# Super Robot Taisen L -- English v1.5.1

An unofficial English fan translation for **Super Robot Taisen L** on Nintendo DS. Only patches are distributed; you supply your own clean Japanese ROM.

## Introduction
Hello,
I was curious about using AI as a tool in order to translate a SRW game (been a fan for a long time now) and I kept having too much fun working on it while throwing deepseek, Claude, Chatgpt at it to push through every bug and fixes I could find.
In my opinion, using AI to help translate a game is far harder than I thought. While AI makes it easier, a lot of work is just figuring things out and applying solutions and waiting. I spent the past few weeks wrestling with SRW L and seeing bugs and issues crop up one over another.
After playing through it a bit and fixing all the bugs I could spot, I feel like this is good enough for a public release and something I'm proud of putting out into the world. Please do let me know if you find any bugs or issues while playing the game. I would be happy to fix them.

## Features
- Full English translation of the story, battle quotes, ending credits, and unit, weapon, pilot and ability descriptions
- Translation has been checked to consistently keep within each series setting, lore and personality to ensure that the writing consistently captured the personality of the characters in the game.
- Official English name spellings for series, characters and mechs where they exist using Akurasu, Fansubs and Wiki as a source
- Terms familiar from other official SRW games like VTX30Y: Will, Valor, Spirit, CQB / RNG / SKL
- Unified NDS12 BIOS-style font across menus, stats, weapons, story scenes, and battle quotes, so lines keep their full meaning
- Menus fitted to the screen, plus translated graphics: title screen, terrain icons, battle badges and pop-ups
- Optional forward-compatible `.bgmpak` vocal BGM packs and an offline **Custom BGM Maker** built into the HTML patcher
- Anti-piracy checks disabled; JIT/dynarec works on melonDS Android and WatermelonDS

## Screenshots

| | |
| --- | --- |
| ![English title screen and main menu](screenshots/v15-title-screen.png) | ![Mari in Stage 23 story dialogue (NDS12 font)](screenshots/v15-story-1.png) |
| ![Kaji in Stage 23 story dialogue (NDS12 font)](screenshots/v15-story-2.png) | ![Unit upgrades screen with HIT stat and roster](screenshots/v15-upgrades.png) |
| ![Battle forecast: Seventh Angel vs Koenig Monster G and Sandrock Kai](screenshots/v15-battle-forecast.png) | ![Canaria cockpit cut-in and battle quote](screenshots/v15-battle-quote.png) |
| ![Canaria anime cut-in during battle](screenshots/v15-battle-cutin.png) | ![Seventh Angel AT Field badge and damage readout](screenshots/v15-battle-atfield.png) |

## What's new in v1.5.1
Unified the entire UI (Font A) to the crisp **NDS12** font, split **Hit / Accuracy** cleanly (`HIT` pilot stat, `Hit` weapon menu, `Accuracy` unit stat & PU bonuses in widened 48 px columns), fixed the Level Up box Spirit border overflow (`Intuition` / `Resupply`), polished PU bonus labels & spacing (`Air: A` / `Land: A` / `Sea: A` / `Space: A`, `Crit Rate +`, `Special Evd 15%`), shortened `KATOU ORG. SOLDIER` → `Katou Troop`, and applied a full-game 51,705-record audit pass (`Goddiner`, `Saviour`, `Darlian`, `Quinze`, `Mazinkaiser`, `Skull Harken`, `Dragon Hang`, `Susanoh`, `Great Jama Kingdom`, `Diokia City`, Sheryl's hospital line, and broken multi-line skill descriptions). Full list in the [v1.5.1 release notes](release_docs/RELEASE_v1.5.1.md). Re-patch from your Japanese ROM; your saves and v1.5 `.bgmpak` vocal BGM packs keep working.

## What's new in v1.5
NDS12 dialogue font, pilot-screen and menu fixes, UI/unit-name consistency (`Blaze/Gunner ZAKU W`, `Blaze/Slash ZAKU P`, `VF-25F/G` & `RVF-25` Super/Armored packs, `Zaul Geyser`, `Ignore` → `Barrier`/`Size`, `HIT Down L2` spacing, Level Up Spirit column alignment), plus another pass over names and story text. Now supports **forward-compatible universal `.bgmpak` vocal BGM packs** and a built-in **Custom BGM Maker** tab in `SRWL_English_v1.5.html` to add your own music and edit in-game song titles. Full list in the [v1.5 release notes](release_docs/RELEASE_v1.5.md). Re-patch from your Japanese ROM; your saves keep working.

## What's new in v1.4
Bug fixes and small menu fixes; the script is the same as v1.3.2. Fixed bugs from the original game: Aoi's A.Combo level on maps, the Great Booster's ammo with B-Save, Spirits staying active after a support attack, Combo attacks started from the target list, and the Dannar Combination cut-in showing Goh instead of Shizuru. Also: enemy info screen labels, a horizontal line in battle with the BGM add-on, the Counter Settings button and help text, Upgrade screen labels, and a stray dot in the weapon list. Full list in the [v1.4 release notes](release_docs/RELEASE_v1.4.md). Re-patch from your Japanese ROM; your saves keep working. If you use a BGM add-on, use the v1.4 add-on (earlier add-ons don't fit v1.4).

## What's new in v1.3.2
Fixes a crash in Stage 12: opening the info screen of the ARMA enemy unit (where its pilot's name is shortened to fit) could freeze or crash the game. Text and graphics are otherwise the same as v1.3.1. Re-patch from your Japanese ROM; your saves keep working. If you use a BGM add-on, use the v1.3.2 add-on (the v1.3.1 add-ons don't fit v1.3.2).

## What's new in v1.3.1
Fixes a freeze on the Saving screen when using the Stereo or Mono BGM add-on; the main patch is unchanged. If you use an add-on, re-patch with the v1.3.1 add-on (your v1.3 ROM or the Japanese ROM both work in the HTML patcher). Your saves keep working.

## What's new in v1.3
A dialogue and presentation pass: about 185 lines corrected for meaning and 380 polished for flow, full names on maps and area titles, and Mission Objectives that name the pilot they need. New: an optional vocal BGM add-on (stereo, with a mono fallback). Older changes are in the [changelog](release_docs/CHANGELOG.md).

## How to patch
You need a clean Japanese ROM of the game (BRWJ, revision 0). Only `SRWL_English_v1.5.1.html`, `SRWL_English_v1.5.1.bps`, and `CHECKSUMS.txt` are hosted on GitHub.

1. Download `SRWL_English_v1.5.1.html` from the [v1.5.1 release](https://github.com/jignx/SRWL-English/releases/tag/v1.5.1).
2. Open it in your browser (works offline, nothing is uploaded), choose your ROM, and it saves `SRWL_English_v1.5.1.nds`.

Prefer your own patcher? Apply `SRWL_English_v1.5.1.bps` with Flips and check the result against `CHECKSUMS.txt`. Dump hashes are in [HEADER_COMPATIBILITY.md](release_docs/HEADER_COMPATIBILITY.md).

### Optional Vocal BGM Packs (Forward-Compatible `.bgmpak`)
To avoid copyright issues on GitHub, the vocal BGM packs are hosted on external mirrors as universal **`.bgmpak`** files. Because `.bgmpak` packs contain no base-ROM SDAT data or hardcoded translation offsets, **one pack works on clean Japanese SRW L, v1.3–v1.5.1, and future English updates** — you don't need to re-download it for future releases.

| Pack | Best For | Size | Gofile | 1fichier | MEGA |
| :--- | :--- | ---: | :---: | :---: | :---: |
| **Stereo (`SRWL_StereoBGM.bgmpak`)** | Recommended — 3DS, emulators, modern flashcarts | 131 MB | [Download](https://gofile.io/d/d8DkQTtJ) | [Download](https://1fichier.com/?75b2mtft24n9gxevm0ve) | [Download](https://mega.nz/file/eaBHhLQA#OPyZcIG3Bji9HfDd60e6qmsbjVbPl52-mE3_Ct9MChc) |
| **Mono (`SRWL_MonoBGM.bgmpak`)** | Smaller file size / older flashcarts | 65 MB | [Download](https://gofile.io/d/rPVRdloF) | [Download](https://1fichier.com/?hsucl54q9puhqog2s9k9) | [Download](https://mega.nz/file/ee5kxJjK#iSNmuWw-EvII8u_mepwMupipWJqoqgPncCb3VjtD6wI) |

To apply: open `SRWL_English_v1.5.1.html`, load your clean Japanese ROM (or an already-patched English ROM), select your `.bgmpak` file in the optional BGM section, and click patch.

### How to Add Custom Music & Edit Song Titles
Open `SRWL_English_v1.5.1.html` and click the **Custom BGM Maker** tab (100% offline in your browser):
1. Load your clean Japanese ROM or patched `SRWL_English_v1.5.1.nds` (and optionally a `.bgmpak` as a base).
2. Choose a BGM slot, drop in your audio file (`.mp3`, `.wav`, `.ogg`, `.flac`, etc.), pick Stereo or Mono, adjust volume/looping, and edit the **in-game song title**.
3. Export a patched `.nds` ROM directly, or save a reusable `.bgmpak` pack for future versions.

Start fresh or load a normal in-game save. Old emulator savestates won't work.

No pre-patched ROMs, please don't ask.

## Compatibility
Tested on New 3DS, Ace3DS+ Wood, SuperCard and DSpico, plus DeSmuME and melonDS. The stereo BGM pack was tested on 3DS. On Android, **melonDS** is recommended (DraStic has an emulator bug that makes SRW L's world map screen appear very dark, even on the unpatched Japanese ROM).

## Report a bug
Open an issue with the version, emulator or hardware, what happened and how to repeat it, and a screenshot if you can. A save near the problem helps a lot. See [PLAYTESTING.md](release_docs/PLAYTESTING.md). Please don't upload ROMs.

## Credits
- Translation and testing: Jignx, with AI help from ChatGPT (Codex), Claude and DeepSeek. Every change was checked in-game by hand.
- Terminology reference: Akurasu
- Fonts: NDS12 by Caveras; GohuFont by Hugo Chargois (WTFPL), adapted to a proportional font; Roboto Condensed by the Roboto Project Authors (SIL OFL 1.1)
- Tools: DeSmuME, xdelta, BPS

Super Robot Taisen L and all its characters, art and music belong to their respective rights holders. This project isn't affiliated with or endorsed by them. Please don't share ROMs or pre-patched games.
