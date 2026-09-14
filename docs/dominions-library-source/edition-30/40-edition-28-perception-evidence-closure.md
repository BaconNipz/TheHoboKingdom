# Progress Edition 28 - Perception and Ability-Evidence Closure

**Release date:** 30 August 2026  
**Base game:** Dominions 6.36  
**Official baseline:** revision-2 main manual, Modding Manual 6.36, and official changes through 6.36  
**Current-description baseline:** pinned 6.35 Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`

## Scope

Edition 28 returns to the three P1 Book XI questions R-047 through R-049. It resolves the category-level perception question, advances the ability-stacking question with explicit confirmed cases, and replaces an underspecified Hall-of-Fame research route with a versioned raw-observation protocol. It does not promote inherited Dominions 5 formulas or treat a data description as a controlled runtime test.

## Source record

| Source | Version or identity | SHA-256 or commit | Use |
| --- | --- | --- | --- |
| Dominions 6 main manual | revision 2 | `65f430fd97c9f27285d63b797b43bc7fe3844241fdf40230b1d25a901ab9f33f` | Player-facing Glamour, Invisibility, Darkvision, and Hall-of-Fame rules |
| Dominions 6 Modding Manual | 6.36 | `9d4a7d2c5101679de7080455ceebed41b25a1e9beba275985e293183269399cf` | Current technical definitions for Glamour, Spirit Sight, True Sight, Invisibility, Unseen, Illusion, Spiritform, Standard, and Inspiring Researcher |
| Official 6.36 announcement | 17 August 2026 | preserved in `data/official-update-6.36.json` | Patch overlay; no perception-family correction found |
| Dominions 6 Inspector | pinned 6.35 source | `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc` | Current spell and item description layer for Blur, Displacement, Invisibility, Mirror Image, Spirit Sight, and True Sight |

All sources were checked on 30 August 2026. The Inspector source is one game patch behind the live baseline, so its descriptions are used only after checking the official 6.36 announcement for a relevant change.

## Status changes

| ID | Edition 27 | Edition 28 | Result |
| --- | --- | --- | --- |
| R-047 | queued | in progress | Official formula boundary recorded; controlled observation template and first three test questions published |
| R-048 | queued | completed | Glamour, Invisibility, Unseen, Illusion, Spiritform, Blur, and Displacement separated by rule path; remaining runtime edges moved to R-058 |
| R-049 | queued | in progress | Standard, Inspiring Researcher, experience, Horror Mark, and the Blur/Displacement/Invisibility group classified; no universal source-precedence rule asserted |
| R-058 | absent | queued | Narrow test for innate Glamour's Mirror Image and non-scout strategic information channels |

## Perception result

The old family-level wording encouraged a false equivalence: several effects make a unit difficult to target, but they do not use the same mechanic. Edition 28 divides them into strategic concealment, melee Attack penalties, image selection, temporary states, and technical creature classes.

| Subject | Settled current result | Evidence | Remaining boundary |
| --- | --- | --- | --- |
| Glamour trait | Strategic concealment plus Mirror Image; adds 25 only to existing Stealth | OM and MM 6.36 | Spirit Sight and blind interaction with the innate images remains R-058 |
| Invisibility | Spirit Sight governs documented strategic patrol detection; live technical rule applies −10 melee Attack without Spirit Sight | MM 6.36 | Revision-2 manual's −9 is superseded, not silently deleted |
| Unseen | Uses Invisible behaviour and ends when hit; the current Invisibility spell grants this state | MM 6.36 and UI | No separate universal permanence claim |
| Blur | −2 melee Attack; True Sight, Spirit Sight, and blindness ignore it | UI | None at the category level |
| Displacement | First strike −10, later strikes −5; True Sight, Spirit Sight, and blindness ignore it; does not stack with Blur or Invisibility | UI | None at the category level |
| Mirror Image | Image-selection defence; the current spell description says True Sight does not negate it | UI | Innate Glamour versus Spirit Sight and blindness remains R-058 |
| Illusion | Spiritform-like creature class that remains susceptible to illusion magic despite Mindless | MM 6.36 | Individual spells still require their own target checks |
| Spiritform | Spirit-like class with defined immunities; no generic concealment or targeting penalty | MM 6.36 | Individual immunities remain ability-specific |
| Darkvision | Reduces darkness penalties only; does not help when blind | OM and MM 6.36 | It is not an anti-concealment substitute |

### Version conflict retained

The revision-2 main manual gives a −9 melee Attack penalty for Invisibility. The current 6.36 Modding Manual gives −10. Edition 28 uses −10 for the live 6.36 rule and keeps −9 only as a source-labelled historical value.

## Ability-stacking result

R-049 cannot be answered by a source hierarchy such as “items override spells” or “different sources stack.” The effect owns the rule. Standard and Inspiring Researcher are highest-only; Displacement explicitly does not stack with Blur or Invisibility; experience and Horror Mark accumulate in their documented ways; unlike defensive families can remain separate resolution gates.

The new matrix records only these verified cases. Every other form, item, bless, and spell interaction remains ability-specific until its description or a controlled test establishes the result.

## Hall-of-Fame result

R-047 remains open because the official manuals do not publish the score weights, tie order, heroic-family selection weights, or growth formulas. Edition 28 adds `data/edition-28-hall-of-fame-observation-template.csv`, which requires exact version, seed, commander identity, before-and-after Hall state, battles, kills, heroic family, displayed values, survival, and evidence locators.

The first controlled series separates survival from credited kills, then tests exact ties, then measures heroic growth across hosting while Hall membership is held constant. No equation should enter the public register until that series or an engine-backed trace can reproduce it.

## Publication artifacts

| Artifact | Pages | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Complete Knowledge Library, Progress Edition 28 | 811 | 3,701,338 | `1772cfdeee023abe13931f431808f2c4a1f1f22fe6298457028667f3072ec777` |
| Core Rules and Strategy | 378 | 1,723,564 | `bf7c708a90b6fa7f40d30e1528e1ffd81aa963b4ef6025daffe147ea1126c47c` |
| Middle Age Nation Compendium, Volume I | 101 | 461,047 | `7fc4a5a6f6ca230eaf6307f057370a19a02f9129b9db3fedf8c6f3eb05db5b6c` |
| Technical and Modding Reference | 346 | 1,519,009 | `db36560bb2511d0bf7aabd3f34cf1b840be42a0c6a5d234d5b5ad21f5243ce30` |
| Turn and Economy Quick Reference | 12 | 107,868 | `56c9b8e88972b2acf02f20c0b940acd548dbcc527df32bf10da6bd1226ba50a1` |

## Quality record

- corpus validation: 16 reader documents, 2,527 headings, 226,264 words, 624 internal links, no unresolved link or corpus errors, and no cross-document duplicate group at the 40-word threshold;
- style audit: completed with the standing whole-corpus tendency counts and no release blocker;
- full-PDF structural check: 811 pages, 4,465 link annotations, 425 top-level outline entries reported by the parser, no empty page, and all Edition 28 target phrases located;
- split-reader structural check: 837 total pages across four files, 4,054 link annotations, embedded outlines, and no empty page;
- visual render check: omnibus and split-reader covers, research-register continuation, stacking table and continuation, perception matrix and continuation, and Hall-of-Fame protocol and continuation inspected without clipping or broken page flow;
- website export validation: 17 JSON files parse; the generated corpus reports 58 research items, including completed R-048 and queued R-058; all three Edition 28 CSV files have consistent column counts.
