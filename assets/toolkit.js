const toolkitSchema = "thehobokingdom-tool-record";
const toolkitSchemaVersion = 1;

const toolkitCopy = async (output, status) => {
  const text = output?.textContent.trim();
  if (!text) {
    status.textContent = "Create the record first.";
    return;
  }
  try {
    await navigator.clipboard.writeText(text);
    status.textContent = "Copied.";
  } catch {
    status.textContent = "The browser blocked clipboard access. Select and copy the text instead.";
  }
};

const toolkitFilename = (value, fallback) => {
  const cleaned = String(value || "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 60);
  return cleaned || fallback;
};

const toolkitDownload = (filename, value) => {
  const blob = new Blob([`${JSON.stringify(value, null, 2)}\n`], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
};

const toolkitEnvelope = (tool, data) => ({
  schema: toolkitSchema,
  schemaVersion: toolkitSchemaVersion,
  tool,
  exportedAt: new Date().toISOString(),
  data,
});

const toolkitStorageLoad = (key) => {
  try {
    return JSON.parse(window.localStorage.getItem(key) || "null");
  } catch {
    return null;
  }
};

const toolkitStorageSave = (key, data, status) => {
  try {
    window.localStorage.setItem(key, JSON.stringify(data));
    window.thkStorageMarkUpdated?.(key);
    status.textContent = "Saved in this browser.";
  } catch {
    status.textContent = "Browser storage is unavailable. Export the record before leaving this page.";
  }
};

const toolkitFieldValues = (fields) => Object.fromEntries(fields.map((field) => [field.name, field.value]));

const toolkitApplyFields = (fields, values = {}) => {
  for (const field of fields) {
    if (Object.hasOwn(values, field.name) && ["string", "number"].includes(typeof values[field.name])) {
      field.value = values[field.name];
    }
  }
};

const toolkitValue = (value, fallback = "Not recorded.") => String(value || "").trim() || fallback;

const toolkitWireRecord = ({
  root,
  tool,
  storageKey,
  getData,
  setData,
  build,
  reset,
  filename,
  liveBuild = true,
}) => {
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");
  const importInput = root.querySelector("[data-record-import]");

  const save = () => toolkitStorageSave(storageKey, getData(), status);

  root.addEventListener("input", (event) => {
    if (event.target === importInput) return;
    save();
    if (liveBuild) build();
  });
  root.addEventListener("change", (event) => {
    if (event.target === importInput) return;
    save();
    if (liveBuild) build();
  });
  root.addEventListener("submit", async (event) => {
    event.preventDefault();
    save();
    await build();
  });
  root.querySelector("[data-record-copy]").addEventListener("click", async () => {
    await build();
    await toolkitCopy(output, status);
  });
  root.querySelector("[data-record-export]").addEventListener("click", () => {
    const data = getData();
    toolkitDownload(`${toolkitFilename(filename(data), tool)}.json`, toolkitEnvelope(tool, data));
    status.textContent = "JSON backup downloaded.";
  });
  importInput.addEventListener("change", async () => {
    const file = importInput.files?.[0];
    if (!file) return;
    try {
      if (file.size > 1_000_000) throw new Error("The selected JSON file is larger than this record format should require.");
      const record = JSON.parse(await file.text());
      if (record?.schema !== toolkitSchema || record?.schemaVersion !== toolkitSchemaVersion || record?.tool !== tool || !record?.data) {
        throw new Error("The selected file belongs to a different tool or schema version.");
      }
      await setData(record.data);
      toolkitStorageSave(storageKey, getData(), status);
      await build();
      status.textContent = "Backup restored and saved here.";
    } catch (error) {
      status.textContent = `Import failed: ${error.message}`;
    } finally {
      importInput.value = "";
    }
  });
  root.querySelector("[data-record-clear]").addEventListener("click", async () => {
    if (!window.confirm("Clear this saved record from the current browser? Export it first if it may be needed later.")) return;
    window.localStorage.removeItem(storageKey);
    window.thkStorageForget?.(storageKey);
    await reset();
    await build();
    output.textContent = "";
    status.textContent = "Saved record cleared.";
  });
};

const pretenderDesign = document.querySelector("[data-pretender-design]");

if (pretenderDesign) {
  const storageKey = "thk-dominions-pretender-design-v1";
  const fields = [...pretenderDesign.querySelectorAll("[data-pretender-field]")];
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");
  const pathCodes = ["f", "a", "w", "e", "s", "d", "n", "g", "b"];
  const scaleFields = [
    ["Order/Turmoil", "scale-order"],
    ["Productivity/Sloth", "scale-productivity"],
    ["Heat/Cold", "scale-temperature"],
    ["Growth/Death", "scale-growth"],
    ["Luck/Misfortune", "scale-luck"],
    ["Magic/Drain", "scale-magic"],
  ];

  const getData = () => ({ fields: toolkitFieldValues(fields) });
  const setData = (data) => toolkitApplyFields(fields, data.fields);
  const build = () => {
    const values = toolkitFieldValues(fields);
    const paths = pathCodes
      .map((code) => [code.toUpperCase(), Math.max(0, Number(values[`path-${code}`]) || 0)])
      .filter(([, level]) => level > 0)
      .map(([code, level]) => `${code}${level}`)
      .join(" ") || "No purchased magic paths recorded.";
    output.textContent = [
      `PRETENDER DESIGN — ${toolkitValue(values.design, "Unnamed design")}`,
      `Nation: ${toolkitValue(values.nation)}`,
      `Ruleset: ${toolkitValue(values.ruleset)}`,
      `Chassis: ${toolkitValue(values.chassis)}`,
      `Awakening: ${toolkitValue(values.awakening)}`,
      `Dominion: ${toolkitValue(values.dominion)}`,
      `Paths: ${paths}`,
      `Scales: ${scaleFields.map(([label, name]) => `${label} ${values[name]}`).join("; ")}`,
      "",
      `SACRED ROSTER\n${toolkitValue(values.sacreds)}`,
      `BLESS EFFECTS AND JOBS\n${toolkitValue(values.bless)}`,
      `SCALE REASONING\n${toolkitValue(values.scaleReason)}`,
      `AWAKENING AND EXPANSION ROLE\n${toolkitValue(values.expansion)}`,
      `PATH ACCESS AND RESEARCH GOALS\n${toolkitValue(values.pathGoals)}`,
      `WEAKNESSES AND FAILURE BRANCH\n${toolkitValue(values.failure)}`,
      `TEST RECORD\n${toolkitValue(values.tests)}`,
      `OTHER NOTES\n${toolkitValue(values.notes)}`,
      "",
      "This is a record of the design entered above. Use the game for design points; this sheet does not rate the strategy.",
    ].join("\n\n");
  };

  const saved = toolkitStorageLoad(storageKey);
  if (saved) setData(saved);
  toolkitWireRecord({
    root: pretenderDesign,
    tool: "dominions-pretender-design",
    storageKey,
    getData,
    setData,
    build,
    reset: () => pretenderDesign.reset(),
    filename: (data) => `${data.fields.design || "pretender-design"}-pretender-design`,
  });
  build();
  if (saved) status.textContent = "The saved design was restored from this browser.";
}

const sessionRecord = document.querySelector("[data-session-record]");

if (sessionRecord) {
  const storageKey = "thk-shared-session-record-v1";
  const fields = [...sessionRecord.querySelectorAll("[data-session-field]")];
  const rowsHost = sessionRecord.querySelector("[data-session-players]");
  const playerTemplate = document.querySelector("[data-session-player-template]");
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");

  const renumberPlayers = () => rowsHost.querySelectorAll("[data-session-player-row]").forEach((row, index) => {
    const number = index + 1;
    row.querySelectorAll("[data-session-player]").forEach((field) => field.setAttribute("aria-label", `Player ${number} ${field.dataset.sessionPlayer}`));
    row.querySelector("[data-row-remove]").setAttribute("aria-label", `Remove player ${number}`);
  });
  const addPlayer = (values = {}) => {
    const row = playerTemplate.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-session-player]").forEach((field) => { field.value = values[field.dataset.sessionPlayer] || ""; });
    row.querySelector("[data-row-remove]").addEventListener("click", () => {
      row.remove();
      if (!rowsHost.children.length) addPlayer();
      renumberPlayers();
      toolkitStorageSave(storageKey, getData(), status);
    });
    rowsHost.append(row);
    renumberPlayers();
  };
  const playerData = () => [...rowsHost.querySelectorAll("[data-session-player-row]")].map((row) => Object.fromEntries([...row.querySelectorAll("[data-session-player]")].map((field) => [field.dataset.sessionPlayer, field.value])));
  const getData = () => ({ fields: toolkitFieldValues(fields), players: playerData() });
  const setData = (data) => {
    toolkitApplyFields(fields, data.fields);
    rowsHost.replaceChildren();
    const players = Array.isArray(data.players) && data.players.length ? data.players : Array.from({ length: 6 }, () => ({}));
    players.forEach(addPlayer);
  };
  const build = () => {
    const values = toolkitFieldValues(fields);
    const players = playerData().filter((player) => Object.values(player).some((value) => value.trim()));
    const playerLines = players.length
      ? players.map((player) => `- ${toolkitValue(player.player, "Unnamed player")} — ${toolkitValue(player.role, "Role not recorded")} — responsibility: ${toolkitValue(player.responsibility)} — objective: ${toolkitValue(player.objective)}`)
      : ["- No players recorded."];
    output.textContent = [
      `${toolkitValue(values.game, "MULTIPLAYER").toUpperCase()} — ${toolkitValue(values.campaign, "Unlabelled campaign")}`,
      `Session ${toolkitValue(values.session, "?")} · ${toolkitValue(values.date)} · ${toolkitValue(values.status)}`,
      `Game version: ${toolkitValue(values.version)}`,
      `Host and connection: ${toolkitValue(values.connection)}`,
      `Mod profile: ${toolkitValue(values.manifest)}`,
      `Save or backup: ${toolkitValue(values.backup)}`,
      "",
      "PLAYERS AND RESPONSIBILITIES",
      ...playerLines,
      "",
      `STARTING STATE\n${toolkitValue(values.start)}`,
      `SESSION GOALS\n${toolkitValue(values.goals)}`,
      `PROGRESS AND CHECKPOINTS\n${toolkitValue(values.progress)}`,
      `DECISIONS AND AGREEMENTS\n${toolkitValue(values.decisions)}`,
      `PROBLEMS, CRASHES, AND FIXES\n${toolkitValue(values.issues)}`,
      `NEXT SESSION\n${toolkitValue(values.next)}`,
      `FILES AND HANDOUTS\n${toolkitValue(values.files)}`,
      `OTHER NOTES\n${toolkitValue(values.notes)}`,
    ].join("\n\n");
  };

  sessionRecord.querySelector("[data-session-add-player]").addEventListener("click", () => {
    addPlayer();
    toolkitStorageSave(storageKey, getData(), status);
  });
  const saved = toolkitStorageLoad(storageKey);
  setData(saved || { fields: {}, players: Array.from({ length: 6 }, () => ({})) });
  toolkitWireRecord({
    root: sessionRecord,
    tool: "shared-multiplayer-session",
    storageKey,
    getData,
    setData,
    build,
    reset: () => { sessionRecord.reset(); setData({ fields: toolkitFieldValues(fields), players: Array.from({ length: 6 }, () => ({})) }); },
    filename: (data) => `${data.fields.game || "multiplayer"}-${data.fields.campaign || "session"}-session-${data.fields.session || "1"}`,
  });
  build();
  if (saved) status.textContent = "The saved session was restored from this browser.";
}

const diplomacyLog = document.querySelector("[data-diplomacy-log]");

if (diplomacyLog) {
  const storageKey = "thk-dominions-diplomacy-log-v1";
  const fields = [...diplomacyLog.querySelectorAll("[data-diplomacy-field]")];
  const rows = [...diplomacyLog.querySelectorAll("[data-diplomacy-row]")];
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");

  const relationshipData = () => rows.map((row) => Object.fromEntries([...row.querySelectorAll("[data-diplomacy-col]")].map((field) => [field.dataset.diplomacyCol, field.value])));
  const getData = () => ({ fields: toolkitFieldValues(fields), relationships: relationshipData() });
  const setData = (data) => {
    toolkitApplyFields(fields, data.fields);
    rows.forEach((row, index) => {
      const values = data.relationships?.[index] || {};
      row.querySelectorAll("[data-diplomacy-col]").forEach((field) => { field.value = values[field.dataset.diplomacyCol] || (field.tagName === "SELECT" ? field.options[0].value : ""); });
    });
  };
  const build = () => {
    const values = toolkitFieldValues(fields);
    const turn = Math.max(1, Math.floor(Number(values.turn) || 1));
    const relationships = relationshipData().filter((entry) => entry.party.trim());
    const due = [];
    const lines = relationships.map((entry) => {
      const expiry = Math.max(0, Math.floor(Number(entry.expires) || 0));
      let timing = "no expiry recorded";
      if (expiry) {
        const remaining = expiry - turn;
        timing = remaining < 0 ? `expired ${Math.abs(remaining)} turn${Math.abs(remaining) === 1 ? "" : "s"} ago` : remaining === 0 ? "expires this turn" : `${remaining} turn${remaining === 1 ? "" : "s"} remaining`;
        if (remaining <= 3) due.push(`${entry.party}: ${timing}`);
      }
      return `- ${entry.party} — ${entry.stance} — ${entry.evidence}\n  ${toolkitValue(entry.terms)}\n  Starts: ${toolkitValue(entry.starts)}; expires: ${toolkitValue(entry.expires)} (${timing})\n  Next action: ${toolkitValue(entry.action)}`;
    });
    output.textContent = [
      `DIPLOMACY LOG — TURN ${turn} — ${toolkitValue(values.game, "Unlabelled game and nation")}`,
      `Table rules: ${toolkitValue(values.ruleset)}`,
      "",
      "RELATIONSHIPS AND AGREEMENTS",
      ...(lines.length ? lines : ["- No parties recorded."]),
      "",
      "EXPIRED OR DUE WITHIN THREE TURNS",
      ...(due.length ? due.map((item) => `- ${item}`) : ["- None recorded."]),
      "",
      `AWAITING REPLY\n${toolkitValue(values.pending)}`,
      `TRADES AND OBLIGATIONS\n${toolkitValue(values.obligations)}`,
      `OBSERVED BEHAVIOUR\n${toolkitValue(values.observations)}`,
      `PRIVATE STRATEGIC NOTES\n${toolkitValue(values.notes)}`,
      "",
      "The evidence label says where the note came from. It says nothing about whether the other player is trustworthy.",
    ].join("\n\n");
  };

  const saved = toolkitStorageLoad(storageKey);
  if (saved) setData(saved);
  toolkitWireRecord({
    root: diplomacyLog,
    tool: "dominions-diplomacy-log",
    storageKey,
    getData,
    setData,
    build,
    reset: () => diplomacyLog.reset(),
    filename: (data) => `${data.fields.game || "dominions"}-turn-${data.fields.turn || "1"}-diplomacy`,
  });
  build();
  if (saved) status.textContent = "The saved diplomacy log was restored from this browser.";
}

const modManifest = document.querySelector("[data-mod-manifest]");

if (modManifest) {
  const storageKey = "thk-mod-manifest-v1";
  const fields = [...modManifest.querySelectorAll("[data-manifest-field]")];
  const rowsHost = modManifest.querySelector("[data-manifest-rows]");
  const template = document.querySelector("[data-manifest-row-template]");
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");

  const renumber = () => rowsHost.querySelectorAll("[data-manifest-row]").forEach((row, index) => {
    const number = index + 1;
    row.querySelector("[data-row-number]").textContent = number;
    row.querySelectorAll("[data-manifest-col]").forEach((field) => field.setAttribute("aria-label", `Mod ${number} ${field.dataset.manifestCol}`));
    row.querySelector("[data-row-remove]").setAttribute("aria-label", `Remove mod ${number}`);
  });
  const addRow = (values = {}) => {
    const row = template.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-manifest-col]").forEach((field) => {
      const key = field.dataset.manifestCol;
      if (Object.hasOwn(values, key)) field.value = values[key];
    });
    row.querySelector("[data-row-remove]").addEventListener("click", () => {
      row.remove();
      if (!rowsHost.children.length) addRow();
      renumber();
      toolkitStorageSave(storageKey, getData(), status);
    });
    rowsHost.append(row);
    renumber();
  };
  const modData = () => [...rowsHost.querySelectorAll("[data-manifest-row]")].map((row) => Object.fromEntries([...row.querySelectorAll("[data-manifest-col]")].map((field) => [field.dataset.manifestCol, field.value])));
  const getData = () => ({ fields: toolkitFieldValues(fields), mods: modData() });
  const setData = (data) => {
    toolkitApplyFields(fields, data.fields);
    rowsHost.replaceChildren();
    const mods = Array.isArray(data.mods) && data.mods.length ? data.mods : Array.from({ length: 6 }, () => ({}));
    mods.forEach(addRow);
  };
  const digest = async (data) => {
    if (!window.crypto?.subtle) return "Unavailable in this browser";
    const bytes = new TextEncoder().encode(JSON.stringify(data));
    const hash = await window.crypto.subtle.digest("SHA-256", bytes);
    return [...new Uint8Array(hash)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
  };
  const build = async () => {
    const data = getData();
    const values = data.fields;
    const mods = data.mods.filter((mod) => mod.name.trim());
    const states = mods.reduce((counts, mod) => ({ ...counts, [mod.test]: (counts[mod.test] || 0) + 1 }), {});
    const fingerprint = await digest({ fields: values, mods });
    output.textContent = [
      `MOD MANIFEST — ${toolkitValue(values.name, "Unnamed profile")}`,
      `Game: ${toolkitValue(values.game)} ${toolkitValue(values.gameVersion, "")}`.trim(),
      `Profile version: ${toolkitValue(values.profileVersion)}`,
      `Loader or platform: ${toolkitValue(values.loader)}`,
      `Status: ${toolkitValue(values.status)}; frozen: ${toolkitValue(values.freezeDate)}`,
      `Host: ${toolkitValue(values.host)}; reference: ${toolkitValue(values.reference)}`,
      `Manifest SHA-256: ${fingerprint}`,
      "",
      "MODS IN LOAD ORDER",
      ...(mods.length ? mods.map((mod, index) => `${index + 1}. ${mod.name} — ${toolkitValue(mod.version)} — ${toolkitValue(mod.file)}\n   Side: ${mod.side}; test: ${mod.test}; dependencies/interactions: ${toolkitValue(mod.dependencies)}; notes: ${toolkitValue(mod.notes)}`) : ["No mods recorded."]),
      "",
      `TEST STATES\n${Object.keys(states).length ? Object.entries(states).map(([state, count]) => `${state}: ${count}`).join("; ") : "No mod rows recorded."}`,
      `KNOWN WORKING COMBINATIONS\n${toolkitValue(values.working)}`,
      `KNOWN ISSUES AND SUSPECTED CONFLICTS\n${toolkitValue(values.issues)}`,
      `RECOVERY BASELINE\n${toolkitValue(values.recovery)}`,
      `UPDATE PROCEDURE\n${toolkitValue(values.updates)}`,
      "",
      "Compatibility only applies to the versions and tests recorded above.",
    ].join("\n\n");
  };

  modManifest.querySelector("[data-manifest-add]").addEventListener("click", () => {
    addRow();
    toolkitStorageSave(storageKey, getData(), status);
  });
  const saved = toolkitStorageLoad(storageKey);
  setData(saved || { fields: {}, mods: Array.from({ length: 6 }, () => ({})) });
  toolkitWireRecord({
    root: modManifest,
    tool: "mod-manifest",
    storageKey,
    getData,
    setData,
    build,
    reset: () => { modManifest.reset(); setData({ fields: toolkitFieldValues(fields), mods: Array.from({ length: 6 }, () => ({})) }); },
    filename: (data) => `${data.fields.name || "mod-profile"}-${data.fields.profileVersion || "manifest"}`,
    liveBuild: false,
  });
  build();
  if (saved) status.textContent = "The saved manifest was restored from this browser.";
}

