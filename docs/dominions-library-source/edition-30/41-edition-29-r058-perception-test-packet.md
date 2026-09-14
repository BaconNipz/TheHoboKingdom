# Edition 29 Working Paper - R-058 Perception Edges

**Prepared:** 31 August 2026  
**Base game:** unmodded Dominions 6.36  
**Status:** in progress; no runtime result has been claimed  
**Purpose:** settle the remaining boundary between innate Glamour, Mirror Image, Spirit Sight, blindness, and strategic information channels

## What this pass established

The strategic half of R-058 is no longer wholly unknown. The revision-2 main manual explicitly names two non-scout channels that can reveal Glamour units:

1. **Arcoscephale's special dominion scrying** reveals enemy units using Glamour to hide in provinces under Arcoscephale's dominion. The same information is available to disciple players.
2. **The Eyes of God** detects glamoured or invisible troops that are not stealthing inside the caster's own dominion.

These are narrow permissions, not proof that every form of scrying defeats Glamour. The manual's general scrying entry promises very accurate military information but does not say that ordinary scrying reveals Glamour units. Spy information is described as scout information plus extra province details, so it is not safe to treat Spy as a Glamour counter without a current observation.

The battle half remains open. The current technical definitions say that Spirit Sight sees invisible units and that True Sight sees through illusions and glamour. They do not say whether Spirit Sight or blindness changes the image-selection defence created by the innate Glamour trait. The current Mirror Image spell description also says that True Sight does not negate its images, so sight rules cannot be transferred from Blur, Displacement, or Invisibility by analogy.

## Evidence boundary

| Claim | Evidence | Publication state |
| --- | --- | --- |
| Innate Glamour grants Mirror Image in combat and hides the unit in friendly provinces | Main manual revision 2 and Modding Manual 6.36 | confirmed |
| Arcoscephale dominion scrying reveals enemy Glamour units | Main manual revision 2, Special Dominions | confirmed, narrow |
| Eyes of God detects non-stealthing Glamour or Invisible troops inside the caster's dominion | Main manual revision 2, spell description | confirmed, narrow |
| Generic scrying reveals Glamour units | no explicit statement found | open |
| A Spy reveals Glamour units | Spy is described as scout information plus other fields, but the concealment interaction is not explicit | open |
| Spirit Sight changes innate Glamour's images | no explicit current rule found | open; runtime test required |
| Blindness changes innate Glamour's images | no explicit current rule found | open; runtime test required |
| True Sight removes innate Glamour's images | technical wording and the Mirror Image spell description point in different directions for this exact case | open; use as a control, not an answer |

## Controlled battle matrix

The test must use one target chassis and one attacker chassis throughout. The target must have the innate **Glamour trait**, not only the Mirror Image spell. Every attacker variant must keep weapon, Attack, action points, size, morale, and script unchanged; only the perception state changes.

| Case | Attacker state | Target state | Purpose |
| --- | --- | --- | --- |
| B-00 | ordinary sight | no Glamour and no Mirror Image | confirm ordinary attack and damage flow |
| B-01 | ordinary sight | innate Glamour | establish the image-selection baseline |
| B-02 | Spirit Sight | innate Glamour | test the first unresolved interaction |
| B-03 | blind | innate Glamour | test the second unresolved interaction |
| B-04 | True Sight | innate Glamour | distinguish technical True Sight wording from Mirror Image behaviour |
| B-05 | Spirit Sight and blind | innate Glamour | determine whether blindness suppresses or coexists with Spirit Sight |
| B-06 | ordinary sight | Mirror Image spell only | separate spell-created images from the innate trait |
| B-07 | Spirit Sight | Mirror Image spell only | check whether any Spirit Sight result is trait-specific |
| B-08 | blind | Mirror Image spell only | check whether any blindness result is trait-specific |
| B-09 | True Sight | Mirror Image spell only | reproduce the current description's stated non-negation |
| B-10 | ordinary sight | Blur | positive control for a sight-countered glamour spell |
| B-11 | Spirit Sight | Blur | confirm the Spirit Sight control behaves as expected |
| B-12 | blind | Blur | confirm the blindness control behaves as expected |

