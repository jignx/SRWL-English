## v1.3.2

Fixes a crash in Stage 12. Everything else is the same as v1.3.1.

Opening the info screen of the ARMA enemy unit in Stage 12 could freeze or crash the game. Its pilot's name is shortened to fit that screen, and the shortened label was written to the wrong place in the text buffer, so the text renderer ran past its memory. That label now goes where the renderer expects it.

### How to update

- Re-patch from your Japanese ROM with `SRWL_English_v1.3.2.html` (or apply `SRWL_English_v1.3.2.bps` to the clean dump). A ROM patched with an earlier version can't be updated in place. Your saves keep working; back up your save and cold boot.
- **Using a BGM add-on:** use the v1.3.2 add-on. The v1.3.1 add-ons don't fit the v1.3.2 ROM. The music and the player are the same as v1.3.1.

### How to patch

Open `SRWL_English_v1.3.2.html` in your browser and pick your Japanese ROM, or apply `SRWL_English_v1.3.2.bps` to the clean dump. No earlier version needed. Saves from v1.1 and later carry over.

**BGM add-on:** in the HTML patcher, also pick `SRWL_English_v1.3.2_StereoBGM_addon.bps` (or `..._MonoBGM_addon.bps`) and it builds the BGM ROM in one go. It also works on an already-patched v1.3.2 ROM. The add-on files are downloaded separately from the GitHub release; download links will be added to these notes shortly. Flips or ROM Patcher JS work too. The ROM grows to about 266 MB (stereo) or 197 MB (mono).

### Found a bug?

Please [open an issue](https://github.com/jignx/SRWL-English/issues) with the version, your emulator or hardware, where it happened, and a screenshot of both screens. A save near the problem helps. Please don't upload ROMs.

### Checksums (SHA-256)

- Japanese source ROM: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- `SRWL_English_v1.3.2.bps`: `eed96d08e6474fb1ebcc33d90e970ee18e8c0ea868f3917239468725af9b4f77`
- `SRWL_English_v1.3.2.html`: `31cf1f3bbf9c155a965c47699c08a1e24f63b2923c03accb2921263e7cee853f`
- `SRWL_English_v1.3.2_StereoBGM_addon.bps`: `394eaa0bbefd99c0ec91483859c548ea705d5a30fbd26e6164a046bfce5ddd27`
- `SRWL_English_v1.3.2_MonoBGM_addon.bps`: `6bf61b94506b2895dcb75b2f0b65bfda9d5d424346df03a16c7c0b80c1f2ddf2`
- Patched ROM: `d727da13ebe78a9da22ff3e4f8584565f406218e5eac579675032e60cea09797`
- With stereo add-on: `4c1bdcf5cd12fc1695b38ba0a5da47c6c7c173f8027cb78e57610687777569b3`
- With mono add-on: `9f7646da0e9bbb83836bb398c246f5ccec7156c4b27fe5dfc85e255634963858`
