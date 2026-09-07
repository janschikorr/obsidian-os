A goal (`03_Goals/<slug>.md`) describes a desired end-state – "something I want" – not an active initiative. It answers *why*, not *how*. It does not need a running project to exist (e.g. "Beziehung organisch wachsen lassen" has no project); if an active initiative does exist to pursue it, link to that `04_Projects/` note instead of duplicating its operational details here.

**One goal, one file.** Even when several goals share a life area (e.g. "Warze entfernen", "Dehnungsstreifen behandeln" and "Talgpickel entfernen" are all health-related), each gets its own file – don't bundle multiple goals into one note just because they're thematically close. Group related goals via the `tags` frontmatter field instead (e.g. `tags: [gesundheit]`), so Obsidian's tag search/graph and `01_Me/goals.md` can list them together without merging their SMART/timeline/status into a shared file that would blur which change belongs to which goal.

Every goal is formulated **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound). If one of the five is genuinely not yet known, say so explicitly under "Missing Context" instead of inventing a value – per rule 2, only evidenced information goes into the SMART fields themselves.

SMART covers *what/why/by when* but not *how it survives contact with reality*. Three additional, evidence-based systems close that gap and are part of every goal (research: Oettingen's WOOP/mental contrasting, Gollwitzer's implementation intentions, Matthews' accountability study, and progress-monitoring meta-analyses – see `01_Me/goals.md` timeline for sources):

- **Hindernis & If-Then-Plan (WOOP):** name the most likely *inner* obstacle (a thought/emotion/habit, not just external circumstance), then wire it to a concrete if-then plan ("Wenn `<Hindernis/Trigger>`, dann `<Handlung>`"). Same rule as SMART: if not yet identified, say so under "Missing Context" rather than guessing – this needs real reflection, ideally a dedicated conversation, not invention.
- **Review-Rhythmus:** a fixed interval (täglich/wöchentlich/monatlich/...) at which this goal's "Aktueller Stand" gets revisited and the Timeline updated. Shorter loops outperform longer ones – prefer weekly for active/fast-moving goals, monthly for slower ones, per the goal's own pace.
- **Accountability:** who/what holds this goal accountable. Default for this system: Claudian (this Personal OS) as the reporting partner at every review/update – reviews happen in chat and get logged to the Timeline either way. State explicitly if a real person is also involved (e.g. a partner, for goals where that fits).

```yaml
---
id: <unique-id>
type: identity
title: Ziel – <title>
status: <aktiv|pausiert|erreicht>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
references: [ich-ziele]
tags: [<domain, e.g. gesundheit|finanzen|karriere|aussehen|beziehung>]
---

## Current State

### SMART
- **Specific:** <the concrete, unambiguous target>
- **Measurable:** <the metric/number that proves it's reached>
- **Achievable:** <why this is realistic given current means/pace>
- **Relevant:** <why this matters, link to the overarching life goal in `01_Me/goals.md`>
- **Time-bound:** <target date, or explicit note that none is set yet>

### Hindernis & If-Then-Plan
- **Wahrscheinlichstes inneres Hindernis:** <thought/emotion/habit likely to derail this>
- **If-Then-Plan:** Wenn <Hindernis/Trigger>, dann <konkrete Handlung>.

### Review-Rhythmus
- **Intervall:** <täglich|wöchentlich|monatlich|...>
- **Nächstes Review:** <YYYY-MM-DD, optional>

### Accountability
- **Mechanismus:** <e.g. Claudian bei jedem Review; ggf. zusätzlich eine reale Person>

### Aktueller Stand
<Where things stand right now>

### Nächster Schritt
<The next concrete action – link a `05_Tasks/` note or `04_Projects/` note if one exists>

### Vision (3-5 Jahre)
<Optional longer-horizon framing beyond the SMART target, if useful>

## Missing Context
<Which SMART fields, obstacle/if-then plan, review rhythm, or accountability details are still incomplete, and what's needed to fill them>

## Sources / References
- Übergeordnetes Ziel: `[[03_Goals/goals.md]]`
<Related project(s), conversations this is based on>

## Timeline
- YYYY-MM-DD: <change> (source: <reference>)
```
