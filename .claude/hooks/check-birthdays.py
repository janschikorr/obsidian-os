#!/usr/bin/env python3
"""SessionStart hook: meldet Geburtstage aus 05_People/*.md, die heute oder in den naechsten 3 Tagen anstehen.
Nur Tag/Monat werden ausgewertet - siehe Skill check-birthdays fuer die Begruendung (Jahr im Notion-Import unzuverlaessig)."""
import json
import os
import re
import sys
from datetime import date, timedelta

MONATE = {
    "januar": 1, "februar": 2, "märz": 3, "maerz": 3, "april": 4, "mai": 5, "juni": 6,
    "juli": 7, "august": 8, "september": 9, "oktober": 10, "november": 11, "dezember": 12,
}

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PEOPLE_DIR = os.path.join(REPO_ROOT, "people")

GEBURTSTAG_RE = re.compile(r"Geburtstag:\s*(\d{1,2})\.\s*([A-Za-zÄäÖöÜüß]+)\s+\d{4}")
TITEL_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)


def find_hits(today: date, horizon_days: int = 3):
    hits = []
    if not os.path.isdir(PEOPLE_DIR):
        return hits
    for fname in sorted(os.listdir(PEOPLE_DIR)):
        if not fname.endswith(".md") or fname.startswith("_"):
            continue
        path = os.path.join(PEOPLE_DIR, fname)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        m = GEBURTSTAG_RE.search(content)
        if not m:
            continue
        day = int(m.group(1))
        monat_name = m.group(2).lower()
        month = MONATE.get(monat_name)
        if not month:
            continue
        titel_m = TITEL_RE.search(content)
        name = titel_m.group(1).strip() if titel_m else fname[:-3]

        try:
            bday_this_year = date(today.year, month, day)
        except ValueError:
            continue
        delta = (bday_this_year - today).days
        if delta < 0:
            try:
                bday_next_year = date(today.year + 1, month, day)
            except ValueError:
                continue
            delta = (bday_next_year - today).days

        if 0 <= delta <= horizon_days:
            hits.append((delta, name, day, month))
    hits.sort(key=lambda h: h[0])
    return hits


def format_hits(hits):
    lines = []
    for delta, name, day, month in hits:
        when = "Heute" if delta == 0 else ("Morgen" if delta == 1 else f"In {delta} Tagen")
        lines.append(f"- {when}: {name} ({day:02d}.{month:02d}.)")
    return "\n".join(lines)


def main():
    today = date.today()
    hits = find_hits(today)
    if not hits:
        print(json.dumps({}))
        return

    text = format_hits(hits)
    output = {
        "systemMessage": "Geburtstage anstehend:\n" + text,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "Geburtstags-Erinnerung (aus 05_People/, Jahr im Notion-Import unzuverlaessig, "
                "nur Tag/Monat massgeblich):\n" + text
            ),
        },
    }
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
