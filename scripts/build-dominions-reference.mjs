import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { gunzipSync, gzipSync } from "node:zlib";

const sourcePath = "dominions/library/data/base-object-register.json.gz";
const outputPath = "dominions/tools/reference/data/catalogue.json.gz";
const source = JSON.parse(gunzipSync(readFileSync(sourcePath)));
const records = [];
const units = new Map();

const categoryLabels = {
  spell: "Spell",
  item: "Magic item",
  unit: "Referenced unit",
  pretender: "Pretender form",
  summon: "Summon relation",
  site: "Magic site",
  throne: "Throne",
  mercenary: "Mercenary company",
};

const pathCode = {
  Fire: "F",
  Air: "A",
  Water: "W",
  Earth: "E",
  Astral: "S",
  Death: "D",
  Nature: "N",
  Glamour: "G",
  Blood: "B",
  Holy: "H",
};

const asText = (value) => {
  if (value === null || value === undefined || value === "") return "";
  if (Array.isArray(value)) return value.map(asText).filter(Boolean).join(", ");
  if (typeof value === "object") return Object.entries(value).map(([key, entry]) => `${key} ${asText(entry)}`.trim()).join(", ");
  return String(value);
};

const requirements = (entries = []) => entries.map((entry) => `${entry.path}${entry.level}`).join(" ");
const pathCodes = (entries = []) => [...new Set(entries.map((entry) => entry.path || pathCode[entry]).filter(Boolean))];
const libraryUrl = (sectionId) => `/dominions/library/books/book-xii/#${sectionId || "b12-base-game-objects-and-the-searchable-reference-layer"}`;
const properties = (value = {}) => Object.entries(value).filter(([, entry]) => entry !== null && entry !== "");
const attribute = (label, value) => {
  const text = asText(value);
  return text ? [label, text] : null;
};
const attributes = (...entries) => entries.filter(Boolean);

const addRecord = (record) => records.push({
  categoryLabel: categoryLabels[record.category],
  engineId: null,
  paths: [],
  eras: [],
  level: null,
  status: "",
  properties: [],
  ...record,
});

const noteUnit = (unit, context, canonicalSectionId) => {
  if (!unit?.unit_id || !unit?.name) return;
  const id = Number(unit.unit_id);
  const current = units.get(id) || { id, name: unit.name, contexts: new Set(), sectionIds: [] };
  current.contexts.add(context);
  if (canonicalSectionId) current.sectionIds.push(canonicalSectionId);
  units.set(id, current);
};

const spellById = new Map(source.records.spells.map((spell) => [spell.id, spell]));

for (const spell of source.records.spells) {
  const paths = pathCodes(spell.path_requirements);
  const pathText = requirements(spell.path_requirements) || "No path requirement recorded";
  const effect = spell.effect || {};
  const access = spell.allowed_nations?.length
    ? spell.allowed_nations.map((nation) => `${nation.era || ""} ${nation.name || nation.nation_id}`.trim()).join(", ")
    : spell.access_scope;
  addRecord({
    id: spell.id,
    category: "spell",
    name: spell.name,
    engineId: spell.engine_id,
    paths,
    eras: [...new Set((spell.allowed_nations || []).map((nation) => nation.era).filter(Boolean))],
    level: spell.research_level,
    evidence: spell.evidence_status,
    status: spell.public_status,
    summary: `${spell.school} ${spell.research_level} · ${pathText} · ${spell.spell_kind}`,
    attributes: attributes(
      attribute("School", `${spell.school} ${spell.research_level}`),
      attribute("Paths", pathText),
      attribute("Spell kind", spell.spell_kind),
      attribute("Fatigue cost (raw)", spell.fatigue_cost_raw),
      attribute("Gem or slave cost (raw)", spell.gem_or_slave_cost_raw),
      attribute("Effect", effect.effect_name),
      attribute("Range", effect.range_base === undefined ? "" : `${effect.range_base} base; ${effect.range_per_level || 0} per level`),
      attribute("Area", effect.area_battlefield_percent ? `${effect.area_battlefield_percent}% of battlefield` : effect.area_base === undefined ? "" : `${effect.area_base} base; ${effect.area_per_level || 0} per level`),
      attribute("Role tags", spell.role_tags),
      attribute("Access", access),
      attribute("Summon targets", (spell.summon_target_units || []).map((unit) => `${unit.name} (#${unit.unit_id})`)),
      attribute("Selection groups", spell.summon_groups),
    ),
    properties: properties(Object.fromEntries((spell.extra_attributes || []).map((entry) => [entry.name || entry.key || "attribute", entry.value ?? entry]))),
    libraryUrl: libraryUrl(spell.canonical_section_id),
  });
}

