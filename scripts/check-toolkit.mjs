import { existsSync, readFileSync } from "node:fs";
import { gunzipSync } from "node:zlib";

const failures = [];
const newTools = [
  { route: "tools/mod-manifest", selector: "data-mod-manifest", searchUrl: "/tools/mod-manifest/" },
  { route: "tools/session-record", selector: "data-session-record", searchUrl: "/tools/session-record/" },
  { route: "dominions/tools/pretender-design", selector: "data-pretender-design", searchUrl: "/dominions/tools/pretender-design/" },
  { route: "dominions/tools/diplomacy-log", selector: "data-diplomacy-log", searchUrl: "/dominions/tools/diplomacy-log/" },
  { route: "dominions/tools/library-reading", selector: "data-library-reading", searchUrl: "/dominions/tools/library-reading/" },
  { route: "dominions/tools/battle-plan", selector: "data-battle-plan", searchUrl: "/dominions/tools/battle-plan/" },
  { route: "dominions/tools/throne-tracker", selector: "data-throne-plan", searchUrl: "/dominions/tools/throne-tracker/" },
];

const sharedHub = readFileSync("tools/index.html", "utf8");
const dominionsHub = readFileSync("dominions/tools/index.html", "utf8");
const search = readFileSync("_data/search.yml", "utf8");
const toolkit = readFileSync("assets/toolkit.js", "utf8");
const manifest = JSON.parse(readFileSync("dominions/library/data/manifest.json", "utf8"));
const referencePage = readFileSync("dominions/tools/reference/index.html", "utf8");
const referenceScript = readFileSync("assets/dominions-reference.js", "utf8");
const siteSearchPage = readFileSync("search/index.html", "utf8");
const siteSearchScript = readFileSync("assets/site-search.js", "utf8");
const siteScript = readFileSync("assets/site.js", "utf8");
const reportPage = readFileSync("report/index.html", "utf8");
const reportScript = readFileSync("assets/report.js", "utf8");
const footer = readFileSync("_includes/footer.html", "utf8");
const dossierData = readFileSync("_data/dominions_dossiers.yml", "utf8");
const nationIndex = readFileSync("dominions/nations/index.html", "utf8");
const nationCatalogue = readFileSync("_includes/dominions-age-catalogue.html", "utf8");
const nationBook = readFileSync("dominions/library/books/book-vii/index.html", "utf8");
const toolDataPage = readFileSync("tools/data/index.html", "utf8");
const toolDataScript = readFileSync("assets/tool-data.js", "utf8");
const siteStyles = readFileSync("assets/site.css", "utf8");
const updatesData = readFileSync("_data/updates.yml", "utf8");
const updatesPage = readFileSync("updates/index.html", "utf8");
const updatesScript = readFileSync("assets/updates.js", "utf8");
const reference = JSON.parse(gunzipSync(readFileSync("dominions/tools/reference/data/catalogue.json.gz")));

for (const tool of newTools) {
  const page = `${tool.route}/index.html`;
  if (!existsSync(page)) {
    failures.push(`Missing tool page: ${page}`);
    continue;
  }
  const source = readFileSync(page, "utf8");
  if (!source.includes("extra_js: /assets/toolkit.js")) failures.push(`Missing toolkit script front matter: ${page}`);
  if (!source.includes("data-record-export") || !source.includes("data-record-import")) failures.push(`Missing export or import control: ${page}`);
  if (!toolkit.includes(`[${tool.selector}]`)) failures.push(`Missing JavaScript hook: ${tool.selector}`);
  if (!search.includes(`url: ${tool.searchUrl}`)) failures.push(`Missing search entry: ${tool.searchUrl}`);
}

for (const route of ["/tools/mod-manifest/", "/tools/session-record/"]) {
  if (!sharedHub.includes(route)) failures.push(`Shared tools hub does not link ${route}`);
}
for (const route of ["/dominions/tools/reference/", "/dominions/tools/pretender-design/", "/dominions/tools/battle-plan/", "/dominions/tools/diplomacy-log/", "/dominions/tools/throne-tracker/", "/dominions/tools/library-reading/"]) {
  if (!dominionsHub.includes(route)) failures.push(`Dominions tools hub does not link ${route}`);
}

const dominionsCardCount = [...dominionsHub.matchAll(/class="tool-card-code"/g)].length;
if (dominionsCardCount !== 18) failures.push(`Dominions hub has ${dominionsCardCount} numbered cards instead of 18`);
if (!sharedHub.includes("21 working tools")) failures.push("Shared tools hub does not report 21 working tools");

