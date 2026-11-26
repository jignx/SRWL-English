## v1.5

NDS12 dialogue font, pilot-screen and menu fixes, UI and unit-name polish, another pass over names and story text, forward-compatible universal `.bgmpak` vocal BGM packs, and a built-in **Custom BGM Maker** tab in the HTML patcher.

### Screen fixes & font
- **New dialogue font (NDS12):** All story and battle dialogue now uses an official Nintendo DS BIOS-style Font B (`NDS12`, 95 printable ASCII glyphs with baseline-aligned punctuation), with every story and battle box reflowed to fit cleanly.
- Pilot screens: Spirit and Skill names that came up blank (`Intuition`, `Resupply`, `Attune`, `Disrupt`, `Combo Attack`, and others) now show in full on the map pilot page, the Spirit list, the level-up screen (with re-aligned 3-column Spirit spacing so Column 3 stays inside the border), and Upgrade Units.
- UI & terminology polish: Stat and weapon lists read `HIT` instead of `Hit`; pilot stats use `ACC` / `EVD`; weapon details show `Ignore` with full `Barrier` / `Size` and spaced effect levels (`HIT Down L2`); pilot skills use `Infight` / `Gunfight` / `S. Attack` / `S. Defend` (`S.Atk` / `S.Def`); Spirit commands use `Wall` / `Guard`; and abilities/items use `Status Immunity`, `Repair Unit`, `Resupply Unit`, `Sword`, `Gun`, `Shield`, `Beam Shield`, and `Anti-Beam Shield`.
- Menus: several labels that were blank or clipped now fit, including Shortcut Settings labels, the X List overlap, the SP list Unit column, and the `Side: Ally` row. `MAP Wpn` and `A.Combo` battle tags fit their window.
- Rei Ayanami's name plate now reads `Rei`, and Rey Za Burrel's reads `Rey`.

### Names and text
- Unit & weapon naming consistency: Standardized ZAKU short names (`Blaze ZAKU W`, `Gunner ZAKU W`, `Blaze ZAKU P`, `Slash ZAKU P`), Macross Frontier VF-25/RVF-25 pack names (`VF-25F Super F/B`, `VF-25S Armored F/B`, `VF-25G Super F/B`, `RVF-25 Super F/B`), and Gaiking's `Zaul Geyser`.
- `Chang Wufei` is now in that order in the story text.
- Honorifics are gone from Ai's plate and 51 battle quotes.
- Dancouga Nova's attacks use the official names (`Dancouho`, `Final Dancouho`, `Dancou Dangaiken`, `Dancouken`).
- Crow's `Machine Gun` is named correctly, and five lines that said Lou Liruri now say `Roo Riruri`.
- Three Choudenji lines now read `Super Electromagnetic`.
- About 20 typos and contractions fixed, plus a consistency pass (`Longo`, `Seimi`, `Bubby`, `Baleon`, `Borot`, `A.T. Field`, and others).
- Story lines break more smoothly: about 480 lines that left one word alone on the last row were rebalanced, and `{Ichitaka}` / `{Alice}` / `{Team}` lines were rebalanced so max custom names fit without clipping.

### Battle
- Safer text fitting in battle: long lines are checked more strictly, so quotes are less likely to cut off or glitch.

---

### How to patch (GitHub files)

Only `SRWL_English_v1.5.html`, `SRWL_English_v1.5.bps`, and `CHECKSUMS.txt` are hosted on GitHub. You need a clean Japanese ROM of the game (`BRWJ`, revision 0).

1. Download `SRWL_English_v1.5.html` from this release.
2. Open it in your browser (works offline; nothing is uploaded), choose your clean Japanese `.nds` ROM, and click patch to save `SRWL_English_v1.5.nds`.

*(Prefer your own patcher? Apply `SRWL_English_v1.5.bps` to the canonical clean dump with Flips and verify against `CHECKSUMS.txt`.)*

If you're updating from v1.4 or earlier: re-patch from your clean Japanese ROM (a previously patched ROM can't be updated in place). Your in-game saves keep working; back up your save and cold boot.

---

