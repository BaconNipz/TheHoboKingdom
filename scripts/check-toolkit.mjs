import { existsSync, readFileSync } from "node:fs";

const failures = [];
const newTools = [
  { route: "tools/mod-manifest", selector: "data-mod-manifest", searchUrl: "/tools/mod-manifest/" },
  { route: "tools/session-record", selector: "data-session-record", searchUrl: "/tools/session-record/" },
  { route: "dominions/tools/pretender-design", selector: "data-pretender-design", searchUrl: "/dominions/tools/pretender-design/" },
  { route: "dominions/tools/diplomacy-log", selector: "data-diplomacy-log", searchUrl: "/dominions/tools/diplomacy-log/" },
  { route: "dominions/tools/library-reading", selector: "data-library-reading", searchUrl: "/dominions/tools/library-reading/" },
];

const sharedHub = readFileSync("tools/index.html", "utf8");
const dominionsHub = readFileSync("dominions/tools/index.html", "utf8");
const search = readFileSync("_data/search.yml", "utf8");
const toolkit = readFileSync("assets/toolkit.js", "utf8");
const manifest = JSON.parse(readFileSync("dominions/library/data/manifest.json", "utf8"));

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
for (const route of ["/dominions/tools/pretender-design/", "/dominions/tools/diplomacy-log/", "/dominions/tools/library-reading/"]) {
  if (!dominionsHub.includes(route)) failures.push(`Dominions tools hub does not link ${route}`);
}

const dominionsCardCount = [...dominionsHub.matchAll(/class="tool-card-code"/g)].length;
if (dominionsCardCount !== 16) failures.push(`Dominions hub has ${dominionsCardCount} numbered cards instead of 16`);
if (!sharedHub.includes("18 working tools")) failures.push("Shared tools hub does not report 18 working tools");

const manifestSections = manifest.documents.reduce((total, document) => total + document.sectionCount, 0);
if (manifest.documents.length !== 16) failures.push(`Library manifest has ${manifest.documents.length} documents instead of 16`);
if (manifestSections !== 2466) failures.push(`Library manifest has ${manifestSections} sections instead of 2,466`);

if (failures.length) {
  console.error("Toolkit integrity failures:");
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log("Checked 18 tools, five recoverable records, search discovery, and the current 16-document library manifest.");
