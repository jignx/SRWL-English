## v1.0.1 — Battle quote and name fixes

A small update to v1.0 that fixes wrong battle quotes, a cut-off Combo label and some names.

**What's fixed:**
- **Combination attacks show the right pilots again.** Some battles showed the wrong speaker with
  an untranslated line, for example "Heero" during Steel Jeeg's Mach Drill, and left out the
  yellow Combo label. A long English weapon or unit name could run past a hidden battle slot and
  change how the game picked the quote. Mach Drill now shows Kenji and Tsubaki with the Combo
  label, and other battles that picked the wrong quote the same way are fixed too. This was
  present in v1.0 and earlier.
- **Combo label no longer cut off.** The yellow label on combination attacks is fully visible
  again.
- **Pilot names on one line.** Twenty-three enemy and NPC names that are drawn as pictures were
  split over two lines, and the speaker box cut off the top line. They now fit on one line: the
  numbered Angels, EVA Unit 01, SOUND ONLY, NERV Agent and NERV Staff, Neos Gold and Darius XVII
  keep their names, and seven longer ones are shortened to fit (Unk. Soldr, Logos Man, UN Officer,
  UN Soldier, Vajra Q., B. Galaxy, MP Machina).
- **Godannar names.** "Go Dannar" is now **Godannar** throughout, and the Go-Okusaer and
  Neo-Okusaer names now match the Japanese.
- **Clearer list menus.** On the Assigned Units, Pilot Abilities, Unit Stats and Skill Parts lists, column headers now use short labels that fit their columns (S.Atk, S.Def, Arm, Hit, Left), rows with no level keep their columns lined up, and the ability column shows an English marker instead of a Japanese one.

Everything from v1.0 is included.

**How to patch:**
1. Get your own clean Japanese dump of Super Robot Taisen L (134,217,728 bytes). Its SHA-256
   should match one of the two hashes below.
2. Download `SRWL_English_v1.0.1.xdelta` from this release.
3. Apply it to a copy of your **clean Japanese dump**, not to a v1.0 ROM, with Delta Patcher or
   xdelta3, keeping checksum validation on:
   `xdelta3 -d -s clean-jp.nds SRWL_English_v1.0.1.xdelta SRWL_English_v1.0.1.nds`
4. Check that the patched ROM is 128,485,436 bytes with the SHA-256 below.
5. Back up your save and cold boot the game. Old save states won't work, but normal in-game saves
   carry over.

**Known issues:**
- The weapon Type line shows an extra comma for combination attacks and a few other types, for
  example `CQB, Combo,`. It's cosmetic only.
- Very long weapon, unit and pilot names are cut short on battle screens. This is on purpose and
  prevents crashes and wrong quotes. The names are unchanged everywhere else.
- The game hasn't been played start to finish on every route yet, so some late-game lines, rare
  menus or long names may still overflow.
- Tested mainly in DeSmuME. Real DS/3DS hardware hasn't been fully checked.

**Found a bug?** Please [open an issue](https://github.com/jignx/SRWL-English/issues) and include
the patch version, your emulator or hardware, where it happened (stage, menu or battle), the steps
to make it happen again and a screenshot of both screens. A normal in-game save near the problem
helps a lot. See [PLAYTESTING.md](https://github.com/jignx/SRWL-English/blob/main/release_docs/PLAYTESTING.md)
for the full checklist. Please don't upload ROMs.

### Verification

- Canonical source SHA-256: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- Alternate-header source SHA-256: `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f`
- Patch SHA-256: `61aaa5880eec76c25086888da95236180b2291de2ec0b6a5981859f45327284e`
- Patched output SHA-256 (both sources): `648b7b6c918e10cc62e6dc7fbe690b71bb24d011acc2b18d4f6e7177fa4e9031`

Only the translation patch and checksums are attached. Supply your own clean Japanese dump.