### Optional Vocal BGM Packs (Forward-Compatible `.bgmpak`)

To avoid hosting copyrighted music on GitHub, the optional vocal BGM packs are hosted on external mirrors as **universal `.bgmpak` files** instead of per-version `.bps` add-ons.

**Why `.bgmpak` is forward-compatible:**
- A `.bgmpak` pack contains only the custom stream player and audio streams — no base-ROM SDAT data and no hardcoded translation offsets.
- That means **one `.bgmpak` download works on clean Japanese SRW L, v1.3, v1.4, v1.5, and future English releases** — you won't need to re-download the music pack when future translation updates come out.

**External BGM Pack Downloads:**

| Pack | Best For | Size | Gofile | 1fichier | MEGA |
| :--- | :--- | ---: | :---: | :---: | :---: |
| **Stereo (`SRWL_StereoBGM.bgmpak`)** | Recommended — 3DS, emulators, modern flashcarts | 131 MB | [Download](https://gofile.io/d/d8DkQTtJ) | [Download](https://1fichier.com/?75b2mtft24n9gxevm0ve) | [Download](https://mega.nz/file/eaBHhLQA#OPyZcIG3Bji9HfDd60e6qmsbjVbPl52-mE3_Ct9MChc) |
| **Mono (`SRWL_MonoBGM.bgmpak`)** | Smaller file size / older flashcarts | 65 MB | [Download](https://gofile.io/d/rPVRdloF) | [Download](https://1fichier.com/?hsucl54q9puhqog2s9k9) | [Download](https://mega.nz/file/ee5kxJjK#iSNmuWw-EvII8u_mepwMupipWJqoqgPncCb3VjtD6wI) |

**How to apply a `.bgmpak`:**
1. Open `SRWL_English_v1.5.html` in your browser.
2. Select your clean Japanese ROM (or an already-patched English `.nds` ROM).
3. In the optional BGM section, select `SRWL_StereoBGM.bgmpak` or `SRWL_MonoBGM.bgmpak` and patch.

---

### How to Add Customized Music & Edit Song Titles

`SRWL_English_v1.5.html` includes a built-in **Custom BGM Maker** tab that runs completely offline in your browser:

1. Open `SRWL_English_v1.5.html` and switch to the **Custom BGM Maker** tab.
2. Load your clean Japanese ROM or patched `SRWL_English_v1.5.nds` (you can also load a downloaded `.bgmpak` as a starting base if you only want to replace a few tracks).
3. Pick any BGM slot, drop in your own audio file (`.mp3`, `.wav`, `.ogg`, `.flac`, etc.), choose Stereo or Mono, adjust volume/looping, and edit the **in-game song title**.
4. Export either a **patched `.nds` ROM directly** or a **custom `.bgmpak` pack** that you can reuse on future updates.

---

### Found a bug?

Please [open an issue](https://github.com/jignx/SRWL-English/issues) with the version, your emulator or hardware, where it happened, and a screenshot of both screens. A save near the problem helps. Please don't upload ROMs.

### Checksums (SHA-256)

- Japanese source ROM: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- `SRWL_English_v1.5.bps`: `39ae147b355bfa096475b5af96a4515789d80537fdb2760e216434d614c72fbf`
- `SRWL_English_v1.5.html`: `dccb0f10a40ea3c15388b4335921a16d0a4992f51b7324727764e34d7ec83c4a`
- `SRWL_StereoBGM.bgmpak`: `59045208829ea20fe90fc214c431e1581bb4c4c6f095f28907d97b962c7e419b`
- `SRWL_MonoBGM.bgmpak`: `9d8fc0e804f1f03c961df3ace50d4e647d9c556718024c789e00a1d9b16d946f`
- Patched ROM: `d716d4ac3bfea78c715696547a047258650814c262e0dabb1ad03f76d27c90f9`
- Patched ROM (Stereo BGM pack): `79a3ccf0e584ded96117061d51bbc44df8ac604383587513e4c73c2ab452a069`
- Patched ROM (Mono BGM pack): `b8ef3d872b1354bc1ac8dd289dca73e08a4bae42ca495cc92b9c40d92b9c78a6`
