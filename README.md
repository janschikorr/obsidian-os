# 🧠 Obsidian OS

A Personal OS: an [Obsidian](https://obsidian.md) vault structure plus [Claude Code](https://claude.com/product/claude-code) agent rules, skills, and checks for managing my own identity, goals, projects, tasks, events, people, and knowledge — all as plain markdown notes.

This repo is the "code" layer only — rules, templates, skills, structure. **No personal data lives here**, see [Repo scope](#-repo-scope) below.

## 🤔 Why

Existing all-in-one tools (Notion, TaskNotes, …) bundle a query language, a database layer, and a UI I don't control. This system instead treats the vault as the single source of truth — one responsible file per piece of information — with an AI agent (Claude Code) reading and updating it under a small set of binding rules, and a handful of purpose-built Obsidian plugins for the views a plain markdown file can't give you (task list, calendar, contacts, mail sync).

## 🗺️ Structure

| Folder | Responsibility |
|---|---|
| `00_Inbox/` | Raw data input, divided by medium (mail, daily log, conversations, session handoffs, transcripts, recordings) — nothing here is a finished truth yet |
| `01_Me/` | Identity: character, working style, history, career, `finance/`, `health/` |
| `02_Visions/` | Long-term future visions — qualitative pictures of where I want to be |
| `03_Goals/` | Concrete, measurable (SMART) goals, derived from visions |
| `04_Projects/` | Ongoing and completed private projects, one folder per project |
| `05_Tasks/` | Tasks, managed via the custom [Plain Tasks](https://github.com/janschikorr/obsidian-plain-tasks) plugin |
| `06_Events/` | Calendar entries, managed via the custom [Plain Calendar](https://github.com/janschikorr/obsidian-plain-calendar) plugin |
| `07_Knowledge/` | External knowledge (Claude Code, Obsidian, …) — nothing that concerns my own context |
| `08_People/` | One file per person, managed via the custom [Plain Contacts](https://github.com/janschikorr/obsidian-plain-contacts) plugin |
| `10_Reviews/` | Documented decisions (`decisions/`) and the idea pipeline (`ideas/`, offen → doing → ignoriert) |
| `11_Work/` | Professional content — strictly separated from private context |
| `98_Rules/` | System rules and file templates (`98_Rules/rules.md`, `98_Rules/templates/`) |
| `99_Scripts/` | Automated checks, e.g. `check_structure.py` (frontmatter schema, broken links, orphaned files) |
| `.claude/skills/` | Repeatable workflows as regular Claude Code skills |

Every folder is only ever meant to hold one clearly scoped type of thing — see `98_Rules/rules.md` rule 5. Full table with more detail: [`index.md`](index.md).

## 🚪 How an agent enters this system

`AGENTS.md` is the fixed entry point every agent (Claude Code, Codex, others) reads first, in order: `index.md` → `user.md` → `soul.md` → `98_Rules/rules.md`. Only after that does it read whatever the concrete task needs. `soul.md` is the short behavior contract (push back on contradictions, read before acting, no speculation); `98_Rules/rules.md` is the binding constitution (one file per truth, append-only timelines, ideas aren't an implementation order, ...).

## 🔒 Repo scope

This repo tracks the Personal OS's structure only:

- **Tracked:** `98_Rules/`, `99_Scripts/`, `.claude/` (minus local settings), root docs, `.gitignore`, non-machine-local `.obsidian/*.json` config — and an empty `.gitkeep` skeleton of every content folder, so the folder layout is visible on a fresh clone
- **Ignored:** the actual content of every folder above (real notes, mail, health/finance data, …), `.obsidian/plugins/` (the `plain-*` plugins are their own repos; everything else is reproducible from `community-plugins.json`), and machine-local caches (`.obsidian/workspace.json`, `.claudian/`)

See [`10_Reviews/decisions/vault-git-scope.md`](10_Reviews/decisions/vault-git-scope.md) for the full reasoning and what's excluded.

## 📓 Versioning

`CHANGELOG.md` versions the vault's *structure* (folder layout, frontmatter schemas the `plain-*` plugins read) — not its content, and independent of the plugins' own version numbers. See rule 10 in `98_Rules/rules.md` and [`10_Reviews/decisions/vault-versioning.md`](10_Reviews/decisions/vault-versioning.md).

## 🔗 Companion plugins

- [Plain Tasks](https://github.com/janschikorr/obsidian-plain-tasks)
- [Plain Calendar](https://github.com/janschikorr/obsidian-plain-calendar)
- [Plain Contacts](https://github.com/janschikorr/obsidian-plain-contacts)
- [Plain Mail](https://github.com/janschikorr/obsidian-plain-mail)

## ⚠️ Status

This is my own, actively evolving personal system — published as-is for reference/inspiration, not maintained as a reusable template or accepting external contributions.
