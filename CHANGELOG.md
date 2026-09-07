# Changelog

Only the structure of this vault is versioned - folder layout and the frontmatter schemas under `98_Rules/templates/` that the `plain-*` plugins read from - not the content itself. Schema (`MAJOR.MINOR`) and when an entry is due: `10_Reviews/decisions/vault-versioning.md`.

## 1.0.0 - 2026-09-07

First versioned baseline. Structure at the time of this entry:

- `00_Inbox/` (raw data: mail, daily, sessions, transcripts, recordings), `01_Me/` (identity, `finance/`, `health/`), `02_Visions/`, `03_Goals/`, `04_Projects/`, `05_Tasks/`, `06_Events/`, `07_Knowledge/`, `08_People/`, `10_Reviews/` (`decisions/`, `ideas/`), `98_Rules/`, `99_Scripts/`
- Frontmatter schemas read by the `plain-*` plugins (see `98_Rules/templates/`): Task (`status`/`priority`/`scheduled`/`due`/`project`/`goal`/`recurrence`), Event, Person, Mail

**Compatibility:**
- `plain-tasks >= 1.10.1` for the `goal` field on tasks (frontmatter `goal`, `[[wikilink]]` to `03_Goals/*.md` with `type: identity`). **1.10.0 was broken here:** the code looked for goals under `01_Me/goals/`, a folder that never existed in this vault - the field never found a goal. Only fixed in 1.10.1.
- `plain-calendar`, `plain-contacts`, `plain-mail`: no known version constraints, they read their folders (`06_Events/`, `08_People/`, `00_Inbox/mail/`) from a per-device local, unversioned setting (`data.json`) - a future folder rename requires manually updating that setting (see Missing Context).

**Repo hygiene:**
- `.gitignore` reworked: the vault repo now tracks only structure (`98_Rules/`, `99_Scripts/`, `.claude/`, root docs), no more content folders - see `10_Reviews/decisions/vault-git-scope.md`.
- The previous local git history (7 commits since 2026-09-03) already contained real personal data (among others `01_ich/charakter.md`). No remote existed, yet the history was discarded instead of cleaned up retroactively - the repo starts fresh with this commit at `1.0.0`.

## Missing Context

- No automated check whether an installed plugin version matches the current vault structure (e.g. the broken `goal` field in 1.10.0 would have been caught earlier this way).
- Plugin folder settings (`data.json`: `eventsFolder`, `tasksFolder`, `projectsFolder`, `folder`, `mailFolder`) are not part of this versioning (device-local, gitignored) - a future folder rename in `index.md` must be manually applied there too. During the last rename (`06_Calendar` → `06_Events`) this was exactly what got missed and was corrected retroactively on 2026-09-07.