for (const item of source.records.items) {
  const paths = pathCodes(item.path_requirements);
  const pathText = requirements(item.path_requirements) || "No path requirement recorded";
  addRecord({
    id: item.id,
    category: "item",
    name: item.name,
    engineId: item.engine_id,
    paths,
    level: item.construction_level,
    evidence: item.evidence_status,
    status: item.tier_class,
    summary: `${item.slot_type} · Construction ${item.construction_level} · ${pathText}`,
    attributes: attributes(
      attribute("Slot", item.slot_type),
      attribute("Construction", item.construction_level),
      attribute("Tier", item.tier_class),
      attribute("Paths", pathText),
      attribute("Weapon ID", item.weapon_id),
      attribute("Armour ID", item.armor_id),
    ),
    properties: properties(item.mechanical_properties),
    libraryUrl: libraryUrl(item.canonical_section_id),
  });
}

for (const site of source.records.sites) {
  const paths = pathCodes([site.site_path]);
  const recruits = (site.recruitable_units || []).map((unit) => `${unit.name} (#${unit.unit_id})`);
  const commanders = (site.recruitable_commanders || []).map((unit) => `${unit.name} (#${unit.unit_id})`);
  const summoned = (site.summoned_units || []).map((unit) => `${unit.name} (#${unit.unit_id})`);
  site.recruitable_units?.forEach((unit) => noteUnit(unit, `Recruitable at ${site.name}`, site.canonical_section_id));
  site.recruitable_commanders?.forEach((unit) => noteUnit(unit, `Commander at ${site.name}`, site.canonical_section_id));
  site.summoned_units?.forEach((unit) => noteUnit(unit, `Summoned by ${site.name}`, site.canonical_section_id));
  addRecord({
    id: site.id,
    category: "site",
    name: site.name,
    engineId: site.engine_id,
    paths,
    level: site.search_level,
    evidence: site.evidence_status,
    status: site.site_class,
    summary: `${site.site_path} · search level ${site.search_level} · ${site.site_class}`,
    attributes: attributes(
      attribute("Path", site.site_path),
      attribute("Search level", site.search_level),
      attribute("Site class", site.site_class),
      attribute("Locations", site.locations),
      attribute("Gem income", site.gem_income),
      attribute("Income after claim", site.claimed_gem_income),
      attribute("Recruitable units", recruits),
      attribute("Recruitable commanders", commanders),
      attribute("Summoned units", summoned),
    ),
    properties: properties(site.mechanical_properties),
    libraryUrl: libraryUrl(site.canonical_section_id),
  });
}

for (const throne of source.records.thrones) {
  const paths = pathCodes([throne.site_path]);
  throne.recruitable_units?.forEach((unit) => noteUnit(unit, `Recruitable at ${throne.name}`, throne.canonical_section_id));
  throne.recruitable_commanders?.forEach((unit) => noteUnit(unit, `Commander at ${throne.name}`, throne.canonical_section_id));
  throne.summoned_units?.forEach((unit) => noteUnit(unit, `Summoned by ${throne.name}`, throne.canonical_section_id));
  addRecord({
    id: throne.id,
    category: "throne",
    name: throne.name,
    engineId: throne.engine_id,
    paths,
    level: throne.throne_level,
    evidence: throne.evidence_status,
    status: `level-${throne.throne_level}`,
    summary: `Level ${throne.throne_level} Throne · ${throne.site_path}`,
    attributes: attributes(
      attribute("Throne level", throne.throne_level),
      attribute("Site path", throne.site_path),
      attribute("Locations", throne.locations),
      attribute("Gem income", throne.gem_income),
      attribute("Income after claim", throne.claimed_gem_income),
      attribute("Recruitable units", (throne.recruitable_units || []).map((unit) => `${unit.name} (#${unit.unit_id})`)),
      attribute("Recruitable commanders", (throne.recruitable_commanders || []).map((unit) => `${unit.name} (#${unit.unit_id})`)),
    ),
    properties: properties(throne.mechanical_properties),
    libraryUrl: libraryUrl(throne.canonical_section_id),
  });
}

for (const pretender of source.records.pretenders) {
  const paths = pathCodes(pretender.innate_paths);
  const innate = requirements(pretender.innate_paths) || "No innate paths recorded";
  const nations = (pretender.available_to || []).map((nation) => `${nation.era} ${nation.name}, ${nation.epithet}`);
  const eras = [...new Set((pretender.available_to || []).map((nation) => nation.era).filter(Boolean))];
  addRecord({
    id: pretender.id,
    category: "pretender",
    name: pretender.name,
    engineId: pretender.engine_id,
    paths,
    eras,
    evidence: pretender.evidence_status,
    status: "pretender-form",
    summary: `Dominion ${pretender.starting_dominion} · new path ${pretender.new_path_cost} · ${innate}`,
    attributes: attributes(
      attribute("Starting dominion", pretender.starting_dominion),
      attribute("New path cost", pretender.new_path_cost),
      attribute("Minimum imprisonment (raw)", pretender.minimum_imprisonment_raw),
      attribute("Innate paths", innate),
      attribute("Base statistics", pretender.base_statistics),
      attribute("Available to", nations),
      attribute("Reduced cost 20", (pretender.cheap_god_20_for || []).map((nation) => `${nation.era} ${nation.name}`)),
      attribute("Reduced cost 40", (pretender.cheap_god_40_for || []).map((nation) => `${nation.era} ${nation.name}`)),
    ),
    properties: properties(pretender.mechanical_properties),
    libraryUrl: libraryUrl(pretender.canonical_section_id),
  });
}

