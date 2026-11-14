## v1.1.2

A hotfix for v1.1.1. A player reported that the patched game stayed on a white screen on a DSi
with a DSpico, while the Japanese ROM booted fine.

### What changed

- The ROM header now marks this as its own release: version 1 instead of the Japanese game's
  version 0. Pico Loader, which the DSpico uses, keeps a list of games that need an anti-piracy
  fix, and SRW L is on it by game code and version. When it found our ROM it patched the
  anti-piracy code as it loaded, on top of our own patch that already switches anti-piracy off,
  and the two together left the game on a white screen. With version 1 the loader no longer finds
  the game on that list and leaves the code alone, so only our fix runs.
- The game code stays BRWJ. Loaders look up the save type by game code alone, so the save chip
  is still detected correctly and existing saves keep working.
- Other flashcart loaders that keep a similar list will skip it the same way. That's fine,
  because our patch already turns anti-piracy off. Emulators ignore the version number.
- Nothing else changed. The text, font and graphics are the same as v1.1.1.

If you play on an emulator or a flashcart that already worked, you don't need this update, but it
won't hurt. If it still white-screens on your DSpico, please open an issue.

### How to patch

Same as before: open `SRWL_English_v1.1.2.html` in your browser and pick your Japanese ROM, or
apply `SRWL_English_v1.1.2.bps` to the clean dump with the canonical header. Both work from the
Japanese ROM, so you don't need an earlier version first.

Saves from v1.1 and v1.1.1 carry over.

### Known issues

- Combination attacks and a few other weapon types show an extra comma on the Type line
  (`CQB, Combo,`). It's only cosmetic.
- Very long weapon, unit and pilot names get cut short on battle screens on purpose.
- Nobody has played every route start to finish yet, so some late-game lines, rare menus or
  long names may still overflow.

### Found a bug?

Please [open an issue](https://github.com/jignx/SRWL-English/issues) with the patch version, your
emulator or hardware, where it happened (stage, menu or battle), how to make it happen again and
a screenshot of both screens. A normal in-game save near the problem helps a lot. Please don't
upload ROMs.

### Checksums

- Canonical source SHA-256: `a2b666a294df476688ea40e37b9ef53ed609a65bd4a14013ba730057247d594f`
- Alternate-header source SHA-256 (browser patcher only): `1bc8e2e0c3bc93eb10bcc189c829ee028590aa48b7f2e7cdb3a5723ee071f37f`
- HTML patcher SHA-256: `0c864bb0df5ea27e3b632a6f811d0742558f8c54c10e6adb38de5b55a591f938`
- BPS patch SHA-256: `cb86e11a3e72cdb9f5662ab8d838126a4334970e04ce119d91eda9d33f5b7e46`
- Patched ROM: 128,452,668 bytes, SHA-256 `b7d13764e408ddd2048f4aa87ad8ccf0c68f733413d59a5010f8b74c80da3fac`
