---
name: analyze-conversation
description: Analysiert ein Gespräch, einen Call oder ein Transkript (aus 00_Inbox/) und aktualisiert damit die betroffenen Personen-, Projekt-, Entscheidungs- und Aufgabendateien im Personal OS. Nutzen, wenn der Nutzer ein Transkript/eine Gesprächsnotiz auswerten und ins System einarbeiten lassen will.
---

# Gespräch analysieren

## Process
1. **Quelle lesen.** Das vollständige Transkript/die Notiz lesen. Original unverändert an seinem Ort belassen.
2. **Trennen.** Aussagen, Entscheidungen und offene Punkte aus dem Gespräch identifizieren und voneinander trennen.
3. **Relevanz prüfen.** Welche Personen (`05_People/`) oder Projekte (`04_Projects/`) sind betroffen? Existiert für sie bereits eine Datei? Wenn nicht, nach Vorlage (`03_Rules/templates/`) neu anlegen.
4. **Betroffene Dateien aktualisieren.** Nur den belegten Stand ändern (Abschnitt "Current State"), mit Verweis auf diese Gesprächsquelle.
5. **Interaktion protokollieren.** War dieses Gespräch selbst ein tatsächlicher Kontakt mit einer Person aus `05_People/` (nicht nur eine Erwähnung über sie)? Dann in deren Abschnitt "Interaktionen" einen Eintrag ergänzen (Art des Kontakts, ein Satz worüber, Quelle = dieses Gespräch) – siehe `03_Rules/templates/person.md`.
6. **Entscheidungen ableiten.** Wurde im Gespräch etwas entschieden? Neue Datei in `08_Decisions/` anlegen oder bestehende referenzieren.
7. **Aufgaben ableiten.** Ergibt sich ein nächster Schritt? Aktuell gibt es kein Aufgaben-Tool (TaskNotes wurde entfernt, Ersatz noch nicht gebaut, siehe `00_Inbox/notes/ideas.md`) – den nächsten Schritt stattdessen im Abschnitt "Current State" der betroffenen Projekt-/Personendatei festhalten.
8. **Prüfen.** Sind alle Links korrekt gesetzt? Wurden die Regeln aus `03_Rules/rules.md` eingehalten? Gibt es Widersprüche zu bestehenden Entscheidungen?
9. **Zurückschreiben.** Timeline-Einträge in allen geänderten Dateien ergänzen (Datum, Änderung, Quelle = dieses Gespräch).

## Result
Alle betroffenen Personen-, Projekt-, Entscheidungs- und Aufgabendateien sind aktualisiert, verlinkt, geprüft und verweisen nachvollziehbar auf die Gesprächsquelle.
