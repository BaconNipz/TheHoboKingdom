const tabletopRecordSchema = "thehobokingdom-tool-record";
const tabletopRecordVersion = 1;
const tabletopMetadataKey = "thk-tool-data-metadata-v1";

const tabletopValue = (value, fallback = "Not recorded") => String(value || "").trim() || fallback;
const tabletopSigned = (value) => Number(value) >= 0 ? `+${Number(value)}` : String(Number(value));
const tabletopModifier = (score) => Math.floor(((Number(score) || 10) - 10) / 2);
const tabletopSlug = (value, fallback = "record") => String(value || fallback).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || fallback;

const tabletopMarkSaved = (key) => {
  try {
    const metadata = JSON.parse(window.localStorage.getItem(tabletopMetadataKey) || "{}");
    metadata[key] = new Date().toISOString();
    window.localStorage.setItem(tabletopMetadataKey, JSON.stringify(metadata));
  } catch {
    // The tool itself still works when browser storage is unavailable.
  }
};

const tabletopSave = (key, data, status) => {
  try {
    window.localStorage.setItem(key, JSON.stringify(data));
    tabletopMarkSaved(key);
    if (status) status.textContent = "Saved in this browser.";
  } catch {
    if (status) status.textContent = "The browser blocked local saving. Export the record before leaving this page.";
  }
};

const tabletopLoad = (key) => {
  try {
    return JSON.parse(window.localStorage.getItem(key) || "null");
  } catch {
    return null;
  }
};

const tabletopRemove = (key) => {
  try {
    window.localStorage.removeItem(key);
    const metadata = JSON.parse(window.localStorage.getItem(tabletopMetadataKey) || "{}");
    delete metadata[key];
    window.localStorage.setItem(tabletopMetadataKey, JSON.stringify(metadata));
  } catch {
    // Nothing else is required when storage is unavailable.
  }
};

