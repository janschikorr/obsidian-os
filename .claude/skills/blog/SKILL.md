---
name: blog
description: Ruft einen Blog-/Artikel-Link ab und fasst ihn immer auf Deutsch zusammen, abgelegt in 02_Knowledge/. Nutzen, wenn der Nutzer einen Artikel-/Blog-Link teilt und daraus wichtige Infos oder eine Zusammenfassung möchte. Analog zu /youtube, nur mit einem geschriebenen Artikel statt einem Video als Quelle.
---

# Blog-Artikel zusammenfassen

## Process
1. **Artikel abrufen.** Den Inhalt der Artikel-URL laden (z. B. per WebFetch) und dabei Titel, Autor:in und Veröffentlichungsdatum mit ermitteln, wenn im Artikel erkennbar.
2. **Volltext lesen.** Den kompletten Artikel lesen, nicht nur den Anfang oder eine Vorschau.
3. **Thema bestimmen.** Passenden Themenordner in `02_Knowledge/` finden oder neu anlegen (z. B. `02_Knowledge/<thema>/`).
4. **Quelle dokumentieren, nicht kopieren.** Anders als beim Transkript-Skill wird der Artikeltext NICHT vollständig als Rohquelle gespeichert (Urheberrecht). Stattdessen in `02_Knowledge/<thema>/raw/<artikel-id-oder-titel>.md` nur festhalten:
   - Original-URL, Titel, Autor:in, Datum
   - maximal 2-3 kurze, wörtliche Zitate (klar in Anführungszeichen, mit Quellenangabe) als Beleg für zentrale Aussagen
   - keine vollständige oder nahezu vollständige Wiedergabe des Artikeltexts
5. **Zusammenfassung schreiben.** Eine `wiki.md` (oder Ergänzung einer bestehenden) nach der Wissens-Vorlage `03_Rules/templates/knowledge.md` erstellen: kurze Antwort, Kernpunkte in eigenen Worten, Quellen, Grenzen/offene Fragen.
   **Die Zusammenfassung wird immer auf Deutsch geschrieben – unabhängig von der Sprache des Originalartikels.**
6. **Verlinken.** Wiki-Datei verweist auf die Rohquelle (Schritt 4) und die Original-URL.
7. **Prüfen & Timeline.** Regeln aus `03_Rules/rules.md` beachten (Quelle vorhanden, keine Spekulation), Timeline-Eintrag in der Wiki-Datei ergänzen.

## Result
Ein Themenordner in `02_Knowledge/` mit Quellenangabe + wenigen kurzen Zitaten als Beleg (keine vollständige Textkopie) und einer deutschen Zusammenfassung in eigenen Worten nach Wissens-Vorlage, verlinkt und mit Timeline-Eintrag.
