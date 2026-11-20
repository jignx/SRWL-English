## v1.3.1

Fixes a freeze on the Saving screen when using the Stereo or Mono BGM add-on. Main patch unchanged.

With a v1.3 BGM add-on, saving on a map could leave the game stuck on "Saving... Do not power off." The save itself was written, so reloading it works. The music player now waits while the game is writing the save, instead of reading music at the same moment.

### How to update from v1.3

- **Using a BGM add-on:** open `SRWL_English_v1.3.1.html`, pick your Japanese ROM or your patched v1.3 ROM, add `SRWL_English_v1.3.1_StereoBGM_addon.bps` (or `..._MonoBGM_addon.bps`) and press Patch. With Flips, apply the v1.3.1 add-on to your patched v1.3 ROM (not to the v1.3 BGM ROM). Your saves keep working.
- **Not using an add-on:** nothing to do. The main patch and patched ROM are the same as v1.3.

### How to patch

Open `SRWL_English_v1.3.1.html` in your browser and pick your Japanese ROM, or apply `SRWL_English_v1.3.1.bps` to the clean dump. No earlier version needed. Back up your save and cold boot; saves from v1.1 and later carry over.

**BGM add-on:** in the HTML patcher, also pick `SRWL_English_v1.3.1_StereoBGM_addon.bps` (or `..._MonoBGM_addon.bps`) and it builds the BGM ROM in one go. It also works on an already-patched v1.3 or v1.3.1 ROM. The add-on files are downloaded separately from the GitHub release; download links will be added to these notes shortly. Flips or ROM Patcher JS work too. The ROM grows to about 266 MB (stereo) or 197 MB (mono).

### Found a bug?

Please [open an issue](https://github.com/jignx/SRWL-English/issues) with the version, your emulator or hardware, where it happened, and a screenshot of both screens. A save near the problem helps. Please don't upload ROMs.

### Checksums (SHA-256)

- Japanese source ROM: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- `SRWL_English_v1.3.1.bps` (same as v1.3): `39215bf4fb8dbccfc8cbcadb1dac07b882482566a2f879112e6a7f6b1a487203`
- `SRWL_English_v1.3.1.html`: `48452d46a15962f1a98b1d27a5136d38f9b01a9ec424147951c41d02be68327e`
- `SRWL_English_v1.3.1_StereoBGM_addon.bps`: `c1885c46950f52038be6d3bba6c19c324b7e2e9fca953061d8bf1c12b70a269d`
- `SRWL_English_v1.3.1_MonoBGM_addon.bps`: `9be2a8204c9ab1dd8efc358250f3cbd97ad9f379a0df3b0b17bfa17f31e12a05`
- Patched ROM (same as v1.3): `6ca621dd431f71a26ef8870161262e0c656c09b26729af0d9ab1f4b21607cdc0`
- With stereo add-on: `00cde860141abbe08bac6b4f844afe3583134b44fb2ed46b63633c3495b981d3`
- With mono add-on: `f1345a89129d59a302ad7354534833a0227473afb1f3868cbb31a47fe7680c85`
