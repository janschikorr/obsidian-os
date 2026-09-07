# Changelog

Versioniert wird nur die Struktur dieses Vaults (Ordnerlayout, Frontmatter-Schemas unter `98_Rules/`) - nicht der Inhalt. Siehe `10_Reviews/decisions/vault-versioning.md` für das Schema (MAJOR.MINOR) und wann ein Eintrag fällig ist.

## 1.0.0 - 2026-09-07

- Erstversion dieses Changelogs.
- Kompatibilität: `plain-tasks >= 1.10.0` für das neue `goal`-Feld auf Tasks (Frontmatter `goal`, erwartet `01_Me/goals/*.md` mit `type: identity`) - ältere `plain-tasks`-Versionen ignorieren das Feld, kein Bruch.
- `.gitignore` überarbeitet: das Vault-Repo trackt nur noch Struktur (Rules, Skills, Scripts, Root-Docs), keine persönlichen Daten mehr - siehe `10_Reviews/decisions/vault-git-scope.md`.
