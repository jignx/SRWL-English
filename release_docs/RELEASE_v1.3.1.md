## v1.3.1

Fixes a freeze on the Saving screen when using the Stereo or Mono BGM add-on. Main patch unchanged.

With a v1.3 BGM add-on, saving on a map could leave the game stuck on "Saving... Do not power off." The save itself was written, so reloading it works. The music player now waits while the game is writing the save, instead of reading music at the same moment.

### How to update from v1.3

- **Using a BGM add-on:** open `SRWL_English_v1.3.1.html`, pick your Japanese ROM or your patched v1.3 ROM, add `SRWL_English_v1.3.1_StereoBGM_addon.bps` (or `..._MonoBGM_addon.bps`) and press Patch. With Flips, apply the v1.3.1 add-on to your patched v1.3 ROM (not to the v1.3 BGM ROM). Your saves keep working.
- **Not using an add-on:** nothing to do. The main patch and patched ROM are the same as v1.3.

### How to patch

Open `SRWL_English_v1.3.1.html` in your browser and pick your Japanese ROM, or apply `SRWL_English_v1.3.1.bps` to the clean dump. No earlier version needed. Back up your save and cold boot; saves from v1.1 and later carry over.

**BGM add-on:** in the HTML patcher, also pick `SRWL_English_v1.3.1_StereoBGM_addon.bps` (or `..._MonoBGM_addon.bps`) and it builds the BGM ROM in one go. It also works on an already-patched v1.3 or v1.3.1 ROM. Flips or ROM Patcher JS work too. The ROM grows to about 266 MB (stereo) or 197 MB (mono).

### Found a bug?

Please [open an issue](https://github.com/jignx/SRWL-English/issues) with the version, your emulator or hardware, where it happened, and a screenshot of both screens. A save near the problem helps. Please don't upload ROMs.

### Checksums (SHA-256)

- Japanese source ROM: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- `SRWL_English_v1.3.1.bps` (same as v1.3): `39215bf4fb8dbccfc8cbcadb1dac07b882482566a2f879112e6a7f6b1a487203`
- `SRWL_English_v1.3.1.html`: `3b4d9e0fe7ab5a688366d65eb27f1ab716501b9e3c489d652f54609f12b3c27a`
- `SRWL_English_v1.3.1_StereoBGM_addon.bps`: `ed743e5bbc2ae711b10905584e6d6d50e4875a6fe0b6d78e38a8d8e1e2a9fd7e`
- `SRWL_English_v1.3.1_MonoBGM_addon.bps`: `3f999118f065ef5c63a7049026c4fc6756a8848be013dff88c675c5df20ed4e6`
- Patched ROM (same as v1.3): `6ca621dd431f71a26ef8870161262e0c656c09b26729af0d9ab1f4b21607cdc0`
- With stereo add-on: `ba5bf54d28052d637efed1905dab1129a1bc8da2521c989a56bf9d696742b54f`
- With mono add-on: `9f62a7fa39ede82c5e69c451eb8af7c8cc2255676a56c511e45ad2e9b262c465`