const libraryReading = document.querySelector("[data-library-reading]");

if (libraryReading) {
  const storageKey = "thk-dominions-library-reading-v1";
  const form = libraryReading.querySelector("[data-reading-form]");
  const fields = [...form.querySelectorAll("[data-reading-field]")];
  const rowsHost = libraryReading.querySelector("[data-reading-rows]");
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");
  const progress = libraryReading.querySelector("[data-reading-progress]");
  const progressLabel = libraryReading.querySelector("[data-reading-progress-label]");
  const sectionStat = libraryReading.querySelector("[data-reading-sections]");
  const bookStat = libraryReading.querySelector("[data-reading-books]");
  const percentStat = libraryReading.querySelector("[data-reading-percent]");
  let manifest = null;

  const rowData = () => Object.fromEntries([...rowsHost.querySelectorAll("[data-reading-row]")].map((row) => [row.dataset.bookId, {
    completed: row.querySelector("[data-reading-completed]").value,
    priority: row.querySelector("[data-reading-priority]").value,
    next: row.querySelector("[data-reading-next]").value,
  }]));
  const getData = () => ({ edition: manifest?.edition || "", fields: toolkitFieldValues(fields), books: rowData() });
  const setData = (data) => {
    toolkitApplyFields(fields, data.fields);
    rowsHost.querySelectorAll("[data-reading-row]").forEach((row) => {
      const values = data.books?.[row.dataset.bookId];
      if (!values) return;
      row.querySelector("[data-reading-completed]").value = values.completed ?? 0;
      row.querySelector("[data-reading-priority]").value = values.priority || "Normal";
      row.querySelector("[data-reading-next]").value = values.next || "";
    });
  };
  const build = () => {
    if (!manifest) return;
    const plan = toolkitFieldValues(fields);
    const books = rowData();
    const records = manifest.documents.map((book, index) => {
      const values = books[book.id] || {};
      const completed = Math.min(book.sectionCount, Math.max(0, Math.floor(Number(values.completed) || 0)));
      return { ...book, index, completed, priority: values.priority || "Normal", next: values.next || "" };
    });
    const totalSections = records.reduce((sum, book) => sum + book.sectionCount, 0);
    const completedSections = records.reduce((sum, book) => sum + book.completed, 0);
    const completedBooks = records.filter((book) => book.completed >= book.sectionCount).length;
    const percentage = totalSections ? completedSections / totalSections * 100 : 0;
    progress.value = percentage;
    progressLabel.textContent = `${completedSections.toLocaleString("en-AU")} of ${totalSections.toLocaleString("en-AU")} sections recorded`;
    sectionStat.textContent = completedSections.toLocaleString("en-AU");
    bookStat.textContent = completedBooks.toLocaleString("en-AU");
    percentStat.textContent = `${percentage.toLocaleString("en-AU", { maximumFractionDigits: 1 })}%`;

    const priorityOrder = { Next: 0, Normal: 1, Later: 2 };
    const nextBooks = records
      .filter((book) => book.completed < book.sectionCount)
      .sort((left, right) => (priorityOrder[left.priority] - priorityOrder[right.priority]) || ((right.completed > 0) - (left.completed > 0)) || left.index - right.index)
      .slice(0, 5);
    output.textContent = [
      toolkitValue(plan.plan, "READING PLAN").toUpperCase(),
      `Edition: ${manifest.edition}`,
      `Purpose: ${toolkitValue(plan.purpose)}`,
      `Progress: ${completedSections.toLocaleString("en-AU")} / ${totalSections.toLocaleString("en-AU")} sections (${percentage.toLocaleString("en-AU", { maximumFractionDigits: 1 })}%)`,
      "",
      "NEXT READING",
      ...(nextBooks.length ? nextBooks.map((book, index) => `${index + 1}. ${book.title}\n   ${book.completed} / ${book.sectionCount} sections; priority: ${book.priority}; next: ${toolkitValue(book.next)}`) : ["Every book in the current manifest is marked complete."]),
      "",
      "The order follows the priorities entered here; it is not an automatic claim that one subject matters more than another.",
    ].join("\n");
  };
  const renderRows = () => {
    rowsHost.replaceChildren();
    for (const book of manifest.documents) {
      const row = document.createElement("tr");
      row.dataset.readingRow = "";
      row.dataset.bookId = book.id;
      const heading = document.createElement("th");
      heading.textContent = book.title;
      const count = document.createElement("small");
      count.textContent = `${book.sectionCount.toLocaleString("en-AU")} sections`;
      heading.append(count);
      const completedCell = document.createElement("td");
      const completed = document.createElement("input");
      completed.type = "number";
      completed.min = "0";
      completed.max = String(book.sectionCount);
      completed.value = "0";
      completed.dataset.readingCompleted = "";
      completed.setAttribute("aria-label", `${book.title} sections completed`);
      const markComplete = document.createElement("button");
      markComplete.type = "button";
      markComplete.className = "reading-mark-complete";
      markComplete.textContent = "All";
      markComplete.setAttribute("aria-label", `Mark every ${book.title} section complete`);
      markComplete.addEventListener("click", () => {
        completed.value = String(book.sectionCount);
        toolkitStorageSave(storageKey, getData(), status);
        build();
      });
      const countControl = document.createElement("div");
      countControl.className = "reading-count-control";
      countControl.append(completed, markComplete);
      completedCell.append(countControl);
      const priorityCell = document.createElement("td");
      const priority = document.createElement("select");
      priority.dataset.readingPriority = "";
      priority.setAttribute("aria-label", `${book.title} priority`);
      ["Next", "Normal", "Later"].forEach((value) => priority.add(new Option(value, value, false, value === "Normal")));
      priorityCell.append(priority);
      const nextCell = document.createElement("td");
      const next = document.createElement("input");
      next.dataset.readingNext = "";
      next.placeholder = "Next heading, question, or purpose";
      next.setAttribute("aria-label", `${book.title} next reading note`);
      nextCell.append(next);
      const linkCell = document.createElement("td");
      const link = document.createElement("a");
      link.className = "text-link";
      link.href = `/dominions/library/books/${book.slug}/`;
      link.textContent = "Open →";
      linkCell.append(link);
      row.append(heading, completedCell, priorityCell, nextCell, linkCell);
      rowsHost.append(row);
    }
  };

  fetch(libraryReading.dataset.manifestUrl)
    .then((response) => {
      if (!response.ok) throw new Error(`manifest request returned ${response.status}`);
      return response.json();
    })
    .then((data) => {
      if (!Array.isArray(data.documents)) throw new Error("the manifest does not contain a document list");
      manifest = data;
      renderRows();
      const saved = toolkitStorageLoad(storageKey);
      if (saved) setData(saved);
      toolkitWireRecord({
        root: form,
        tool: "dominions-library-reading",
        storageKey,
        getData,
        setData,
        build,
        reset: () => { form.reset(); renderRows(); },
        filename: (record) => `${record.fields.plan || "dominions-library-reading"}-progress`,
      });
      build();
      status.textContent = saved ? "The saved reading plan was restored from this browser." : "Progress is saved only in this browser.";
    })
    .catch((error) => {
      rowsHost.innerHTML = `<tr><td colspan="5">The current library manifest could not be loaded.</td></tr>`;
      progressLabel.textContent = "Reading tracker unavailable";
      status.textContent = `Could not load the library manifest: ${error.message}`;
    });
}

