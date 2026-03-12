# Skill

## Name

/elvis-reporting-system

## Beschreibung

Baut ein dauerhaftes wöchentliches und monatliches Reporting-System mit 5 Pflicht-Metriken, standardisierten Report-Templates und einem definierten Verteilungs-Prozess auf. Im Gegensatz zu einem einmaligen Report-Dokument definiert dieser Skill das System dahinter: wer berichtet, was gemessen wird, in welchem Format und an wen die Ergebnisse verteilt werden. Das Ergebnis ist ein wiederverwendbares Reporting-Ritual, das jeden Montag (Weekly) und am ersten Monatsersten (Monthly) in unter 30 Minuten abgearbeitet werden kann.

## Ziele

- Definierte 5 Pflicht-Metriken mit Quelle, Formel und Zielwert pro Metrik
- Standardisiertes Weekly-Report-Template (1-Seite, max. 10 Minuten Erstellung)
- Standardisiertes Monthly-Report-Template (3-Seiten, max. 20 Minuten Erstellung)
- Festgelegter Verteilungs-Prozess: wer erhält welchen Report in welchem Format (PDF / Notion / E-Mail)
- Archivierungs-Systematik: Reports sind dauerhaft auffindbar und vergleichbar

## Strategie

Das Reporting-System priorisiert Einfachheit über Vollständigkeit: 5 konsistent gemessene Pflicht-Metriken liefern mehr strategischen Wert als 20 sporadisch erhobene. Das Weekly-Format ist bewusst minimal gehalten (1 Seite, 5 Metriken, 1 Handlungs-Empfehlung) — zu viele Reports werden nicht gelesen. Das Monthly-Format erlaubt tiefere Analyse und Trend-Betrachtung. Die Trennung zwischen "was gemessen wird" (Metriken) und "wer es braucht" (Verteilung) hält das System flexibel bei wechselnden Empfängern.

## Einschränkungen

- Exakt 5 Pflicht-Metriken pro Reporting-Zyklus — Erweiterungen erfordern explizite Entscheidung
- Weekly-Reports beschränkt auf 1 Seite / Monthly-Reports auf max. 3 Seiten (Lesbarkeits-Grenze)
- Keine automatische Datenerhebung — der Skill definiert das System, der Operator führt die Messung durch
- Empfänger-Liste maximal 5 Personen / Rollen — größere Verteiler erfordern separaten Kommunikationsplan
- Archiv-Format standardisiert (Dateiname: `[YYYY-WW]-weekly-report.md` bzw. `[YYYY-MM]-monthly-report.md`)

## Ausführungsschritte

