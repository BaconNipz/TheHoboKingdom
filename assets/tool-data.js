const toolDataManager = document.querySelector("[data-tool-data-manager]");

if (toolDataManager) {
  const bundleSchema = "thehobokingdom-local-data";
  const bundleSchemaVersion = 1;
  const metadataKey = "thk-tool-data-metadata-v1";
  const registry = [
    { key: "thk-mod-manifest-v1", name: "Mod manifest", version: 1, url: "/tools/mod-manifest/", description: "Game, loader, exact files, dependencies, order, test state, and recovery notes." },
    { key: "thk-shared-session-record-v1", name: "Multiplayer session record", version: 1, url: "/tools/session-record/", description: "Players, roles, connection details, decisions, progress, problems, and next jobs." },
    { key: "thk-dominions-pretender-design-v1", name: "Pretender design", version: 1, url: "/dominions/tools/pretender-design/", description: "Chassis, paths, scales, bless, purpose, tests, and failure branch." },
    { key: "thk-dominions-diplomacy-log-v1", name: "Diplomacy log", version: 1, url: "/dominions/tools/diplomacy-log/", description: "Relationships, evidence, agreements, expiry turns, obligations, and private notes." },
    { key: "thk-dominions-library-reading-v1", name: "Library reading tracker", version: 1, url: "/dominions/tools/library-reading/", description: "Completed sections, priorities, notes, and the next place to continue." },
    { key: "thk-dominions-battle-plan-v1", name: "Battle plan", version: 1, url: "/dominions/tools/battle-plan/", description: "Army groups, scripts, terrain, intelligence, objectives, and fallback branches." },
    { key: "thk-dominions-throne-plan-v2", name: "Throne victory tracker", version: 2, url: "/dominions/tools/throne-tracker/", description: "Thrones, controllers, claim state, intelligence age, targets, and victory progress." },
    { key: "thk-dominions-build-sheet", name: "Research build sheet", version: 1, url: "/dominions/tools/build-sheet/", description: "Ruleset, mage pool, research route, delivery package, timing, and end state." },
    { key: "thk-dominions-game-settings", name: "Multiplayer settings", version: 1, url: "/dominions/tools/game-settings/", description: "Map, players, mods, Thrones, hosting, security, and table rules." },
    { key: "thk-dominions-site-search", name: "Magic-site coverage", version: 1, url: "/dominions/tools/site-search/", description: "Province notes and the site-search levels planned across every magic path." },
    { key: "thk-dominions-battle-script", name: "Battle script", version: 1, url: "/dominions/tools/battle-script/", description: "Commander orders, equipment, gems, position, protection, and retreat policy." },
    { key: "thk-dominions-turn-planner", name: "Turn planner", version: 1, url: "/dominions/tools/turn-planner/", description: "Checklist state and notes for the current turn audit." },
    { key: "thk-library-recent", name: "Recently viewed Library sections", version: 1, url: "/dominions/library/", description: "The short on-device list used to return to recently opened Library sections." },
  ];
  const knownKeys = new Set(registry.map((record) => record.key));
  const count = toolDataManager.querySelector("[data-tool-data-count]");
  const size = toolDataManager.querySelector("[data-tool-data-size]");
  const lastExport = toolDataManager.querySelector("[data-tool-data-exported]");
  const recordsHost = toolDataManager.querySelector("[data-tool-data-records]");
  const exportButton = toolDataManager.querySelector("[data-tool-data-export]");
  const importInput = toolDataManager.querySelector("[data-tool-data-import]");
  const importMode = toolDataManager.querySelector("[data-tool-data-mode]");
  const restoreButton = toolDataManager.querySelector("[data-tool-data-restore]");
  const status = toolDataManager.querySelector("[data-tool-data-status]");
  const preview = toolDataManager.querySelector("[data-tool-data-preview]");
  let pendingImport = null;

  const readMetadata = () => {
    try {
      const metadata = JSON.parse(window.localStorage.getItem(metadataKey) || "{}");
      return metadata && typeof metadata === "object" && !Array.isArray(metadata) ? metadata : {};
    } catch {
      return {};
    }
  };

  const writeMetadata = (metadata) => window.localStorage.setItem(metadataKey, JSON.stringify(metadata));

  const formatDate = (value, fallback = "Date not recorded") => {
    if (!value) return fallback;
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return fallback;
    return new Intl.DateTimeFormat("en-AU", { dateStyle: "medium", timeStyle: "short" }).format(date);
  };

  const formatBytes = (bytes) => {
    if (bytes < 1024) return `${bytes.toLocaleString("en-AU")} B`;
    return `${(bytes / 1024).toLocaleString("en-AU", { maximumFractionDigits: 1 })} KB`;
  };

  const savedRecords = () => registry.flatMap((record) => {
    const data = window.localStorage.getItem(record.key);
    return data === null ? [] : [{ ...record, data }];
  });

  const buildBundle = (records) => {
    const metadata = readMetadata();
    return {
      schema: bundleSchema,
      schemaVersion: bundleSchemaVersion,
      exportedAt: new Date().toISOString(),
      source: "TheHoboKingdom local tool data",
      records: records.map((record) => ({
        key: record.key,
        name: record.name,
        toolVersion: record.version,
        updatedAt: metadata[record.key] || null,
        data: record.data,
      })),
    };
  };

  const downloadBundle = (bundle, filename, markFullExport = false) => {
    const blob = new Blob([`${JSON.stringify(bundle, null, 2)}\n`], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.append(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    if (markFullExport) {
      const metadata = readMetadata();
      metadata.__lastFullExport = bundle.exportedAt;
      writeMetadata(metadata);
      lastExport.textContent = formatDate(bundle.exportedAt);
    }
  };

  const appendText = (parent, tag, text, className = "") => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = text;
    parent.append(element);
    return element;
  };

  const render = () => {
    recordsHost.replaceChildren();
    const metadata = readMetadata();
    let savedCount = 0;
    let savedBytes = 0;
    for (const record of registry) {
      const data = window.localStorage.getItem(record.key);
      const isSaved = data !== null;
      if (isSaved) {
        savedCount += 1;
        savedBytes += new Blob([data]).size;
      }
      const card = document.createElement("article");
      card.className = `local-data-record${isSaved ? " is-saved" : ""}`;
      const top = document.createElement("div");
      top.className = "local-data-record-top";
      appendText(top, "span", isSaved ? "Saved on this device" : "No saved data", `dossier-status${isSaved ? " dossier-status--complete" : ""}`);
      appendText(top, "span", `Format ${record.version}`, "local-data-version");
      const heading = appendText(card, "h3", record.name);
      heading.before(top);
      appendText(card, "p", record.description);
      const detail = isSaved
        ? `${formatBytes(new Blob([data]).size)} · ${formatDate(metadata[record.key], "Saved before date tracking began")}`
        : "This area will appear in a backup after the corresponding tool has saved something.";
      appendText(card, "small", detail, "local-data-record-detail");
      const actions = document.createElement("div");
      actions.className = "local-data-record-actions";
      const open = appendText(actions, "a", "Open tool");
      open.href = record.url;
      const exportOne = appendText(actions, "button", "Export record");
      exportOne.type = "button";
      exportOne.disabled = !isSaved;
      exportOne.addEventListener("click", () => {
        const currentData = window.localStorage.getItem(record.key);
        if (currentData === null) return;
        const bundle = buildBundle([{ ...record, data: currentData }]);
        downloadBundle(bundle, `thehobokingdom-${record.key.replace(/^thk-/, "")}-${bundle.exportedAt.slice(0, 10)}.json`);
        status.textContent = `${record.name} backup downloaded.`;
      });
      const clear = appendText(actions, "button", "Clear local copy");
      clear.type = "button";
      clear.disabled = !isSaved;
      clear.addEventListener("click", () => {
        if (!window.confirm(`Clear the saved ${record.name} data from this browser? Export it first if it may be needed later.`)) return;
        window.localStorage.removeItem(record.key);
        const currentMetadata = readMetadata();
        delete currentMetadata[record.key];
        writeMetadata(currentMetadata);
        status.textContent = `${record.name} was cleared from this browser.`;
        render();
      });
      card.append(actions);
      recordsHost.append(card);
    }
    count.textContent = `${savedCount} of ${registry.length}`;
    size.textContent = formatBytes(savedBytes);
    lastExport.textContent = formatDate(metadata.__lastFullExport, "Not recorded");
    exportButton.disabled = savedCount === 0;
  };

  const validateBundle = (bundle) => {
    if (bundle?.schema !== bundleSchema || bundle?.schemaVersion !== bundleSchemaVersion || !Array.isArray(bundle.records)) {
      throw new Error("This is not a supported TheHoboKingdom local-data backup.");
    }
    const seen = new Set();
    const records = [];
    for (const record of bundle.records) {
      if (!knownKeys.has(record?.key)) continue;
      const current = registry.find((entry) => entry.key === record.key);
      if (seen.has(record.key)) throw new Error(`The backup contains ${record.key} more than once.`);
      if (!Number.isInteger(record.toolVersion) || record.toolVersion > current.version) throw new Error(`The ${record.key} record uses a newer data format than this site supports.`);
      if (typeof record.data !== "string" || record.data.length > 2_000_000) throw new Error(`The ${record.key} record is damaged or too large.`);
      JSON.parse(record.data);
      seen.add(record.key);
      records.push(record);
    }
    if (!records.length) throw new Error("The backup contains no recognised tool records.");
    return records;
  };

  exportButton.addEventListener("click", () => {
    try {
      const records = savedRecords();
      if (!records.length) {
        status.textContent = "There is no saved tool data to export yet.";
        return;
      }
      const bundle = buildBundle(records);
      downloadBundle(bundle, `thehobokingdom-local-data-${bundle.exportedAt.slice(0, 10)}.json`, true);
      status.textContent = `${records.length} saved area${records.length === 1 ? "" : "s"} exported in one backup.`;
    } catch {
      status.textContent = "The browser could not create the backup. Check whether local storage and downloads are allowed.";
    }
  });

  importInput.addEventListener("change", async () => {
    pendingImport = null;
    restoreButton.disabled = true;
    preview.hidden = true;
    const file = importInput.files?.[0];
    if (!file) return;
    try {
      if (file.size > 5_000_000) throw new Error("The selected file is larger than a tool-data backup should be.");
      const bundle = JSON.parse(await file.text());
      const records = validateBundle(bundle);
      pendingImport = { bundle, records };
      restoreButton.disabled = false;
      preview.hidden = false;
      preview.textContent = `${records.length} recognised record${records.length === 1 ? "" : "s"} · exported ${formatDate(bundle.exportedAt)} · ${records.map((record) => registry.find((entry) => entry.key === record.key)?.name).join(", ")}`;
      status.textContent = "Backup checked. Choose the restore mode, then restore it when ready.";
    } catch (error) {
      status.textContent = `Backup rejected: ${error.message}`;
      importInput.value = "";
    }
  });

  restoreButton.addEventListener("click", () => {
    if (!pendingImport) return;
    const replace = importMode.value === "replace";
    if (replace && !window.confirm("Replace matching records already saved in this browser? Records not included in the backup will be left alone.")) return;
    try {
      const metadata = readMetadata();
      let restored = 0;
      let skipped = 0;
      for (const record of pendingImport.records) {
        if (!replace && window.localStorage.getItem(record.key) !== null) {
          skipped += 1;
          continue;
        }
        window.localStorage.setItem(record.key, record.data);
        metadata[record.key] = record.updatedAt || pendingImport.bundle.exportedAt || new Date().toISOString();
        restored += 1;
      }
      metadata.__lastImportedAt = new Date().toISOString();
      writeMetadata(metadata);
      status.textContent = `${restored} record${restored === 1 ? "" : "s"} restored${skipped ? `; ${skipped} existing record${skipped === 1 ? " was" : "s were"} left unchanged` : ""}. Reload an open tool page before using the restored copy.`;
      pendingImport = null;
      importInput.value = "";
      restoreButton.disabled = true;
      preview.hidden = true;
      render();
    } catch {
      status.textContent = "The browser could not restore the backup. Existing records may be unchanged; export them before trying again.";
    }
  });

  try {
    render();
  } catch {
    count.textContent = "Unavailable";
    size.textContent = "Unavailable";
    status.textContent = "This browser is blocking access to local storage. The individual tools can still be used without saving.";
    exportButton.disabled = true;
  }
}
