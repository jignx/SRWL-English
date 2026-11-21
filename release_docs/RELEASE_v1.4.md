## v1.4

Bug fixes and small menu fixes. The script is the same as v1.3.2.

### Bugs from the original game we fixed
- Aoi's A.Combo: on maps, Aoi Hidaka's A.Combo was one level lower than the intermission screen showed, so she never reached level 3. It now matches.
- Great Booster ammo: with B-Save on the Great Mazinger, the Great Booster showed 4/6 instead of 6/6 and lost shots it shouldn't. It now gets its full ammo.
- Spirits after a support attack: Soul and Hot Blood (and Direct Hit, Mercy, Luck and Effort) boosted a support attack but stayed active afterwards. They are now used up, like after a normal attack.
- Combo attacks from the target list: pressing X on a Combo weapon's target list could start a battle that hit nothing or froze. It now starts the combo attack.
- Dannar Combination cut-in: when Anna or Mira started the Combination attack with Shizuru on board, the cut-in showed Goh instead of Shizuru. It now shows Shizuru.

### Other fixes
- Enemy info screen: the pilot labels "Nuke Missile" and "Stray Mach." no longer get cut off, and extra checks guard against the kind of crash fixed in v1.3.2 (Stage 12 ARMA).
- BGM add-on: a horizontal line that could show up in battle scenes is gone.
- Counter Settings: the blank "Always Counter" button now reads "Counter", and the help lines are no longer clipped.
- Upgrade screen: "Fund" is no longer clipped, and the weapon list header now reads "Atk".
- Weapon list: a stray pink dot next to the weapon icon is gone.

### How to update

- Re-patch from your Japanese ROM with `SRWL_English_v1.4.html` (or apply `SRWL_English_v1.4.bps` to the clean dump). A ROM patched with an earlier version can't be updated in place. Your saves keep working; back up your save and cold boot.
- **Using a BGM add-on:** use the v1.4 add-on. Earlier add-ons don't fit the v1.4 ROM.

### How to patch

Open `SRWL_English_v1.4.html` in your browser and pick your Japanese ROM, or apply `SRWL_English_v1.4.bps` to the clean dump. No earlier version needed. Saves from v1.1 and later carry over.

**BGM add-on:** in the HTML patcher, also pick `SRWL_English_v1.4_StereoBGM_addon.bps` (or `..._MonoBGM_addon.bps`) and it builds the BGM ROM in one go. It also works on an already-patched v1.4 ROM. The add-on files are downloaded separately from the GitHub release (links below). Flips or ROM Patcher JS work too. The ROM grows to about 266 MB (stereo) or 197 MB (mono).

Mirror downloads for the v1.4 BGM add-ons:

- Stereo: [Gofile](https://gofile.io/d/fdHC3rB8) · [1fichier](https://1fichier.com/?7dc46khps1cskb7unzoe) · [MEGA](https://mega.nz/file/DfphyLjS#5h93ZXpTBrfJTXP1d7G4oqPPgDFWRcCOsCw4EJxKOhk)
- Mono: [Gofile](https://gofile.io/d/KuRgBefu) · [1fichier](https://1fichier.com/?6l4xw2s40hs1pe9ufoxn) · [MEGA](https://mega.nz/file/KOBEyazY#6Ckc5Xhla47knCPnzYqN7zj1XPxvIubOwl6Q3s7eCbQ)

### Found a bug?

Please [open an issue](https://github.com/jignx/SRWL-English/issues) with the version, your emulator or hardware, where it happened, and a screenshot of both screens. A save near the problem helps. Please don't upload ROMs.

### Checksums (SHA-256)

- Japanese source ROM: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- `SRWL_English_v1.4.bps`: `2ac84747abf64cf26c985ddc790bbc98c53d77d3ab87cc261b25dbae0ebda4fb`
- `SRWL_English_v1.4.html`: `f500ab4a98fe537a7efbb2f3be7dacbaeb1d05f304d3e39dc39ffc0614ab463c`
- `SRWL_English_v1.4_StereoBGM_addon.bps`: `f2040026ae62f552d963ff01f027687d4e2084616950b11e1677ed39e404faf1`
- `SRWL_English_v1.4_MonoBGM_addon.bps`: `53cf58a727675e69f6fc385b80843c386b6d6546ab959cc3000bb16ecd952be3`
- Patched ROM: `cc7969fd4e6eeeb39c709d30219a3a89f959b9569f39a0f0fb94022501f0bc08`
- With stereo add-on: `efd428750a6d46b93710955bff859e80cc68e6acb0871c2087315714d386a682`
- With mono add-on: `04a5eab315b86c012bbad041318070989887e286a9b7f7e4e43a5504178a10d1`
