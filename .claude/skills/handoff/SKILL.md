---
name: handoff
description: Fasst die laufende Claude-Code-Session zusammen und legt die Zusammenfassung als Notiz in 00_Inbox/sessions/ ab. Nutzen, wenn der Nutzer die Session übergeben/beenden/pausieren will und den Stand für später oder eine andere Session festhalten möchte (z. B. "/handoff", "fass die Session zusammen", "Übergabe schreiben").
---

# Session-Handoff schreiben

## Process
1. **Session durchgehen.** Den bisherigen Gesprächsverlauf dieser Session überblicken: was wurde gemacht, was wurde entschieden, was ist noch offen. Nur das zusammenfassen, was tatsächlich passiert ist (Regel 2) - keine Ausblicke auf Dinge, die nicht besprochen wurden.
2. **Betroffene Dateien/Projekte identifizieren.** Welche Dateien wurden angelegt oder geändert, welche Projekte (`04_Projects/`), Personen (`05_People/`) oder Entscheidungen (`08_Decisions/`) sind betroffen? Für Verweise in der Zusammenfassung nutzen.
3. **Dateiname bestimmen.** `00_Inbox/sessions/YYYY-MM-DD-<kurzer-thema-slug>.md` (heutiges Datum, Slug aus dem Hauptthema der Session). Gibt es an dem Tag schon eine Handoff-Datei zum selben Thema, diese stattdessen ergänzen statt eine zweite mit gleichem Slug anzulegen; bei einem anderen Thema am selben Tag einen eigenen Slug wählen.
4. **Zusammenfassung schreiben.** Freitext-Notiz (kein festes Frontmatter-Schema nötig, siehe `12_Scripts/check_structure.py`), aber mit fester Grobstruktur:
   - Kurzer Titel/Datum
   - Was gemacht wurde (Kernpunkte, keine Nacherzählung jeder Nachricht)
   - Entscheidungen, die gefallen sind (mit Verweis auf `08_Decisions/...` falls dort dokumentiert)
   - Offene Punkte / nächste Schritte
   - Betroffene Dateien/Projekte/Personen als Links (`[[...]]`)
5. **Nicht doppelt loggen.** Wurden Änderungen bereits als Timeline-Einträge in den betroffenen Dateien selbst festgehalten (Regel 4), hier nicht erneut ausführlich wiederholen - kurz referenzieren reicht, die Handoff-Notiz ist der Überblick, nicht die Quelle der Wahrheit.
6. **Sichtbar machen.** Dem Nutzer den Pfad der neu geschriebenen/ergänzten Datei nennen.

## Result
Eine neue oder ergänzte Notiz in `00_Inbox/sessions/` mit einer kompakten, belegten Zusammenfassung der Session (Kernpunkte, Entscheidungen, offene Punkte, betroffene Dateien), sodass eine spätere Session oder eine andere Person schnell den Stand erfassen kann.
