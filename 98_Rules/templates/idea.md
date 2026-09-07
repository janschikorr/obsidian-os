Ideen-Dateien leben in `10_Reviews/ideas/idea-YYYY-MM-DD-<slug>.md`. Eine Datei pro Idee.

```yaml
---
id: idea-YYYY-MM-DD-<slug>
type: idea
title: <Idee in einem Satz>
date: YYYY-MM-DD
source: "[[YYYY-MM-DD]]"
status: offen
tags: []
---

<optionaler Freitext für mehr Kontext>
```

**Status-Werte:**
- `offen` – noch nicht bewertet
- `doing` – wird aktiv verfolgt (Task oder Projekt existiert bereits)
- `ignoriert` – bewusst verworfen

**Tags:** frei wählbar, z. B. `[plugin, infrastruktur, finanzen, obsidian, import, sicherheit]`

**Flow:**
1. Idee entsteht in `## Ideen` einer Daily Note (`00_Inbox/daily/YYYY-MM-DD.md`)
2. Mit Claude in `10_Reviews/ideas/` als eigene Datei übertragen, Daily Note behält den Originaltext und bekommt zusätzlich einen `→ [[idea-...]]`-Link
3. In `10_Reviews/ideas.base` (View "Offen") bewerten: Status auf `doing` oder `ignoriert` setzen
4. Bei `doing`: Task in `05_Tasks/` oder Projekt in `04_Projects/` anlegen
