#!/usr/bin/env python3
"""Validates that the vault follows the conventions from 98_Rules/rules.md and 98_Rules/templates/.

Usage: python 99_Scripts/check_structure.py [--strict]

--strict treats warnings as errors (non-zero exit code).
Checks only structure/schema (frontmatter fields, section headers, links) -
never judges the German prose content itself.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIR_PARTS = {".git", ".obsidian", "node_modules"}

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")

HEADER_SETS = {
    "standard": ["Current State", "Missing Context", "Sources / References", "Timeline"],
    "knowledge": ["Short Answer", "Sources", "Limits / Open Questions", "Timeline"],
    "tracking": ["Purpose", "Measurements", "Timeline"],
}

# type: -> which header set applies. Types without a dedicated template
# (identity, draft, user) reuse the "standard" person/project/decision shape.
TYPE_TO_HEADER_SET = {
    "person": "standard",
    "project": "standard",
    "decision": "standard",
    "identity": "standard",
    "user": "standard",
    "draft": "standard",
    "knowledge": "knowledge",
    "tracking": "tracking",
}

# folder -> type(s) expected for files in it (besides _template.md). Used for
# a soft warning only, since content is allowed to evolve past the template.
FOLDER_EXPECTED_TYPES = {
    "08_People": {"person"},
    "07_Knowledge": {"knowledge"},
    "01_Me": {"identity", "tracking"},  # finance/ and health/ subfolders use type "tracking"
    "04_Projects": {"project", "draft"},
}

REQUIRED_SCHEMA_FIELDS = ["id", "type", "title", "status", "created", "updated", "references"]

# root-level docs and other files exempt from the orphan check: they are
# entry points, not content meant to be linked from other notes.
ORPHAN_EXEMPT_NAMES = {"README.md"}

TIMELINE_ENTRY_RE = re.compile(r"^-\s+\d{4}-\d{2}-\d{2}:", re.MULTILINE)
SOURCE_MARKER_RE = re.compile(r"\((?:source|quelle)\s*:", re.IGNORECASE)

errors = []
warnings = []


def err(path, msg):
    errors.append(f"{path}: {msg}")


def warn(path, msg):
    warnings.append(f"{path}: {msg}")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def iter_md_files():
    for dirpath, dirnames, filenames in os.walk(ROOT, onerror=lambda e: None):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_PARTS]
        for name in filenames:
            if name.endswith(".md"):
                yield Path(dirpath) / name


def parse_frontmatter(text: str):
    """Minimal YAML-ish frontmatter parser: flat key: value pairs plus
    simple inline lists ([a, b]) and simple indented '- item' lists."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = {}
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            key, value = kv.group(1), kv.group(2).strip()
            if value == "":
                # possible block list on following indented lines
                items = []
                j = i + 1
                while j < len(lines) and re.match(r"^\s*-\s*(.+)$", lines[j]):
                    items.append(re.match(r"^\s*-\s*(.+)$", lines[j]).group(1).strip())
                    j += 1
                if items:
                    fm[key] = items
                    i = j
                    continue
                fm[key] = ""
            elif value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                fm[key] = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()] if inner else []
            else:
                fm[key] = value.strip('"').strip("'")
        i += 1
    return fm


def extract_section(text: str, header: str):
    m = re.search(rf"^##\s+{re.escape(header)}\s*$(.*?)(?=^##\s|\Z)", text, re.MULTILINE | re.DOTALL)
    return m.group(1) if m else None


def check_timeline_sources(path: Path, text: str):
    """Rule 3 ('every change needs a source'): every dated Timeline bullet
    should carry a (source: ...) / (Quelle: ...) marker. 06_Events/ is exempt
    per rule 4."""
    body = extract_section(text, "Timeline")
    if body is None:
        return
    starts = [m.start() for m in TIMELINE_ENTRY_RE.finditer(body)]
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(body)
        entry = body[start:end]
        if not SOURCE_MARKER_RE.search(entry):
            snippet = " ".join(entry.split())
            if len(snippet) > 80:
                snippet = snippet[:77] + "..."
            warn(rel(path), f"Timeline entry without a (source: ...) marker: \"{snippet}\"")


