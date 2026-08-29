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
if (!sharedHub.includes("20 working tools")) failures.push("Shared tools hub does not report 20 working tools");

if (!referencePage.includes("extra_js: /assets/dominions-reference.js")) failures.push("Reference page does not load its catalogue script");
if (!referencePage.includes("data-reference-catalogue")) failures.push("Reference page is missing its catalogue root");
if (!referenceScript.includes("[data-reference-catalogue]")) failures.push("Reference JavaScript is missing its catalogue hook");
if (!search.includes("url: /dominions/tools/reference/")) failures.push("Search discovery is missing the reference catalogue");
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

console.log("Checked 20 site tools, seven recoverable records, the 5,340-record reference catalogue, search discovery, and the current 16-document library manifest.");
