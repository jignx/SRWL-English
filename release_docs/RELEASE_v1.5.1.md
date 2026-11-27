# Super Robot Wars L — English Patch v1.5.1

## Highlights

- **Unified NDS12 UI Font (Font A → NDS12):** Swapped the entire UI font (menus, stats, weapons, units, spirits, skills, and battle HUD) to match the crisp NDS12 dialogue font introduced in v1.5, with tabular `6 px` alignment on `4` to keep numeric columns sharp.
- **Clear Hit / Accuracy Split:**
  - Pilot stat (`命中`): **`HIT`**
  - Weapon menu: **`Hit`**
  - Unit/Robot stat & PU Bonuses (`照準値`): **`Accuracy`** (widened the Unit Stats / Upgrades stat label column from `40 px` to `48 px` so `Accuracy` fits cleanly with zero collision; compact 24 px list headers use `Acc.`).
- **Level Up Box Spirit Overflow Fix:** Adjusted `ov10` Level Up Spirit slots to per-slot widths (`x=(9, 14, 19, 9, 15)`, `w=(5, 5, 6, 6, 6)`) inside the exact `x=9..25` box so `Intuition` (`40 px` in NDS12) and `Resupply` (`44 px`) never break the right border.
- **PU Bonuses & Spacing Polish:** Unified terrain bonuses to `Air: A` / `Land: A` / `Sea: A` / `Space: A` (and `S`), updated `Crit Hit +` → `Crit Rate +`, `Special Eva15%` → `Special Evd 15%`, and fixed `Combo Atk L1` / `In-Fight Lv +1` / `Gun Fight Lv +1` / `SupAtk Lv +1` / `SupDef Lv +1` consistency.
- **Enemy Plate & Targeted Fixes:**
  - Shortened `KATOU ORG. SOLDIER` (`93 px`) → **`Katou Troop`** (`61/64 px`) so it no longer overflows the green enemy plate.
  - Fixed Aoi's dialogue (`God Dannar` → **`Goddiner`**) and Sheryl's hospital dialogue (`leave hospital` → natural rewrite).
- **Full-Game Audit Pass (51,705 records):** Fixed lookalike proper-noun mistranslations (`Saviour`, `Darlian`, `Quinze`, `Mazinkaiser`, `Iczelio`, `Totsugeki Love Heart`, `Skull Harken`, `Dan Blade`, `Dan Stinger`, `Breaker Shoot`, `Dragon Hang`, `Jeeg Pantheroid`, `Volt Machine Spin`, `Volt Paralyzer`, `Gells-Ghe`, `Queadluun-Rhea`, `Mezura`, `Yajin`, `Susanoh`, `Sanc Kingdom`, `Super EM Whirlwind`, `Great Jama Kingdom`, `Diokia City`), broken multi-line skill descriptions, and over-trimmed v1.5 lines.

## Downloads & Checksums

| File | Size | SHA-256 | CRC32 |
|---|---:|---|---|
| `SRWL_English_v1.5.1.html` | `6,233,325` bytes | `586cc21cc4d0abec960815704bf785e5fe9642d4f28052dabb1c238d24bc4536` | `45C32065` |
| `SRWL_English_v1.5.1.bps` | `4,530,805` bytes | `2bf28932ff3dfb5e6a462c319b3176e28acf64ec3240737565166f4af71da175` | `2144DF1C` |
| `SRWL_English_v1.5.1.nds` *(patched output)* | `128,458,300` bytes | `08077538fcd0563023644b1f9e6c321006ccde166b5357c137277be79f000bd2` | `61D1DCE3` |

## Optional Vocal BGM Packs (Universal `.bgmpak`)

The universal `.bgmpak` vocal BGM packs from v1.5 work directly with `SRWL_English_v1.5.1.html` — no re-download needed if you already have them:

| Pack | Gofile | 1fichier | MEGA |
|---|---|---|---|
| **Stereo BGM** (`SRWL_StereoBGM.bgmpak`, 131 MB) | [Gofile](https://gofile.io/d/d8DkQTtJ) | [1fichier](https://1fichier.com/?75b2mtft24n9gxevm0ve) | [MEGA](https://mega.nz/file/eaBHhLQA#OPyZcIG3Bji9HfDd60e6qmsbjVbPl52-mE3_Ct9MChc) |
| **Mono BGM** (`SRWL_MonoBGM.bgmpak`, 65 MB) | [Gofile](https://gofile.io/d/rPVRdloF) | [1fichier](https://1fichier.com/?hsucl54q9puhqog2s9k9) | [MEGA](https://mega.nz/file/ee5kxJjK#iSNmuWw-EvII8u_mepwMupipWJqoqgPncCb3VjtD6wI) |