### Run rules

- Use unmodded 6.36 for the result. A helper mod may create otherwise identical test units, but it must not replace the Glamour, Spirit Sight, True Sight, blind, or Mirror Image mechanics.
- Fix the map, participants, equipment, formation, orders, and game settings. Record the game seed if available.
- Use a high-accuracy, low-damage attack so images can be cleared without ending the test immediately. Do not compare raw hit totals between blind and sighted attackers unless their effective Attack values have been normalised.
- Capture the battle replay and the target's visible image state before each qualifying strike. Record whether the strike selected an image, removed an image, reached the real unit, missed for an ordinary Attack-versus-Defence reason, or failed for another defence.
- Run at least 100 qualifying strikes per stochastic case. If a sight state appears to remove the image layer deterministically, reproduce that result in ten fresh battles before classifying it.
- Repeat B-01 through B-05 with a second innate-Glamour chassis. This protects against an undocumented unit-specific property being mistaken for the general rule.

### Required battle record

| Field | Record |
| --- | --- |
| game version and build | exact title-screen value |
| mods | none, or helper-mod filename and SHA-256 |
| case ID and repetition | for example `B-02-017` |
| attacker and target identities | unit names and object IDs where available |
| attacker perception state | ordinary, Spirit Sight, blind, True Sight, or combined |
| target image source | innate Glamour, spell Mirror Image, Blur, or none |
| effective Attack and Defence | values at the moment of the strike |
| image count before and after | replay observation |
| resolution class | image, real unit, ordinary miss, other defence, or indeterminate |
| evidence locator | save, turn, battle, round, frame or timestamp, and screenshot filename |

## Controlled strategic matrix

Use one Glamour commander in a province friendly to that commander. The observing nation must not own the province. Hold the unit's Stealth state constant and change only the information channel.

| Case | Observer channel | Stealthing? | Current evidence | Needed result |
| --- | --- | ---: | --- | --- |
| S-00 | ordinary scout | no | manual says Glamour units cannot be discovered by scouts | reproduce as negative control |
| S-01 | scout with Spirit Sight | no | no explicit Glamour permission found | observe |
| S-02 | Spy | no | Spy is scout information plus extra province fields | observe; do not infer |
| S-03 | ordinary targeted scrying | no | general entry promises very accurate military information only | observe |
| S-04 | Arcoscephale special dominion scrying | no | explicitly reveals enemy Glamour units | reproduce as positive control |
| S-05 | Eyes of God inside the caster's dominion | no | explicitly detects glamoured or invisible troops that are not stealthing | reproduce as positive control |
| S-06 | Eyes of God inside the caster's dominion | yes | description excludes stealthing troops from the explicit detection sentence | observe |
| S-07 | Eyes of God outside the caster's dominion | no | explicit permission is limited to own dominion | observe |
| S-08 | battle or remote-attack report only | no | no persistent-map reveal rule established | observe separately from province intelligence |

For every strategic case, record both the province's military-information panel and the map display before and after hosting. A battle report that shows the unit is not the same result as the unit remaining visible in province intelligence next month.

## Decision rules

- A result changes the public rule only if the relevant positive and negative controls both behave correctly.
- A deterministic difference must reproduce on a second chassis and a fresh game.
- A statistical difference must include raw counts, sample size, and a confidence interval. Do not publish a percentage from replay impressions.
- If Spirit Sight or blindness changes hit chance only through Attack penalties but leaves image selection unchanged, classify the image interaction as **no observed effect** and document the separate statistic change.
- If a channel reveals the unit only while it is not stealthing, record that condition in the rule. Do not shorten it to “reveals Glamour.”
- If ordinary targeted scrying and the two named special channels disagree, preserve the difference. Special dominion scrying and Eyes of God must not be used to claim a universal scry rule.

## Register update

R-058 moves from **queued** to **in progress**. The strategic branch now has two confirmed narrow answers, while generic scrying, Spy reports, Spirit Sight against innate images, and blindness against innate images remain open. This working paper is the test specification; it is not a completed 6.36 reproduction.

