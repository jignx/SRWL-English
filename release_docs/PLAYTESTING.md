# Playtesting and bug reports

Test the exact patch version named in your packet. Verify the source and patched-output checksums, back up your battery save, cold boot and load normally. Old emulator save states may retain outdated code, fonts and text.

## What to check

- Title/copyright: cold boot through the licensor logos, grey fade, black copyright background, English title and menu. Check the logo border/glow, readable lettering, all 13 copyright attributions and dates, wrapping and clipping on both screens. Exercise New Game, Load and Continue, then leave the title idle through its attract sequence. Record whether your patch includes the separate title-art work.
- Forecast terrain icons: check cloud/air, mountains/land, waves/sea and star/space in naturally reached battles, including enemy-phase and alternate forecast layouts. Verify colours, rank letters and hit percentages, with no missing icons or displaced text. Sea/space evidence so far uses renderer fixtures. Compare Unit Stats and Weapon Power, formation and sortie grids as well.
- Spirit names: verify Will in stats/effects and Valor/Spirit in command lists, descriptions, search, compact markers and battle banners. Check Flash, Wall, Hope, Fury and Break consistently, including selection, targeting and casting. Check centring and long descriptions; do not report ordinary dialogue words such as morale or yell as automatic terminology errors.
- Battle quotes: check meaning, speaker identity and voice throughout the cast, especially the remaining Daiya/Gaiking and Lulu review work. Look for missing apostrophes, lost spaces beside custom player/team names, incorrect attack-name casing, clipped final words and pages needing more than three rows. Preserve route and trigger details in reports.
- Overflow: clipped or overlapping text, missing final letters, broken wrapping, page transitions and text outside boxes.
- Names: consistent spellings in dialogue, pilot and unit lists, weapons and battle quotes; custom player and team names should substitute correctly. Try long names as well as defaults.
- Menus: title and load screens, intermission, settings, search, upgrades, unit and pilot details, objectives and mission titles. Check cursor alignment, tab spacing, numbers and labels.
- Battle screens: command lists, status and terrain icons, attack names, animation quotes, damage and result popups, EXP and level-up displays.
- Routes at stages 21/22: exercise each available branch, record the choice and stage actually reached, and check dialogue, objectives, transitions and save/load behavior on both paths.
- Routes at stages 29-31: cover each available route and stage transition, recording earlier choices and conditions. Check speakers, names, battle events, objectives and progression through the next stage.
- Revisit alternate routes with separate saves; record routes you could not test rather than marking them complete.

## Open items carried from development records

These are targeted checks from the development STATUS/ISSUES records and their follow-ups, not a claim that every old issue is still present. Later fixes supersede older entries; report the behavior of your exact patch.

- v0.9 includes the Action-tab and tagged-tab ghost fixes. Recheck Abilities/Skill Parts/BGM, the Upgrade Units tick, the mark before Wasteland and Sortie Auto for remaining layout-specific residue.
- Icon-to-name spacing in unit, weapon, pilot, Skill Parts, Change Pilot and Upgrade fields; narrow Macross picture names must remain visible. Check Will/Lv/value separation, three-digit Will, alternate Combo layouts, and Spirit search-name centring.
- Katou Organization Soldier and Mass-Produced Machina in 72px fields and nonstandard forecasts. Check long weapon names against the forecast's measured 112px field, rather than assuming the 128px catalog limit guarantees fit. Six longer Macross labels still need layout/wording follow-up.
- Dialogue baseline, bearings and spacing, especially gaps around lowercase r/f/t and the reported Sawatari spelling split. Distinguish literal spaces from font spacing; capture full screens at native resolution.
- Full names and descriptions still blocked by fit or identity: support-attack/defense and skill-level labels, Form/Combine, Rage/Guts/Special Eva, Mimetic/Super Mimetic/Domega/Gargoras, Hiiragi/Rongo identity, and VF-25S/25G/RVF-25 shared Armored/Super picture labels. Check other uncertain spellings against the Japanese before proposing changes.
- Clear Data title scrolling and mission-title/card agreement, including split cards at stages 3, 8, 21 and 29-31; long titles must scroll without losing words. Four route-label description proposals remain unapplied because of shared storage limits.
- v0.9 installs the gold support badges and the Iczer-1 attack crash correction. Exercise both support roles with animations on/off, and check target-select/forecast action labels. World-map region badges and untested variants remain separate coverage items.
- Trigger Barrier + bonuses and animation-off Critical results naturally. Check bonus prefixes and label prefixes, including labels that formerly used a special formatting prefix.
- Ending staff credits remain deferred and disabled in production: English page fixtures were checked, but genuine ending-state continuation is still required. Do not confuse these with the translated boot copyright screens.
- Recheck save loading, Upgrade Units purchases/cancel and long-name Stats/Weapon Power screens. Earlier freezes were fixed; retain these as regression checks, not currently confirmed defects. Broad UI, rare layouts, hardware and a complete route playthrough remain coverage gaps.

## Report a bug

Open an issue in the project's issue tracker with a short descriptive title. Include:

1. Patch version, patched-ROM checksum, emulator/version or hardware, and whether you cold booted.
2. Stage, route choices, speaker or exact menu path, and the loaded battery-save slot.
3. Numbered button/menu steps, expected result, actual result and how often it happens.
4. A screenshot showing both DS screens; an English description and record ID if known are sufficient.
5. A suggested correction if you have one, and a copy of a battery save near the trigger when needed. Review attachments for personal information before sharing.

Do not upload source or patched ROMs. A save state can be supplementary evidence, but include normal-save reproduction steps. Never overwrite your only progress save to test a report.
