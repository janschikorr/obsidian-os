# Changelog

Versioniert wird nur die Struktur dieses Vaults - Ordnerlayout und die Frontmatter-Schemas unter `98_Rules/templates/`, auf die die `plain-*`-Plugins zugreifen - nicht der Inhalt selbst. Schema (`MAJOR.MINOR`) und wann ein Eintrag fällig ist: `10_Reviews/decisions/vault-versioning.md`.

## 1.0.0 - 2026-09-07

Erste versionierte Baseline. Struktur zum Zeitpunkt dieses Eintrags:

- `00_Inbox/` (Rohdaten: Mail, Daily, Sessions, Transkripte, Recordings), `01_Me/` (Identität, `finance/`, `health/`), `02_Visions/`, `03_Goals/`, `04_Projects/`, `05_Tasks/`, `06_Events/`, `07_Knowledge/`, `08_People/`, `10_Reviews/` (`decisions/`, `ideas/`), `98_Rules/`, `99_Scripts/`
- Frontmatter-Schemas, die von den `plain-*`-Plugins gelesen werden (siehe `98_Rules/templates/`): Task (`status`/`priority`/`scheduled`/`due`/`project`/`goal`/`recurrence`), Event, Person, Mail

**Kompatibilität:**
- `plain-tasks >= 1.10.1` für das `goal`-Feld auf Tasks (Frontmatter `goal`, `[[wikilink]]` auf `03_Goals/*.md` mit `type: identity`). **1.10.0 war hier kaputt:** der Code suchte Ziele unter `01_Me/goals/`, einem Ordner, der in diesem Vault nie existiert hat - das Feld hat nie ein Ziel gefunden. Erst in 1.10.1 gefixt.
- `plain-calendar`, `plain-contacts`, `plain-mail`: keine bekannten Versions-Constraints, lesen ihre Ordner (`06_Events/`, `08_People/`, `00_Inbox/mail/`) aus einer pro Gerät lokalen, nicht versionierten Einstellung (`data.json`) - bei einer künftigen Ordner-Umbenennung muss diese Einstellung manuell nachgezogen werden (siehe Missing Context).

**Repo-Hygiene:**
- `.gitignore` überarbeitet: das Vault-Repo trackt nur noch Struktur (`98_Rules/`, `99_Scripts/`, `.claude/`, Root-Docs), keine Inhaltsordner mehr - siehe `10_Reviews/decisions/vault-git-scope.md`.
- Die vorherige lokale Git-History (7 Commits seit 2026-09-03) enthielt bereits echte persönliche Daten (u. a. `01_ich/charakter.md`). Kein Remote existierte, trotzdem wurde die History verworfen statt nachträglich bereinigt - Repo beginnt mit diesem Commit neu bei `1.0.0`.

## Missing Context

- Keine automatisierte Prüfung, ob eine installierte Plugin-Version zur aktuellen Vault-Struktur passt (z. B. das defekte `goal`-Feld in 1.10.0 wäre so früher aufgefallen).
- Ordner-Einstellungen der Plugins (`data.json`: `eventsFolder`, `tasksFolder`, `projectsFolder`, `folder`, `mailFolder`) sind nicht Teil dieser Versionierung (gerätelokal, gitignored) - eine künftige Ordner-Umbenennung in `index.md` muss dort manuell nachgezogen werden. Bei der letzten Umbenennung (`06_Calendar` → `06_Events`) wurde genau das übersehen und am 2026-09-07 nachträglich korrigiert.
