# Progress Edition 24 - Full-Corpus Editorial Pass

**Status:** completed  
**Reader corpus:** sixteen books and references used by the combined PDF and website export  
**Rules baseline inherited from Edition 23:** Dominions 6.36  
**Purpose:** bring the complete reader-facing library into one natural, direct voice without altering its rules content or evidence strength

## Scope

Edition 24 covers every source listed in `navigation.py`. Back-office release audits remain historical records and are not rewritten into the reader's voice. Generated registers are edited through their templates and introductory material; exact object rows, patch records, command tokens and source-derived values are left intact.

The pass includes:

- introductions, explanations, examples, transitions, summaries and recommendations;
- headings that sound needlessly formal or abstract;
- repeated contrast structures and stock transitions;
- paragraphs that announce their purpose instead of making their point;
- unnecessary repetition between prose and the table immediately beside it;
- inconsistent use of `we`, `players`, `a nation`, and direct second person;
- dense sentences that can be split without changing their conditions.

## Locked content

No stylistic edit may change a version number, ruleset label, evidence label, qualification, formula, exact value, identifier, citation, stable link target, table relationship, research status, file name, hash or frozen load order. Historical rules remain labelled instead of being silently rewritten as current rules.

## Working voice

The target voice is that of a careful player writing for other players. It is informed without being clinical, confident where the evidence is firm, and open about gaps where the evidence is not firm. The prose favours direct explanations, practical consequences and familiar game terms. It does not copy typing errors or casual chat shorthand.

## Completion record

All sixteen reader-facing sources were reviewed. The pass rewrote 351 complete source lines or prose blocks across the Reader's Guide, field reference, and Books I-XIV. Generated object, patch, ability, and command entries were left source-exact; their introductions and explanatory passages received the same editorial treatment as the narrative books.

The diagnostic wording counts changed as follows:

| Diagnostic pattern | Edition 23 | Edition 24 | Editorial result |
| --- | ---: | ---: | --- |
| chapter or volume announcements | 39 | 13 | retained mainly where a section must identify its canonical scope |
| `therefore` | 226 | 0 | replaced with direct causation or removed where the relationship was already clear |
| `however` | 5 | 0 | contrast stated directly |
| `not merely` | 44 | 4 | four technical or title contexts retained |
| `not simply` | 13 | 2 | two exact mechanical contrasts retained |
| `rather than` | 215 | 176 | retained where it distinguishes two real rules, states, parsers, targets, or evidence classes |
| selected abstract process nouns | 38 | 25 | retained where they are genuine technical terms |

These counts are prompts for editorial judgement, not a prohibited-word test. Natural technical contrasts remain where replacing them would make the rule less exact.

## Preservation audit

Edition 24 was compared directly with the archived Edition 23 source. The following reader-facing structures are unchanged:

- all 2,466 headings and stable destinations;
- every Markdown table row;
- every fenced code block;
- every internal and external link target;
- every inline command or code value;
- the complete multiset of numeric tokens, apart from the added Edition 24 release label.

The corpus validator reports sixteen documents, 218,340 indexed words, 624 source-level internal links, sixteen valid website JSON files, no invalid internal destinations, no unbalanced code fences, no conversational drafting residue, and no exact cross-document prose duplicate at the forty-word threshold.

The generated website layer still contains 2,466 sections, 106 glossary entries, 213 subject records, 57 research records, 93 ability records, 213 redirects, and six reading paths. The official patch ledger remains 1,090 records from 32 announcements. The command lexicon remains 1,609 manual tokens, 97 controlled aliases, and 226 patch tokens with no unresolved patch token.

## PDF verification

The Edition 24 reader contains 789 A4 pages, 2,466 outline destinations, and 4,392 link annotations: 4,305 internal and 87 external. It has no blank pages, replacement glyphs, form widgets, unexpected annotations, or detected drafting phrases.

The cover, contents, the opening page of the Reader's Guide, field reference, and every Foundation Book, plus the final page, were rendered and inspected. Close inspection covered Books I, V, VIII, and XIV. The latest render shows no clipping, overlap, broken table, unreadable glyph, or inconsistent page furniture.

**PDF:** `dominions-6-knowledge-library-progress-edition-24.pdf`  
**Size:** 3,602,255 bytes  
**SHA-256:** `73bce923121f3351d598e63696a9d219d54614cd68c36e5fad0b65f834ea3f3f`

The editable project archive is checked for compressed-data integrity after it is assembled. Its checksum belongs to the delivery record because the archive cannot contain its own final checksum.