const battlePlan = document.querySelector("[data-battle-plan]");

if (battlePlan) {
  const storageKey = "thk-dominions-battle-plan-v1";
  const fields = [...battlePlan.querySelectorAll("[data-battle-field]")];
  const checks = [...battlePlan.querySelectorAll("[data-battle-check]")];
  const groupsHost = battlePlan.querySelector("[data-battle-groups]");
  const commandersHost = battlePlan.querySelector("[data-battle-commanders]");
  const groupTemplate = document.querySelector("[data-battle-group-template]");
  const commanderTemplate = document.querySelector("[data-battle-commander-template]");
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");

  const renumber = (host, rowSelector, fieldSelector, label) => host.querySelectorAll(rowSelector).forEach((row, index) => {
    const number = index + 1;
    row.querySelector("[data-row-number]").textContent = number;
    row.querySelectorAll(fieldSelector).forEach((field) => field.setAttribute("aria-label", `${label} ${number} ${field.dataset[label === "Army group" ? "battleGroup" : "battleCommander"]}`));
    row.querySelector("[data-row-remove]").setAttribute("aria-label", `Remove ${label.toLowerCase()} ${number}`);
  });
  const readRows = (host, rowSelector, fieldSelector, key) => [...host.querySelectorAll(rowSelector)].map((row) => Object.fromEntries([...row.querySelectorAll(fieldSelector)].map((field) => [field.dataset[key], field.value])));
  const groupData = () => readRows(groupsHost, "[data-battle-group-row]", "[data-battle-group]", "battleGroup");
  const commanderData = () => readRows(commandersHost, "[data-battle-commander-row]", "[data-battle-commander]", "battleCommander");
  const getData = () => ({
    fields: toolkitFieldValues(fields),
    groups: groupData(),
    commanders: commanderData(),
    checked: checks.filter((check) => check.checked).map((check) => check.value),
  });

  const attachRemoval = (row, host, fallback, rowSelector, fieldSelector, label) => {
    row.querySelector("[data-row-remove]").addEventListener("click", () => {
      row.remove();
      if (!host.children.length) fallback();
      renumber(host, rowSelector, fieldSelector, label);
      toolkitStorageSave(storageKey, getData(), status);
      build();
    });
  };
  const addGroup = (values = {}) => {
    const row = groupTemplate.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-battle-group]").forEach((field) => { field.value = values[field.dataset.battleGroup] || ""; });
    attachRemoval(row, groupsHost, addGroup, "[data-battle-group-row]", "[data-battle-group]", "Army group");
    groupsHost.append(row);
    renumber(groupsHost, "[data-battle-group-row]", "[data-battle-group]", "Army group");
  };
  const addCommander = (values = {}) => {
    const row = commanderTemplate.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-battle-commander]").forEach((field) => { field.value = values[field.dataset.battleCommander] || ""; });
    attachRemoval(row, commandersHost, addCommander, "[data-battle-commander-row]", "[data-battle-commander]", "Commander");
    commandersHost.append(row);
    renumber(commandersHost, "[data-battle-commander-row]", "[data-battle-commander]", "Commander");
  };
  const setData = (data) => {
    toolkitApplyFields(fields, data.fields);
    const checked = new Set(data.checked || []);
    checks.forEach((check) => { check.checked = checked.has(check.value); });
    groupsHost.replaceChildren();
    commandersHost.replaceChildren();
    const groups = Array.isArray(data.groups) && data.groups.length ? data.groups : Array.from({ length: 6 }, () => ({}));
    const commanders = Array.isArray(data.commanders) && data.commanders.length ? data.commanders : Array.from({ length: 4 }, () => ({}));
    groups.forEach(addGroup);
    commanders.forEach(addCommander);
  };
  const build = () => {
    const values = toolkitFieldValues(fields);
    const groups = groupData().filter((group) => Object.values(group).some((value) => value.trim()));
    const commanders = commanderData().filter((commander) => Object.values(commander).some((value) => value.trim()));
    const complete = checks.filter((check) => check.checked).map((check) => check.value);
    const outstanding = checks.filter((check) => !check.checked).map((check) => check.value);
    output.textContent = [
      `BATTLE PLAN — TURN ${toolkitValue(values.turn, "?")} — ${toolkitValue(values.plan, "Unnamed battle")}`,
      `Game and nation: ${toolkitValue(values.game)}`,
      `Opponent: ${toolkitValue(values.opponent)}`,
      `Province: ${toolkitValue(values.province)}`,
      `Position: ${toolkitValue(values.side)}`,
      `Primary objective: ${toolkitValue(values.objective)}`,
      `Minimum acceptable result: ${toolkitValue(values.minimum)}`,
      `Loss limit or preservation priority: ${toolkitValue(values.lossLimit)}`,
      "",
      `BATTLEFIELD CONDITIONS\n${toolkitValue(values.conditions)}`,
      `GLOBALS AND BATTLEFIELD EFFECTS\n${toolkitValue(values.effects)}`,
      `ENEMY FORCE AND SCRIPTS OBSERVED\n${toolkitValue(values.enemy)}`,
      `EVIDENCE AND LAST OBSERVATION\n${toolkitValue(values.evidence)}`,
      `IMPORTANT UNKNOWNS\n${toolkitValue(values.unknowns)}`,
      `REINFORCEMENTS AND MOVEMENT\n${toolkitValue(values.movement)}`,
      "",
      "ARMY GROUPS",
      ...(groups.length ? groups.map((group, index) => `${index + 1}. ${toolkitValue(group.unit, "Unnamed group")} — count ${toolkitValue(group.count, "?")} — ${toolkitValue(group.role, "role not recorded")}\n   Position: ${toolkitValue(group.position)}; orders: ${toolkitValue(group.orders)}; protection/weakness: ${toolkitValue(group.notes)}`) : ["- No army groups recorded."]),
      "",
      "COMMANDERS AND MAGES",
      ...(commanders.length ? commanders.map((commander, index) => `${index + 1}. ${toolkitValue(commander.commander, "Unnamed commander")}\n   Paths/stats: ${toolkitValue(commander.paths)}\n   Items/gems: ${toolkitValue(commander.equipment)}\n   Script: ${toolkitValue(commander.script)}\n   Protection/fallback: ${toolkitValue(commander.protection)}`) : ["- No commanders recorded."]),
      "",
      `READINESS AUDIT\nComplete: ${complete.length} of ${checks.length}\n${outstanding.length ? outstanding.map((item) => `- Outstanding: ${item}`).join("\n") : "- No checklist items remain."}`,
      "",
      `THREAT AND RESPONSE LEDGER\n${toolkitValue(values.threats)}`,
      `EXPECTED BATTLE SEQUENCE\n${toolkitValue(values.sequence)}`,
      `FAVOURABLE BRANCH\n${toolkitValue(values.favourable)}`,
      `FAILURE BRANCH\n${toolkitValue(values.failure)}`,
      `RETREAT, RALLY, AND RECOVERY\n${toolkitValue(values.retreat)}`,
      `TEST RECORD AND REQUIRED REVISION\n${toolkitValue(values.tests)}`,
      "",
      "This sheet only records what was entered above. It does not simulate the battle or guess the result.",
    ].join("\n\n");
  };

  battlePlan.querySelector("[data-battle-add-group]").addEventListener("click", () => {
    addGroup();
    toolkitStorageSave(storageKey, getData(), status);
    build();
  });
  battlePlan.querySelector("[data-battle-add-commander]").addEventListener("click", () => {
    addCommander();
    toolkitStorageSave(storageKey, getData(), status);
    build();
  });
  const saved = toolkitStorageLoad(storageKey);
  setData(saved || { fields: {}, groups: Array.from({ length: 6 }, () => ({})), commanders: Array.from({ length: 4 }, () => ({})), checked: [] });
  toolkitWireRecord({
    root: battlePlan,
    tool: "dominions-battle-plan",
    storageKey,
    getData,
    setData,
    build,
    reset: () => {
      battlePlan.reset();
      setData({ fields: toolkitFieldValues(fields), groups: Array.from({ length: 6 }, () => ({})), commanders: Array.from({ length: 4 }, () => ({})), checked: [] });
    },
    filename: (data) => `${data.fields.game || "dominions"}-turn-${data.fields.turn || "1"}-${data.fields.plan || "battle-plan"}`,
  });
  build();
  if (saved) status.textContent = "The saved battle plan was restored from this browser.";
}

