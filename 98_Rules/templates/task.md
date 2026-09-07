Tasks (to-dos) are created as a task note in `05_Tasks/`, managed via the custom "Plain Tasks" plugin (`.obsidian/plugins/plain-tasks/`).

## Creating

Either via the plugin (ribbon icon/command "Plain Tasks: New task" or "+ New task" in the list view) or directly as a markdown file with this frontmatter (field names in English, see `.obsidian/plugins/plain-tasks/src/main.ts`):

```yaml
---
title: <short description>
tags:
  - task
status: open        # open | in-progress | blocked | done
priority: normal    # low | normal | high
scheduled: <YYYY-MM-DD>   # optional: when to start working on it
due: <YYYY-MM-DD>         # optional: hard deadline – also the anchor for recurrence
project: "[[<project>]]"  # optional: reference to 04_Projects/
goal: "[[<goal>]]"        # optional: reference to 01_Me/goals/ (use instead of project when there's no active initiative yet)
recurrence: <FREQ=...>    # optional, only allowed when due is set
dateCreated: <YYYY-MM-DD>
dateModified: <YYYY-MM-DD>
---

## Timeline
- <YYYY-MM-DD>: Created (source: plain-tasks)
```

## Recurring Tasks

`recurrence` uses the same RRULE-like short syntax as for events (see `98_Rules/templates/event.md`): only `FREQ`/`INTERVAL`/`UNTIL`/`COUNT`, no `BYDAY`/`BYMONTHDAY`. The anchor is always `due` (not `scheduled`) – without `due` no recurrence is possible.

The list view always shows only one line per series: the next still-open occurrence. Checking off such a line automatically creates an exception note with `series`/`replaces`/`status: done` for exactly that occurrence; editing/deleting asks (like the calendar) "Only this occurrence" / "This and all following" / "The entire series".

## Conventions

- The timeline requirement applies as usual (rule 4) – unlike events there is no exception here. The plugin only scaffolds the creation entry; substantive changes (why blocked, what was decided) are added to the timeline manually or by Claude.
- Reference to a person: link to `08_People/<name>` in the body.
- Reference to a project: set the `project` property to the project file.
- Reference to a goal: set the `goal` property to the goal file (`03_Goals/<slug>.md`) – use this when the task serves a goal directly and no project exists for it yet. Prefer `project` over `goal` once an active initiative exists.
- What blocks the task belongs in the body or in the `blocked` status – don't guess, record it as an open question.
- Recurring events (e.g. birthdays) still go through `06_Events/`/`plain-calendar`, not through tasks.
- Completed tasks remain as a file (status `done`), they are not deleted.
