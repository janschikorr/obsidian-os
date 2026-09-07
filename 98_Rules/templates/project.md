Each project gets its own folder under `04_Projects/<slug>/`, not a single loose file: the main state file repeats the slug (`04_Projects/<slug>/<slug>.md`, not `index.md` — with several projects open as Obsidian tabs, "index.md" everywhere is indistinguishable, the repeated name stays readable in tabs/quick-switcher). Files the project owns (drafts, exports, other `type: draft` notes) live alongside it in the same folder, e.g. `04_Projects/personal-branding/personal-branding-readme-draft.md`. Reference them from the main file's "Sources / References" section as usual.

Main state file (`04_Projects/<slug>/<slug>.md`):

```yaml
---
id: <unique-id>
type: project
title: <title>
status: <active|completed|paused>
priority: <high|medium|low>
deadline: <YYYY-MM-DD oder leer>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
references: []
---

## Current State
<Goal, current state, next confirmed step>

## Missing Context
<Which roles, details, connections are still missing>

## Sources / References
<Conversations, people, companies, documents this state is based on>

## Timeline
- YYYY-MM-DD: <change> (source: <reference>)
```
