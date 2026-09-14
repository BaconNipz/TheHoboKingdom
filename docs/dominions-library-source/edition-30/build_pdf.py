#!/usr/bin/env python3
"""Build the Dominions 6 Knowledge Library as a polished PDF."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

from navigation import (
    SOURCE_SPECS,
    aliases_by_target,
    cross_reference_targets,
    heading_catalog,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT.parent / "output" / "pdf" / "dominions-6-knowledge-library-progress-edition-28.pdf"
SOURCES = [ROOT / spec.filename for spec in SOURCE_SPECS]
HEADING_CATALOG = heading_catalog(ROOT)
BOOK_TARGETS, PART_TARGETS, SECTION_TARGETS = cross_reference_targets(HEADING_CATALOG)
ALIASES_BY_TARGET = aliases_by_target()

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#101B2D")
NAVY_2 = colors.HexColor("#172840")
INK = colors.HexColor("#202631")
MUTED = colors.HexColor("#5C6572")
GOLD = colors.HexColor("#C8A650")
GOLD_LIGHT = colors.HexColor("#F3E8C6")
PALE = colors.HexColor("#F4F6F8")
LINE = colors.HexColor("#D4D9DF")
WHITE = colors.white


def normalize(text: str) -> str:
    """Normalize troublesome punctuation while retaining game notation."""
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
        "\u2026": "...",
        "\u2192": "->",
        "\u00d7": "x",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def soft_hashes(text: str) -> str:
    """Permit long hexadecimal fingerprints to wrap at readable intervals."""
    return re.sub(
        r"\b([0-9a-f]{48,})\b",
        lambda m: "&#8203;".join(
            m.group(1)[i : i + 8] for i in range(0, len(m.group(1)), 8)
        ),
        text,
    )


def inline_markup(text: str) -> str:
    """Convert the small inline-Markdown subset used by the archive."""
    text = normalize(text.strip())
    tokens: list[str] = []

    def stash(value: str) -> str:
        tokens.append(value)
        return f"@@TOKEN{len(tokens) - 1}@@"

    text = re.sub(
        r"`([^`]+)`",
        lambda m: stash(
            f'<font name="DejaVuSansMono" size="8.1">{html.escape(m.group(1))}</font>'
        ),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+|#[A-Za-z0-9_.:-]+)\)",
        lambda m: stash(
            f'<link href="{html.escape(m.group(2), quote=True)}" '
            f'color="#315E86">{html.escape(m.group(1))}</link>'
        ),
        text,
    )
    text = re.sub(
        r"\bBook\s+([IVX]+),?\s+Part\s+([IVXLCDM]+)\b",
        lambda m: stash(
            f'<link href="#{PART_TARGETS[(m.group(1), m.group(2))]}" color="#315E86">'
            f'{html.escape(m.group(0))}</link>'
        )
        if (m.group(1), m.group(2)) in PART_TARGETS
        else m.group(0),
        text,
    )
    text = re.sub(
        r"\bBook\s+IX,?\s+Section\s+(\d+(?:\.\d+)*)\b",
        lambda m: stash(
            f'<link href="#{SECTION_TARGETS[m.group(1)]}" color="#315E86">'
            f'{html.escape(m.group(0))}</link>'
        )
        if m.group(1) in SECTION_TARGETS
        else m.group(0),
        text,
    )
    text = re.sub(
        r"\bBook\s+([IVX]+)\b",
        lambda m: stash(
            f'<link href="#{BOOK_TARGETS[m.group(1)]}" color="#315E86">'
            f'{html.escape(m.group(0))}</link>'
        )
        if m.group(1) in BOOK_TARGETS
        else m.group(0),
        text,
    )
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = soft_hashes(text)
    for i, token in enumerate(tokens):
        text = text.replace(f"@@TOKEN{i}@@", token)
    return text


def split_cells(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [
        part.strip().replace(r"\|", "|")
        for part in re.split(r"(?<!\\)\|", line)
    ]


def is_table_separator(line: str) -> bool:
    if "|" not in line:
        return False
    cells = split_cells(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def build_styles():
    base = getSampleStyleSheet()
    styles = {}
    styles["cover_kicker"] = ParagraphStyle(
        "CoverKicker",
        parent=base["Normal"],
        fontName="DejaVuSans-Bold",
        fontSize=10,
        leading=13,
        tracking=1.6,
        textColor=GOLD,
        spaceAfter=14,
    )
    styles["cover_title"] = ParagraphStyle(
        "CoverTitle",
        parent=base["Title"],
        fontName="DejaVuSans-Bold",
        fontSize=31,
        leading=37,
        textColor=WHITE,
        alignment=TA_LEFT,
        spaceAfter=16,
    )
    styles["cover_subtitle"] = ParagraphStyle(
        "CoverSubtitle",
        parent=base["Normal"],
        fontName="DejaVuSans",
        fontSize=14,
        leading=21,
        textColor=colors.HexColor("#DDE4EC"),
        spaceAfter=24,
    )
    styles["cover_note"] = ParagraphStyle(
        "CoverNote",
        parent=base["Normal"],
        fontName="DejaVuSans",
        fontSize=9.5,
        leading=15,
        textColor=colors.HexColor("#CAD3DD"),
    )
    styles["h1"] = ParagraphStyle(
        "ArchiveH1",
        parent=base["Heading1"],
        fontName="DejaVuSans-Bold",
        fontSize=22,
        leading=27,
        textColor=NAVY,
        spaceBefore=12,
        spaceAfter=12,
        keepWithNext=True,
    )
    styles["h2"] = ParagraphStyle(
        "ArchiveH2",
        parent=base["Heading2"],
        fontName="DejaVuSans-Bold",
        fontSize=14.5,
        leading=19,
        textColor=NAVY_2,
        spaceBefore=15,
        spaceAfter=7,
        keepWithNext=True,
    )
    styles["h3"] = ParagraphStyle(
        "ArchiveH3",
        parent=base["Heading3"],
        fontName="DejaVuSans-Bold",
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#765F24"),
        spaceBefore=11,
        spaceAfter=5,
        keepWithNext=True,
    )
    styles["body"] = ParagraphStyle(
        "ArchiveBody",
        parent=base["BodyText"],
        fontName="DejaVuSans",
        fontSize=9.35,
        leading=14.1,
        textColor=INK,
        spaceAfter=7,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["bullet"] = ParagraphStyle(
        "ArchiveBullet",
        parent=styles["body"],
        fontSize=9.1,
        leading=13.5,
        spaceAfter=2,
    )
    styles["quote"] = ParagraphStyle(
        "ArchiveQuote",
        parent=styles["body"],
        leftIndent=10,
        rightIndent=8,
        borderColor=GOLD,
        borderWidth=0,
        borderPadding=(2, 8, 2, 10),
        backColor=colors.HexColor("#FBF8EF"),
        textColor=colors.HexColor("#3C424A"),
        spaceBefore=4,
        spaceAfter=8,
    )
    styles["table_head"] = ParagraphStyle(
        "ArchiveTableHead",
        parent=styles["body"],
        fontName="DejaVuSans-Bold",
        fontSize=7.5,
        leading=9.5,
        textColor=WHITE,
        spaceAfter=0,
    )
    styles["table_cell"] = ParagraphStyle(
        "ArchiveTableCell",
        parent=styles["body"],
        fontSize=7.4,
        leading=9.6,
        spaceAfter=0,
        wordWrap=None,
        splitLongWords=True,
    )
    styles["table_dense_head"] = ParagraphStyle(
        "ArchiveDenseTableHead",
        parent=styles["table_head"],
        fontSize=6.8,
        leading=8.2,
        splitLongWords=False,
    )
    styles["table_dense_cell"] = ParagraphStyle(
        "ArchiveDenseTableCell",
        parent=styles["table_cell"],
        fontSize=6.7,
        leading=8.4,
        # Long canonical anchors have no spaces; containing them is preferable to
        # letting them overprint the adjacent status column.
        splitLongWords=True,
    )
    styles["toc_title"] = ParagraphStyle(
        "TOCTitle",
        parent=styles["h1"],
        fontSize=24,
        leading=29,
        spaceAfter=17,
    )
    styles["section_label"] = ParagraphStyle(
        "SectionLabel",
        parent=styles["body"],
        fontName="DejaVuSans-Bold",
        fontSize=7.6,
        leading=9,
        tracking=1.3,
        textColor=GOLD,
        spaceAfter=5,
    )
    return styles


STYLES = build_styles()


class ArchiveDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(
            filename,
            pagesize=A4,
            rightMargin=18 * mm,
            leftMargin=18 * mm,
            topMargin=20 * mm,
            bottomMargin=20 * mm,
            title="The Dominions 6 Knowledge Library - Foundation Books I-XIV",
            author="TheHoboKingdom",
            subject="Dominions 6 rulesets, operations, hosting, economy, statecraft, Pretenders, dominion, armies, magic, strategy, nations, base-game objects, official patch history, command terminology, modding, AI scaffolds, maps, scenarios, Dominions Enhanced, and Divinitus",
            creator="TheHoboKingdom",
        )
        self.heading_counter = 0

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name not in {"ArchiveH1", "ArchiveH2", "ArchiveH3"}:
            return
        level = {"ArchiveH1": 0, "ArchiveH2": 1, "ArchiveH3": 2}[style_name]
        text = flowable.getPlainText()
        key = getattr(flowable, "_archive_bookmark_key", None)
        if key is None:
            key = f"heading-{self.heading_counter}"
            flowable._archive_bookmark_key = key
            self.heading_counter += 1
        self.canv.bookmarkPage(key)
        for alias in ALIASES_BY_TARGET.get(key, []):
            self.canv.bookmarkPage(alias)
        self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
        if level <= 1:
            self.notify("TOCEntry", (level, text, self.page, key))


def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(NAVY_2)
    canvas.rect(0, 0, PAGE_W, 33 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
    canvas.rect(18 * mm, PAGE_H - 59 * mm, 34 * mm, 1.5 * mm, fill=1, stroke=0)
    canvas.setFont("DejaVuSans", 7.5)
    canvas.setFillColor(colors.HexColor("#AEBBC9"))
    canvas.drawString(18 * mm, 17 * mm, "THEHOBOKINGDOM")
    canvas.setFillColor(GOLD)
    canvas.drawRightString(PAGE_W - 18 * mm, 17 * mm, "PROGRESS EDITION 28")
    canvas.restoreState()


def draw_body(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.75)
    canvas.line(18 * mm, PAGE_H - 13 * mm, PAGE_W - 18 * mm, PAGE_H - 13 * mm)
    canvas.setFont("DejaVuSans-Bold", 7.2)
    canvas.setFillColor(NAVY)
    canvas.drawString(18 * mm, PAGE_H - 10 * mm, "DOMINIONS 6 KNOWLEDGE LIBRARY")
    canvas.setFont("DejaVuSans", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 10 * mm, "FOUNDATION BOOKS I-XIV - LINKED READER'S EDITION")
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.45)
    canvas.line(18 * mm, 13 * mm, PAGE_W - 18 * mm, 13 * mm)
    canvas.setFont("DejaVuSans", 7.1)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 8.5 * mm, "TheHoboKingdom | 30 August 2026")
    canvas.drawRightString(PAGE_W - 18 * mm, 8.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def paragraph(text: str, style="body") -> Paragraph:
    return Paragraph(inline_markup(text), STYLES[style])


def make_table(rows: list[list[str]], available_width: float) -> Table:
    headers = [normalize(c) for c in rows[0]]
    col_count = len(headers)
    dense_research_register = headers == [
        "ID",
        "Priority",
        "Domain",
        "Question",
        "Why it matters",
        "Reliable route",
        "Primary anchor",
        "Status",
    ]
    if dense_research_register:
        proportions = [0.075, 0.075, 0.10, 0.16, 0.17, 0.17, 0.15, 0.10]
    elif "SHA-256" in headers and col_count == 6:
        proportions = [0.151, 0.217, 0.101, 0.093, 0.107, 0.331]
    elif headers == ["Token", "Status", "Domain", "Official locator", "Strongest syntax"]:
        proportions = [0.16, 0.11, 0.16, 0.20, 0.37]
    elif headers == ["Patch token", "Reconciliation", "Resolves to", "Version", "Editorial note"]:
        proportions = [0.18, 0.20, 0.21, 0.10, 0.31]
    elif headers == ["Patch token", "Present resolution", "First version", "Patch records"]:
        proportions = [0.18, 0.48, 0.16, 0.18]
    elif headers == ["Search alias", "Official template", "Derivation"]:
        proportions = [0.36, 0.38, 0.26]
    elif headers == ["Step", "Resolution", "What happens", "Why timing matters"]:
        proportions = [0.07, 0.17, 0.37, 0.39]
    elif headers == ["#", "Test", "Controlled question"]:
        proportions = [0.07, 0.25, 0.68]
    else:
        max_lens = []
        for col in range(col_count):
            length = max(
                len(normalize(row[col])) if col < len(row) else 0 for row in rows
            )
            max_lens.append(max(5, min(length, 38)))
        total = sum(max_lens)
        proportions = [n / total for n in max_lens]
        proportions = [min(0.53, max(0.12, p)) for p in proportions]
        scale = sum(proportions)
        proportions = [p / scale for p in proportions]
    widths = [available_width * p for p in proportions]
    data = []
    for row_index, row in enumerate(rows):
        if dense_research_register:
            style = "table_dense_head" if row_index == 0 else "table_dense_cell"
        else:
            style = "table_head" if row_index == 0 else "table_cell"
        padded = row + [""] * (col_count - len(row))
        data.append([paragraph(cell, style) for cell in padded[:col_count]])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY_2),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, 0), 5),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
                ("TOPPADDING", (0, 1), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE]),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD),
            ]
        )
    )
    if dense_research_register:
        table.setStyle(
            TableStyle(
                [
                    ("LEFTPADDING", (0, 0), (-1, -1), 3),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )
    return table


def flush_paragraph(buffer: list[str], story: list):
    if not buffer:
        return
    text = " ".join(part.strip() for part in buffer).strip()
    if text:
        story.append(paragraph(text))
    buffer.clear()


def flush_list(items: list[str], ordered: bool, story: list):
    if not items:
        return
    # A single large ListFlowable can paint continuation items into the top
    # margin after a page split. One-item flowables retain the same appearance
    # while allowing the frame to paginate each item safely.
    for index, item in enumerate(items):
        value = index + 1
        list_item = ListItem(
            paragraph(item, "bullet"),
            leftIndent=10,
            value=value if ordered else None,
        )
        list_options = {
            "bulletType": "1" if ordered else "bullet",
            "bulletFontName": "DejaVuSans-Bold",
            "bulletFontSize": 8.2,
            "bulletColor": colors.HexColor("#876D28") if ordered else GOLD,
            "leftIndent": 17,
            "bulletIndent": 2,
            "spaceBefore": 1 if index == 0 else 0,
            "spaceAfter": 7 if index == len(items) - 1 else 0,
        }
        if ordered:
            list_options["start"] = value
        story.append(ListFlowable([list_item], **list_options))
    items.clear()


def markdown_to_story(path: Path, available_width: float) -> list:
    lines = normalize(path.read_text(encoding="utf-8")).splitlines()
    heading_records = HEADING_CATALOG.get(path.name, [])
    heading_ordinal = 0
    story: list = []
    para_buffer: list[str] = []
    list_items: list[str] = []
    list_ordered = False
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph(para_buffer, story)
            flush_list(list_items, list_ordered, story)
            i += 1
            continue

        if stripped.startswith("<!--") and stripped.endswith("-->"):
            flush_paragraph(para_buffer, story)
            flush_list(list_items, list_ordered, story)
            i += 1
            continue

        table_starts = (
            "|" in line
            and i + 1 < len(lines)
            and is_table_separator(lines[i + 1])
        )
        if table_starts:
            flush_paragraph(para_buffer, story)
            flush_list(list_items, list_ordered, story)
            rows = [split_cells(line)]
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                rows.append(split_cells(lines[i]))
                i += 1
            story.extend([Spacer(1, 3), make_table(rows, available_width), Spacer(1, 8)])
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            flush_paragraph(para_buffer, story)
            flush_list(list_items, list_ordered, story)
            level = len(heading.group(1))
            heading_text = re.sub(
                r"\s+\{#[A-Za-z0-9_.:-]+\}\s*$", "", heading.group(2)
            )
            if heading_text in {
                "Part XVI: Middle Age Marignon, Fiery Justice",
                "Part XVII: Middle Age Pyrène, Time of the Akelarre",
            }:
                story.append(PageBreak())
            if heading_text == "What this unlocks":
                story.append(CondPageBreak(85 * mm))
            elif level == 2:
                story.append(CondPageBreak(24 * mm))
            elif level == 3:
                story.append(CondPageBreak(18 * mm))
            heading_paragraph = paragraph(heading_text, f"h{level}")
            if heading_ordinal < len(heading_records):
                heading_paragraph._archive_bookmark_key = heading_records[
                    heading_ordinal
                ].anchor
            heading_ordinal += 1
            story.append(heading_paragraph)
            if level == 1:
                story.append(
                    HRFlowable(
                        width="100%",
                        thickness=1,
                        color=GOLD,
                        spaceBefore=0,
                        spaceAfter=7,
                    )
                )
            i += 1
            continue

        list_match = re.match(r"^[-*]\s+(.+)$", stripped)
        number_match = re.match(r"^\d+\.\s+(.+)$", stripped)
        if list_match or number_match:
            flush_paragraph(para_buffer, story)
            new_ordered = bool(number_match)
            if list_items and new_ordered != list_ordered:
                flush_list(list_items, list_ordered, story)
            list_ordered = new_ordered
            list_items.append((number_match or list_match).group(1))
            i += 1
            continue

        if stripped.startswith(">"):
            flush_paragraph(para_buffer, story)
            flush_list(list_items, list_ordered, story)
            story.append(paragraph(stripped.lstrip("> ").strip(), "quote"))
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph(para_buffer, story)
            flush_list(list_items, list_ordered, story)
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(html.escape(lines[i]))
                i += 1
            code = "<br/>".join(code_lines)
            code_style = ParagraphStyle(
                "CodeBlock",
                parent=STYLES["body"],
                fontName="DejaVuSansMono",
                fontSize=7.8,
                leading=10.5,
                backColor=colors.HexColor("#EEF1F4"),
                borderColor=LINE,
                borderWidth=0.5,
                borderPadding=7,
                spaceBefore=3,
                spaceAfter=8,
            )
            story.append(Paragraph(code or " ", code_style))
            i += 1
            continue

        if list_items:
            flush_list(list_items, list_ordered, story)
        para_buffer.append(stripped)
        i += 1

    flush_paragraph(para_buffer, story)
    flush_list(list_items, list_ordered, story)
    return story


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(
        TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    )
    pdfmetrics.registerFont(
        TTFont(
            "DejaVuSans-Bold",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        )
    )
    pdfmetrics.registerFont(
        TTFont(
            "DejaVuSansMono",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        )
    )

    doc = ArchiveDocTemplate(str(OUTPUT))
    cover_frame = Frame(
        18 * mm,
        33 * mm,
        PAGE_W - 36 * mm,
        PAGE_H - 55 * mm,
        id="cover_frame",
        showBoundary=0,
    )
    body_frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="body_frame",
        showBoundary=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="Cover", frames=[cover_frame], onPage=draw_cover),
            PageTemplate(id="Body", frames=[body_frame], onPage=draw_body),
        ]
    )

    story = [
        Spacer(1, 36 * mm),
        Paragraph("DOMINIONS 6 RESEARCH PROJECT", STYLES["cover_kicker"]),
        Paragraph(
            "The Dominions 6<br/>Knowledge Library",
            STYLES["cover_title"],
        ),
        Paragraph(
            "Reader's guide and Foundation Books I-XIV: rulesets, turn resolution, economy, statecraft, "
            "Pretenders, dominion, blessings, armies, battle, magic, strategy, "
            "nations, modding, AI scaffolds, maps, scenarios, and the "
            "Dominions Enhanced/Divinitus technical encyclopaedia; plus the practical "
            "operations, interface, setup, orders, and hosting manual; plus the systematic "
            "unit-class, ability, experience, heroic-ability, and condition reference; plus the "
            "versioned base-game object reference for spells, items, summons, Pretenders, Thrones, "
            "sites, mercenaries, independents, and special dominions; plus the complete official "
            "6.01-6.36 version history and 1,090-record patch ledger; plus the searchable "
            "command and terminology lexicon covering 1,609 official-manual tokens, 97 controlled "
            "aliases, and all 226 command-like patch tokens",
            STYLES["cover_subtitle"],
        ),
        Spacer(1, 7 * mm),
        HRFlowable(width=44 * mm, thickness=1.4, color=GOLD, hAlign="LEFT"),
        Spacer(1, 7 * mm),
        Paragraph(
            "<b>Progress Edition 28</b><br/>30 August 2026<br/><br/>"
            "Linked reader's edition: beginner-readable, expert-useful, "
            "source-verifiable, and prepared for website publication.",
            STYLES["cover_note"],
        ),
        NextPageTemplate("Body"),
        PageBreak(),
        Paragraph("Contents", STYLES["toc_title"]),
        Paragraph(
            "This reader-facing edition begins with a concordance, linked learning "
            "paths, and a research-priority register. It then presents the complete "
            "63-step hosting "
            "model, a turn-and-economy quick reference, the economy-and-state "
            "foundation with the Edition 23 rounding map, upkeep-display boundaries, "
            "unrest candidates, fort-supply evidence gate, and starvation-state audit, the full "
            "Pretender, dominion, scales, and blessings foundation with the source-traced "
            "awakening-evidence boundary, reconciled Call God model, and same-turn Throne state matrix, and the "
            "armies-and-battle, magic, and strategy foundations; the complete "
            "Arcoscephale, Marignon, and Pyrène nation dossiers; and the modding-and-scenario foundation. "
            "Book VIII covers source architecture, objects, events, diplomacy "
            "reactions, AI scaffolds, maps, compatibility, and release testing. "
            "Book IX inventories Dominions Enhanced 2.16 and Divinitus 1.15.3 DE "
            "from the supplied source files, separating explicit definitions, "
            "official engine rules, combined-load-order deductions, and unresolved "
            "runtime questions. It includes the complete DE global and blessing "
            "layers, Divinitus event architecture, cross-mod identity analysis, "
            "and a practical verification register. Edition 28 resolves the category-level perception "
            "matrix, records the live Invisibility value against superseded manual wording, advances "
            "ability-stacking evidence, and publishes a controlled Hall-of-Fame observation protocol. "
            "It preserves the direct, practical house style across the complete reader corpus and the exact evidence, "
            "tables, formulas, citations, and research boundaries. Repeated internal baselines, "
            "source inventories, formulas, and essays have been consolidated under "
            "one authoritative chapter each. Book X then supplies the player-facing "
            "operating layer: game creation, joining and hosting, interface controls, "
            "recruitment and army workflow, strategic orders, a guided first campaign, "
            "troubleshooting, and campaign administration. Book XI adds the retrieval layer for "
            "unit classes, movement and command tags, defensive and offensive abilities, "
            "experience, the Hall of Fame, heroic traits, lasting conditions, counters, and "
            "current patch corrections. Book XII adds the versioned object-reference method and "
            "a 4,196-record website data layer covering spells, items, summon relations, Pretender "
            "forms, Thrones, sites, mercenary companies, independent-coverage status, realm-expanded spell access, and special "
            "dominion systems without duplicating the strategic teaching in Books II-VI. Book XIII adds the official "
            "version spine: all 32 public update announcements and 1,090 change records from 6.01 through 6.36, "
            "with a release chronology, source hashes, editorial classifications, canonical maintenance links, "
            "a stale-guide repair method, and a command chronology. Book XIV supplies the retrieval and "
            "reconciliation layer for command terminology: 1,609 distinct tokens from the official modding, "
            "event, and map manuals; 97 controlled aliases; all 226 patch-note tokens reconciled, including five official 6.36 patch-only commands; "
            "context-sensitive command domains; syntax and source locators; documentation-status distinctions; "
            "and explicit handling of manual-version drift and official spelling discrepancies. The project archive and evidence "
            "ledger remain separate from the published book.",
            STYLES["body"],
        ),
        Spacer(1, 5),
    ]

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOCLevel1",
            fontName="DejaVuSans-Bold",
            fontSize=10.3,
            leading=15,
            leftIndent=0,
            firstLineIndent=0,
            textColor=NAVY,
            spaceBefore=5,
        ),
        ParagraphStyle(
            "TOCLevel2",
            fontName="DejaVuSans",
            fontSize=8.6,
            leading=12,
            leftIndent=13,
            firstLineIndent=0,
            textColor=INK,
        ),
        ParagraphStyle(
            "TOCLevel3",
            fontName="DejaVuSans",
            fontSize=7.7,
            leading=10.5,
            leftIndent=27,
            firstLineIndent=0,
            textColor=MUTED,
        ),
    ]
    story.extend([toc, PageBreak()])

    for index, source in enumerate(SOURCES):
        if index:
            story.append(PageBreak())
        story.append(
            Paragraph(
                f"DOCUMENT {index + 1} OF {len(SOURCES)}",
                STYLES["section_label"],
            )
        )
        story.extend(markdown_to_story(source, doc.width))

    doc.multiBuild(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
