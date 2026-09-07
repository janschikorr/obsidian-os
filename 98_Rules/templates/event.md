Events (calendar entries) are created as their own note in `06_Events/`. Managed via the custom "Plain Calendar" plugin (`.obsidian/plugins/plain-calendar/`).

## Creating

Either via the calendar plugin (click a day in the calendar view) or directly as a markdown file with this frontmatter (field names in English, see `.obsidian/plugins/plain-calendar/src/main.ts`):

```yaml
---
title: <short description>
tags:
  - event
date: <YYYY-MM-DD>
time: <HH:mm>       # optional, empty = all-day
end: <HH:mm>        # optional, end of the time span (otherwise 60 min. default duration in day/week view)
location: <location> # optional
recurrence: <FREQ=...>  # optional, recurring event, see below
dateCreated: <YYYY-MM-DD>
dateModified: <YYYY-MM-DD>
---

<One sentence of context: what the event arose from>
```

## Recurring Events

`recurrence` uses an RRULE-like short syntax (`FREQ=YEARLY` for birthdays etc.), but only the part `FREQ`/`INTERVAL`/`UNTIL`/`COUNT` – no `BYDAY`/`BYMONTHDAY`.

- `FREQ=DAILY|WEEKLY|MONTHLY|YEARLY` (required)
- `INTERVAL=<n>` – every nth unit (default 1)
- `UNTIL=<YYYY-MM-DD>` – last occurrence (inclusive)
- `COUNT=<n>` – total number of occurrences

Examples: `FREQ=YEARLY` (yearly, e.g. birthday/anniversary), `FREQ=WEEKLY;INTERVAL=2` (every two weeks), `FREQ=MONTHLY;COUNT=6` (monthly, 6 times total).

For recurring events, `date` is the first occurrence (the note with `recurrence` is the "series note"/master).

### Exceptions to a series (Outlook model)

Editing or deleting an occurrence via the calendar asks what the change applies to:

- **Only this event** – creates (or changes) a separate event note for this one occurrence, with `series: <path of the series note>` and `replaces: <original date>` (which pattern slot is being replaced), without its own `recurrence` field. Deleting "only this event" instead adds the date to `excluded` in the series note (no leftover file).
- **This and all following** – splits the series at this date: the existing series note ends before it, a new series note takes over the pattern from this date on. Existing single exceptions from this date on automatically move to the new series note.
- **The entire series** – changes/deletes the series note itself (when deleting, including all associated single exceptions).

New frontmatter fields:

- `excluded: [YYYY-MM-DD, ...]` (series note only) – deleted occurrences of the pattern.
- `series: <path>` (exception note only) – which series note this note overrides.
- `replaces: <YYYY-MM-DD>` (exception note only) – which pattern occurrence it replaces.

**Known limitation:** if the date or the recurrence pattern itself is moved during "edit the entire series", existing single exceptions may miss their original slot – this can lead to duplicate or missing occurrences. There is no automatic migration for this.

## Conventions

- One sentence in the body is enough as a source (rule 3) – the file's git history documents further changes.
- Reference to a person: link to `08_People/<name>` in the body.
- Reference to a project: link to `04_Projects/<project>` in the body.
- Past events remain as a file, they are not deleted.