const tabletopDownload = (record, filename) => {
  const blob = new Blob([`${JSON.stringify(record, null, 2)}\n`], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `${tabletopSlug(filename)}.json`;
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
};

const tabletopWireRecord = ({ root, tool, storageKey, getData, setData, reset, filename, status, render }) => {
  let saveTimer;
  const save = () => {
    clearTimeout(saveTimer);
    saveTimer = window.setTimeout(() => tabletopSave(storageKey, getData(), status), 180);
  };
  root.addEventListener("input", () => { render(); save(); });
  root.addEventListener("change", () => { render(); save(); });
  root.querySelector("[data-record-export]")?.addEventListener("click", () => {
    const data = getData();
    tabletopDownload({ schema: tabletopRecordSchema, schemaVersion: tabletopRecordVersion, tool, exportedAt: new Date().toISOString(), data }, filename(data));
    status.textContent = "JSON backup downloaded.";
  });
  root.querySelector("[data-record-import]")?.addEventListener("change", async (event) => {
    const file = event.currentTarget.files?.[0];
    if (!file) return;
    try {
      if (file.size > 2_000_000) throw new Error("The selected file is too large for this tool record.");
      const record = JSON.parse(await file.text());
      if (record?.schema !== tabletopRecordSchema || record?.schemaVersion !== tabletopRecordVersion || record?.tool !== tool || !record.data) throw new Error("This is not a compatible backup for this tool.");
      setData(record.data);
      render();
      tabletopSave(storageKey, getData(), status);
      status.textContent = "Backup restored and saved in this browser.";
    } catch (error) {
      status.textContent = `Import rejected: ${error.message}`;
    }
    event.currentTarget.value = "";
  });
  root.querySelector("[data-record-clear]")?.addEventListener("click", () => {
    if (!window.confirm("Clear this saved record from the browser? Export it first if it may be needed later.")) return;
    tabletopRemove(storageKey);
    reset();
    render();
    status.textContent = "The saved record was cleared.";
  });
  return save;
};

const tabletopPrint = (className) => {
  document.body.classList.add(className);
  const cleanup = () => document.body.classList.remove(className);
  window.addEventListener("afterprint", cleanup, { once: true });
  window.print();
  window.setTimeout(cleanup, 60000);
};

const tabletopFields = (fields) => Object.fromEntries(fields.map((field) => [field.name, field.type === "checkbox" ? field.checked : field.value]));
const tabletopSetFields = (fields, values = {}) => fields.forEach((field) => {
  if (!(field.name in values)) return;
  if (field.type === "checkbox") field.checked = Boolean(values[field.name]);
  else field.value = values[field.name] ?? "";
});

const characterBuilder = document.querySelector("[data-character-builder]");

if (characterBuilder) {
  const storageKey = "thk-dnd-character-builder-v1";
  const tool = "dnd-character-builder";
  const fields = [...characterBuilder.querySelectorAll("[data-character-field], [data-character-ability], [data-character-save]")];
  const skillRows = [...characterBuilder.querySelectorAll(".skill-builder-row")];
  const attacksHost = characterBuilder.querySelector("[data-character-attacks]");
  const attackTemplate = document.querySelector("[data-character-attack-template]");
  const output = document.querySelector("[data-character-output]");
  const status = document.querySelector("[data-record-status]");
  let save = () => {};

  const attackData = () => [...attacksHost.querySelectorAll("[data-character-attack-row]")].map((row) => Object.fromEntries([...row.querySelectorAll("[data-attack-field]")].map((field) => [field.dataset.attackField, field.value])));
  const addAttack = (values = {}) => {
    const row = attackTemplate.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-attack-field]").forEach((field) => { field.value = values[field.dataset.attackField] || ""; });
    row.querySelector("[data-row-remove]").addEventListener("click", () => { row.remove(); if (!attacksHost.children.length) addAttack(); render(); save(); });
    attacksHost.append(row);
  };
  const skillData = () => Object.fromEntries(skillRows.map((row) => {
    const rank = row.querySelector("[data-skill-rank]");
    const extra = row.querySelector("[data-skill-extra]");
    return [rank.dataset.skillRank, { rank: Number(rank.value), extra: Number(extra.value) || 0 }];
  }));
  const getData = () => ({ fields: tabletopFields(fields), skills: skillData(), attacks: attackData() });
  const setData = (data = {}) => {
    tabletopSetFields(fields, data.fields || {});
    skillRows.forEach((row) => {
      const rank = row.querySelector("[data-skill-rank]");
      const extra = row.querySelector("[data-skill-extra]");
      rank.value = data.skills?.[rank.dataset.skillRank]?.rank ?? 0;
      extra.value = data.skills?.[rank.dataset.skillRank]?.extra ?? 0;
    });
    attacksHost.replaceChildren();
    const attacks = Array.isArray(data.attacks) && data.attacks.length ? data.attacks : Array.from({ length: 4 }, () => ({}));
    attacks.forEach(addAttack);
  };
  const paragraph = (parent, label, value) => {
    const section = document.createElement("section");
    const heading = document.createElement("h3");
    heading.textContent = label;
    const body = document.createElement("p");
    body.textContent = tabletopValue(value, "—");
    section.append(heading, body);
    parent.append(section);
  };
  const render = () => {
    const values = tabletopFields(fields);
    const level = Math.min(20, Math.max(1, Number(values.level) || 1));
    const proficiency = values.proficiency_override === "" ? 2 + Math.floor((level - 1) / 4) : Number(values.proficiency_override) || 0;
    const modifiers = {};
    characterBuilder.querySelectorAll("[data-character-ability]").forEach((field) => {
      modifiers[field.dataset.characterAbility] = tabletopModifier(field.value);
      characterBuilder.querySelector(`[data-character-mod="${field.dataset.characterAbility}"]`).textContent = tabletopSigned(modifiers[field.dataset.characterAbility]);
      const proficient = characterBuilder.querySelector(`[data-character-save="${field.dataset.characterAbility}"]`).checked;
      characterBuilder.querySelector(`[data-character-save-total="${field.dataset.characterAbility}"]`).textContent = tabletopSigned(modifiers[field.dataset.characterAbility] + (proficient ? proficiency : 0));
    });
    skillRows.forEach((row) => {
      const rank = row.querySelector("[data-skill-rank]");
      const ability = rank.dataset.skillAbility;
      const extra = Number(row.querySelector("[data-skill-extra]").value) || 0;
      row.querySelector("[data-skill-total]").textContent = tabletopSigned(modifiers[ability] + (Number(rank.value) * proficiency) + extra);
    });
    const initiative = modifiers.dexterity + (Number(values.initiative_extra) || 0);
    const perceptionRow = skillRows.find((row) => row.querySelector("[data-skill-rank]").dataset.skillRank === "perception");
    const perceptionRank = Number(perceptionRow.querySelector("[data-skill-rank]").value);
    const perceptionExtra = Number(perceptionRow.querySelector("[data-skill-extra]").value) || 0;
    const passive = 10 + modifiers.wisdom + (perceptionRank * proficiency) + perceptionExtra + (Number(values.passive_extra) || 0);
    characterBuilder.querySelector("[data-character-proficiency]").textContent = tabletopSigned(proficiency);
    characterBuilder.querySelector("[data-character-initiative]").textContent = tabletopSigned(initiative);
    characterBuilder.querySelector("[data-character-passive]").textContent = String(passive);
    const spellAbility = values.spell_ability;
    characterBuilder.querySelector("[data-character-spell-attack]").textContent = spellAbility ? tabletopSigned(proficiency + modifiers[spellAbility] + (Number(values.spell_attack_extra) || 0)) : "—";
    characterBuilder.querySelector("[data-character-spell-dc]").textContent = spellAbility ? String(8 + proficiency + modifiers[spellAbility] + (Number(values.spell_dc_extra) || 0)) : "—";

    output.replaceChildren();
    const header = document.createElement("header");
    const name = document.createElement("h2");
    name.textContent = tabletopValue(values.name, "Unnamed character");
    const identity = document.createElement("p");
    identity.textContent = [tabletopValue(values.class, "Class not recorded"), `Level ${level}`, tabletopValue(values.species, "Species not recorded"), tabletopValue(values.background, "Background not recorded")].join(" · ");
    header.append(name, identity);
    const numbers = document.createElement("div");
    numbers.className = "character-number-grid";
    const numberPairs = [["AC", values.ac], ["HP", `${values.hp_current || 0} / ${values.hp_max || 0}`], ["Initiative", tabletopSigned(initiative)], ["Speed", values.speed], ["Proficiency", tabletopSigned(proficiency)], ["Passive Perception", passive]];
    numberPairs.forEach(([label, value]) => { const item = document.createElement("section"); const strong = document.createElement("strong"); strong.textContent = String(value); const small = document.createElement("span"); small.textContent = label; item.append(strong, small); numbers.append(item); });
    const abilities = document.createElement("div");
    abilities.className = "character-ability-summary";
    Object.entries(modifiers).forEach(([ability, modifier]) => { const item = document.createElement("span"); item.textContent = `${ability.slice(0, 3).toUpperCase()} ${values[ability]} (${tabletopSigned(modifier)})`; abilities.append(item); });
    const details = document.createElement("div");
    details.className = "character-print-details";
    const attacks = attackData().filter((entry) => Object.values(entry).some((value) => value.trim())).map((entry) => `${entry.name || "Action"}: ${[entry.attack, entry.damage, entry.range, entry.notes].filter(Boolean).join(" · ")}`).join("\n");
    paragraph(details, "Attacks and actions", attacks);
    paragraph(details, "Features, traits, and boons", values.features);
    paragraph(details, "Equipment and treasure", values.equipment);
    paragraph(details, "Proficiencies and languages", values.proficiencies);
    paragraph(details, "Cantrips and spells", values.spells);
    paragraph(details, "Appearance and personality", values.personality);
    paragraph(details, "Allies and contacts", values.allies);
    paragraph(details, "Backstory and campaign notes", values.notes);
    output.append(header, numbers, abilities, details);
  };
  setData(tabletopLoad(storageKey) || {});
  save = tabletopWireRecord({ root: characterBuilder, tool, storageKey, getData, setData, reset: () => { characterBuilder.reset(); setData({}); }, filename: (data) => `${data.fields.name || "character"}-5e-record`, status, render });
  characterBuilder.addEventListener("submit", (event) => { event.preventDefault(); render(); tabletopSave(storageKey, getData(), status); status.textContent = "Character record updated and saved."; });
  characterBuilder.querySelector("[data-character-add-attack]").addEventListener("click", () => { addAttack(); render(); save(); });
  characterBuilder.querySelector("[data-character-print]").addEventListener("click", () => { render(); tabletopPrint("print-character"); });
  render();
}

