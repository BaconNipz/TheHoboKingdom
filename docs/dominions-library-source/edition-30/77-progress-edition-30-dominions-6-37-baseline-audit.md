# Progress Edition 30: Dominions 6.37 Baseline Audit

## Scope

This unit advances the current unmodded rules baseline from Dominions 6.36 to 6.37 without performing runtime tests or preparing test assets. It updates the official chronology, current-version website metadata, and command-layer version boundary. Historical version references remain historical, and the pinned 6.35 Inspector object snapshot is not relabelled as 6.37 data.

## Official evidence

The [official Dominions 6.37 Steam announcement](https://store.steampowered.com/news/app/2511500/view/717915822014595135) was published on 9 September 2026. A [SteamDB record of the same announcement](https://steamdb.info/patchnotes/25190634/) supplies the public date and build locator used for cross-checking.

The announcement contains six General bullets:

- correction of inaccessible level-nine research;
- correction of drowning sometimes failing on non-commanders;
- increased recovery delay after a Drake uses its breath weapon in melee;
- correction of a memory leak when switching between games;
- anti-cheat improvements;
- unspecified statistic and typo corrections.

The complete official chronology therefore contains 33 named public announcements and 1,096 change bullets through 6.37. The 2026 subtotal becomes four announcements and 100 bullets. Version 6.37 names no hash-prefixed mod commands, so the 226 patch-token total established through 6.36 does not change.

## Evidence boundary

The patch note does not identify which level-nine spells were affected, enumerate drowning triggers, state the corrected Drake delay, describe the anti-cheat changes, or name the objects covered by the generic statistic correction. No object row, formula, timing value, or affected roster entry is inferred from those omissions.

The evidence layers now read:

| Layer | Current label | Boundary |
| --- | --- | --- |
| Live executable and official patch baseline | Dominions 6.37 | Official changes through 9 September 2026 |
| Main manual | Revision 2 | Separately versioned general rules source |
| Live Modding Manual | 6.36 | One release behind the executable |
| Complete command-locator extraction | 6.34 | Retained until every token and page locator is rebuilt |
| Structured object register | Inspector 6.35 pinned commit | Not silently promoted to 6.37 |

## Files changed

- `README.md`: current release and patch-history baseline.
- `00-master-plan.md`: current release statement and Book XIII chronology totals.
- `26-foundation-book-xiii-official-patch-history.md`: 6.36 and 6.37 release rows, 6.37 maintenance impact, totals, and current-baseline language.
- `28-foundation-book-xiv-command-terminology-lexicon.md`: 6.37 executable boundary, 6.36 live manual distinction, and unchanged 226-token patch total.
- `tools/build_website_exports.py`: 6.37 edition, article, and unmodded-dossier ruleset metadata, with the working draft correctly based on the 8 September Edition 29 release.
- `tools/build_dossier_pdfs.py`: default current-baseline subtitle for future reader builds.
- `website/*.json`: regenerated draft exports after validation.

## Unresolved work preserved

R-047, R-058, and all other engine-dependent claims remain open. The new research, drowning, Drake-delay, anti-cheat, statistic, and typo details are also left unresolved wherever the official note does not supply a complete rule or object list.

## Validation

- Website export: pass as a Progress Edition 30 working draft.
- JSON parse: pass for all nine generated website files.
- Corpus inventory: 16 reader documents and 3,093 unique section anchors.
- Ruleset metadata: 654 dossier sections carry `dom6-6.37-unmodded`; none retains the superseded `dom6-6.36-unmodded` tag.
- Python syntax: pass for navigation, website-export, and dossier-reader builders.
- Structured links: no new unresolved target; the six inherited unresolved references remain exactly the previously recorded set.

## Publication boundary

This is an unpublished Progress Edition 30 working checkpoint. It is not a release commit, website deployment, or repository push.
