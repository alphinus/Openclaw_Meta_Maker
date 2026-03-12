# Skill

## Name

/elvis-performance-tracker

## Beschreibung

Baut ein fortlaufendes Performance-Tracking-System mit 10 Kern-Metriken und wöchentlicher Mess-Cadence auf. Im Gegensatz zu `elvis-growth-audit` (einmaliger Snapshot) liefert dieser Skill ein dauerhaftes Mess-System: Er definiert Metriken, Mess-Zeitpunkte, Datenquellen und ein Visualisierungsformat für Trend-Vergleiche über mehrere Wochen. Das Ergebnis ist ein wöchentlich wiederverwendbares Tracking-Dashboard.

## Ziele

- Definiertes Mess-System mit exakt 10 Kern-Metriken (je mit Quelle, Formel und Zielwert)
- Festgelegte wöchentliche Mess-Cadence mit konkreten Erhebungszeitpunkten (Wochentag + Uhrzeit)
- Trend-Visualisierungsformat: 4-Wochen-Verlauf pro Metrik in einer Vergleichstabelle
- Ampel-System (🟢 / 🟡 / 🔴) für sofortige Status-Einschätzung je Metrik
- Dokumentierter Baseline-Wert für alle 10 Metriken als Referenz für Trend-Vergleiche

## Strategie

Das System priorisiert Konsistenz über Vollständigkeit — 10 konsequent gemessene Metriken liefern mehr Erkenntnisse als 30 sporadisch erhobene. Die wöchentliche Cadence ist bewusst gewählt: täglich erzeugt Rauschen, monatlich ist zu langsam für Kursanpassungen. Das Ampel-System übersetzt Rohdaten sofort in Handlungsbedarf: 🔴 signalisiert sofortigen Handlungsbedarf, 🟡 erfordert Beobachtung, 🟢 bestätigt den Kurs. Baseline-Werte werden in Woche 1 erhoben und dienen dauerhaft als Vergleichsanker.

## Einschränkungen

- Exakt 10 Kern-Metriken pro Tracking-System — nicht mehr, nicht weniger (Fokus-Disziplin)
- Nur Metriken die wöchentlich messbar sind (keine Metriken die monatliche Datenquellen erfordern)
- Keine automatischen Datenerhebungen — der Skill definiert das System, der Operator führt die Messung durch
- Keine Metriken von Drittanbieter-Plattformen ohne explizite Freigabe durch den Operator
- Max. 4 Wochen rückwirkende Daten im Dashboard — ältere Perioden in Archiv-Tab auslagern

## Ausführungsschritte

1. Ermittle gemeinsam mit dem Operator die wichtigsten Geschäftsbereiche (max. 3 Bereiche, z.B. Content, Wachstum, Monetarisierung). Erfasse für jeden Bereich die 3–4 relevantesten Kennzahlen. Reduziere auf exakt 10 Kern-Metriken durch Priorisierung: Welche 10 Metriken würden bei Verschlechterung sofort zum Handeln zwingen?
2. Dokumentiere jede der 10 Metriken in einem standardisierten Metrik-Steckbrief: Name (kurz, verständlich), Bereich (Content / Wachstum / Monetarisierung), Formel oder Messmethode (z.B. "Likes + Reposts / Impressionen × 100"), Datenquelle (wo wird die Zahl abgelesen?), Zielwert (was ist der angestrebte Wert?), Alarm-Schwelle (ab wann 🔴?).
3. Lege die wöchentliche Mess-Cadence fest: Wähle einen festen Wochentag und eine Uhrzeit für die Erhebung (Empfehlung: Montag 09:00 Uhr für die Vorwoche). Dokumentiere für jede Metrik den genauen Erhebungsweg (Klickpfad in der jeweiligen Plattform oder Export-Dateiname). Ziel: Die komplette Messung dauert max. 20 Minuten.
4. Erhebe die Baseline-Werte für alle 10 Metriken in der aktuellen Woche. Erstelle eine Baseline-Tabelle mit 3 Spalten: Metrik-Name, Baseline-Wert (Datum), Zielwert. Diese Tabelle ist unveränderlich — sie dient dauerhaft als Vergleichsanker.
5. Erstelle das Tracking-Dashboard als Markdown-Tabelle mit 7 Spalten: Metrik, Zielwert, Woche 1, Woche 2, Woche 3, Woche 4, Status (🟢/🟡/🔴). Fülle die aktuelle Woche als erste Datenpunkt-Zeile ein. Leere Wochen werden als "—" eingetragen.
6. Definiere die Ampel-Logik für jede Metrik: 🟢 = Zielwert erreicht oder übertroffen, 🟡 = 80–99 % des Zielwerts, 🔴 = unter 80 % des Zielwerts oder unter Alarm-Schwelle. Dokumentiere diese Logik als Kommentar in der Tabellen-Fußzeile.
7. Schreibe eine Kurzanleitung (max. 10 Sätze) für die wöchentliche Aktualisierung: Wann messen, wo die Daten abrufen, wie die Tabelle befüllen, wie den Status aktualisieren. Füge einen Erinnerungs-Template-Text für Kalender-Einladung bei (Betreff + 3-Zeilen-Beschreibung).

## Verifikation

- Vollständigkeit: Exakt 10 Metriken mit ausgefülltem Steckbrief (alle 6 Felder pro Metrik)
- Messbarkeit: Alle 10 Metriken haben eine konkrete Datenquelle (keine abstrakten "Gefühl"-Metriken)
- Baseline vorhanden: Alle 10 Metriken haben einen gemessenen Baseline-Wert mit Datum
- Ampel-Logik: Jede Metrik hat definierte 🟢/🟡/🔴-Schwellen
- Failure-Indikator: Wenn weniger als 5 der 10 Metriken wöchentlich messbar sind → Skill gibt aus: "Weniger als 5 Metriken messbar — Tracking-System nicht operationsfähig. Bitte Datenquellen prüfen oder Metriken anpassen."
- Akzeptanzkriterium: Tracking-Dashboard mit Baseline-Werten, vollständige Mess-Anleitung, Ampel-System für alle 10 Metriken

## Abhängigkeiten

- Input: Liste der wichtigsten Geschäftsbereiche und Zugang zu mindestens einer Analytics-Plattform (z.B. X Analytics, Google Analytics, Stripe Dashboard)
- Empfohlene Vorgänger-Skills: /elvis-growth-audit (liefert ersten Überblick über messbare Metriken), /elvis-kpi-dashboard (definiert Zielwerte für die Ampel-Logik)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) 10 Metrik-Steckbriefe (Name, Formel, Quelle, Zielwert, Alarm-Schwelle), (2) Tracking-Dashboard-Tabelle (7 Spalten × 10 Zeilen, Baseline-Woche befüllt), (3) Mess-Anleitung für wöchentliche Aktualisierung (max. 10 Sätze + Klickpfade), (4) Kalender-Erinnerungs-Template. Sofort einsatzbereit als wöchentliches Ritual-Dokument.
