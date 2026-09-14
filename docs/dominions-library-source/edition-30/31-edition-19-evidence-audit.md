# Progress Edition 19 — Evidence Maintenance Audit

**Release date:** 18 August 2026  
**Game baseline:** Dominions 6.35  
**Scope:** Foundation Books I–XIV and their website-ready retrieval layer

**Superseded note (20 August 2026):** Edition 20 advances the live baseline to 6.36 and completes R-016. The Edition 19 divergence entry that removed Frost Mist Weapons' Cold 1 requirement was based on an unsupported transcription and has been corrected in Book III; the official manual and current reference both require Water 7 and Cold 1. This file remains a historical release audit, not a current-rule source.

## Purpose

Edition 19 is an evidence-maintenance release, not a new Foundation Book. It closes three high-priority questions in their existing canonical chapters, strengthens the blessing divergence record, and preserves the separation between verified rules, current structured data, planning estimates, and unresolved engine behaviour.

## Questions closed in this edition

### R-006 — Growth and Death income

The current unmodded baseline is **2% income per Growth or Death step**. The revision-2 main manual prints 1%, but the later official Modding Manual 6.34 defines the default `#deathincome` value as 2. No official announcement through version 6.35 changes that default. The newer explicit default therefore governs the current reference, while the older manual entry remains recorded as a version conflict.

### R-007 — Order and Turmoil resources

The current unmodded baseline is **2% resources per Order or Turmoil step**. This agrees with the revision-2 main manual, and the complete official announcement ledger through version 6.35 contains no later general change. Unsourced three-percent tables are not treated as current evidence.

### R-015 — Ordinary dominion hosting order

The official rules now support the following macro-order:

1. step 6: Preach;
2. step 7: heretic preaching;
3. step 8: claim Thrones;
4. step 42: ordinary dominion spread;
5. step 43: dominion effects;
6. step 56: elimination;
7. step 57: victory.

The official manual also supplies the ordinary spread sources, check probabilities, local resolution rules, and cross-water reroll. It does not publish the random-number stream or the internal iteration order among simultaneous passive sources; Edition 19 does not infer either.

## Blessing evidence advanced

R-016 remains in progress, but the main blessing chapter now carries a revision-2 divergence register. It records current or officially patched differences for Inspirational Presence, Frost Mist Weapons, Resilience of the Earth, Fortitude, Reconstruction, Fear, Heroism, Fear/Dread stacking, Enchanted Blood, and passive Pretender effects outside friendly dominion.

The register is deliberately narrower than a claim of complete engine reproduction. Stacking, death, absence, damaging-hit, mount, shape, item, and display-versus-engine cases remain open until they have dependable evidence.

## Boundaries retained

Edition 19 leaves the following questions unresolved rather than converting estimates into rules:

- R-008: exact integer rounding points;
- R-009: current Commander Point base and exceptional stacking;
- R-010: sacred, slave, mount, shape, and related upkeep cases;
- R-011: exact unrest thresholds for Recruitment Points and Commander Points;
- R-012: exact fort-supply arithmetic, where official formula and example material conflict;
- R-013: commander starvation and exceptional survival cases;
- R-014: the full probability distribution inside the official awakening ranges;
- R-016: remaining blessing activation and interaction cases;
- R-017: exact Call God thresholds and special variants;
- R-018: same-turn Throne claim, loss, ownership, and victory edge cases.

## Source basis

The changed claims were checked against:

- the official Dominions 6 main manual, revision 2;
- the official Dominions 6 Modding Manual, version 6.34;
- the complete official Steam announcement record through version 6.35;
- the local version-6.35 structured Inspector snapshot where the claim concerned current object data.

No community assertion was promoted over contradictory or more recent official evidence.

## Retrieval and duplication audit

The website export contains:

- 16 canonical documents;
- 2,437 indexed sections;
- 106 glossary entries;
- 6 reading paths;
- 57 research-register items;
- 213 subject entries;
- 93 ability records;
- 213 maintained redirects.

All research-register primary anchors resolve. A scan for exact repeated sequences of 35 words or more found one document pair and 25 matching windows: the field-reference fort table repeated between the quick reference and Book II. That duplication is intentional because one occurrence is an operational lookup and the other is the explanatory canonical treatment. No new essay-level duplication was introduced.

## PDF verification

The linked reader was rebuilt after the layout correction and checked as follows:

- 768 A4 pages;
- 3,518,629 bytes;
- no blank pages;
- no replacement glyphs;
- no leaked Markdown markers;
- 2,437 outline entries, all resolving to valid pages;
- 4,268 internal links;
- 73 external links;
- visual inspection of the cover, research register, revised scale tables, dominion order, blessing divergence register, Call God boundary, and closing page.

**SHA-256:** `dcd4e0fce590d32891da6c48e8e729772c5277fdd2a322b407224a6e8f8a8f74`

## Next evidence pass

The most productive next pass is R-016, because additional blessing edge cases can be compared against current structured data and official patch history without requiring player-supplied testing. The remaining economy and Pretender questions should advance only when a reliable current source or controlled reproduction is available.
