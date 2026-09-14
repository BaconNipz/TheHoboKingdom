# Progress Edition 30: Complete Middle Age Dossier Expansion Audit

## Result

Book VII now contains an evidence-bounded dossier for every one of the 37 unmodded Middle Age nations in the pinned Inspector nation table. Nineteen new compact dossiers were added for Phlegra, Asphodel, Ermor, Sceleria, Na'Ba, Ind, Bandar Log, Nazca, Mictlan, Xibalba, Phaeacia, Vanarus, Jotunheim, Nidavangr, Ys, Pelagia, Oceania, Atlantis, and R'lyeh.

Each new dossier contains 27 indexed sections: command brief, evidence boundary, conversion chain, recruitment geography, commander and troop tables, mage portfolio, sites, national spells, item and hero records, army identities, expansion and fort controls, research and access ladders, battlefield packages, Pretender families, matchup matrix, monthly audit, unresolved claims, and source note.

## Structured reconciliation

| Nation | Commander identities | Troop identities | Sites | Active restricted spells | Item links | Hero slots |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Phlegra | 9 | 6 | 2 | 6 | 2 | 1 |
| Asphodel | 8 | 10 | 0 | 12 | 7 | 2 |
| Ermor | 0 | 0 | 0 | 23 | 2 | 4 |
| Sceleria | 8 | 12 | 3 | 11 | 0 | 2 |
| Na'Ba | 9 | 8 | 3 | 14 | 6 | 2 |
| Ind | 10 | 4 | 4 | 8 | 3 | 2 |
| Bandar Log | 9 | 17 | 1 | 31 | 2 | 1 |
| Nazca | 12 | 11 | 2 | 5 | 1 | 2 |
| Mictlan | 11 | 9 | 4 | 13 | 1 | 3 |
| Xibalba | 7 | 9 | 3 | 13 | 0 | 2 |
| Phaeacia | 8 | 8 | 3 | 9 | 3 | 2 |
| Vanarus | 7 | 10 | 2 | 16 | 0 | 3 |
| Jotunheim | 10 | 15 | 2 | 8 | 2 | 4 |
| Nidavangr | 9 | 6 | 1 | 3 | 1 | 3 |
| Ys | 10 | 9 | 1 | 2 | 0 | 2 |
| Pelagia | 16 | 10 | 1 | 2 | 1 | 0 |
| Oceania | 8 | 12 | 1 | 1 | 0 | 0 |
| Atlantis | 9 | 13 | 1 | 1 | 2 | 2 |
| R'lyeh | 8 | 13 | 2 | 0 | 3 | 3 |

Counts report identities resolved from ordinary-fort, non-fort, coast, and explicit site-recruit fields. A zero or low count does not erase special recruitment. Ermor explicitly does not recruit regular armies; Ind and other geographically unusual nations also expose capacity through mechanics not represented as universal fort membership. Those special systems remain described qualitatively and visibly bounded rather than reconstructed from undocumented attribute codes.

## Evidence and version boundary

- Player-facing authority: *Dominions 6 Manual*, revision 2.
- Live executable baseline: Dominions 6.37 and official patch history through 9 September 2026.
- Structured source: Dominions 6 Data Inspector commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`, pinned to 6.35.
- Random path records retain their source chance, count, link, and raw mask fields; masks are not expanded where the complete semantics are not already established.
- The generic 6.37 statistic correction is not assigned to unnamed units, spells, or items.
- Runtime testing and creation of test assets remained paused.

## Retrieval integration

- All 19 chapters have stable nation aliases plus direct aliases for roster, mages, spells, research, and unresolved evidence.
- Every new dossier contributes exactly 27 isolated entries to the website index.
- The website draft now contains 3,606 sections and 519 redirects.
- All 513 new sections carry the correct nation, Middle Age, unmodded, and `dom6-6.37-unmodded` metadata.

## Standalone readers

Nineteen new A4 standalone readers were built. Eighteen contain ten pages and Bandar Log contains eleven pages. Every PDF was reopened successfully, contains the dossier source register, and passed representative cover and body-page visual inspection for clipping, table overflow, typography, margins, headers, footers, and page numbering.

## Unresolved work preserved

Exact expansion numbers, random-path display, special recruitment timing, freespawn and reanimation composition, Blood returns, transformation and mount resolution, summon arrival state, item-price stacking, hero timing, stealth and sailing behaviour, land-water transitions, event outcomes, combat scripts, and casualty ranges remain open. R-047, R-058, and all comparable engine-dependent questions remain parked.

## Publication boundary

This is an unpublished Progress Edition 30 working expansion. Nothing was committed, published, deployed, or pushed.
