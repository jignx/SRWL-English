# Super Robot Taisen L -- English v0.9

An unofficial English fan translation for **Super Robot Taisen L** on Nintendo DS. This is a public playtesting release. Only an xdelta patch, checksums and documentation are distributed; supply your own clean Japanese cartridge dump.

## Features

- English story, battle dialogue, names, weapons, mission objectives and menus, with meaning/style reviews across stages 1--41 and alternate routes.
- Proportional English lettering and many translated graphic labels, series plates, pilot-name pictures, all 55 stage cards, title and boot copyright screens.
- Fresh Japanese-based translations of the opening narration and pre-Chapter 1 history, approved in-game.
- Gold English support attack/defend badges, with the Iczer-1 attack regression corrected.
- UI sweep fixes for Predict, support values, Potential levels, unit-panel spacing, Skill Parts and BGM layout. The BGM guard checks all 39 entries / 37 songs, including Godannar.
- Updated Will, Valor and Spirit terminology, custom name tokens, and guarded native text/graphics insertion.

## Download

Get `SRWL_English_v0.9.xdelta` and `CHECKSUMS.txt` from the **v0.9** release on this repository's Releases page. No prepatched ROM is supplied.

## Required clean source

Use a clean, untrimmed, unpatched Japanese ROM, game code **BRWJ**, revision 0.

- Size: **134,217,728 bytes**
- SHA-256: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- SHA-1: `f97ecb45c0313a44b15fdfed585ef4d5f32c4062`

The source CRC32 and all patch/output hashes are in [CHECKSUMS.txt](CHECKSUMS.txt). Stop if your source does not match.

## How to patch

1. Verify your clean ROM's SHA-256 against the value above.
2. Open an xdelta-compatible patcher such as Delta Patcher. Choose your clean ROM as **Original file** and `SRWL_English_v0.9.xdelta` as **Patch**.
3. Apply to a new output file. Keep your clean ROM unchanged.
4. Verify the patched ROM's SHA-256 and CRC32 against `CHECKSUMS.txt`.
5. Back up your battery save, then cold boot the patched ROM. Avoid loading an old emulator save state after changing patches; it can retain old code and graphics.

Command-line alternative:

```sh
xdelta3 -d -s clean-jp.nds SRWL_English_v0.9.xdelta SRWL_English_v0.9.nds
```

Patched ROM SHA-256: `8caaa39d45c18d532a2b5cb0115bb3dbc0f8487d6fa1d4fca22493b3fab762b2`.

## Validation and known limits

The release patch was applied to a fresh copy of the clean ROM; the result matches the build's SHA-256 and CRC32. The build has **0 insertion errors**, passes **12/12 overlay guards** and current engine-source verification, and cold-boots in DeSmuME QA. Narration screenshots match the game's renderer exactly; the history scroll was reached with a native scene-entry fixture.

Standalone tests: **99 modules / 583 tests**. The three known exceptions are `test_engine_source`, `test_spirit_marker_fix` and `test_text_presence`; all other modules pass. The legacy story-fit diagnostic remains at **4,073**, so this is not a claim of zero clipping or a complete route-by-route playthrough.

Some narrow labels, rare UI layouts, long names and alternate routes still need playtesting. The English ending staff roll remains disabled pending genuine ending-continuation verification; boot copyright screens are translated. Hardware and every route have not been comprehensively verified.

See [playtesting and bug reports](release_docs/PLAYTESTING.md) and the [changelog](release_docs/CHANGELOG.md).

## Credits

Thanks to the translation, engineering, editing and playtesting contributors; the Sol and DeepSeek passes; Brunom1's SRW L Let's Play for retained attributed dialogue/title references; Akurasu for terminology/context; and the emulator, xdelta and font authors. This project used AI assistance, including Codex, Claude and DeepSeek, with human review and playtesting. The two narration replacements are newly translated from Japanese.

Font acknowledgements: GohuFont by Hugo Chargois (WTFPL), with a project proportional adaptation; Roboto Condensed by the Roboto Project Authors (SIL Open Font License 1.1), used for raster lettering. Original game, artwork, music and character rights belong to their respective rights holders. This project is not affiliated with or endorsed by those rights holders.

Do not upload or redistribute source/patched ROMs or original game assets.