for (const summon of source.records.summons) {
  const spell = spellById.get(summon.spell_id);
  const targets = (summon.target_units || []).map((unit) => `${unit.name} (#${unit.unit_id})`);
  summon.target_units?.forEach((unit) => noteUnit(unit, `Summoned by ${summon.spell_name}`, summon.canonical_section_id));
  addRecord({
    id: summon.id,
    category: "summon",
    name: summon.spell_name,
    engineId: summon.spell_engine_id,
    paths: pathCodes(spell?.path_requirements),
    eras: [...new Set((spell?.allowed_nations || []).map((nation) => nation.era).filter(Boolean))],
    level: spell?.research_level ?? null,
    evidence: summon.evidence_status,
    status: summon.unresolved_selection?.length ? "unresolved-selection" : "resolved-or-named-selection",
    summary: targets.length ? `Targets ${targets.join(", ")}` : `Selection ${asText(summon.selection_groups) || "not fully resolved"}`,
    attributes: attributes(
      attribute("Spell", `${summon.spell_name} (#${summon.spell_engine_id})`),
      attribute("School", spell ? `${spell.school} ${spell.research_level}` : ""),
      attribute("Paths", requirements(spell?.path_requirements)),
      attribute("Target units", targets),
      attribute("Selection groups", summon.selection_groups),
      attribute("Resolution notes", summon.summon_resolution_notes),
      attribute("Unresolved selection", summon.unresolved_selection),
    ),
    libraryUrl: libraryUrl(summon.canonical_section_id),
  });
}

for (const company of source.records.mercenaries) {
  noteUnit(company.commander_unit, `Commander of ${company.name}`, company.canonical_section_id);
  noteUnit(company.troop_unit, `Troops of ${company.name}`, company.canonical_section_id);
  addRecord({
    id: company.id,
    category: "mercenary",
    name: company.name,
    engineId: company.engine_id,
    eras: company.eras || [],
    evidence: company.evidence_status,
    status: "mercenary-company",
    summary: `${company.commander_name} · ${company.starting_troops} ${company.troop_unit?.name || "troops"} · minimum bid ${company.minimum_bid_gold} gold`,
    attributes: attributes(
      attribute("Commander", `${company.commander_name}; ${company.commander_unit?.name || "unit not recorded"}`),
      attribute("Troops", `${company.starting_troops} ${company.troop_unit?.name || "units"}`),
      attribute("Minimum survivors", company.minimum_survivors),
      attribute("Minimum bid", `${company.minimum_bid_gold} gold`),
      attribute("Starting experience", company.starting_experience),
      attribute("Eras", company.eras),
      attribute("Fixed items", company.fixed_items),
    ),
    libraryUrl: libraryUrl(company.canonical_section_id),
  });
}

for (const unit of [...units.values()].sort((left, right) => left.id - right.id)) {
  const contexts = [...unit.contexts].sort();
  addRecord({
    id: `referenced-unit-${String(unit.id).padStart(4, "0")}`,
    category: "unit",
    name: unit.name,
    engineId: unit.id,
    evidence: "source-confirmed-reference",
    status: "referenced-subset",
    summary: contexts.slice(0, 2).join(" · ") + (contexts.length > 2 ? ` · ${contexts.length - 2} more contexts` : ""),
    attributes: attributes(attribute("Referenced by", contexts)),
    libraryUrl: libraryUrl(unit.sectionIds[0]),
  });
}

records.sort((left, right) => left.category.localeCompare(right.category) || left.name.localeCompare(right.name) || String(left.id).localeCompare(String(right.id)));
const counts = Object.fromEntries(Object.keys(categoryLabels).map((category) => [category, records.filter((record) => record.category === category).length]));
const catalogue = {
  schemaVersion: "1.0.0",
  edition: source.edition,
  generatedOn: source.generated_on,
  ruleset: source.ruleset,
  evidenceKey: source.evidence_key,
  coverage: {
    statement: "Spells, items, sites, Thrones, Pretender forms, summon relations, and mercenaries come from the pinned base-game object register. Referenced units are only units named by those records; they are not an exhaustive national troop and commander catalogue.",
    currentLibraryBaseline: "Dominions 6.36",
  },
  counts,
  totalRecords: records.length,
  records,
};
const rendered = `${JSON.stringify(catalogue)}\n`;
const compressed = gzipSync(Buffer.from(rendered), { level: 9 });

if (process.argv.includes("--check")) {
  if (!existsSync(outputPath) || !readFileSync(outputPath).equals(compressed)) {
    console.error(`Reference catalogue is out of date. Run: node ${process.argv[1]}`);
    process.exit(1);
  }
  console.log(`Reference catalogue is current: ${records.length.toLocaleString("en-AU")} records.`);
} else {
  writeFileSync(outputPath, compressed);
  console.log(`Wrote ${outputPath} with ${records.length.toLocaleString("en-AU")} records.`);
}