1. Ermittle gemeinsam mit dem Operator die 5 wichtigsten Pflicht-Metriken: Welche 5 Kennzahlen, wenn sie sich verschlechtern, erfordern sofortiges Handeln? Dokumentiere für jede Metrik: Name, Quelle (wo wird die Zahl abgelesen?), Formel (wie wird sie berechnet?), Zielwert (wöchentlich / monatlich), Alarm-Schwelle (ab wann kritisch?).
2. Erstelle das Weekly-Report-Template mit 5 fixierten Abschnitten: (A) Datum + Berichtszeitraum, (B) Metriken-Tabelle (5 Zeilen × 3 Spalten: Metrik | Ist-Wert | Status 🟢/🟡/🔴), (C) Highlights der Woche (max. 3 Bullet Points), (D) Probleme / Abweichungen (max. 2 Bullet Points), (E) Empfohlene Maßnahme der Woche (1 konkreter Satz). Template in Markdown-Format als Copy-Paste-Vorlage.
3. Erstelle das Monthly-Report-Template mit 6 fixierten Abschnitten: (A) Monats-Zusammenfassung (3–5 Sätze Executive Summary), (B) Metriken-Trendtabelle (5 Metriken × 4 Wochen-Vergleich), (C) Ziel-Erreichungs-Status (Ziele vs. Ist, Ampel-System), (D) Top 3 Erkenntnisse des Monats, (E) Handlungs-Prioritäten für den Folgemonat, (F) Anhang: detaillierte Rohdaten.
4. Definiere den Verteilungs-Prozess: Erstelle eine Verteilungs-Matrix mit 3 Spalten — Empfänger/Rolle, erhält Weekly, erhält Monthly. Lege für jeden Empfänger fest: Kanal (E-Mail / Slack / Notion-Link), Format (Markdown / PDF / Link), Versand-Zeitpunkt (Weekly: Montag 10:00 Uhr / Monthly: 1. des Monats 09:00 Uhr).
5. Richte die Archivierungs-Systematik ein: Erstelle einen Archiv-Ordner (z.B. `reports/weekly/` und `reports/monthly/`). Definiere die Dateinamens-Konvention (`[YYYY-WW]-weekly-report.md` und `[YYYY-MM]-monthly-report.md`). Schreibe eine Archiv-Index-Datei (`reports/README.md`) mit Tabelle: Datum | Report-Typ | Dateiname | Highlights-Stichwort.
6. Befülle den ersten Weekly-Report mit aktuellen Daten als Proof-of-Concept: Erhebe die 5 Pflicht-Metriken für die aktuelle Woche, fülle das Weekly-Template aus, archiviere ihn gemäß Konvention. Dieser erste Report dient als Referenz-Beispiel für alle Folgereports.
7. Schreibe eine Reporting-Anleitung (max. 1 Seite): Wann wird welcher Report erstellt, wo werden die Daten abgeholt, wie wird das Template befüllt, wie wird der Report verteilt, wie wird er archiviert. Diese Anleitung soll eine Person ohne Vorwissen in unter 30 Minuten in das System einarbeiten.

## Verifikation

- Template-Vollständigkeit: Weekly-Template hat alle 5 Pflicht-Abschnitte, Monthly-Template hat alle 6 Pflicht-Abschnitte
- Metriken-Qualität: Alle 5 Pflicht-Metriken haben Quelle, Formel, Zielwert und Alarm-Schwelle dokumentiert
- Verteilungs-Klarheit: Für jeden Empfänger sind Kanal, Format und Zeitpunkt definiert
- Erster Report erstellt: Mindestens ein ausgefüllter Weekly-Report als Referenz-Beispiel vorhanden
- Failure-Indikator: Wenn für mehr als 2 der 5 Pflicht-Metriken die Datenquellen nicht verfügbar sind → Skill gibt aus: "Datenquellen für >2 Pflicht-Metriken nicht verfügbar — Reporting-System nicht operationsfähig. Bitte Metriken-Auswahl oder Datenquellen-Zugang prüfen."
- Akzeptanzkriterium: Zwei ausgefüllte Templates (Weekly + Monthly), Verteilungs-Matrix, Archivierungs-Konvention und 1-seitige Anleitung — alles sofort einsatzbereit

## Abhängigkeiten

- Input: Liste der wichtigsten Geschäftsziele und Zugang zu mindestens 3 der 5 gewählten Datenquellen
- Empfohlene Vorgänger-Skills: /elvis-performance-tracker (liefert 10 Metriken als Auswahlpool für die 5 Pflicht-Metriken), /elvis-kpi-dashboard (liefert strategische KPIs als Basis für monatliche Ziel-Erreichungs-Messung)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) 5 Pflicht-Metriken-Steckbriefe (Quelle, Formel, Zielwert, Alarm-Schwelle), (2) Weekly-Report-Template (Copy-Paste-fertig, 5 Abschnitte), (3) Monthly-Report-Template (Copy-Paste-fertig, 6 Abschnitte), (4) Verteilungs-Matrix (Empfänger × Kanal × Zeitpunkt), (5) Archivierungs-Anleitung mit Dateinamens-Konvention und Index-Template. Erster ausgefüllter Weekly-Report als Referenz-Beispiel beigefügt.
