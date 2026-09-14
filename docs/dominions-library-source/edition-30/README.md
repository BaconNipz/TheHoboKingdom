# Dominions 6 Knowledge Library - Progress Edition 30

This directory is the reconstructed canonical source for Progress Edition 30. It combines the complete Edition 28 source archive, the later Edition 29 publication and R-058 records, the Dominions 6.37 baseline correction, and the completed 37-nation Middle Age Book VII checkpoint. It remains under review and has not been published.

## Release baseline

- Dominions 6.37 live rules baseline;
- official revision-2 manual;
- official Modding Manual 6.36 for the Edition 28 ability-evidence pass;
- official patch record through 6.37;
- structured base-game records pinned to the declared 6.35 Inspector export;
- Dominions Enhanced 2.16 and Divinitus 1.15.3 DE kept as separately labelled rulesets.

The reconstructed reader contains sixteen documents, 3,646 indexed sections, and 325,553 words. Edition 28's perception matrix, current Invisibility correction, stacking evidence, Hall-of-Fame observation boundary, and five-star veteran Hit Point correction remain part of the collection.

Book VII now covers all 37 unmodded Middle Age nations, with nation-aware retrieval metadata and standalone readers for the nineteen nations added in the final expansion. Engine-dependent claims and the hands-on testing queue remain parked.

The final incremental checkpoint retained a 3,606-section export but not the revised Markdown for ten unchanged foundation books. This reconstruction restores those books from the last complete canonical archive and regenerates the index from the source actually present here. The resulting 3,646-section reader is the reproducible publication candidate; the older 3,606-section export is retained only as an audit record and is not presented as rebuildable source.

## Build

From this directory:

```bash
python build_pdf.py
python tools/build_reader_set_pdfs.py
```

The complete PDF and split reader PDFs are written to `../output/pdf/`. Standalone readers for every compact Middle Age dossier can be rebuilt with `python tools/build_dossier_pdfs.py`; pass a supported `--nation` slug to build one reader.

## Regenerate structured exports

```bash
python tools/build_website_exports.py
python tools/build_base_object_register.py
python tools/build_command_lexicon.py
python tools/build_official_patch_ledger.py
```

The website-ready JSON files are written to `website/`.

## Validate

```bash
python tools/validate_reader_corpus.py
python tools/style_audit.py
```

Edition 28's omnibus record, page counts, and hashes remain in `40-edition-28-perception-evidence-closure.md`. The Edition 29 web publication boundary is recorded in `58-edition-29-web-release-record.md`; the Edition 30 baseline and completed Middle Age expansion are recorded in audits 77 and 78.

## Evidence discipline

Official facts, pinned structured records, community references, historical reverse-engineering, and strategic judgement are labelled separately. Precise but version-mismatched evidence remains useful history; it is not silently promoted to current law.

Edition 28 adds `data/edition-28-perception-matrix.csv`, `data/edition-28-stacking-evidence-matrix.csv`, `data/edition-28-hall-of-fame-observation-template.csv`, and `website/perception-matrix.json`. The larger Book XIV command-locator export retains its declared 6.34 extraction until its complete token and page-locator set is rebuilt against the new live manual.
