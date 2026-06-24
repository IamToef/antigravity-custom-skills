#!/usr/bin/env python3
"""
parse_mom.py — Parse Biên Bản Họp (.docx) và extract issues / action items.

Usage:
    python3 parse_mom.py <path_to_docx>
    python3 parse_mom.py <path_to_docx> --latest  # scan folder, pick newest

Output: JSON to stdout
"""

import sys
import json
import re
from pathlib import Path


def install_if_needed():
    try:
        from docx import Document  # noqa
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install",
                               "python-docx", "--break-system-packages", "-q"])


install_if_needed()
from docx import Document  # noqa: E402


# ── Sections that contain action items / issues worth publishing ──────────────
FOLLOW_UP_KEYWORDS = [
    "cần follow up", "đang + chưa hoàn thành", "chưa hoàn thành",
    "task còn tồn", "còn tồn", "trao đổi khác",
]
DONE_KEYWORDS = ["hoàn thành"]
RETRO_KEYWORDS = ["retrospective", "retro", "vấn đề"]

# ── Deadline pattern ──────────────────────────────────────────────────────────
DEADLINE_RE = re.compile(r"\b(\d{2}/\d{2}/\d{4})\b")


def deduplicate_cells(row):
    """Remove duplicate text caused by merged cells in python-docx."""
    seen = set()
    result = []
    for cell in row.cells:
        text = cell.text.strip()
        if text not in seen:
            result.append(text)
            seen.add(text)
    return result


def parse_metadata_table(table):
    """Parse the first table: project, date, time, location, participants."""
    meta = {"type": "", "date": "", "time": "", "project": "", "location": "",
            "participants": {"dev": [], "ba_po": []}}
    participants_mode = False

    for row in table.rows:
        cells = deduplicate_cells(row)
        flat = " | ".join(cells)

        if "dự án" in flat.lower():
            # value is after "Dự án:"
            for i, c in enumerate(cells):
                if "dự án" in c.lower() and i + 1 < len(cells):
                    meta["project"] = cells[i + 1].strip()
                    break

        if "ngày" in flat.lower() and "/" in flat:
            for i, c in enumerate(cells):
                if "ngày" in c.lower() and i + 1 < len(cells):
                    meta["date"] = cells[i + 1].strip()
                if "giờ" in c.lower() and i + 1 < len(cells):
                    meta["time"] = cells[i + 1].strip()

        if "địa điểm" in flat.lower():
            for i, c in enumerate(cells):
                if "địa điểm" in c.lower() and i + 1 < len(cells):
                    meta["location"] = cells[i + 1].strip()

        if "mục đích" in flat.lower():
            for i, c in enumerate(cells):
                if "mục đích" in c.lower() and i + 1 < len(cells):
                    meta["type"] = cells[i + 1].strip()

        # Detect header row for participants
        if "dev" in flat.lower() and ("ba" in flat.lower() or "po" in flat.lower()):
            participants_mode = True
            continue

        if participants_mode:
            # Expect: [STT, DEV name, BA/PO name] or similar
            non_empty = [c for c in cells if c and not c.isdigit()]
            if len(non_empty) >= 1:
                meta["participants"]["dev"].append(non_empty[0])
            if len(non_empty) >= 2:
                meta["participants"]["ba_po"].append(non_empty[1])

    return meta


def classify_section(section_text: str) -> str:
    """Return 'done' | 'follow_up' | 'retro' | 'other'"""
    lower = section_text.lower()
    # Check follow_up first — "chưa hoàn thành" / "đang + chưa" beats "hoàn thành"
    if any(k in lower for k in FOLLOW_UP_KEYWORDS):
        return "follow_up"
    if any(k in lower for k in RETRO_KEYWORDS):
        return "retro"
    if any(k in lower for k in DONE_KEYWORDS):
        return "done"
    return "other"


def split_owners(owner_text: str) -> list:
    """Split 'Khánh Đồng + Khoa Nguyễn' → ['Khánh Đồng', 'Khoa Nguyễn']"""
    if not owner_text:
        return []
    parts = re.split(r"\s*[+,/]\s*", owner_text)
    return [p.strip() for p in parts if p.strip()]


def extract_deadline(text: str) -> str:
    """Extract first date pattern dd/mm/yyyy from text."""
    m = DEADLINE_RE.search(text)
    return m.group(1) if m else ""


