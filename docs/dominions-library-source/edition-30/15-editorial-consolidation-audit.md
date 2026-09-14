# Editorial Consolidation Audit

## Scope

This audit covers Foundation Books I-IX and the Turn and Economy Quick Reference as revised on 31 July 2026. It addresses two different problems:

1. literal duplication, where the same paragraph or formula appears in more than one file;
2. editorial duplication, where different wording teaches the same material twice.

The second problem was considerably larger. Before editing, only five groups of substantial paragraphs were exact cross-book matches, but several subjects had been independently re-explained in two or three volumes.

## Editorial ownership

| Subject | Authoritative home |
| --- | --- |
| ruleset, evidence language, notation, glossary, and hosting order | Book I |
| deliberately repeated field formulas and timing facts | Turn and Economy Quick Reference |
| economy, recruitment, infrastructure, supplies, PD, and siege arithmetic | Book II |
| Pretenders, dominion, scales, and unmodded blessing design | Book III |
| battle resolution, including the combat arithmetic of spells | Book IV |
| magical planning, research, gems, communions, rituals, forging, and globals | Book V |
| campaign doctrine, diplomacy, logistics, recovery, and victory conversion | Book VI |
| nation-specific final application, beginning with MA Arcoscephale | Book VII |
| generic modding, event, AI, map, compatibility, and validation methods | Book VIII |
| exact DE 2.16 and Divinitus 1.15.3 DE source findings | Book IX |

## Consolidations made

### Library-wide front matter

- Repeated three-audience declarations were replaced with natural openings tailored to each subject.
- Repeated baseline and evidence-key blocks were replaced with short edition notes pointing back to Book I.
- Repeated "new player / competitive / research" routes were replaced with shorter, book-specific guidance.
- Internal completion summaries were removed. Unresolved questions remain because they affect the reliability of the material.

### Economy and Pretender material

- Book II no longer reproduces DE's global-command block and object-command count tables. It explains the economic consequences and points to Book IX for exact values.
- Book III no longer reproduces the complete DE scale, blessing, Pretender, and Divinitus source tables. It keeps the design consequences and audit method.
- The field reference remains the only deliberate duplicate of the most-used income and siege formulas.

### Battle and magic

- Book IV is now the single home for preparation, interruption, spell accuracy, Magic Resistance contests, spell fatigue, damage families, and battlefield-enchantment duration.
- Book V uses those results for package design rather than printing the formulas again.
- Siege arithmetic was removed from Books IV and VI. Book IV retains storm-battle context; Book VI retains the operational siege clock.
- Book V's mod-command inventory was removed in favour of Book IX's exact source catalogue.

### Strategy and nation application

- Book VI now assumes the earlier mechanics and focuses on campaign use.
- The Grand Hierophant reconstruction remains with the MA Arcoscephale dossier in Book VII.
- Book VIII keeps the generic shared-object reconstruction method without duplicating the Arcoscephale values.

### Modding and the technical encyclopaedia

- Book VIII no longer carries a second DE/Divinitus overlap count or file inventory.
- Book IX now imports the generic loader and validation rules from Book VIII, retaining only modpack-specific allocation and verification consequences.
- Duplicate Book IX essays on load order, event systems, blessings, and compatibility were removed. Their original essays remain in Books III and VIII.
- Book IX's repeated source summary, evidence-key appendix, and second combined-rules checklist were removed.

## Literal-duplication result

After consolidation, the automated paragraph comparison found one remaining exact cross-book match:

`Modified income = (population / 100) x dominion-scale modifiers x (1 + fort Administration / 200)`

It appears in Book II and the field reference by design. The field reference explicitly identifies itself as the library's deliberate pocket summary and is not treated as a second source of authority.

## Human-editing changes

The revised books now:

- open in different voices suited to their subjects;
- spend less time describing their own structure;
- avoid repeated evidence-label definitions;
- use cross-references where one author would naturally refer back to an earlier chapter;
- keep research caveats close to the exact uncertain claim;
- remove stale statements about what "the next book" will cover;
- remove mechanical inventories of what each completed volume supposedly contains;
- preserve the project's low use of direct second-person address.

The edit removed approximately 2,000 words while retaining the rules, examples, source boundaries, checklists, and unresolved research questions.

## Material intentionally retained in more than one context

Some conceptual overlap remains because it serves a different job:

- the quick reference repeats a few field calculations;
- patch corrections appear in the volume whose advice they change;
- a nation dossier may restate a general rule briefly before applying it to a specific roster;
- bibliographies repeat core official sources so individual volumes remain traceable;
- strategic chapters can mention a mechanic without reprinting its full arithmetic.

These are controlled recaps rather than competing explanations.