def check_schema_file(path: Path, text: str):
    fm = parse_frontmatter(text)
    if fm is None:
        err(rel(path), "no YAML frontmatter found")
        return

    for field in REQUIRED_SCHEMA_FIELDS:
        if field not in fm or (isinstance(fm[field], str) and fm[field] == "" and field != "references"):
            err(rel(path), f"missing/empty frontmatter field '{field}'")

    for field in ("created", "updated"):
        val = fm.get(field)
        if isinstance(val, str) and val and not DATE_RE.match(val):
            err(rel(path), f"'{field}: {val}' is not YYYY-MM-DD")

    file_type = fm.get("type")
    if not file_type:
        return

    folder = path.relative_to(ROOT).parts[0]
    expected = FOLDER_EXPECTED_TYPES.get(folder)
    if expected and file_type not in expected:
        warn(rel(path), f"type '{file_type}' unexpected for folder '{folder}/' (expected one of {sorted(expected)})")

    header_set_name = TYPE_TO_HEADER_SET.get(file_type)
    if not header_set_name:
        warn(rel(path), f"unknown type '{file_type}' - not mapped to a header set in check_structure.py")
        return

    body_headers = H2_RE.findall(text)
    for required in HEADER_SETS[header_set_name]:
        if required not in body_headers:
            err(rel(path), f"missing '## {required}' section (type: {file_type})")

    if "Timeline" in HEADER_SETS[header_set_name]:
        body = extract_section(text, "Timeline")
        if body is not None and not TIMELINE_ENTRY_RE.search(body):
            warn(rel(path), "Timeline section has no dated entries")
        check_timeline_sources(path, text)

    return fm


def check_calendar_file(path: Path, text: str):
    fm = parse_frontmatter(text)
    if fm is None:
        err(rel(path), "no YAML frontmatter found")
        return
    for field in ("title", "date", "dateCreated", "dateModified"):
        if not fm.get(field):
            err(rel(path), f"missing/empty frontmatter field '{field}'")
    if fm.get("date") and not DATE_RE.match(fm["date"]):
        err(rel(path), f"'date: {fm['date']}' is not YYYY-MM-DD")
    tags = fm.get("tags") or []
    if "event" not in tags:
        warn(rel(path), "tags missing 'event'")


def check_idea_file(path: Path, text: str):
    fm = parse_frontmatter(text)
    if fm is None:
        err(rel(path), "no YAML frontmatter found")
        return
    for field in ("id", "type", "title", "date", "source", "status"):
        if not fm.get(field):
            err(rel(path), f"missing/empty frontmatter field '{field}'")
    date_val = fm.get("date")
    if date_val and not DATE_RE.match(str(date_val)):
        err(rel(path), f"'date: {date_val}' is not YYYY-MM-DD")
    status_val = fm.get("status", "")
    if status_val and status_val not in ("offen", "doing", "ignoriert"):
        err(rel(path), f"invalid status '{status_val}' (expected offen|doing|ignoriert)")


def check_daily_file(path: Path, text: str):
    if path.name == "README.md":
        return
    fm = parse_frontmatter(text)
    if fm is None:
        err(rel(path), "no YAML frontmatter found")
        return
    for field in ("id", "type", "date"):
        if not fm.get(field):
            err(rel(path), f"missing/empty frontmatter field '{field}'")
    date_val = fm.get("date")
    if date_val and not DATE_RE.match(str(date_val)):
        err(rel(path), f"'date: {date_val}' is not YYYY-MM-DD")
    id_val = fm.get("id", "")
    date_from_name = path.stem  # e.g. "2026-09-07"
    if id_val and id_val != f"daily-{date_from_name}":
        warn(rel(path), f"id '{id_val}' does not match expected 'daily-{date_from_name}'")


def check_mail_file(path: Path, text: str):
    fm = parse_frontmatter(text)
    if fm is None:
        err(rel(path), "no YAML frontmatter found")
        return
    for field in ("title", "from", "date", "dateCreated"):
        if not fm.get(field):
            err(rel(path), f"missing/empty frontmatter field '{field}'")
    if fm.get("date") and not DATE_RE.match(fm["date"]):
        err(rel(path), f"'date: {fm['date']}' is not YYYY-MM-DD")
    tags = fm.get("tags") or []
    if "mail" not in tags:
        warn(rel(path), "tags missing 'mail'")


