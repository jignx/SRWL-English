# Changelog

## v0.9 -- 2026-10-25

- Publishes the merged story/meaning/style, overflow, description, terminology and graphics work summarized below as a patch against the clean Japanese revision-0 ROM.
- Includes the gold support-badge correction and Iczer-1 crash fix; Action-tab and tab-ghost fixes; UI sweep 2 wording/spacing; and the all-song BGM title guard.
- Includes the newly translated Japanese-based opening narration and history graphics, approved in-game.
- Verified by standalone tests (three documented exceptions), zero insertion errors, 12 overlay guards, cold-boot smoke, and fresh-source patch reapplication with matching SHA-256/CRC32.
- Uses the v0.9 checksums at the repository root. Historical build numbers below do not identify the v0.9 patch or its output.

## Historical development notes

This summary describes recorded development work and earlier release notes. It is draft documentation, not a fresh release certification.

## Unreleased work after v309

- Completed the full story meaning/style audit across stages 1-41, including alternate routes, the ending and epilogue. Applied approved stages 1-5 and 6-10 revisions; stages 11-20 received 519 revisions, stages 21-30 received 343, and stages 31-41 received 481. Character voices, meaning, grammar, contractions, apostrophes, ranks and settled wording were reviewed. Internal test labels were excluded.
- Reviewed all 622 high-risk story overflow rows and applied their revisions. Native insertion checks report zero overflows; the older story-fit diagnostic still reports 4,073 and must not be described as a clean full-playthrough result.
- Audited all 23,415 battle-quote pages for style and meaning. Applied 55 low-risk style fixes and 268 meaning fixes; retained the canonical Glain Neidr spelling instead of one conflicting proposal. Higher-risk style proposals remain review work. Repaired spaces beside dynamic name tokens in 13 pages and checked all 165 dynamic pages without changing their controls or substitution order. The approved Ichitaka/Alice voice pass is retained; Daiya and Lulu review drafts are separate from installed work.
- Audited non-dialogue descriptions, ability/skill/part names, units, weapons, mission titles, objectives and Spirit/UI labels. Applied 132 low-risk style rows and 23 meaning revisions; nine meaning findings were already satisfied. Four route-label proposals could not be repacked safely. Unresolved fit and identity questions remain listed for playtesting.
- Settled the mechanic terms **Will**, **Valor** and **Spirit** in place of Morale, Hot Blood and Yell. Applied 14 follow-up term records, including the missed Will -20 line. Ordinary dialogue uses of morale, yelling and hot-blooded remain context-dependent.
- Standardized character-name spellings, terminology, ranks and punctuation, with regression checks and a term-variant review.
- Added player and team name-token support in story text.
- Applied short mission titles to the relevant title strings; Clear Data short-title drafts remain separate from installed changes.
- Improved menu wording and fit, including bonus and Use-screen labels, battle-result EXP and upgrade accuracy text.
- Installed approved English series plates, ability/status and Spirit banners, BGM lettering and 29 pilot-name pictures. Added all 55 English stage cards, corrected title-to-card mapping and applied the approved title wording. Full enemy labels fit the tested story/battle headers; narrow fields still need coverage.
- Added map-result graphics, including the title-case Critical popup. Installed coloured terrain silhouettes on tested Unit Stats and Weapon Power screens: cloud for air, mountains for land, waves for sea and star for space. Added separate forecast dictionary pictures without changing shared alphabet or upgrade-bar art. Natural forecast checks cover air/land; sea/space were verified with renderer fixtures and still need natural gameplay coverage. Underground remains a draft.
- Localized the title plate and boot copyright screens in separate private title-art builds. The approved English logo retains the corrected straight lower border and red glow. Larger mixed-case copyright lettering preserves all 13 complete attributions, dates and copyright symbols within the original tile budgets; cold-boot and visual checks passed for those builds. This is distinct from the deferred ending staff-credit roll.
- Centered the search grid and recorded further map-screen and title-screen findings. Leftover text under orange tabs and icon-spacing blockers remain documented issues; do not assume every menu finding is fixed.
- Refined Turns, Save Data Name/Funds alignment, Overview, Combo, All Units/Team BGM, Swap Unit, Pick Unit/Pick PU, Stat/Now/After/Parts, Barrier + and Hit wording. Corrected texture tile counting while preserving native positioning. Some labels were verified only in specific layouts; Barrier + still needs a naturally reached example.

These entries summarize development across several local branches and private test builds. They do not claim that every change is merged into one published patch. No ROM, patch or new release certification is produced by this documentation update. Latest recorded broad checks retain known test failures; focused checks and earlier runtime evidence apply only to their recorded builds.

## v309 - 2026-10-22

- Existing cumulative English patch packet, including the approved text package and recorded graphics fixes.
- Source and output checksums are documented in the existing release packet. No new ROM or patch was generated for this documentation branch.

## Earlier work

- v308 recorded a passing full test run; v309 superseded it for testing.
- Earlier builds developed dialogue, battle text, names, menus, fonts and graphics through repeated audits and runtime checks.
- Historical test counts and screenshots describe their original builds; a new release requires validation of its own artifact.