const thronePlan = document.querySelector("[data-throne-plan]");

if (thronePlan) {
  const storageKey = "thk-dominions-throne-plan-v2";
  const fields = [...thronePlan.querySelectorAll("[data-throne-field]")];
  const rowsHost = thronePlan.querySelector("[data-throne-rows]");
  const template = document.querySelector("[data-throne-row-template]");
  const output = document.querySelector("[data-record-output]");
  const status = document.querySelector("[data-record-status]");
  const friendlyStates = new Set(["Controlled, unclaimed", "Ready to claim", "Claimed by us"]);

  const renumber = () => rowsHost.querySelectorAll("[data-throne-row]").forEach((row, index) => {
    const number = index + 1;
    row.querySelector("[data-row-number]").textContent = number;
    row.querySelectorAll("[data-throne-col]").forEach((field) => field.setAttribute("aria-label", `Throne ${number} ${field.dataset.throneCol}`));
    row.querySelector("[data-throne-target]").setAttribute("aria-label", `Include Throne ${number} as a victory target`);
    row.querySelector("[data-row-remove]").setAttribute("aria-label", `Remove Throne ${number}`);
  });
  const throneData = () => [...rowsHost.querySelectorAll("[data-throne-row]")].map((row) => ({
    ...Object.fromEntries([...row.querySelectorAll("[data-throne-col]")].map((field) => [field.dataset.throneCol, field.value])),
    target: row.querySelector("[data-throne-target]").checked,
  }));
  const getData = () => ({ fields: toolkitFieldValues(fields), thrones: throneData() });
  const addRow = (values = {}) => {
    const row = template.content.firstElementChild.cloneNode(true);
    row.querySelectorAll("[data-throne-col]").forEach((field) => {
      const key = field.dataset.throneCol;
      if (Object.hasOwn(values, key)) field.value = values[key];
    });
    row.querySelector("[data-throne-target]").checked = Boolean(values.target);
    row.querySelector("[data-row-remove]").addEventListener("click", () => {
      row.remove();
      if (!rowsHost.children.length) addRow();
      renumber();
      toolkitStorageSave(storageKey, getData(), status);
      build();
    });
    rowsHost.append(row);
    renumber();
  };
  const setData = (data) => {
    toolkitApplyFields(fields, data.fields);
    rowsHost.replaceChildren();
    const thrones = Array.isArray(data.thrones) && data.thrones.length ? data.thrones : Array.from({ length: 8 }, () => ({}));
    thrones.forEach(addRow);
  };
  const build = () => {
    const values = toolkitFieldValues(fields);
    const turn = Math.max(1, Math.floor(Number(values.turn) || 1));
    const required = Math.max(1, Math.floor(Number(values.required) || 1));
    const outsideClaimed = Math.max(0, Math.floor(Number(values.outsideClaimed) || 0));
    const thrones = throneData().filter((throne) => throne.name.trim() || throne.state !== "Unknown" || throne.target);
    const points = (rows) => rows.reduce((sum, throne) => sum + Math.max(1, Math.min(3, Math.floor(Number(throne.level) || 1))), 0);
    const claimedRows = thrones.filter((throne) => throne.state === "Claimed by us");
    const readyRows = thrones.filter((throne) => throne.state === "Ready to claim");
    const controlledRows = thrones.filter((throne) => throne.state === "Controlled, unclaimed");
    const targetRows = thrones.filter((throne) => throne.target && !friendlyStates.has(throne.state));
    const claimed = outsideClaimed + points(claimedRows);
    const readyPoints = points(readyRows);
    const controlledPoints = points(controlledRows);
    const targetPoints = points(targetRows);
    const afterReady = claimed + readyPoints;
    const controlledPotential = afterReady + controlledPoints;
    const namedPotential = controlledPotential + targetPoints;
    const remaining = Math.max(0, required - claimed);
    const remainingAfterReady = Math.max(0, required - afterReady);
    const stale = thrones.filter((throne) => {
      const verified = Math.max(0, Math.floor(Number(throne.verified) || 0));
      return verified > 0 && turn - verified > 3 && throne.state !== "Claimed by us";
    });
    const currentState = claimed >= required
      ? "The entered claimed total meets the Ascension requirement."
      : afterReady >= required
        ? "The ready claim orders reach the requirement if every listed order remains legal and survives hosting."
        : controlledPotential >= required
          ? "Friendly controlled Thrones contain enough points, but more claim orders or hosting cycles are required."
          : namedPotential >= required
            ? "The friendly position is short; the marked target pool can reach the requirement if captured, held, and claimed."
            : "The entered friendly and marked target pools do not yet contain enough points.";
    const throneLines = thrones.map((throne, index) => {
      const verified = throne.verified ? `turn ${throne.verified}` : "turn not recorded";
      return `${index + 1}. ${toolkitValue(throne.name, "Unnamed Throne")} — ${throne.level} AP — ${throne.state}${throne.target ? " — VICTORY TARGET" : ""}\n   Controller: ${toolkitValue(throne.controller)}; claimant/action: ${toolkitValue(throne.claimant)}\n   Evidence: ${throne.evidence}; last verified: ${verified}; notes: ${toolkitValue(throne.notes)}`;
    });
    output.textContent = [
      `THRONE AND VICTORY POSITION — TURN ${turn}`,
      `Game: ${toolkitValue(values.game)}; nation: ${toolkitValue(values.nation)}`,
      `Victory requirement: ${required} AP`,
      `Claimed AP: ${claimed} (${outsideClaimed} not itemised; ${points(claimedRows)} from listed friendly claims)`,
      `Remaining now: ${remaining} AP`,
      "",
      `Ready to claim: ${readyRows.length} Throne${readyRows.length === 1 ? "" : "s"}, ${readyPoints} AP`,
      `Projected after ready orders: ${afterReady} AP; ${remainingAfterReady} AP remaining`,
      `Controlled but not ready: ${controlledRows.length} Throne${controlledRows.length === 1 ? "" : "s"}, ${controlledPoints} AP`,
      `Potential after every friendly controlled Throne is claimed: ${controlledPotential} AP`,
      `Marked targets outside friendly control: ${targetRows.length}, ${targetPoints} AP`,
      `Potential including marked targets: ${namedPotential} AP`,
      "",
      currentState,
      "",
      "READY CLAIM ORDERS",
      ...(readyRows.length ? readyRows.map((throne) => `- ${toolkitValue(throne.name, "Unnamed Throne")} — ${throne.level} AP — ${toolkitValue(throne.claimant, "claimant not recorded")}`) : ["- None recorded."]),
      "",
      "INTELLIGENCE OLDER THAN THREE TURNS",
      ...(stale.length ? stale.map((throne) => `- ${toolkitValue(throne.name, "Unnamed Throne")} — last verified turn ${throne.verified}`) : ["- None among the entered dated records."]),
      "",
      "THRONE REGISTER",
      ...(throneLines.length ? throneLines : ["- No named Thrones recorded."]),
      "",
      `TABLE RULE OR VICTORY NOTE\n${toolkitValue(values.rules)}`,
      `CATACLYSM OR ENDGAME TIMING\n${toolkitValue(values.cataclysm)}`,
      `CLAIM SEQUENCE AND HOSTING RISK\n${toolkitValue(values.sequence)}`,
      `ENEMY VICTORY WARNING\n${toolkitValue(values.enemy)}`,
      `DEFENCE AND REINFORCEMENT PLAN\n${toolkitValue(values.defence)}`,
      `DIPLOMACY AND INFORMATION BOUNDARY\n${toolkitValue(values.diplomacy)}`,
      "",
      "The totals use the levels and states entered above. They cannot prove a legal claim, successful movement, control after battle, or survival through hosting.",
    ].join("\n\n");
  };

  thronePlan.querySelector("[data-throne-add]").addEventListener("click", () => {
    addRow();
    toolkitStorageSave(storageKey, getData(), status);
    build();
  });
  const saved = toolkitStorageLoad(storageKey);
  setData(saved || { fields: {}, thrones: Array.from({ length: 8 }, () => ({})) });
  toolkitWireRecord({
    root: thronePlan,
    tool: "dominions-throne-plan",
    storageKey,
    getData,
    setData,
    build,
    reset: () => {
      thronePlan.reset();
      setData({ fields: toolkitFieldValues(fields), thrones: Array.from({ length: 8 }, () => ({})) });
    },
    filename: (data) => `${data.fields.game || "dominions"}-turn-${data.fields.turn || "1"}-throne-position`,
  });
  build();
  if (saved) status.textContent = "The saved Throne register was restored from this browser.";
}
