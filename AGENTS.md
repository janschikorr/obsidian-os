# Agents – Entry Point for Every AI Agent

This is a Personal OS: a folder holding the user's entire structured context. Every agent (Claude Code, Codex, others) reads the following files in this order at the start of a new chat/task, before making any changes:

1. `index.md` – table of contents, which folder is responsible for what
2. `user.md` – who the user is, how they work
3. `soul.md` – how the agent should behave
4. `98_Rules/rules.md` – binding rules for changes to the system

Recurring workflows live as regular Claude Code skills under `.claude/skills/` (the standard mechanism, no custom resolver needed – each skill's `description` in its frontmatter decides when it applies).

After that, the agent only reads the context the concrete task actually needs (e.g. a specific project or person file) – not the entire system at once.

## Core Principle

- Every truth has exactly one responsible place (one file).
- Changes are only made based on context that has been read and is evidenced.
- Every change is logged in the timeline of the affected file and references its source.
- New ideas are not implemented immediately, but first collected in `00_Inbox/notes/ideas.md`.

See `98_Rules/rules.md` for details.