def check_task_file(path: Path, text: str):
    fm = parse_frontmatter(text)
    if fm is None:
        err(rel(path), "no YAML frontmatter found")
        return
    for field in ("title", "status", "priority", "dateCreated", "dateModified"):
        if not fm.get(field):
            err(rel(path), f"missing/empty frontmatter field '{field}'")
    if fm.get("status") and fm["status"] not in ("open", "in-progress", "blocked", "done"):
        err(rel(path), f"invalid status '{fm['status']}' (expected open|in-progress|blocked|done)")
    if fm.get("priority") and fm["priority"] not in ("low", "normal", "high"):
        err(rel(path), f"invalid priority '{fm['priority']}' (expected low|normal|high)")
    tags = fm.get("tags") or []
    if "task" not in tags:
        warn(rel(path), "tags missing 'task'")
    if "## Timeline" not in text:
        warn(rel(path), "missing '## Timeline' section")
    else:
        check_timeline_sources(path, text)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    strict = "--strict" in sys.argv

    all_ids = {}
    all_basenames = set()
    schema_frontmatters = {}

    md_files = list(iter_md_files())
    for path in md_files:
        all_basenames.add(path.stem)

    for path in md_files:
        if path.name.startswith("_"):
            continue  # template files
        parts = path.relative_to(ROOT).parts
        text = path.read_text(encoding="utf-8")

        if parts[0] == "06_Events":
            check_calendar_file(path, text)
            continue
        if parts[0] == "05_Tasks":
            check_task_file(path, text)
            continue
        if parts[0] == "00_Inbox" and len(parts) > 1 and parts[1] == "mail":
            check_mail_file(path, text)
            continue
        if parts[0] == "98_Rules" and "templates" in parts:
            continue  # templates use placeholder values on purpose
        if parts[0] == "10_Reviews" and len(parts) > 1 and parts[1] == "decisions":
            check_schema_file(path, text)
            continue
        if parts[0] == "10_Reviews" and len(parts) > 1 and parts[1] == "ideas":
            check_idea_file(path, text)
            continue
        if parts[0] == "00_Inbox" and len(parts) > 1 and parts[1] == "daily":
            check_daily_file(path, text)
            continue
        if parts[0] == "00_Inbox" and len(parts) > 1 and parts[1] != "mail":
            continue  # free-form raw input (conversations, sessions, transcripts), no frontmatter schema

        fm = parse_frontmatter(text)
        if fm and "type" in fm:
            fm2 = check_schema_file(path, text)
            if fm2:
                schema_frontmatters[rel(path)] = fm2
                if "id" in fm2 and fm2["id"]:
                    if fm2["id"] in all_ids:
                        err(rel(path), f"duplicate id '{fm2['id']}' (also in {all_ids[fm2['id']]})")
                    else:
                        all_ids[fm2["id"]] = rel(path)

    def normalize_ref(raw: str) -> str:
        ref = raw.strip().strip("[]")
        ref = ref.split("/")[-1]
        if ref.endswith(".md"):
            ref = ref[:-3]
        return ref

    referenced_stems = set()

    # reference resolution: references: [...] should point at a known id or filename
    for file_rel, fm in schema_frontmatters.items():
        refs = fm.get("references") or []
        for ref in refs:
            target = normalize_ref(ref)
            if not target:
                continue
            if target in all_ids:
                referenced_stems.add(Path(all_ids[target]).stem)
            elif target in all_basenames:
                referenced_stems.add(target)
            else:
                warn(file_rel, f"reference '{ref}' does not match any known id or filename")

    # wikilink resolution across the whole vault (skip templates: placeholders on purpose)
    for path in md_files:
        parts = path.relative_to(ROOT).parts
        if path.name.startswith("_") or (parts[0] == "98_Rules" and "templates" in parts):
            continue
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            target = normalize_ref(match.group(1))
            if not target:
                continue
            if target not in all_basenames:
                err(rel(path), f"broken wikilink [[{match.group(1)}]]")
            elif Path(path).stem != target:  # don't count a self-link as "referenced"
                referenced_stems.add(target)

    # orphan check: content files nobody links to or references (informational only)
    for path in md_files:
        parts = path.relative_to(ROOT).parts
        if path.name.startswith("_") or path.name in ORPHAN_EXEMPT_NAMES:
            continue
        if len(parts) == 1:
            continue  # root-level docs (AGENTS.md, index.md, ...) are entry points
        if parts[0] in ("98_Rules", "00_Inbox", "06_Events", "05_Tasks", ".claude"):
            continue  # Claude Code config/skills and workflow folders aren't cross-linked content
        if path.stem not in referenced_stems:
            warn(rel(path), "not referenced by any wikilink or reference in the vault (orphaned?)")

    print(f"Checked {len(md_files)} markdown files.\n")

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print()

    if not errors and not warnings:
        print("Structure OK - no issues found.")

    exit_errors = errors or (strict and warnings)
    sys.exit(1 if exit_errors else 0)


if __name__ == "__main__":
    main()
