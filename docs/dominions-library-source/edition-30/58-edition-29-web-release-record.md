# Edition 29 Web Release Record

**Status:** published and verified  
**Published:** 8 September 2026  
**Rules baseline:** Dominions 6.36  
**Publication:** TheHoboKingdom website  
**Runtime work:** paused; no engine-dependent claim was promoted

## What was released

Progress Edition 29 expands the searchable website from 2,527 to 2,857 sections. The published reader contains sixteen documents and 264,306 words. Book VII now contains twelve complete Middle Age nation dossiers:

- Arcoscephale;
- Marignon;
- Pyrène;
- Ulm;
- Man;
- Abysia;
- Pythium;
- Eriu;
- Agartha;
- Uruk;
- Ashdod;
- T'ien Ch'i.

Nine standalone Edition 29 readers were added for Ulm through T'ien Ch'i. Each public dossier has a stable Book VII route, a nation-catalogue entry, search metadata, and a direct PDF download.

## Deliberate publication boundary

Edition 29 is a website-first release. It does not relabel the 811-page Edition 28 omnibus as Edition 29. The site identifies Edition 28 as the latest complete all-in-one PDF while presenting the expanded Edition 29 material through the searchable reader and standalone nation PDFs.

R-047, R-058, random-display behaviour, conscription quantities, variable summons, transformation persistence, forge-rebate stacking, hero timing, and comparable engine-dependent questions remain open. Publication did not convert a test plan, hypothesis, pinned 6.35 field, or strategy judgement into a current 6.36 observed result.

## Repository record

| Record | Commit | Purpose |
| --- | --- | --- |
| Edition 29 release | `01a30176f18755458627564703aabd269abaad34` | Published the web corpus, search layer, catalogue records, stable routes, and nine PDFs on top of Edition 28. |
| Validation guardrail | `bec65f8fd652a21eb2746f5af1e68c22a53f6b01` | Updated the toolkit check from the Edition 28 total of 2,527 sections to the verified Edition 29 total of 2,857. |

The branch update was a normal fast-forward from Edition 28. No force push or history replacement was used.

## Validation result

- all website YAML metadata parsed;
- all JSON files and the compressed content index parsed;
- the manifest total matched 2,857 sections and 264,306 words;
- the public dossier register contained twelve completed nations;
- all nine Edition 29 PDF files passed PDF parsing;
- all nine new nation aliases resolved to Book VII destinations;
- the base-game reference catalogue remained current at 5,340 records;
- the toolkit integrity check passed across twenty-one tools and thirteen managed browser records;
- the GitHub Pages deployment completed successfully;
- the full repository build and internal-link workflow completed successfully;
- the live library displayed Edition 29 and 2,857 indexed sections;
- the live nation catalogue displayed twelve of 102 dossiers complete;
- the public T'ien Ch'i download returned a valid 118,674-byte PDF.

## Next safe work

Select the next unmodded Middle Age nation only after its ordinary and capital recruitment, random paths, national sites, spells, items, heroes, and named patch history can all be reconciled. Continue nation writing, metadata cleanup, navigation, and retrieval work without preparing runtime tests. Keep every engine-dependent claim open until hands-on testing is explicitly resumed.