const chronicleBuilder = document.querySelector("[data-chronicle-builder]");

if (chronicleBuilder) {
  const storageKey = "thk-dnd-session-chronicle-v1";
  const tool = "dnd-session-chronicle";
  const fields = [...chronicleBuilder.querySelectorAll("[data-chronicle-field]")];
  const privateFields = [...chronicleBuilder.querySelectorAll("[data-chronicle-private]")];
  const partyHost = chronicleBuilder.querySelector("[data-chronicle-party]");
  const partyTemplate = document.querySelector("[data-chronicle-party-template]");
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");
  let save = () => {};
  const partyData = () => [...partyHost.querySelectorAll("[data-chronicle-party-row]")].map((row) => Object.fromEntries([...row.querySelectorAll("[data-party-field]")].map((field) => [field.dataset.partyField, field.value])));
  const addMember = (values = {}) => {
    const row = partyTemplate.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-party-field]").forEach((field) => { field.value = values[field.dataset.partyField] || ""; });
    row.querySelector("[data-row-remove]").addEventListener("click", () => { row.remove(); if (!partyHost.children.length) addMember(); render(); save(); });
    partyHost.append(row);
  };
  const getData = () => ({ fields: tabletopFields(fields), private: tabletopFields(privateFields), party: partyData() });
  const setData = (data = {}) => {
    tabletopSetFields(fields, data.fields || {});
    tabletopSetFields(privateFields, data.private || {});
    partyHost.replaceChildren();
    const party = Array.isArray(data.party) && data.party.length ? data.party : Array.from({ length: 5 }, () => ({}));
    party.forEach(addMember);
  };
  const render = () => {
    const values = tabletopFields(fields);
    const party = partyData().filter((member) => member.character.trim()).map((member) => `- ${member.character}${member.player ? ` (${member.player})` : ""}${member.role ? ` — ${member.role}` : ""}${member.condition ? ` — ended: ${member.condition}` : ""}`);
    output.textContent = [
      tabletopValue(values.title, `${tabletopValue(values.campaign, "Campaign")} — Session ${tabletopValue(values.session, "?")}`),
      `${tabletopValue(values.date)} · ${tabletopValue(values.start_location)} to ${tabletopValue(values.end_location)}`,
      "", "PARTY", ...(party.length ? party : ["- Party not recorded."]),
      "", `OPENING SITUATION\n${tabletopValue(values.opening)}`,
      `WHAT HAPPENED\n${tabletopValue(values.events)}`,
      `DECISIONS\n${tabletopValue(values.decisions)}`,
      `PEOPLE AND PLACES\n${tabletopValue(values.people_places)}`,
      `DISCOVERIES\n${tabletopValue(values.discoveries)}`,
      `REWARDS, LOSSES, AND CHANGES\n${tabletopValue(values.rewards)}`,
      `VISIBLE CONSEQUENCES\n${tabletopValue(values.consequences)}`,
      `OPEN QUESTIONS\n${tabletopValue(values.questions)}`,
    ].join("\n\n");
  };
  setData(tabletopLoad(storageKey) || {});
  save = tabletopWireRecord({ root: chronicleBuilder, tool, storageKey, getData, setData, reset: () => { chronicleBuilder.reset(); setData({}); }, filename: (data) => `${data.fields.campaign || "campaign"}-session-${data.fields.session || "record"}`, status, render });
  chronicleBuilder.addEventListener("submit", (event) => { event.preventDefault(); render(); tabletopSave(storageKey, getData(), status); status.textContent = "Public chronicle rebuilt. Private fields remain excluded."; });
  chronicleBuilder.querySelector("[data-record-copy]").addEventListener("click", async () => { render(); try { await navigator.clipboard.writeText(output.textContent); status.textContent = "Public chronicle copied. GM-only fields were excluded."; } catch { status.textContent = "The browser blocked clipboard access. Select and copy the public chronicle instead."; } });
  chronicleBuilder.querySelector("[data-chronicle-print]").addEventListener("click", () => { render(); tabletopPrint("print-chronicle"); });
  chronicleBuilder.querySelector("[data-chronicle-add-member]").addEventListener("click", () => { addMember(); render(); save(); });
  render();
}

