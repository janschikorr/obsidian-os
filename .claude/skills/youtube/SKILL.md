---
name: youtube
description: Ruft das Transkript eines YouTube-Videos ab und fasst es immer auf Deutsch zusammen, abgelegt in 02_Knowledge/. Nutzen, wenn der Nutzer einen YouTube-Link teilt und eine Zusammenfassung/wichtige Infos daraus möchte.
---

# YouTube-Video zusammenfassen

## Process
1. **Transkript abrufen.** Das Transkript des Videos über die YouTube-Transcript-API besorgen (unabhängig von der Videosprache). Falls `youtube_transcript_api` nicht verfügbar ist, in einem Scratchpad-Virtualenv installieren:
   ```
   python3 -m venv <scratchpad>/venv
   <scratchpad>/venv/bin/pip install --quiet youtube_transcript_api
   ```
   Danach das Transkript per Python abrufen (Sprache zuerst Deutsch, sonst Englisch/Originalsprache probieren) und in eine Datei im Scratchpad schreiben.
2. **Metadaten ermitteln.** Video-Titel und Kanalname möglichst mit ermitteln.
3. **Volltext lesen.** Das komplette Transkript lesen (bei langen Transkripten in Teilen), nicht nur den Anfang.
4. **Thema bestimmen.** Passenden Themenordner in `02_Knowledge/` finden oder neu anlegen (z. B. `02_Knowledge/<thema>/`).
5. **Rohquelle ablegen.** Das vollständige Transkript unverändert unter `02_Knowledge/<thema>/raw/<video-id-oder-titel>.md` speichern, mit Verweis auf die Original-URL.
6. **Zusammenfassung schreiben.** Eine `wiki.md` (oder Ergänzung einer bestehenden) nach der Wissens-Vorlage `03_Rules/templates/knowledge.md` erstellen: kurze Antwort, Kernpunkte, Quellen, Grenzen/offene Fragen.
   **Die Zusammenfassung wird immer auf Deutsch geschrieben – unabhängig von der Sprache des Originalvideos.**
7. **Verlinken.** Wiki-Datei verweist auf die Rohquelle (Schritt 5) und die Original-YouTube-URL.
8. **Prüfen & Timeline.** Regeln aus `03_Rules/rules.md` beachten (Quelle vorhanden, keine Spekulation), Timeline-Eintrag in der Wiki-Datei ergänzen.

## Result
Ein Themenordner in `02_Knowledge/` mit unverändertem Transkript als Rohquelle und einer deutschen Zusammenfassung nach Wissens-Vorlage, verlinkt und mit Timeline-Eintrag.
