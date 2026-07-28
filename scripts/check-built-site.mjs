import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import {
  dirname,
  extname,
  join,
  normalize,
  relative,
  resolve,
} from "node:path";

const root = resolve(process.argv[2] || "_site");
const failures = [];
const htmlFiles = [];

function walk(directory) {
  for (const entry of readdirSync(directory)) {
    const fullPath = join(directory, entry);
    const stat = statSync(fullPath);

    if (stat.isDirectory()) {
      walk(fullPath);
    } else if (extname(entry).toLowerCase() === ".html") {
      htmlFiles.push(fullPath);
    }
  }
}

function targetExists(target) {
  if (existsSync(target) && statSync(target).isFile()) {
    return true;
  }

  if (existsSync(target) && statSync(target).isDirectory()) {
    return existsSync(join(target, "index.html"));
  }

  if (!extname(target)) {
    return (
      existsSync(`${target}.html`) || existsSync(join(target, "index.html"))
    );
  }

  return false;
}

if (!existsSync(root)) {
  console.error(`Built site not found: ${root}`);
  process.exit(1);
}

walk(root);

for (const file of htmlFiles) {
  const html = readFileSync(file, "utf8");
  const attributes = html.matchAll(/\b(?:href|src)=["']([^"'#]+)["']/g);

  for (const match of attributes) {
    const raw = match[1].trim();

    if (
      raw.startsWith("http://") ||
      raw.startsWith("https://") ||
      raw.startsWith("mailto:") ||
      raw.startsWith("tel:") ||
      raw.startsWith("data:")
    ) {
      continue;
    }

    const clean = decodeURIComponent(raw.split("?")[0].split("#")[0]);
    const target = clean.startsWith("/")
      ? join(root, clean)
      : normalize(join(dirname(file), clean));

    if (!targetExists(target)) {
      failures.push(`${relative(root, file)} → ${raw}`);
    }
  }
}

if (failures.length > 0) {
  console.error("Broken internal links:");
  for (const failure of failures) {
    console.error(`- ${failure}`);
  }
  process.exit(1);
}

console.log(
  `Checked ${htmlFiles.length} HTML files. No broken internal links found.`,
);