def parse_content_table(table):
    """
    Parse the main content table (rows with STT, content, notes, owner columns).
    Returns a list of sections, each with its items.
    """
    sections = []
    current_section = None
    header_detected = False

    for row in table.rows:
        cells = deduplicate_cells(row)
        flat = " | ".join(cells)
        lower_flat = flat.lower()

        # Skip empty rows
        if not any(c for c in cells):
            continue

        # Detect header row (STT | Nội dung | ...)
        if "stt" in lower_flat and ("nội dung" in lower_flat or "content" in lower_flat):
            header_detected = True
            continue

        first_cell_lower = cells[0].lower() if cells else ""

        # ── Retro sections: check BEFORE section-header detection ──────────────
        # Retro items don't have numeric STT; process them early so "các task" in
        # a retro item isn't mistaken for a new section header.
        if current_section and current_section["kind"] == "retro":
            # Skip sub-header rows like "Vấn đề | Lý do | Giải pháp" or "Retrospective:"
            skip_kws = ["vấn đề", "lý do", "lí do", "giải pháp", "retrospective"]
            if not any(kw in first_cell_lower for kw in skip_kws):
                item = {
                    "issue": cells[0],
                    "reason": cells[1] if len(cells) > 1 else "",
                    "solution": cells[2] if len(cells) > 2 else "",
                }
                current_section["items"].append(item)
            continue

        # ── Section header detection ────────────────────────────────────────────
        is_section_header = (
            len(cells) <= 2 and
            cells[0] and
            not cells[0].isdigit() and
            not re.match(r"^\d+$", cells[0])
        )
        is_section_header = is_section_header or any(
            kw in first_cell_lower for kw in
            ["các task", "trao đổi", "retro", "vấn đề", "sprint review",
             "scrum review", "encrement"]
        )
        if is_section_header and not cells[0].isdigit():
            kind = classify_section(cells[0])
            current_section = {
                "section": cells[0],
                "kind": kind,
                "items": []
            }
            sections.append(current_section)
            continue

        # For non-retro rows: first cell should be a number
        if not cells or not re.match(r"^\d+$", cells[0]):
            # If it looks like a section header (no digits, substantial text)
            if cells and cells[0] and len(cells[0]) > 5:
                kind = classify_section(cells[0])
                current_section = {
                    "section": cells[0],
                    "kind": kind,
                    "items": []
                }
                sections.append(current_section)
            continue

        if current_section is None:
            current_section = {"section": "Chưa phân loại", "kind": "other", "items": []}
            sections.append(current_section)

        # Map columns: always [STT, content, ..., notes, ..., owner]
        stt = cells[0]
        owner_raw = cells[-1] if len(cells) > 1 else ""
        notes = cells[-2] if len(cells) > 2 else ""
        content = cells[1] if len(cells) > 1 else ""

        # If content is blank (merged), try next
        if not content and len(cells) > 2:
            content = cells[2]

        deadline = extract_deadline(notes)
        owners = split_owners(owner_raw)

        item = {
            "stt": stt,
            "content": content,
            "notes": notes,
            "owners": owners,
            "deadline": deadline,
        }
        current_section["items"].append(item)

    return sections


def parse_retro_table(table):
    """
    Parse Sprint Retrospective table: [Vấn đề | Lý do | Giải pháp]
    """
    items = []
    header_passed = False

    for row in table.rows:
        cells = deduplicate_cells(row)
        flat = " | ".join(cells).lower()

        if "vấn đề" in flat and "lý do" in flat:
            header_passed = True
            continue

        if not header_passed:
            continue

        if len(cells) >= 3 and cells[0]:
            items.append({
                "issue": cells[0],
                "reason": cells[1] if len(cells) > 1 else "",
                "solution": cells[2] if len(cells) > 2 else "",
            })

    return items


def parse_mom(docx_path: str) -> dict:
    doc = Document(docx_path)
    tables = doc.tables

    result = {
        "file": Path(docx_path).name,
        "meeting": {},
        "sections": [],
        "retro": [],
    }

    if not tables:
        return result

    # Table 0: metadata
    result["meeting"] = parse_metadata_table(tables[0])

    # Remaining tables: content
    for table in tables[1:]:
        # Check if this is a retro table
        header_cells = " ".join(
            c.text for c in table.rows[0].cells if c.text
        ).lower() if table.rows else ""

        if "vấn đề" in header_cells and "lý do" in header_cells:
            result["retro"] = parse_retro_table(table)
        else:
            sections = parse_content_table(table)
            result["sections"].extend(sections)

    return result


def find_latest_mom(folder: str) -> str:
    """Find the most recently modified .docx file in a folder."""
    p = Path(folder)
    docx_files = list(p.glob("Meeting_minutes_*.docx"))
    if not docx_files:
        raise FileNotFoundError(f"No Meeting_minutes_*.docx found in {folder}")
    return str(sorted(docx_files, key=lambda f: f.stat().st_mtime, reverse=True)[0])


if __name__ == "__main__":
    # Configure stdout to use utf-8 to prevent encoding errors on Windows console
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) < 2:
        print("Usage: python3 parse_mom.py <path_to_docx>", file=sys.stderr)
        sys.exit(1)

    path_arg = sys.argv[1]

    # If a folder is passed, pick latest
    p = Path(path_arg)
    if p.is_dir():
        path_arg = find_latest_mom(path_arg)
        print(f"[INFO] Using latest file: {path_arg}", file=sys.stderr)

    data = parse_mom(path_arg)
    print(json.dumps(data, ensure_ascii=False, indent=2))
