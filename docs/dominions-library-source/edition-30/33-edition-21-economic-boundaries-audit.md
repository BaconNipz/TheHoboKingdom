# Progress Edition 21 - Economic Boundaries Audit

**Release date:** 21 August 2026  
**Live game baseline:** Dominions 6.36  
**Structured object snapshot:** Dominions 6.35 Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`  
**Scope:** Book II, the Turn and Economy Quick Reference, Evidence Ledger, Reader's Guide, website exports, and the linked reader's PDF

## Purpose

Edition 21 is an evidence and maintenance release rather than Foundation Book XV. It returns to R-008 through R-013, adds only the findings supported by official documentation, current structured data, or a specific published in-game observation, and keeps every unresolved integer boundary visible.

## Canonical placement

The economic material remains in Book II. The field reference carries only the values needed during play; the Evidence Ledger records provenance and uncertainty; the Reader's Guide routes each research question to the authoritative heading. No second economy chapter or stand-alone general volume has been created.

## Research decisions

| Item | Edition 21 decision | Evidence boundary |
| --- | --- | --- |
| R-008 - rounding | Remains queued | One official resource example floors an intermediate value, but the aggregate figures do not reconcile; the full order of income, resource, RP, and fort-draw rounding is not documented. |
| R-009 - Commander Points | Completed | Official fort bonuses, `#slowrec`, `#rpcost`, and AI exclusions are combined with the current community record of the one-point base and multi-month accumulation. |
| R-010 - upkeep | In progress | The published 6.33 observation establishes Sacred-Slave stacking and a mounted component split; the 6.35 object snapshot independently preserves separate bases and tags. Shapechanged bases and fractional monthly aggregation remain open. |
| R-011 - unrest and recruitment capacity | Remains queued | The official 100-unrest shutdown is secure. Community references report percentage reductions before that point, but do not publish the required boundary reproduction. |
| R-012 - fort supply | Remains queued | The official manual supports both a multiplier-of-six formula and multiplier-of-four examples. Current community material follows six, but does not resolve the documentary conflict with a versioned distance series. |
| R-013 - starvation | In progress | `#neednoteat` establishes explicit immunity and update 6.18 confirms that transformation into a non-eating entity removes Starving. Generic commander feeding priority is not promoted to immunity. |

## Commander Point result

For an ordinary current province, the local pool is one base Commander Point plus the current fort bonus. Palisades therefore remain at one, Fortress and Castle provide two, and Citadel and Grand Citadel provide three. Multi-point commanders accumulate capacity over several months. `#slowrec` doubles the commander's cost; it does not alter the province pool. The main manual's AI bonuses explicitly exclude commander recruitment rate and Holy Points.

This closes R-009 at a mixed **Official plus Community-tested** tier. The remaining unrest question is separate: R-011 asks how much of the usable pool survives below the official shutdown at 100 unrest.

## Upkeep result

The revision-2 manual gives ordinary upkeep as gold cost divided by 15 each month and Sacred or Slave upkeep as gold cost divided by 30. A dated in-game observation under version 6.33 reports that Sacred and Slave reductions stack to a divisor of 60. It also decomposes Logrian Cavalry into a 10-gold rider and 20-gold War Horse, displaying 8 and 16 annual upkeep respectively.

The pinned 6.35 object snapshot supports the component model rather than a shortcut based on the visible recruitment card. Rider and mount have separate cost bases and separate Sacred or Slave flags. A mounted audit must therefore inspect both objects. This does not settle which base every transformation form uses or how hidden monthly fractions are accumulated.

## Starvation result

The Modding Manual makes Need Not Eat the decisive explicit tag: the unit consumes no supplies and cannot starve. It also describes how a negative supply bonus may reintroduce consumption without reintroducing starvation, proving that supply use and starvation eligibility are separate states. Official update 6.18 adds the transformation boundary by removing Starving when a unit becomes a non-eating entity.

The 6.35 object snapshot contains 985 Need Not Eat rows and 47 rows that also carry Appetite. Conversely, some Undead or Demon-labelled records do not expose Need Not Eat. Class names are therefore unsafe substitutes for the explicit property. Community descriptions of commander feeding priority remain useful leads, but do not establish generic immunity.

## Editorial safeguards

- The field reference does not repeat the full evidence discussion.
- Rounding, unrest, fort-supply, transformation, and feeding-selection gaps remain labelled rather than smoothed into a universal formula.
- Community observations retain their date, game version, example, and evidence tier.
- Historical Edition 20 and earlier audit files remain unchanged as release records.
- The 6.36 live baseline remains separate from the pinned 6.35 structured object snapshot.

## Sources added or rechecked

- Dominions 6 Manual, revision 2;
- Dominions 6 Modding Manual 6.34;
- official Dominions 6 change history through 6.36;
- current community Commander Point, unrest, population, supply, and starvation references;
- dated December 2025 upkeep observation under Dominions 6.33;
- pinned Dominions 6 Inspector object snapshot at commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`.

## Build verification

The rebuilt website export contains 16 reader documents, 2,460 indexed sections, 106 glossary entries, 213 subject entries, 57 research items, 93 ability records, and 213 redirects. All 16 JSON outputs parse, all generated section references resolve, the official patch builder retains 32 announcements and 1,090 records, and the command builder reconciles 226 patch tokens with no unresolved token.

The reader corpus contains zero exact cross-document prose duplicate groups at the audited paragraph threshold. No document contains a repeated level-one or level-two heading. The controlled assistant-chatter search returns no matches, and every fenced code block is balanced.

The linked reader's PDF contains 784 A4 pages and 215,840 source words. Text extraction found no blank pages and no replacement glyphs. The file contains 4,364 link annotations: 4,284 internal links and 80 external links. Its outline contains 421 top-level entries.

Visual inspection covered the cover; the upkeep and mounted-component tables; Recruitment Point and Commander Point tables; the fort-supply documentary conflict; starvation, Need Not Eat, and unusual-unit logistics; the new economic-boundary essay; and the closing page. Tables remain within the text frame, continuation pages are clean, and no clipping or overlap was observed.

**PDF SHA-256:** `b721e58a3f21da9e8772166c9898c75cfc928998775d54b022e59245b72db78a`  
**PDF size:** 3,577,908 bytes