const initiativeTracker = document.querySelector("[data-initiative-tracker]");

if (initiativeTracker) {
  const storageKey = "thk-tabletop-initiative-v1";
  const tool = "tabletop-initiative-tracker";
  const fields = [...initiativeTracker.querySelectorAll("[data-initiative-field]")];
  const rowsHost = initiativeTracker.querySelector("[data-initiative-rows]");
  const rowTemplate = document.querySelector("[data-initiative-row-template]");
  const roundDisplay = initiativeTracker.querySelector("[data-initiative-round]");
  const status = document.querySelector("[data-record-status]");
  let round = 1;
  let save = () => {};
  const combatantData = () => [...rowsHost.querySelectorAll("[data-initiative-row]")].map((row) => Object.fromEntries([...row.querySelectorAll("[data-combatant-field]")].map((field) => [field.dataset.combatantField, field.type === "checkbox" || field.type === "radio" ? field.checked : field.value])));
  const addCombatant = (values = {}) => {
    const row = rowTemplate.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-combatant-field]").forEach((field) => { if (field.type === "checkbox" || field.type === "radio") field.checked = Boolean(values[field.dataset.combatantField]); else field.value = values[field.dataset.combatantField] ?? field.value; });
    row.querySelector("[data-row-remove]").addEventListener("click", () => { row.remove(); if (!rowsHost.children.length) addCombatant(); render(); save(); });
    rowsHost.append(row);
  };
  const getData = () => ({ fields: tabletopFields(fields), round, combatants: combatantData() });
  const setData = (data = {}) => {
    tabletopSetFields(fields, data.fields || {});
    round = Math.max(1, Number(data.round) || 1);
    rowsHost.replaceChildren();
    const combatants = Array.isArray(data.combatants) && data.combatants.length ? data.combatants : Array.from({ length: 6 }, () => ({}));
    combatants.forEach(addCombatant);
  };
  const render = () => {
    roundDisplay.textContent = String(round);
    rowsHost.querySelectorAll("[data-initiative-row]").forEach((row) => row.classList.toggle("is-active", row.querySelector('[data-combatant-field="active"]').checked));
  };
  setData(tabletopLoad(storageKey) || {});
  save = tabletopWireRecord({ root: initiativeTracker, tool, storageKey, getData, setData, reset: () => { initiativeTracker.reset(); round = 1; setData({}); }, filename: (data) => `${data.fields.name || "encounter"}-initiative`, status, render });
  initiativeTracker.querySelector("[data-initiative-add]").addEventListener("click", () => { addCombatant(); render(); save(); });
  initiativeTracker.querySelector("[data-initiative-sort]").addEventListener("click", () => { const rows = [...rowsHost.children].sort((a, b) => Number(b.querySelector('[data-combatant-field="initiative"]').value) - Number(a.querySelector('[data-combatant-field="initiative"]').value)); rowsHost.append(...rows); render(); save(); status.textContent = "Initiative sorted from highest to lowest."; });
  initiativeTracker.querySelector("[data-initiative-next]").addEventListener("click", () => {
    const rows = [...rowsHost.querySelectorAll("[data-initiative-row]")];
    if (!rows.length) return;
    let current = rows.findIndex((row) => row.querySelector('[data-combatant-field="active"]').checked);
    const next = current < 0 ? 0 : (current + 1) % rows.length;
    if (current >= 0) rows[current].querySelector('[data-combatant-field="active"]').checked = false;
    rows[next].querySelector('[data-combatant-field="active"]').checked = true;
    if (current >= 0 && next === 0) round += 1;
    render(); save();
  });
  initiativeTracker.querySelector("[data-initiative-print]").addEventListener("click", () => tabletopPrint("print-initiative"));
  render();
}

