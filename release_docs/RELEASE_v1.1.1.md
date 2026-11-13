## v1.1.1

A small follow-up to v1.1. Some of you said the narrow font looked rough, especially the capital
W and Y, so we redrew the worst letters. We also fixed battle quotes that ran past the edge of
the box.

### What changed

- Cleaner letters in story scenes and battle quotes. W, M, Y and T are redrawn, capitals and
  numbers are a pixel shorter so they sit better next to lowercase, and g, a, s, j, K, N, S, X
  and 0 are tidied up. Every letter keeps its old width, so no line moved.
- Fixed battle quotes that ran past the right edge of the box and left a stray letter on the
  next row, like Daiya's "We're giving it everything we've got!" in a Gaiking battle. About 170
  pages were re-broken to fit.

### How to patch

Same as v1.1: open `SRWL_English_v1.1.1.html` in your browser and pick your Japanese ROM, or
apply `SRWL_English_v1.1.1.bps` to the clean dump with the canonical header. Both work from the
Japanese ROM, so you don't need v1.1 first.

Back up your save and cold boot. Saves from v1.1 carry over.

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
- HTML patcher SHA-256: `a17fd39d5e1cec388d478065a360aade266d5a13df89795592dc4346c52a3c0d`
- BPS patch SHA-256: `73b7dd1bd2a086caf8bc9dec3ca031160cb693bf30526d07485ce9e46e658f96`
- Patched ROM: 128,452,668 bytes, SHA-256 `dd9f3b4424c0ec531e4093d57b65bbae8517425087cf1439b3b4f8b37dcb2dfd`
