# Index

Table of contents of this Personal OS. Every folder has a clearly scoped responsibility.

| Folder | Responsibility |
|---|---|
| `00_Inbox/` | Raw data input, divided by medium – nothing filed here is a finished truth yet. Subfolders: `00_Inbox/mail/` (relevant emails, managed via the custom "Plain Mail" plugin, `.obsidian/plugins/plain-mail/`), `00_Inbox/daily/` (daily log/journal with health tracking and ideas – see `98_Rules/templates/daily.md`), `00_Inbox/conversations/`, `00_Inbox/sessions/` (Claude Code session handoffs, see `/handoff`), `00_Inbox/transcripts/`, `00_Inbox/recordings/` (voice recordings via Obsidian's core audio recorder plugin; also the vault-wide default attachment folder, see `.obsidian/app.json`) |
| `01_Me/` | Identity: character, working style, history, career. Subfolders: `01_Me/finance/` (personal finances), `01_Me/health/` (health data) |
| `02_Visions/` | Long-term future visions – qualitative pictures of where I want to be |
| `03_Goals/` | Concrete, measurable goals – derived from visions |
| `04_Projects/` | Ongoing and completed private projects, one folder per project (`04_Projects/<slug>/<slug>.md` plus any owned drafts/assets alongside it) |
| `05_Tasks/` | Tasks (to-dos), managed via the custom "Plain Tasks" plugin (`.obsidian/plugins/plain-tasks/`) |
| `06_Events/` | Events (calendar entries), managed via the custom "Plain Calendar" plugin (`.obsidian/plugins/plain-calendar/`) |
| `07_Knowledge/` | External knowledge – nothing that concerns my own context. Current topics: `claude-code/` (Claude Code: agentic loop, CLAUDE.md/memory, hooks, CLI, MCP, skills/agents, CI/CD, security), `obsidian/` (Obsidian: formatting, linking/embeds, plugins, sync/publish, UI/navigation, files/properties) |
| `08_People/` | One file per person I deal with, managed via the custom "Plain Contacts" plugin (`.obsidian/plugins/plain-contacts/`) |
| `10_Reviews/` | Reviews, decisions and idea pipeline. `10_Reviews/decisions/` (documented decisions with reasoning, type: decision); `10_Reviews/ideas/` (one file per idea, type: idea, status: offen/doing/ignoriert). Base files: `decisions.base`, `ideas.base`. |
| `11_Work/` | Professional content – strictly separated from private context |
| `98_Rules/` | System rules, file templates, conventions |
| `99_Scripts/` | Automated checks for this system, e.g. `check_structure.py` (validates frontmatter schema, section headers, links, orphaned files) |
| `.claude/skills/` | Repeatable workflows as regular Claude Code skills |

Root files: `AGENTS.md` (entry point), `user.md` (who I am), `soul.md` (behavior contract).