if (!referencePage.includes("extra_js: /assets/dominions-reference.js")) failures.push("Reference page does not load its catalogue script");
if (!referencePage.includes("data-reference-catalogue")) failures.push("Reference page is missing its catalogue root");
if (!referenceScript.includes("[data-reference-catalogue]")) failures.push("Reference JavaScript is missing its catalogue hook");
if (!search.includes("url: /dominions/tools/reference/")) failures.push("Search discovery is missing the reference catalogue");
if (!siteSearchPage.includes("data-reference-catalogue-url")) failures.push("Main search does not expose the base-game catalogue source");
if (!siteSearchPage.includes("data-reference-search-results")) failures.push("Main search is missing its base-game result list");
if (!siteSearchScript.includes("loadReferenceCatalogue")) failures.push("Main search does not load the base-game catalogue");
if (!siteSearchScript.includes("Reference record")) failures.push("Main search is missing the reference-record type filter");
if (!siteSearchPage.includes("source-confirmed-with-unresolved-selection")) failures.push("Main search is missing the unresolved evidence filter");
if (!siteScript.includes("focusSiteSearch")) failures.push("The site-wide search shortcut is missing");
if (!footer.includes("data-report-link")) failures.push("The site-wide correction link is missing");
if (!reportPage.includes("data-report-kind=\"correction\"") || !reportPage.includes("data-report-kind=\"tool\"")) failures.push("The correction page is missing a required report path");
if (!reportScript.includes("factual-correction.md") || !reportScript.includes("tool-fault.md")) failures.push("Prepared reports are not connected to their issue templates");
for (const template of ["factual-correction.md", "tool-fault.md", "broken-page-or-link.md", "focused-improvement.md"]) {
  if (!existsSync(`.github/ISSUE_TEMPLATE/${template}`)) failures.push(`Missing issue template: ${template}`);
}
const completedDossiers = [...dossierData.matchAll(/^\s{2}- age:/gm)].length;
if (completedDossiers !== 3) failures.push(`Dossier register has ${completedDossiers} completed entries instead of 3`);
if (!nationIndex.includes('id="dossier-progress"')) failures.push("Nation index is missing the dossier progress section");
if (!nationCatalogue.includes("nation-card--dossier")) failures.push("Age catalogues do not mark completed dossiers");
for (const anchor of ["b7-part-ii-middle-age-arcoscephale-the-old-kingdom", "b7-part-xvi-middle-age-marignon-fiery-justice", "b7-part-xvii-middle-age-pyrene-time-of-the-akelarre"]) {
  if (!nationBook.includes(`id="${anchor}"`)) failures.push(`Nation dossier target is missing: ${anchor}`);
}
for (const file of ["downloads/dominions-6-middle-age-nation-compendium-volume-1-edition-27.pdf", "downloads/dominions-6-ma-marignon-nation-dossier-edition-27.pdf", "downloads/dominions-6-ma-pyrene-nation-dossier-edition-27.pdf"]) {
  if (!existsSync(file)) failures.push(`Nation dossier PDF is missing: ${file}`);
}
if (!sharedHub.includes("/tools/data/")) failures.push("Shared tools hub does not link the local-data manager");
if (!search.includes("url: /tools/data/")) failures.push("Search discovery is missing the local-data manager");
if (!toolDataPage.includes("data-tool-data-manager")) failures.push("Local-data page is missing its manager root");
if (!toolDataScript.includes("thehobokingdom-local-data")) failures.push("Local-data manager is missing its bundle schema");
const managedStorageAreas = [...toolDataScript.matchAll(/\{ key: "thk-/g)].length;
if (managedStorageAreas !== 13) failures.push(`Local-data manager recognises ${managedStorageAreas} areas instead of 13`);
if (!siteScript.includes("thkStorageMarkUpdated")) failures.push("Tool save dates are not tracked site-wide");
if (!siteScript.includes("annotateToolTable")) failures.push("Tool tables are not labelled for the mobile card layout");
if (!siteStyles.includes("prefers-reduced-motion: reduce")) failures.push("Reduced-motion support is missing");
if (!siteStyles.includes("content: attr(data-label)")) failures.push("Mobile tool cards are missing their field labels");
const updateEntries = [...updatesData.matchAll(/^- date:/gm)].length;
const updateProjects = [...updatesData.matchAll(/^  project:/gm)].length;
if (updateEntries !== updateProjects) failures.push(`${updateEntries - updateProjects} update records are missing a project field`);
if (!updatesPage.includes("data-update-archive") || !updatesScript.includes("[data-update-archive]")) failures.push("The complete update archive is not wired up");
for (const page of ["dominions/index.html", "aura/index.html", "vintage-story/index.html", "minecraft/index.html", "dnd/index.html", "tabletop/index.html", "stalker/index.html", "bg3/index.html", "armoury/index.html"]) {
  const source = readFileSync(page, "utf8");
  if (!source.includes("project_id:") || !source.includes("project-status.html")) failures.push(`Main project page does not use shared status data: ${page}`);
}
if (reference.totalRecords !== reference.records.length) failures.push("Reference total does not match the record array");
if (reference.totalRecords !== 5340) failures.push(`Reference catalogue has ${reference.totalRecords} records instead of 5,340`);
if (reference.ruleset?.game_version !== "6.35") failures.push("Reference catalogue does not expose its pinned 6.35 ruleset");
if (reference.coverage?.currentLibraryBaseline !== "Dominions 6.36") failures.push("Reference catalogue does not expose the current 6.36 library baseline");
for (const category of ["spell", "item", "unit", "pretender", "summon", "site", "throne", "mercenary"]) {
  if (!reference.counts?.[category]) failures.push(`Reference catalogue is missing category: ${category}`);
}

const manifestSections = manifest.documents.reduce((total, document) => total + document.sectionCount, 0);
if (manifest.documents.length !== 16) failures.push(`Library manifest has ${manifest.documents.length} documents instead of 16`);
if (manifestSections !== 2524) failures.push(`Library manifest has ${manifestSections} sections instead of 2,524`);

if (failures.length) {
  console.error("Toolkit integrity failures:");
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log("Checked 21 site tools, thirteen managed browser records, the 5,340-record catalogue and main-search connection, and the current 16-document Library manifest.");
