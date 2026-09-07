---
name: check-birthdays
description: Prüft alle Personendateien in 05_People/ auf Geburtstage, die heute oder in den nächsten 3 Tagen anstehen, und meldet Treffer als Erinnerung. Nutzen, wenn der Nutzer nach anstehenden Geburtstagen fragt, oder als tägliche Automation für die Geburtstags-Erinnerung.
---

# Geburtstage prüfen

## Purpose
Verhindert vergessene Geburtstage, ohne dass der Nutzer selbst durch alle Personendateien schauen muss. Liest ausschließlich `05_People/*.md`, die einzige zuständige Quelle für Personendaten (siehe `index.md`).

## Process
1. Alle Dateien in `05_People/` außer `_template.md` einlesen.
2. In jeder Datei nach einem Geburtsdatum suchen – typischerweise im Timeline-Eintrag als `Geburtstag: <Tag>. <Monat ausgeschrieben> <Jahr>` (aus dem Notion-Import). Nur Tag und Monat auswerten, das Jahr ist laut vorhandenem Hinweis in `Fehlender Kontext` oft ein Datumsartefakt und unzuverlässig.
3. Heutiges Datum sowie die nächsten 3 Tage gegen Tag/Monat aller gefundenen Geburtstage abgleichen.
4. Für jeden Treffer: Name (`title`), Datum des Geburtstags, Anzahl Tage bis dahin (0 = heute) sammeln.
5. Ergebnis ausgeben:
   - Kein Treffer: kurz bestätigen, dass in den nächsten 3 Tagen niemand Geburtstag hat. Keine weitere Aktion.
   - Treffer: pro Person eine Zeile, sortiert nach Datum, z. B. `Heute: Cornelia Schulz` oder `In 2 Tagen: Olaf Schulz (22.12.)`.

## Explicitly Do Not
- Keine Geburtstagsgrüße oder Nachrichten automatisch verfassen oder verschicken – nur erinnern.
- Kein Jahr aus dem Notion-Import als echtes Geburtsjahr behandeln oder in Ausgaben nennen, solange es nicht verifiziert ist.
- Keine Personendateien bei diesem Check verändern.

## Result
Eine kurze Liste anstehender Geburtstage (oder Fehlanzeige), keine Änderung am System.
