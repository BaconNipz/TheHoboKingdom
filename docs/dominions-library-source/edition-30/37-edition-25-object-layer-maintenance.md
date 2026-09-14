# Progress Edition 25 - Object-Layer Maintenance Audit

**Release date:** 26 August 2026  
**Base game:** Dominions 6.36  
**Structured object snapshot:** Dominions 6 Data Inspector 6.35, commit `cfac4311bc0b58053b8dead7bffbc036ba9bd5dc`

## Scope

Edition 25 maintained the 4,196-record base-game object register without changing its pinned source boundary. The work resolved realm-restricted spell access, improved summon-selector records, and added readable property-label provenance.

## Completed changes

| Layer | Result |
| --- | --- |
| Realm access | Six realm-restricted spells expanded into ninety realm-to-nation links using official realm names and pinned `#homerealm` values |
| Summon selectors | One Dwarf table resolved, eighteen monster-tag selectors named, six raw selectors left genuinely unresolved |
| Item property labels | 233 labels: 221 source-confirmed and 12 derived |
| Site and Throne labels | 78 labels: 74 source-confirmed and 4 derived |
| Source preservation | Raw selectors, property keys, realm numbers, and explicit national entries retained beside every derived field |

## Remaining G-03 work

- independent population-type membership;
- complete weighted candidates behind eighteen named monster tags;
- identity of five `-26` selectors and one `-18` selector;
- stronger source wording for sixteen derived property labels.

Realm-restricted spell access is complete for the pinned snapshot. None of the remaining items prevents the register from supporting website search or nation dossiers.

## Integrity record

The published uncompressed register has SHA-256:

```text
2a4f010e96e64b7e3b35a5c8071a9aa30f1016cb91bc20c5c670472985c180ad
```

The segmented website release retained the earlier stable edition while adding the new versioned download.

