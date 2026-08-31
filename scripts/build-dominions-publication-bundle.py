#!/usr/bin/env python3
"""Build the website publication bundle from the canonical Markdown corpus."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import json
import re
import shutil
import subprocess
from pathlib import Path


DOCUMENT_SLUGS = {
    "guide": "guide",
    "b1": "book-i",
    "field": "field-reference",
    "b2": "book-ii",
    "b3": "book-iii",
    "b4": "book-iv",
    "b5": "book-v",
    "b6": "book-vi",
    "b7": "book-vii",
    "b8": "book-viii",
    "b9": "book-ix",
    "b10": "book-x",
    "b11": "book-xi",
    "b12": "book-xii",
    "b13": "book-xiii",
    "b14": "book-xiv",
}

# Website anchors are public URLs. Keep aliases here when an editorial heading
# changes but the old fragment must continue to land on the same section.
LEGACY_SECTION_ALIASES = {
    "b7-the-nation-dossier-method-and-middle-age-arcoscephale":
        "b7-the-nation-dossier-method-middle-age-arcoscephale-marignon-and-pyrene",
}


def read_json(path: Path):
    if not path.exists() and path.suffix == ".json":
        compressed = path.with_suffix(path.suffix + ".gz")
        if compressed.exists():
            with gzip.open(compressed, "rt", encoding="utf-8") as source:
                return json.load(source)
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if compact:
        encoded = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    else:
        encoded = json.dumps(value, ensure_ascii=False, indent=2)
    path.write_text(encoded + "\n", encoding="utf-8")


def plain_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_~#>|]", " ", text)
    text = re.sub(r"\{#[A-Za-z0-9_.:-]+\}", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def excerpt(text: str, limit: int = 240) -> str:
    if len(text) <= limit:
        return text
    shortened = text[:limit].rsplit(" ", 1)[0]
    return f"{shortened}…"


def compress_large_json(directory: Path, threshold: int = 700_000) -> None:
    for _ in range(3):
        large_paths = [
            path for path in directory.glob("*.json")
            if path.stat().st_size > threshold
        ]
        if not large_paths:
            return
        for path in large_paths:
            compressed_path = path.with_suffix(path.suffix + ".gz")
            with path.open("rb") as source, compressed_path.open("wb") as destination:
                with gzip.GzipFile(
                    filename="",
                    mode="wb",
                    fileobj=destination,
                    compresslevel=9,
                    mtime=0,
                ) as archive:
                    shutil.copyfileobj(source, archive)
            path.unlink()
    remaining = [
        path.name for path in directory.glob("*.json")
        if path.stat().st_size > threshold
    ]
    if remaining:
        raise RuntimeError(f"Large JSON compression did not converge: {remaining}")


def write_partitioned_search_index(
    output: Path,
    entries: list[dict],
    edition: str,
    part_count: int = 8,
) -> None:
    parts = []
    total = len(entries)
    for part_index in range(part_count):
        start = part_index * total // part_count
        end = (part_index + 1) * total // part_count
        chunk = entries[start:end]
        filename = f"search-index.part-{part_index:03d}.json"
        path = output / filename
        write_json(path, chunk)
        payload = path.read_bytes()
        parts.append({
            "file": filename,
            "part": part_index + 1,
            "entries": len(chunk),
            "first_section_id": chunk[0]["id"] if chunk else None,
            "last_section_id": chunk[-1]["id"] if chunk else None,
            "sha256": hashlib.sha256(payload).hexdigest(),
        })
    write_json(output / "search-index.index.json", {
        "schema_version": "1.0",
        "edition": edition,
        "kind": "dominions-library-search-index",
        "entry_count": total,
        "storage": "transparent-json-parts",
        "parts": parts,
    })


def read_search_index(directory: Path) -> list[dict]:
    raw = directory / "search-index.json"
    if raw.exists() or raw.with_suffix(raw.suffix + ".gz").exists():
        return read_json(raw)

    index_path = directory / "search-index.index.json"
    index = read_json(index_path)
    entries = []
    for part in index["parts"]:
        part_path = directory / part["file"]
        payload = part_path.read_bytes()
        expected_hash = part.get("sha256")
        if expected_hash and hashlib.sha256(payload).hexdigest() != expected_hash:
            raise ValueError(f"Search index hash mismatch: {part_path}")
        chunk = json.loads(payload)
        if isinstance(chunk, dict):
            chunk = chunk["entries"]
        if len(chunk) != part["entries"]:
            raise ValueError(f"Search index entry-count mismatch: {part_path}")
        entries.extend(chunk)
    if len(entries) != index["entry_count"]:
        raise ValueError(f"Search index total mismatch: {index_path}")
    return entries


def render_document(
    source_path: Path,
    sections: list[dict],
) -> tuple[str, dict[str, str]]:
    lines = source_path.read_text(encoding="utf-8").splitlines()
    by_line = {section["source_line"]: section for section in sections}
    rewritten: list[str] = []
    section_text: dict[str, str] = {}

    for index, section in enumerate(sections):
        start = section["source_line"]
        end = sections[index + 1]["source_line"] - 1 if index + 1 < len(sections) else len(lines)
        body = "\n".join(lines[start:end])
        section_text[section["id"]] = plain_markdown(body)

    for line_number, line in enumerate(lines, 1):
        section = by_line.get(line_number)
        if section is None:
            rewritten.append(line)
            continue
        for alias in section.get("aliases", []):
            rewritten.append(
                f'<span class="anchor-alias" id="{html.escape(alias, quote=True)}" '
                'aria-hidden="true"></span>'
            )
        if section.get("aliases"):
            rewritten.append("")
        hashes = "#" * section["heading_level"]
        rewritten.append(f'{hashes} {section["title"]} {{#{section["id"]}}}')

    process = subprocess.run(
        [
            "pandoc",
            "--from=markdown+pipe_tables+fenced_code_blocks+raw_html",
            "--to=html5",
            "--wrap=none",
        ],
        input="\n".join(rewritten) + "\n",
        text=True,
        capture_output=True,
        check=True,
    )

    title_by_id = {section["id"]: section["title"] for section in sections}

    def add_heading_link(match: re.Match[str]) -> str:
        level, anchor, inner = match.groups()
        label = html.escape(title_by_id.get(anchor, "this section"), quote=True)
        return (
            f'<h{level} id="{anchor}">{inner}'
            f'<a class="heading-link" href="#{anchor}" '
            f'aria-label="Link to {label}">#</a></h{level}>'
        )

    rendered = re.sub(
        r'<h([1-3]) id="([^"]+)">(.*?)</h\1>',
        add_heading_link,
        process.stdout,
        flags=re.DOTALL,
    )
    rendered = re.sub(
        r'<p>((?:<span\b[^>]*class="anchor-alias"[^>]*></span>\s*)+)</p>',
        r"\1",
        rendered,
    )
    return rendered, section_text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--reuse-from", type=Path)
    args = parser.parse_args()

    corpus = args.corpus.resolve()
    output = args.output.resolve()
    reuse_from = args.reuse_from.resolve() if args.reuse_from else None
    website = corpus / "website"
    content_index = read_json(website / "content-index.json")
    redirects = read_json(website / "redirects.json")["redirects"]
    redirects_by_target: dict[str, list[str]] = {}
    for redirect in redirects:
        redirects_by_target.setdefault(redirect["to"], []).append(redirect["from"])
    for alias, target in LEGACY_SECTION_ALIASES.items():
        redirects_by_target.setdefault(target, []).append(alias)

    output.mkdir(parents=True, exist_ok=True)
    documents_output = output / "documents"
    documents_output.mkdir(parents=True, exist_ok=True)

    for path in website.glob("*.json"):
        shutil.copy2(path, output / path.name)

    sections_by_document: dict[str, list[dict]] = {}
    for section in content_index["sections"]:
        enriched = dict(section)
        enriched["aliases"] = sorted(
            set(enriched.get("aliases", []))
            | set(redirects_by_target.get(enriched["id"], []))
        )
        sections_by_document.setdefault(section["document_id"], []).append(enriched)

    link_locations: dict[str, tuple[str, str]] = {}
    for document_id, sections in sections_by_document.items():
        slug = DOCUMENT_SLUGS[document_id]
        for section in sections:
            link_locations[section["id"]] = (document_id, slug)
            for alias in section.get("aliases", []):
                link_locations[alias] = (document_id, slug)

    manifest_documents = []
    search_index = []
    link_map = {}
    previous_documents = {}
    previous_search_by_document: dict[str, list[dict]] = {}
    if reuse_from and (reuse_from / "manifest.json").exists():
        for previous in read_json(reuse_from / "manifest.json")["documents"]:
            previous_documents[previous["id"]] = read_json(
                reuse_from / "documents" / f"{previous['id']}.json"
            )
        for entry in read_search_index(reuse_from):
            previous_search_by_document.setdefault(entry["documentId"], []).append(entry)

    for document in content_index["documents"]:
        document_id = document["id"]
        sections = sorted(
            sections_by_document[document_id], key=lambda item: item["display_order"]
        )
        slug = DOCUMENT_SLUGS[document_id]
        full_title = sections[0]["title"]
        rendered, section_text = render_document(corpus / document["source_file"], sections)
        def rewrite_cross_document_link(match: re.Match[str]) -> str:
            target = match.group(1)
            location = link_locations.get(target)
            if not location or location[0] == document_id:
                return match.group(0)
            return f'href="/library/{location[1]}#{target}"'

        rendered = re.sub(
            r'href="#([A-Za-z0-9_.:-]+)"',
            rewrite_cross_document_link,
            rendered,
        )
        toc = [
            {"id": section["id"], "title": section["title"], "level": section["heading_level"]}
            for section in sections
            if section["heading_level"] > 1
        ]
        published_document = {
            "id": document_id,
            "slug": slug,
            "title": full_title,
            "shortTitle": document["title"],
            "sectionCount": document["section_count"],
            "wordCount": document["word_count"],
            "html": rendered,
            "toc": toc,
        }
        previous = previous_documents.get(document_id)
        reusable = bool(
            previous
            and previous.get("sectionCount") == published_document["sectionCount"]
            and previous.get("wordCount") == published_document["wordCount"]
        )
        if reusable:
            published_document["html"] = previous["html"]
            published_document["toc"] = previous["toc"]
        write_json(
            documents_output / f"{document_id}.json",
            published_document,
            compact=True,
        )
        manifest_documents.append({key: published_document[key] for key in (
            "id", "slug", "title", "shortTitle", "sectionCount", "wordCount"
        )})

        if reusable and len(previous_search_by_document.get(document_id, [])) == len(sections):
            search_index.extend(previous_search_by_document[document_id])
        else:
            for section in sections:
                body = section_text.get(section["id"], "")
                search_text = " ".join(
                    part for part in [
                        section["title"],
                        full_title,
                        " ".join(section.get("topics", [])),
                        " ".join(section.get("audience", [])),
                        " ".join(section.get("evidence_status", [])),
                        body,
                    ] if part
                ).lower()
                search_index.append({
                    "id": section["id"],
                    "title": section["title"],
                    "documentId": document_id,
                    "documentTitle": full_title,
                    "documentSlug": slug,
                    "level": section["heading_level"],
                    "topics": section.get("topics", []),
                    "audience": section.get("audience", []),
                    "evidence": section.get("evidence_status", []),
                    "excerpt": excerpt(body),
                    "searchText": search_text,
                })

        for section in sections:
            canonical = f"/library/{slug}#{section['id']}"
            link_map[section["id"]] = canonical
            for alias in section.get("aliases", []):
                link_map[alias] = f"/library/{slug}#{alias}"

    edition = content_index["edition"]
    edition_name = edition["name"] if isinstance(edition, dict) else edition
    write_json(output / "manifest.json", {
        "edition": edition_name,
        "documents": manifest_documents,
    })
    write_partitioned_search_index(output, search_index, edition_name)
    write_json(output / "link-map.json", link_map, compact=True)
    compress_large_json(output)

    print(json.dumps({
        "edition": edition_name,
        "documents": len(manifest_documents),
        "sections": len(search_index),
        "output": str(output),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
