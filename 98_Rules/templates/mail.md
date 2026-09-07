A received email is captured as its own note in `00_Inbox/mail/` when it carries relevant information for the system. Managed via the `plain-mail` plugin (`.obsidian/plugins/plain-mail/`) - relevance is decided by configurable rules, not manually per mail.

## Creating

```yaml
---
id: <slug>
type: mail
title: <subject>
from: <sender address/name>
date: <YYYY-MM-DD>
tags:
  - mail
dateCreated: <YYYY-MM-DD>
references: []
messageId: <Message-ID>
---

Von: [[08_People/<name>|<Name>]]   # only if the sender matched a known person, optional

<full plain-text body of the mail>
```

## Conventions

- `messageId` (the mail's `Message-ID` header) is the dedupe key the plugin uses to avoid re-importing the same mail on a later sync - never edit or remove it by hand.
- One sentence in the body would be enough as a source (rule 3) - the file's git history documents further changes, no Timeline section needed (rule 4 exception, like `06_Events/`). In practice the body holds the full plain-text mail (see below), so the "one sentence" only applies to any manually added commentary.
- Reference to a person: the plugin links `08_People/<name>` automatically when the sender's address matches that person's `email` frontmatter field, and appends an entry to that person's `## Interaktionen` section. Reference to a project stays manual in v1 - link `04_Projects/<project>` in the body yourself if relevant.
- The plugin (v1) stores the complete plain-text body as-is, no summarization or truncation - shortening individual mails is a possible later improvement, not done today.
- Not every incoming email becomes a note - only ones matching an `include` relevance rule (or the configured default action). Irrelevant mail (newsletters, ads, notifications) is skipped, see the plugin's settings.