const handoutBuilder = document.querySelector("[data-handout-builder]");

if (handoutBuilder) {
  const storageKey = "thk-tabletop-handout-v1";
  const tool = "tabletop-handout-builder";
  const fields = [...handoutBuilder.querySelectorAll("[data-handout-field]")];
  const preview = document.querySelector("[data-handout-preview]");
  const status = document.querySelector("[data-record-status]");
  const getData = () => ({ fields: tabletopFields(fields) });
  const setData = (data = {}) => tabletopSetFields(fields, data.fields || {});
  const render = () => {
    const values = tabletopFields(fields);
    preview.className = `handout-preview handout-preview--${values.style || "letter"}`;
    preview.querySelector("[data-handout-preview-kicker]").textContent = tabletopValue(values.kicker, values.style === "notice" ? "Public notice" : "Recovered document");
    preview.querySelector("[data-handout-preview-title]").textContent = tabletopValue(values.title, "Untitled handout");
    preview.querySelector("[data-handout-preview-body]").textContent = tabletopValue(values.body, "Start writing to see the printable handout.");
    preview.querySelector("[data-handout-preview-signature]").textContent = values.signature ? `— ${values.signature}` : "";
    preview.querySelector("[data-handout-preview-reference]").textContent = values.reference || "";
    preview.querySelector("[data-handout-preview-footer]").textContent = values.footer || "";
  };
  setData(tabletopLoad(storageKey) || {});
  tabletopWireRecord({ root: handoutBuilder, tool, storageKey, getData, setData, reset: () => { handoutBuilder.reset(); }, filename: (data) => `${data.fields.title || "tabletop-handout"}`, status, render });
  handoutBuilder.addEventListener("submit", (event) => { event.preventDefault(); render(); tabletopSave(storageKey, getData(), status); status.textContent = "Handout updated and saved."; });
  handoutBuilder.querySelector("[data-handout-print]").addEventListener("click", () => { render(); tabletopPrint("print-handout"); });
  render();
}
