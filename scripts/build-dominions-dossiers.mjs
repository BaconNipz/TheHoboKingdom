import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const index = JSON.parse(fs.readFileSync(path.join(root, "docs/dominions-library-source/edition-30/generated/content-index.json"), "utf8"));
const dossiers = index.sections.filter((section) =>
  section.document_id === "b7"
  && section.heading_level === 1
  && section.title.includes("Middle Age ")
);

const quote = (value) => JSON.stringify(String(value));
const lines = [
  "edition: 30",
  "updated: 14 September 2026",
  "total_nations: 102",
  "completed:",
];

for (const section of dossiers) {
  const match = section.title.match(/^Part [^:]+: Middle Age ([^,]+), (.+)$/);
  if (!match) throw new Error(`Could not read dossier title: ${section.title}`);
  const [, nation, subtitle] = match;
  const slug = section.topics.find((topic) => topic.startsWith("nation-"))?.slice(7);
  if (!slug) throw new Error(`Missing nation topic: ${section.id}`);
  const webUrl = section.website_url.replace("/dominions/library/book-vii/", "/dominions/library/books/book-vii/");
  const pdfUrl = slug === "arcoscephale"
    ? "/downloads/dominions-6-middle-age-nation-compendium-volume-1-edition-28.pdf"
    : `/downloads/dominions-6-ma-${slug}-nation-dossier-edition-30.pdf`;
  const pdfLabel = slug === "arcoscephale" ? "Volume I PDF" : "Standalone PDF";
  const ruleset = slug === "arcoscephale"
    ? "Base game, Dominions Enhanced 2.16, and Divinitus 1.15.3 DE"
    : "Unmodded Dominions 6.37";
  lines.push(`  - {age: middle, age_label: Middle Age, slug: ${quote(slug)}, name: ${quote(`${nation}, ${subtitle}`)}, subtitle: ${quote(subtitle)}, web_url: ${quote(webUrl)}, pdf_url: ${quote(pdfUrl)}, pdf_label: ${quote(pdfLabel)}, ruleset: ${quote(ruleset)}}`);
}

lines.push(
  "in_progress: []",
  'next_batch: "Early Age dossier production is next. Engine-dependent questions remain parked until hands-on testing resumes."',
  "",
);

fs.writeFileSync(path.join(root, "_data/dominions_dossiers.yml"), lines.join("\n"));
console.log(`Wrote ${dossiers.length} completed Middle Age dossiers.`);
