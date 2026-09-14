#!/usr/bin/env python3
"""Stable navigation identifiers shared by the PDF and website exports."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceSpec:
    filename: str
    code: str
    label: str
    website_path: str


SOURCE_SPECS = [
    SourceSpec(
        "16-reader-guide-concordance.md",
        "guide",
        "Reader's Guide and Concordance",
        "/dominions/library/guide/",
    ),
    SourceSpec(
        "04-foundation-book-i.md",
        "b1",
        "Foundation Book I",
        "/dominions/library/book-i/",
    ),
    SourceSpec(
        "05-turn-and-economy-quick-reference.md",
        "field",
        "Turn and Economy Quick Reference",
        "/dominions/library/field-reference/",
    ),
    SourceSpec(
        "06-foundation-book-ii-economy-state.md",
        "b2",
        "Foundation Book II",
        "/dominions/library/book-ii/",
    ),
    SourceSpec(
        "07-foundation-book-iii-pretenders-dominion-scales-blesses.md",
        "b3",
        "Foundation Book III",
        "/dominions/library/book-iii/",
    ),
    SourceSpec(
        "08-foundation-book-iv-armies-and-battle.md",
        "b4",
        "Foundation Book IV",
        "/dominions/library/book-iv/",
    ),
    SourceSpec(
        "09-foundation-book-v-magic.md",
        "b5",
        "Foundation Book V",
        "/dominions/library/book-v/",
    ),
    SourceSpec(
        "10-foundation-book-vi-strategy.md",
        "b6",
        "Foundation Book VI",
        "/dominions/library/book-vi/",
    ),
    SourceSpec(
        "12-foundation-book-vii-nations-arcoscephale.md",
        "b7",
        "Foundation Book VII",
        "/dominions/library/book-vii/",
    ),
    SourceSpec(
        "13-foundation-book-viii-modding-scenarios.md",
        "b8",
        "Foundation Book VIII",
        "/dominions/library/book-viii/",
    ),
    SourceSpec(
        "14-foundation-book-ix-de-divinitus.md",
        "b9",
        "Foundation Book IX",
        "/dominions/library/book-ix/",
    ),
    SourceSpec(
        "19-foundation-book-x-player-operations.md",
        "b10",
        "Foundation Book X",
        "/dominions/library/book-x/",
    ),
    SourceSpec(
        "21-foundation-book-xi-unit-ability-reference.md",
        "b11",
        "Foundation Book XI",
        "/dominions/library/book-xi/",
    ),
    SourceSpec(
        "24-foundation-book-xii-base-game-object-reference.md",
        "b12",
        "Foundation Book XII",
        "/dominions/library/book-xii/",
    ),
    SourceSpec(
        "26-foundation-book-xiii-official-patch-history.md",
        "b13",
        "Foundation Book XIII",
        "/dominions/library/book-xiii/",
    ),
    SourceSpec(
        "28-foundation-book-xiv-command-terminology-lexicon.md",
        "b14",
        "Foundation Book XIV",
        "/dominions/library/book-xiv/",
    ),
]


# Semantic aliases remain stable even when an editorial heading uses different
# wording. They also let prose, the PDF, and the website share readable links.
DESTINATION_ALIASES = {
    "b14-command-lexicon": "b14-foundation-book-xiv-the-command-and-terminology-lexicon",
    "b14-syntax": "b14-part-i-reading-the-modding-language",
    "b14-context": "b14-part-ii-context-is-part-of-syntax",
    "b14-evidence": "b14-part-iii-the-evidence-ladder-and-version-drift",
    "b14-domains": "b14-part-iv-command-domains",
    "b14-safe-lookup": "b14-part-v-a-safe-lookup-workflow",
    "b14-patch-reconciliation": "b14-part-vi-patch-to-manual-reconciliation",
    "b14-website": "b14-part-vii-search-and-website-architecture",
    "b14-essays": "b14-part-viii-expert-essays",
    "b14-maintenance": "b14-part-ix-maintenance-and-review-protocols",
    "b14-complete-locator": "b14-part-x-complete-search-locators",
    "b14-sources": "b14-part-xi-source-and-publication-register",
    "b13-official-patch-ledger": "b13-foundation-book-xiii-version-history-and-the-official-patch-ledger",
    "b13-release-timeline": "b13-part-ii-the-complete-official-release-spine",
    "b13-classification-model": "b13-part-iii-the-classification-and-evidence-model",
    "b13-domain-map": "b13-13-domain-tags-are-many-to-many",
    "b13-editorial-review": "b13-14-classification-confidence-is-not-source-confidence",
    "b13-player-facing-changes": "b13-part-iv-player-facing-changes-that-commonly-make-guides-stale",
    "b13-command-chronology": "b13-part-v-modding-and-command-chronology",
    "b13-stale-guide-repair": "b13-part-vi-repairing-stale-guides-and-maintaining-the-library",
    "b13-performance-and-stability": "b13-22-hosting-networking-security-and-integrity",
    "b13-presentation-and-data-maintenance": "b13-21-interface-and-operating-changes",
    "b13-website": "b13-34-website-uses",
    "b13-maintenance": "b13-33-updating-the-official-feed-safely",
    "b12-object-register": "b12-what-the-first-register-contains",
    "b12-spells": "b12-part-ii-spells",
    "b12-items": "b12-part-iii-magic-items-artifacts-and-barding",
    "b12-summons": "b12-part-iv-summons",
    "b12-pretenders": "b12-part-v-pretender-forms",
    "b12-thrones-sites": "b12-part-vi-thrones-and-magic-sites",
    "b12-mercenaries-independents": "b12-part-vii-mercenaries-and-independent-recruitment",
    "b12-special-dominions": "b12-part-viii-special-dominion-systems",
    "b12-website": "b12-part-ix-website-and-research-use",
    "b12-maintenance": "b12-part-x-verification-and-maintenance",
    "b11-ability-register": "b11-part-xii-master-ability-and-condition-register",
    "b11-conditions": "b11-part-xi-conditions-and-lasting-state",
    "b11-counter-matrix": "b11-71-counter-construction-matrix",
    "b11-experience": "b11-part-ix-experience-and-veteran-units",
    "b11-heroic-abilities": "b11-part-x-hall-of-fame-and-heroic-abilities",
    "b11-unit-classes": "b11-part-ii-unit-classes-and-status-tags",
    "b11-unit-reading": "b11-3-begin-with-the-body-not-the-icon",
    "b10-first-campaign": "b10-part-viii-a-guided-first-campaign",
    "b10-game-setup": "b10-part-ii-creating-the-world",
    "b10-hosting": "b10-part-iii-starting-joining-and-hosting",
    "b10-interface": "b10-part-iv-the-main-interface",
    "b10-orders": "b10-part-vii-strategic-order-reference",
    "b10-troubleshooting": "b10-part-ix-troubleshooting-by-symptom",
    "b10-a-turn-staled": "b10-78-a-turn-staled",
    "b10-cannot-find-or-join-the-game": "b10-67-cannot-find-or-join-the-game",
    "b10-current-operational-additions-worth-learning": "b10-26-current-operational-additions-worth-learning",
    "b10-dispute-handling": "b10-85-dispute-handling",
    "b10-first-contact": "b10-62-first-contact",
    "b10-host-setup-sheet": "b10-15-host-setup-sheet",
    "b10-hosting-runbook": "b10-83-hosting-runbook",
    "b10-official-lobby-workflow": "b10-17-official-lobby-workflow",
    "b10-ordinary-movement": "b10-42-ordinary-movement",
    "b10-siege-orders": "b10-46-siege-orders",
    "b10-the-end-of-turn-audit": "b10-33-the-end-of-turn-audit",
    "b10-turn-submission": "b10-18-turn-submission-and-revision",
    "b10-turn-submission-and-revision": "b10-18-turn-submission-and-revision",
    "b1-aging-disease-and-insanity": "b1-phase-vi-attrition-and-end-state",
    "b1-assassinations-resolve-before-conventional-movement": "b1-horrors-and-assassinations-can-remove-movement-leaders",
    "b1-building-construction": "b1-buildings-finish-after-the-month-s-active-systems",
    "b1-eras-and-national-identity": "b1-foundation-book-i-rulesets-language-and-the-anatomy-of-a-turn",
    "b1-evidence-standard": "b1-evidence-and-confidence",
    "b1-immortals-return-after-victory": "b1-victory-before-immortal-return",
    "b1-movement-and-conquest": "b1-phase-iii-movement-and-conquest",
    "b1-rulesets-must-never-be-silently-merged": "b1-ruleset-labels",
    "b2-blood-hunting": "b2-part-xi-blood-economy",
    "b2-commander-points-and-holy-points": "b2-commander-points",
    "b2-dominion-scales-and-the-economy": "b2-scale-interaction",
    "b2-mercenaries": "b2-dominions-as-a-game-of-conversion",
    "b2-part-v-supplies-logistics-and-starvation": "b2-part-vi-supplies-armies-and-logistics",
    "b2-part-vi-infrastructure-and-administration": "b2-part-vii-infrastructure",
    "b2-part-vii-population-unrest-pillage-patrol-and-blood-hunting": "b2-part-v-unrest-and-coercive-economy",
    "b2-recruitment-restrictions": "b2-ownership-and-national-recruitment",
    "b3-heat-and-cold": "b3-temperature",
    "b3-incarnate-effects": "b3-ordinary-innate-and-incarnate",
    "b3-part-iv-dominion-and-religious-territory": "b3-part-iv-dominion",
    "b3-part-vii-pretender-death-recall-and-divine-continuity": "b3-part-viii-death-of-a-god",
    "b3-pretender-design-audit": "b3-expert-design-audit",
    "b3-sacred-capacity": "b3-mass-sacreds-versus-elite-sacreds",
    "b3-special-dominions": "b3-part-ix-special-dominions",
    "b4-armour-and-protection": "b4-damage-and-protection",
    "b4-army-rout": "b4-army-level-rout",
    "b4-battle-groups": "b4-part-i-what-a-battle-decides",
    "b4-battlefield-enchantments": "b4-battle-enchantments",
    "b4-berserk": "b4-part-xi-morale-fear-rout-and-retreat",
    "b4-clouds-and-persistent-area-effects": "b4-clouds-and-auras",
    "b4-critical-hits": "b4-part-x-fatigue-recovery-and-collapse",
    "b4-damage-reversal": "b4-part-xii-resistances-and-special-damage",
    "b4-disease": "b4-part-xiii-afflictions-regeneration-and-lasting-loss",
    "b4-encumbrance": "b4-part-x-fatigue-recovery-and-collapse",
    "b4-fire-and-cold": "b4-part-xii-resistances-and-special-damage",
    "b4-formation-fighter": "b4-formation-types",
    "b4-friendly-fire": "b4-part-viii-missiles-and-ranged-delivery",
    "b4-immortality-and-return": "b4-part-xiii-afflictions-regeneration-and-lasting-loss",
    "b4-magic-resistance-contests": "b4-magic-resistance",
    "b4-mindless-troops": "b4-part-xi-morale-fear-rout-and-retreat",
    "b4-missile-deviation": "b4-deviation",
    "b4-obstacles": "b4-obstacles-and-battlefield-terrain",
    "b4-part-iii-commanders-squads-leadership-and-army-organisation": "b4-part-iii-command-squads-and-army-construction",
    "b4-part-iv-size-mounts-trampling-and-battlefield-movement": "b4-part-ix-mounts-trampling-and-size",
    "b4-part-ix-protection-damage-and-survival": "b4-damage-and-protection",
    "b4-part-v-formations-placement-and-contact": "b4-part-iv-formation-density-and-placement",
    "b4-part-vi-orders-scripts-and-the-spellcasting-ai": "b4-part-v-orders-and-scripting",
    "b4-part-viii-missile-combat": "b4-part-viii-missiles-and-ranged-delivery",
    "b4-part-xii-resistances-special-damage-and-status-effects": "b4-part-xii-resistances-and-special-damage",
    "b4-part-xiii-afflictions-regeneration-and-healing": "b4-part-xiii-afflictions-regeneration-and-lasting-loss",
    "b4-part-xiv-battlefield-magic": "b4-part-xiv-battle-magic-within-the-army",
    "b4-part-xv-counter-construction-and-battle-analysis": "b4-part-xvi-counter-construction",
    "b4-part-xvi-siege-storming-retreat-and-pursuit": "b4-part-xv-sieges-storming-and-battle-context",
    "b4-penetration": "b4-magic-resistance",
    "b4-regeneration": "b4-part-xiii-afflictions-regeneration-and-lasting-loss",
    "b4-spell-targeting": "b4-part-xiv-battle-magic-within-the-army",
    "b4-targeting-orders": "b4-squad-orders",
    "b4-taskmasters": "b4-standards-inspiration-and-taskmasters",
    "b4-trample": "b4-trampling",
    "b4-weapon-profiles": "b4-part-ii-reading-a-unit",
    "b5-artifact-races": "b5-artifacts",
    "b5-battlefield-enchantment-packages": "b5-spell-classes-by-battlefield-job",
    "b5-battlefield-gem-spending": "b5-combat-gem-rules",
    "b5-construction-as-an-access-school": "b5-construction-tiers",
    "b5-empowerment": "b5-empowerment-as-a-bridge",
    "b5-gem-reserves": "b5-reserve-doctrine",
    "b5-hidden-and-indirect-access": "b5-indirect-magic",
    "b5-mage-turn-opportunity-cost": "b5-mage-turn-accounting",
    "b5-magic-duel": "b5-part-vi-the-nine-paths-in-practice",
    "b5-national-and-restricted-magic": "b5-national-access-is-a-distribution",
    "b5-part-ix-domes-remote-attacks-and-magic-movement": "b5-part-ix-domes-and-remote-magic-defence",
    "b5-part-vi-battlefield-magic-by-function": "b5-part-v-the-anatomy-of-battle-magic",
    "b5-part-xii-legendary-and-level-nine-magic": "b5-part-xiii-legendary-and-late-game-magic",
    "b5-research-breakpoints": "b5-research-portfolios",
    "b5-research-discounts": "b5-research-efficiency",
    "b5-scrying": "b5-part-viii-rituals-and-strategic-magic",
    "b6-assassination-defence": "b6-assassin-rules",
    "b6-border-design": "b6-border-shapes",
    "b6-coalition-formation": "b6-coalition-politics",
    "b6-dominion-as-campaign-pressure": "b6-part-xi-diplomacy-treaties-and-reputation",
    "b6-from-expansion-to-the-first-war": "b6-part-viii-war-planning-timing-and-decision",
    "b6-independent-province-classes": "b6-part-ii-expansion",
    "b6-information-denial": "b6-information-denial-and-deception",
    "b6-initiative": "b6-tempo-and-initiative",
    "b6-movement-and-interception": "b6-friendly-hostile-and-intercepting-movement",
    "b6-non-aggression-pacts": "b6-formal-and-social-naps",
    "b6-part-ii-expansion-and-first-contact": "b6-part-ii-expansion",
    "b6-part-vi-logistics-supply-and-operational-reach": "b6-part-vi-movement-logistics-and-force-projection",
    "b6-part-x-timing-attacks-power-spikes-and-deterrence": "b6-part-viii-war-planning-timing-and-decision",
    "b6-part-xiii-army-preservation-and-force-regeneration": "b6-part-xiii-recovery-elastic-defence-and-defeat-management",
    "b6-part-xiv-recovery-replacement-and-war-continuation": "b6-part-xiii-recovery-elastic-defence-and-defeat-management",
    "b6-part-xv-victory-conversion": "b6-part-xii-thrones-cataclysm-and-endgame-conversion",
    "b6-part-xvi-campaign-decision-framework": "b6-part-viii-war-planning-timing-and-decision",
    "b6-patrol-and-stealth": "b6-patrol-and-concealment",
    "b6-pillage-as-a-campaign-tool": "b6-part-vii-raiding-and-counter-raiding",
    "b6-raid-order": "b6-what-a-raid-is",
    "b6-siege-as-an-operational-clock": "b6-the-siege-clock",
    "b6-tempo": "b6-tempo-and-initiative",
    "b7-evidence-architecture": "b7-part-i-the-nation-dossier-method",
    "b7-path-probability-and-thresholds": "b7-magic-access-as-a-probability-portfolio",
    "b7-ma-arcoscephale-dossier": "b7-part-ii-middle-age-arcoscephale-the-old-kingdom",
    "b7-ma-marignon-dossier": "b7-part-xvi-middle-age-marignon-fiery-justice",
    "b7-ma-pyrene-dossier": "b7-part-xvii-middle-age-pyrene-time-of-the-akelarre",
    "b7-ma-ulm-dossier": "b7-part-xviii-middle-age-ulm-forges-of-ulm",
    "b7-ma-man-dossier": "b7-part-xix-middle-age-man-tower-of-avalon",
    "b7-ma-abysia-dossier": "b7-part-xx-middle-age-abysia-blood-and-fire",
    "b7-ma-pythium-dossier": "b7-part-xxi-middle-age-pythium-emerald-empire",
    "b7-ma-eriu-dossier": "b7-part-xxii-middle-age-eriu-last-of-the-tuatha",
    "b7-ma-agartha-dossier": "b7-part-xxiii-middle-age-agartha-golem-cult",
    "b7-ma-uruk-dossier": "b7-part-xxiv-middle-age-uruk-city-states",
    "b7-ma-ashdod-dossier": "b7-part-xxv-middle-age-ashdod-reign-of-the-anakim",
    "b7-ma-tien-chi-dossier": "b7-part-xxvi-middle-age-t-ien-ch-i-imperial-bureaucracy",
    "b7-ma-machaka-dossier": "b7-part-xxvii-middle-age-machaka-reign-of-sorcerors",
    "b7-ma-shinuyama-dossier": "b7-part-xxviii-middle-age-shinuyama-land-of-the-bakemono",
    "b7-ma-ctis-dossier": "b7-part-xxix-middle-age-c-tis-miasma",
    "b7-ma-pangaea-dossier": "b7-part-xxx-middle-age-pangaea-age-of-bronze",
    "b7-ma-vanheim-dossier": "b7-part-xxxi-middle-age-vanheim-arrival-of-man",
    "b7-ma-caelum-dossier": "b7-part-xxxii-middle-age-caelum-reign-of-the-seraphim",
    "b7-ulm-roster": "b7-ulm-roster-by-job",
    "b7-ulm-mages": "b7-ulm-commander-and-mage-portfolio",
    "b7-ulm-randoms": "b7-reading-the-smith-randoms",
    "b7-ulm-spells": "b7-national-spells-and-the-caster-who-owns-them",
    "b7-ulm-items": "b7-national-item-portfolio",
    "b7-ulm-research": "b7-ulm-research-response-tree",
    "b7-ulm-matchups": "b7-ulm-matchup-and-failure-matrix",
    "b7-ulm-open-questions": "b7-ulm-unresolved-evidence-boundary",
    "b7-man-roster": "b7-man-roster-by-job",
    "b7-man-mages": "b7-man-commander-and-mage-portfolio",
    "b7-man-randoms": "b7-reading-avalon-s-random-paths",
    "b7-man-spells": "b7-national-spells-and-caster-access",
    "b7-man-items": "b7-man-national-item-boundary",
    "b7-man-research": "b7-man-research-response-tree",
    "b7-man-matchups": "b7-man-matchup-and-failure-matrix",
    "b7-man-open-questions": "b7-man-unresolved-evidence-boundary",
    "b7-abysia-roster": "b7-abysia-roster-by-job",
    "b7-abysia-mages": "b7-abysia-commander-and-mage-portfolio",
    "b7-abysia-randoms": "b7-reading-the-abysian-random-paths",
    "b7-abysia-sites": "b7-abysia-capital-sites-and-recruitment-queues",
    "b7-abysia-spells": "b7-abysia-national-spells-and-caster-access",
    "b7-abysia-items": "b7-abysia-national-item-boundary",
    "b7-abysia-research": "b7-abysia-research-response-tree",
    "b7-abysia-matchups": "b7-abysia-matchup-and-failure-matrix",
    "b7-abysia-open-questions": "b7-abysia-unresolved-evidence-boundary",
    "b7-pythium-roster": "b7-complete-pythium-roster-by-job",
    "b7-pythium-mages": "b7-pythium-commander-and-mage-portfolio",
    "b7-pythium-randoms": "b7-reading-the-arch-theurg-random-paths",
    "b7-pythium-sites": "b7-pythium-capital-sites-and-recruitment-queues",
    "b7-pythium-spells": "b7-pythium-national-rituals-and-caster-access",
    "b7-pythium-items": "b7-pythium-national-item-boundary",
    "b7-pythium-research": "b7-pythium-research-response-tree",
    "b7-pythium-matchups": "b7-pythium-matchup-and-failure-matrix",
    "b7-pythium-open-questions": "b7-pythium-unresolved-evidence-boundary",
    "b7-eriu-roster": "b7-complete-eriu-roster-by-job",
    "b7-eriu-mages": "b7-eriu-commander-and-mage-portfolio",
    "b7-eriu-randoms": "b7-reading-the-milesian-mage-random-paths",
    "b7-eriu-sites": "b7-eriu-capital-sites-and-recruitment-geography",
    "b7-eriu-spells": "b7-eriu-national-spell-and-ritual-reconciliation",
    "b7-eriu-items": "b7-eriu-national-item-reconciliation",
    "b7-eriu-research": "b7-eriu-research-response-tree",
    "b7-eriu-matchups": "b7-eriu-matchup-and-failure-matrix",
    "b7-eriu-open-questions": "b7-eriu-unresolved-evidence-boundary",
    "b7-agartha-roster": "b7-complete-agartha-roster-by-job",
    "b7-agartha-mages": "b7-agartha-commander-and-mage-portfolio",
    "b7-agartha-randoms": "b7-reading-the-oracle-random-paths",
    "b7-agartha-sites": "b7-agartha-capital-sites-and-recruitment-geography",
    "b7-agartha-spells": "b7-agartha-national-ritual-reconciliation",
    "b7-agartha-dominion": "b7-agartha-national-rules-that-shape-the-plan",
    "b7-agartha-heroes": "b7-agartha-national-hero-records",
    "b7-agartha-research": "b7-agartha-research-response-tree",
    "b7-agartha-matchups": "b7-agartha-matchup-and-failure-matrix",
    "b7-agartha-open-questions": "b7-agartha-unresolved-evidence-boundary",
    "b7-uruk-roster": "b7-complete-uruk-roster-by-job",
    "b7-uruk-mages": "b7-uruk-commander-and-mage-portfolio",
    "b7-uruk-randoms": "b7-reading-the-common-uruk-random-masks",
    "b7-uruk-sites": "b7-uruk-capital-sites-and-recruitment-geography",
    "b7-uruk-spells": "b7-uruk-national-ritual-reconciliation",
    "b7-uruk-items": "b7-uruk-national-item-boundary",
    "b7-uruk-heroes": "b7-uruk-national-hero-records",
    "b7-uruk-research": "b7-uruk-research-response-tree",
    "b7-uruk-matchups": "b7-uruk-matchup-and-failure-matrix",
    "b7-uruk-open-questions": "b7-uruk-unresolved-evidence-boundary",
    "b7-ashdod-roster": "b7-complete-ashdod-roster-by-job",
    "b7-ashdod-mages": "b7-ashdod-commander-and-mage-portfolio",
    "b7-ashdod-randoms": "b7-reading-the-ordinary-ashdod-randoms",
    "b7-ashdod-sites": "b7-ashdod-capital-sites-and-recruitment-geography",
    "b7-ashdod-spells": "b7-ashdod-national-spell-and-ritual-reconciliation",
    "b7-ashdod-items": "b7-ashdod-national-item-boundary",
    "b7-ashdod-heroes": "b7-ashdod-national-hero-records",
    "b7-ashdod-research": "b7-ashdod-research-response-tree",
    "b7-ashdod-matchups": "b7-ashdod-matchup-and-failure-matrix",
    "b7-ashdod-open-questions": "b7-ashdod-unresolved-evidence-boundary",
    "b7-tien-chi-roster": "b7-t-ien-ch-i-roster-by-job",
    "b7-tien-chi-mages": "b7-t-ien-ch-i-guaranteed-mage-and-priest-floor",
    "b7-tien-chi-randoms": "b7-master-of-the-way-random-portfolio",
    "b7-tien-chi-sites": "b7-t-ien-ch-i-capital-sites-and-recruitment-geography",
    "b7-tien-chi-spells": "b7-t-ien-ch-i-national-spell-and-ritual-reconciliation",
    "b7-tien-chi-items": "b7-t-ien-ch-i-national-item-boundary",
    "b7-tien-chi-heroes": "b7-t-ien-ch-i-hero-records",
    "b7-tien-chi-research": "b7-t-ien-ch-i-research-response-tree",
    "b7-tien-chi-matchups": "b7-t-ien-ch-i-matchup-and-failure-matrix",
    "b7-tien-chi-open-questions": "b7-t-ien-ch-i-unresolved-evidence-boundary",
    "b7-machaka-roster": "b7-complete-machaka-troop-membership",
    "b7-machaka-commanders": "b7-complete-machaka-commander-membership",
    "b7-machaka-mages": "b7-machaka-commander-and-mage-portfolio",
    "b7-machaka-randoms": "b7-reading-the-sorcerer-random",
    "b7-machaka-sites": "b7-machaka-capital-sites-and-recruitment-geography",
    "b7-machaka-spells": "b7-machaka-national-ritual-reconciliation",
    "b7-machaka-items": "b7-machaka-national-item-metadata",
    "b7-machaka-heroes": "b7-machaka-hero-records",
    "b7-machaka-research": "b7-machaka-research-response-tree",
    "b7-machaka-information": "b7-machaka-information-and-pressure-network",
    "b7-machaka-matchups": "b7-machaka-matchup-and-failure-matrix",
    "b7-machaka-open-questions": "b7-machaka-unresolved-evidence-boundary",
    "b7-shinuyama-roster": "b7-complete-shinuyama-troop-membership",
    "b7-shinuyama-commanders": "b7-complete-shinuyama-commander-membership",
    "b7-shinuyama-mages": "b7-reading-the-shinuyama-random-paths",
    "b7-shinuyama-randoms": "b7-reading-the-shinuyama-random-paths",
    "b7-shinuyama-sites": "b7-mount-shinuyama-and-the-capital-economy",
    "b7-shinuyama-terrain": "b7-recruitment-geography-and-infrastructure",
    "b7-shinuyama-spells": "b7-shinuyama-ritual-access-ladder",
    "b7-shinuyama-summons": "b7-shinuyama-summon-boundary",
    "b7-shinuyama-items": "b7-shinuyama-national-item-boundary",
    "b7-shinuyama-heroes": "b7-shinuyama-hero-records",
    "b7-shinuyama-research": "b7-shinuyama-research-response-tree",
    "b7-shinuyama-information": "b7-shinuyama-information-and-pressure-network",
    "b7-shinuyama-matchups": "b7-shinuyama-matchup-and-failure-matrix",
    "b7-shinuyama-open-questions": "b7-shinuyama-unresolved-evidence-boundary",
    "b7-ctis-roster": "b7-complete-c-tis-troop-membership",
    "b7-ctis-commanders": "b7-complete-c-tis-commander-membership",
    "b7-ctis-mages": "b7-c-tis-native-path-boundary",
    "b7-ctis-randoms": "b7-reading-the-marshmaster-random-paths",
    "b7-ctis-sites": "b7-c-tis-capital-sites-and-gem-economy",
    "b7-ctis-miasma": "b7-miasma-evidence-boundary",
    "b7-ctis-spells": "b7-c-tis-national-ritual-reconciliation",
    "b7-ctis-items": "b7-c-tis-national-item-the-jade-mask",
    "b7-ctis-heroes": "b7-c-tis-hero-records",
    "b7-ctis-research": "b7-c-tis-research-response-tree",
    "b7-ctis-information": "b7-c-tis-information-and-pressure-network",
    "b7-ctis-pretenders": "b7-c-tis-pretender-families",
    "b7-ctis-matchups": "b7-c-tis-matchup-and-failure-matrix",
    "b7-ctis-open-questions": "b7-c-tis-unresolved-evidence-boundary",
    "b7-pangaea-roster": "b7-complete-pangaea-troop-membership",
    "b7-pangaea-commanders": "b7-complete-pangaea-commander-membership",
    "b7-pangaea-mages": "b7-pangaea-native-path-boundary",
    "b7-pangaea-randoms": "b7-reading-pangaea-s-random-paths",
    "b7-pangaea-sites": "b7-pangaea-capital-sites-and-gem-economy",
    "b7-pangaea-forest": "b7-pangaea-recruitment-geography",
    "b7-pangaea-recuperation": "b7-recuperation-evidence-boundary",
    "b7-pangaea-tunes": "b7-pangaea-national-magical-tunes",
    "b7-pangaea-spells": "b7-pangaea-national-magical-tunes",
    "b7-pangaea-rituals": "b7-pangaea-national-ritual-reconciliation",
    "b7-pangaea-items": "b7-pangaea-national-item-boundary",
    "b7-pangaea-heroes": "b7-pangaea-hero-records",
    "b7-pangaea-research": "b7-pangaea-research-response-tree",
    "b7-pangaea-information": "b7-pangaea-information-and-pressure-network",
    "b7-pangaea-pretenders": "b7-pangaea-pretender-families",
    "b7-pangaea-matchups": "b7-pangaea-matchup-and-failure-matrix",
    "b7-pangaea-open-questions": "b7-pangaea-unresolved-evidence-boundary",
    "b7-vanheim-roster": "b7-complete-vanheim-troop-membership",
    "b7-vanheim-commanders": "b7-complete-vanheim-commander-membership",
    "b7-vanheim-mages": "b7-vanheim-native-path-boundary",
    "b7-vanheim-randoms": "b7-reading-vanheim-s-random-paths",
    "b7-vanheim-sites": "b7-vanheim-capital-sites-and-recruitment-geography",
    "b7-vanheim-capital": "b7-vanheim-capital-queue-doctrine",
    "b7-vanheim-sailing": "b7-sailing-and-trace-income-evidence-boundary",
    "b7-vanheim-spells": "b7-vanheim-national-spell-and-ritual-reconciliation",
    "b7-vanheim-rituals": "b7-vanheim-national-magic-access-ladder",
    "b7-vanheim-directions": "b7-four-directions-ritual-boundary",
    "b7-vanheim-items": "b7-vanheim-national-item-metadata",
    "b7-vanheim-heroes": "b7-vanheim-hero-records",
    "b7-vanheim-research": "b7-vanheim-research-response-tree",
    "b7-vanheim-information": "b7-vanheim-information-and-pressure-network",
    "b7-vanheim-pretenders": "b7-vanheim-pretender-families",
    "b7-vanheim-matchups": "b7-vanheim-matchup-and-failure-matrix",
    "b7-vanheim-open-questions": "b7-vanheim-unresolved-evidence-boundary",
    "b7-caelum-roster": "b7-complete-caelum-troop-membership",
    "b7-caelum-commanders": "b7-complete-caelum-commander-membership",
    "b7-caelum-mages": "b7-caelum-recruitable-magic-access",
    "b7-caelum-randoms": "b7-high-seraph-random-path-probabilities",
    "b7-caelum-sites": "b7-caelum-capital-sites",
    "b7-caelum-capital": "b7-caelum-capital-queue-control",
    "b7-caelum-rules": "b7-caelum-national-rules-that-shape-planning",
    "b7-caelum-spells": "b7-caelum-national-spell-map",
    "b7-caelum-summons": "b7-positive-summon-branch",
    "b7-caelum-drugvant": "b7-call-of-the-drugvant-boundary",
    "b7-caelum-items": "b7-caelum-item-rebates",
    "b7-caelum-heroes": "b7-caelum-hero-boundary",
    "b7-caelum-research": "b7-caelum-research-response-tree",
    "b7-caelum-information": "b7-caelum-information-and-pressure-network",
    "b7-caelum-pretenders": "b7-caelum-pretender-families",
    "b7-caelum-matchups": "b7-caelum-matchup-and-failure-matrix",
    "b7-caelum-open-questions": "b7-caelum-unresolved-evidence-boundary",
    "b8-automatic-allocation": "b8-automatic-allocation-is-convenient-but-fragile",
    "b8-codes-and-variables": "b8-event-variables",
    "b8-current-consolidated-object-limits": "b8-part-i-the-object-and-parser-model",
    "b8-gates-and-multiple-planes": "b8-gates",
    "b8-load-order": "b8-essay-i-load-order-is-part-of-game-design",
    "b8-part-ii-identifiers-allocation-and-collision-safety": "b8-part-i-the-object-and-parser-model",
    "b8-part-iii-weapons-armour-and-combat-components": "b8-part-iii-weapons-armour-and-combat-effects",
    "b8-part-iv-monsters-mounts-shapes-commanders-and-sites": "b8-part-iv-monsters-mounts-shapes-and-commanders",
    "b8-part-x-ai-scaffolding-without-false-claims": "b8-part-x-ai-modding",
    "b8-selection-copying-and-inheritance": "b8-copy-first-and-clear-first-are-different-designs",
    "b9-12-underwater-and-cross-terrain-systems": "b9-10-3-underwater-play",
    "b9-14-divinitus-event-architecture": "b9-15-the-divinitus-event-engine",
    "b9-15-capital-institutions-temple-networks-and-priesthoods": "b9-16-1-capital-institutions",
    "b9-19-4-automatic-id-collision-risk": "b9-19-4-automatic-allocation",
    "b9-24-website-and-inspector-schema": "b9-23-website-architecture",
    "b9-7-de-global-rules": "b9-7-the-six-global-de-rules",
    "b9-8-de-blessing-revision": "b9-8-complete-de-blessing-revision",
    "b9-essay-iv-versioned-knowledge-is-part-of-the-ruleset": "b9-essay-iv-versioned-knowledge-is-the-real-encyclopaedia",
    "field-recruitment-gates": "field-the-four-recruitment-gates",
    "b1-plane": "b1-spatial-terms",
    "b1-randomness-and-the-dominions-random-number": "b1-randomness",
    "b1-remote-attacks-and-magic-battles": "b1-remote-attacks-strike-before-ordinary-movement",
    "b1-size-point": "b1-spatial-terms",
    "b1-sneaking-discovery-can-cause-a-late-battle": "b1-stealth-failure-can-produce-a-late-battle",
    "b1-starvation-is-late": "b1-starvation-follows-battle",
    "b2-fort-supply-range": "b2-fort-supply-distance",
    "b2-part-xv-mathematical-reference": "b2-part-xv-expert-diagnostics",
    "b2-starvation": "b2-starvation-selection-and-effects",
    "b2-unrest-effects": "b2-what-unrest-does",
    "b3-part-ii-chassis-paths-and-design-capabilities": "b3-part-i-pretender-design-as-a-national-system",
    "b4-healing": "b4-healing-categories",
    "b4-leadership": "b4-special-leadership",
    "b4-squads": "b4-squad-orders",
    "b4-square-capacity": "b4-the-square",
    "b5-fatigue-and-overcasting": "b5-overcasting",
    "b5-layered-domes": "b5-layering-domes",
    "b5-research-schools": "b5-the-seven-schools",
    "b6-binding-diplomacy": "b6-formal-and-social-naps",
    "b6-counter-portfolios": "b6-counter-construction",
    "b6-expansion-party-roles": "b6-expansion-party-archetypes",
    "b6-thug-roles": "b6-part-ix-thugs-supercombatants-assassins-and-remote-force",
    "b8-copied-objects-are-not-self-contained": "b8-part-i-the-object-and-parser-model",
    "b8-cross-mod-reference-limits": "b8-combined-mods-behave-differently",
    "b8-event-execution-and-order": "b8-event-effects-and-transactional-thinking",
    "b8-network-and-lobby-test": "b8-load-test",
    "b8-object-lifecycle": "b8-part-i-the-object-and-parser-model",
    "b8-performance-controls": "b8-event-performance",
    "b8-save-compatibility": "b8-part-xi-compatibility-engineering",
    "b8-shape-regression": "b8-shape-relationships-form-graphs",
    "b8-variable-discipline": "b8-event-variables",
    "b8-the-user-data-directory": "b8-locating-the-user-data-directory",
    "field-commander-points": "field-the-four-recruitment-gates",
    "field-holy-points": "field-the-four-recruitment-gates",
    "guide-readers-guide-and-concordance": "guide-reader-s-guide-and-concordance",
}

_REMAINING_MA_NAVIGATION = [
    ("phlegra", "b7-part-xxxiii-middle-age-phlegra-deformed-giants"),
    ("asphodel", "b7-part-xxxiv-middle-age-asphodel-carrion-woods"),
    ("ermor", "b7-part-xxxv-middle-age-ermor-ashen-empire"),
    ("sceleria", "b7-part-xxxvi-middle-age-sceleria-the-reformed-empire"),
    ("na-ba", "b7-part-xxxvii-middle-age-na-ba-queens-of-the-desert"),
    ("ind", "b7-part-xxxviii-middle-age-ind-magnificent-kingdom-of-exalted-virtue"),
    ("bandar-log", "b7-part-xxxix-middle-age-bandar-log-land-of-the-apes"),
    ("nazca", "b7-part-xl-middle-age-nazca-kingdom-of-the-sun"),
    ("mictlan", "b7-part-xli-middle-age-mictlan-reign-of-the-lawgiver"),
    ("xibalba", "b7-part-xlii-middle-age-xibalba-flooded-caves"),
    ("phaeacia", "b7-part-xliii-middle-age-phaeacia-isle-of-the-dark-ships"),
    ("vanarus", "b7-part-xliv-middle-age-vanarus-land-of-the-chuds"),
    ("jotunheim", "b7-part-xlv-middle-age-jotunheim-iron-woods"),
    ("nidavangr", "b7-part-xlvi-middle-age-nidavangr-bear-wolf-and-crow"),
    ("ys", "b7-part-xlvii-middle-age-ys-morgen-queens"),
    ("pelagia", "b7-part-xlviii-middle-age-pelagia-triton-kings"),
    ("oceania", "b7-part-xlix-middle-age-oceania-mermidons"),
    ("atlantis", "b7-part-l-middle-age-atlantis-kings-of-the-deep"),
    ("rlyeh", "b7-part-li-middle-age-r-lyeh-fallen-star"),
]
for _slug, _part in _REMAINING_MA_NAVIGATION:
    _heading = _slug.replace("-", "-")
    DESTINATION_ALIASES.update({
        f"b7-ma-{_slug}": _part,
        f"b7-ma-{_slug}-roster": f"b7-{_heading}-commander-roster",
        f"b7-ma-{_slug}-mages": f"b7-{_heading}-mage-and-priest-portfolio",
        f"b7-ma-{_slug}-spells": f"b7-{_heading}-national-spell-map",
        f"b7-ma-{_slug}-research": f"b7-{_heading}-research-response-tree",
        f"b7-ma-{_slug}-open": f"b7-{_heading}-unresolved-evidence-boundary",
    })
for _suffix, _target_suffix in {
    "roster": "commander-roster",
    "mages": "mage-and-priest-portfolio",
    "spells": "national-spell-map",
    "research": "research-response-tree",
    "open": "unresolved-evidence-boundary",
}.items():
    DESTINATION_ALIASES[f"b7-ma-rlyeh-{_suffix}"] = f"b7-r-lyeh-{_target_suffix}"


def aliases_by_target() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for alias, target in DESTINATION_ALIASES.items():
        result.setdefault(target, []).append(alias)
    return result


@dataclass(frozen=True)
class HeadingRecord:
    source_file: str
    source_code: str
    level: int
    title: str
    anchor: str
    line: int
    ordinal: int
    parent_anchor: str | None


def plain_heading(text: str) -> str:
    """Strip the small Markdown subset that can appear inside headings."""
    text = re.sub(r"\s+\{#[A-Za-z0-9_.:-]+\}\s*$", "", text.strip())
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    return text.strip()


def slugify(text: str) -> str:
    """Create a conservative ASCII destination suitable for PDF and web use."""
    normalized = unicodedata.normalize("NFKD", plain_heading(text))
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    ascii_text = ascii_text.replace("&", " and ")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    return slug or "section"


def parse_headings(path: Path, code: str) -> list[HeadingRecord]:
    """Parse headings and assign deterministic, file-scoped destination IDs."""
    records: list[HeadingRecord] = []
    seen: dict[str, int] = {}
    parent_by_level: dict[int, str] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
        if not match:
            continue
        level = len(match.group(1))
        raw_title = match.group(2)
        explicit = re.search(r"\s+\{#([A-Za-z0-9_.:-]+)\}\s*$", raw_title)
        title = plain_heading(raw_title)
        base = explicit.group(1) if explicit else f"{code}-{slugify(title)}"
        count = seen.get(base, 0) + 1
        seen[base] = count
        anchor = base if count == 1 else f"{base}-{count}"
        parent = next(
            (parent_by_level[n] for n in range(level - 1, 0, -1) if n in parent_by_level),
            None,
        )
        records.append(
            HeadingRecord(
                source_file=path.name,
                source_code=code,
                level=level,
                title=title,
                anchor=anchor,
                line=line_number,
                ordinal=len(records),
                parent_anchor=parent,
            )
        )
        parent_by_level[level] = anchor
        for stale in [n for n in parent_by_level if n > level]:
            del parent_by_level[stale]
    return records


def heading_catalog(root: Path, specs: list[SourceSpec] | None = None) -> dict[str, list[HeadingRecord]]:
    catalog: dict[str, list[HeadingRecord]] = {}
    for spec in specs or SOURCE_SPECS:
        path = root / spec.filename
        if path.exists():
            catalog[spec.filename] = parse_headings(path, spec.code)
    return catalog


def cross_reference_targets(
    catalog: dict[str, list[HeadingRecord]],
) -> tuple[dict[str, str], dict[tuple[str, str], str], dict[str, str]]:
    """Return book, part, and numbered-section destinations for prose linking."""
    books: dict[str, str] = {}
    parts: dict[tuple[str, str], str] = {}
    sections: dict[str, str] = {}
    code_to_roman = {f"b{i}": roman for i, roman in enumerate(
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
    ) if i}
    for records in catalog.values():
        if not records:
            continue
        code = records[0].source_code
        roman = code_to_roman.get(code)
        if roman:
            books[roman] = records[0].anchor
        for record in records:
            part = re.match(r"Part\s+([IVXLCDM]+)\s*:", record.title, re.I)
            if roman and part:
                parts[(roman, part.group(1).upper())] = record.anchor
            if code == "b9":
                section = re.match(r"(\d+(?:\.\d+)*)\.\s+", record.title)
                if section:
                    sections[section.group(1)] = record.anchor
    return books, parts, sections
