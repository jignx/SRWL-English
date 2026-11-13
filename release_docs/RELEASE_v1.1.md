## v1.1 — More text on screen, and lines that read better

The biggest change in v1.1: we found a way to fit more text on each line, in both story scenes
and battle quotes. That extra room let us rework the script so it reads much more naturally.
This release also adds a browser patcher, so you no longer need a separate patching program.

**What's new:**
- **More text per line.** A new narrower font and engine changes let story and battle text use
  the full width of the text box, so each line holds noticeably more text than before. Far fewer
  lines are trimmed or split awkwardly, and lines that had been shortened to fit the old width
  are back to their full wording.
- **Flow pass, made possible by the extra room.** With space to spare, about 2,600 story and
  battle lines were reviewed against the Japanese and reworked where the English read stiffly or
  had to drop meaning to fit. Forms of address are more consistent, and leftover "-san"
  honorifics in battle are gone.
- **Battle quote fixes.** Battle quotes that showed the wrong line, lost part of their meaning or
  broke in odd places have been corrected, including Saruwatari's taunt and the "War of the Giants"
  line.
- **Name pass.** Did another name pass, so character and speaker names match the Japanese more
  closely.
- **New HTML patcher.** Patch the game right in your browser with `SRWL_English_v1.1.html`: no
  separate patching program needed. It works offline, uploads nothing, checks your ROM and the
  result, and handles both supported Japanese dumps.
- **Restored ellipses.** Pauses (…) that were dropped from the Japanese have been put back in
  about 800 lines.
- **More English graphics.** Fifteen more pop-ups are now in English: Iczer Robo Combine/Split,
  Mazin Power, Steel Power, Zero System, Link/Unlink (EVA umbilical cable) and Ammo Refill.
- **Pilot Stats page.** The CQB, RNG and SKL column headers now line up with their numbers, the
  "Q" in CQB is clearer, and the Intuition and Resupply Spirits no longer show as blank slots.

Everything from v1.0.1 is included.

**How to patch (easy way):**
1. Get your own clean Japanese dump of Super Robot Taisen L.
2. Download `SRWL_English_v1.1.html` from this release and open it in your browser. It works
   offline and nothing is uploaded.
3. Choose your Japanese ROM. The page checks it, patches it and saves `SRWL_English_v1.1.nds`.
   Both supported dumps work, and trimmed dumps are restored to full size first.

**How to patch (BPS):**
1. Use your clean Japanese dump with the canonical header (SHA-256 `a2b666a2…`, below).
2. Apply `SRWL_English_v1.1.bps` with Flips or another BPS patcher.
3. Check that the patched ROM is 128,452,668 bytes with the SHA-256 below.

If your dump has the zeroed extended header (`1bc8e2e0…`), use the HTML patcher instead: it fixes
the header for you, and BPS patchers will reject that dump.

Back up your save and cold boot the game. Old save states won't work, but normal in-game saves
carry over.

**Known issues:**
- The weapon Type line shows an extra comma for combination attacks and a few other types, for
  example `CQB, Combo,`. It's cosmetic only.
- Very long weapon, unit and pilot names are cut short on battle screens. This is on purpose and
  prevents crashes and wrong quotes. The names are unchanged everywhere else.
- The game hasn't been played start to finish on every route yet, so some late-game lines, rare
  menus or long names may still overflow.

**Found a bug?** Please [open an issue](https://github.com/jignx/SRWL-English/issues) and include
the patch version, your emulator or hardware, where it happened (stage, menu or battle), the steps
to make it happen again and a screenshot of both screens. A normal in-game save near the problem
helps a lot. See [PLAYTESTING.md](https://github.com/jignx/SRWL-English/blob/main/release_docs/PLAYTESTING.md)
for the full checklist. Please don't upload ROMs.

### Verification

- Canonical source SHA-256: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- Alternate-header source SHA-256 (HTML patcher only): `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f`
- BPS patch SHA-256: `dfa59203a10abc991bb7513aa96dcfba07769131efae0b70f7df6aff967a879c`
- Patched output SHA-256: `d6b89851a743d3526026fc3151df4501abeb022fd9dec5b3f2483e3cf891fcc7`

Only the patchers and checksums are attached. Supply your own clean Japanese dump.
