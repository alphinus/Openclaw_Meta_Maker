# Skill

## Name

/elvis-competitor-monitor

## Beschreibung

Richtet ein fortlaufendes Konkurrenz-Monitoring-System ein: 5 Konkurrenz-Accounts werden wöchentlich auf 4 Kern-Metriken überwacht, mit automatischen Alarm-Triggern bei signifikanten Abweichungen und monatlichem Benchmark-Vergleich. Abgrenzung zu bestehenden Skills: `elvis-competitor-analysis` (S04) ist ein einmaliger 4-Wochen-Scan von 5 Accounts × 5 Metriken als Snapshot. `elvis-competitor-deep-dive` (S05) ist eine qualitative 12-Wochen-Tiefenanalyse eines einzelnen Accounts. Dieser Skill dagegen baut ein dauerhaftes Monitoring-System auf, das Woche für Woche die Konkurrenz trackt und bei kritischen Veränderungen (z.B. 20 % Follower-Sprung in einer Woche) proaktiv alarmiert.

## Ziele

- Definiertes Monitoring-System für 5 Konkurrenz-Accounts mit wöchentlicher Mess-Cadence
- 4 Kern-Metriken pro Account: Follower-Anzahl, durchschnittliche Engagement-Rate, Posting-Frequenz, Top-Content-Format
- Wöchentlicher Alarm-Trigger: Automatische Meldung bei >20 % Abweichung in einer Kern-Metrik gegenüber Vorwoche
- Monatlicher Benchmark-Report: Wie schneidet der eigene Account im Vergleich zum Konkurrenz-Durchschnitt ab?
- 12-Wochen-Trend-Visualisierung: Entwicklung der 4 Metriken pro Konkurrent als Verlaufskurve

## Strategie

Das Monitoring-System setzt auf Frühwarnung statt Nachlauf: Wer die Konkurrenz nur alle paar Monate prüft, verpasst plötzliche Veränderungen (neue Content-Strategie, viraler Post, Kollaboration). Die wöchentliche Cadence identifiziert Trendwenden früh. Die Alarm-Trigger sind bewusst auf signifikante Veränderungen kalibriert (>20 %) — tägliche Schwankungen sollen nicht alarmieren. Das System trackt nicht nur Zahlen, sondern auch qualitative Muster (Top-Content-Format), weil Strategie-Wechsel oft wichtiger sind als Metriken-Sprünge.

## Einschränkungen

- Exakt 5 Konkurrenz-Accounts im fortlaufenden Monitoring — bei mehr verliert das System Fokus
- Nur Accounts monitoren die konsistent trackbar sind (öffentliche Profile, keine Privat-Accounts)
- 4 Kern-Metriken pro Account — mehr Metriken erhöhen Aufwand ohne proportional mehr Erkenntnisse
- Alarm-Trigger erst ab Woche 3 aktiv (erste 2 Wochen dienen Baseline-Erhebung ohne False-Alarm-Rauschen)
- Wöchentliche Messung an festem Wochentag (z.B. jeden Montag) — Konsistenz ist Pflicht für valide Trends

## Ausführungsschritte

1. Identifiziere die 5 relevantesten Konkurrenz-Accounts gemeinsam mit dem Operator: Wer sind die direkten Konkurrenten in derselben Nische mit ähnlicher Zielgruppe? Dokumentiere für jeden Account: Handle, Plattform (X/Twitter / Instagram / LinkedIn), Begründung für Auswahl (warum ist dieser Account relevant?), aktuelle Follower-Anzahl (als Baseline-Referenz).
2. Definiere die 4 Kern-Metriken die wöchentlich getrackt werden: (A) Follower-Anzahl: Gesamtzahl Follower am Mess-Tag. (B) Durchschnittliche Engagement-Rate: `(Likes + Kommentare + Reposts) / Impressionen × 100`, Durchschnitt über alle Posts der letzten 7 Tage. (C) Posting-Frequenz: Anzahl Posts in den letzten 7 Tagen. (D) Top-Content-Format: Welches Format dominiert? (Text-Thread / Video / Bild / Poll). Dokumentiere für jede Metrik die Datenquelle und den Mess-Klickpfad.
3. Erhebe die Baseline-Werte für alle 5 Accounts × 4 Metriken in Woche 1 und Woche 2: Die ersten 2 Wochen dienen als Referenz-Zeitraum für spätere Alarm-Trigger. Berechne den Durchschnittswert jeder Metrik über beide Wochen als Baseline. Erstelle eine Baseline-Tabelle: Account | Follower (Ø) | Engagement-Rate (Ø) | Posting-Frequenz (Ø) | Haupt-Format.
4. Erstelle die wöchentliche Monitoring-Tabelle mit 21 Spalten: Woche | Datum | Account 1: Follower | Δ Follower (%) | Engagement | Δ Engagement (pp) | Posts | Format | Alarm | ... (wiederholt für Account 2–5). Befülle Woche 1 und Woche 2 mit Baseline-Daten.
5. Definiere die Alarm-Trigger-Logik (aktiv ab Woche 3): 🔴 Roter Alarm = >20 % Abweichung in Follower ODER >5 Prozentpunkte Abweichung in Engagement-Rate gegenüber Vorwoche. 🟡 Gelber Alarm = 10–20 % Abweichung in Follower ODER 3–5 pp Abweichung in Engagement. 🟢 Kein Alarm = Veränderungen im normalen Bereich (<10 % / <3 pp). Bei 🔴: Automatisch Alarm-Text generieren: "Account [Handle]: [Metrik] um [X %] gestiegen/gefallen — mögliche Ursache: [Hypothese basierend auf Content-Analyse der letzten Woche]."
6. Erstelle den monatlichen Benchmark-Report-Prozess: Am Ende jedes Monats (alle 4 Wochen) wird der eigene Account gegen den Konkurrenz-Durchschnitt verglichen. Berechne für jede der 4 Metriken: (A) Eigene Position im Ranking (1–6, wobei 1 = beste Performance). (B) Abstand zum Konkurrenz-Durchschnitt in % bzw. Prozentpunkten. (C) Trend-Richtung: Verbessert oder verschlechtert sich die relative Position? Template: "Eigener Account: Follower-Wachstum Rank 3/6 (−15 % unter Konkurrenz-Ø), Engagement-Rate Rank 2/6 (+8 pp über Konkurrenz-Ø)."
7. Schreibe die wöchentliche Monitoring-Anleitung (max. 10 Schritte): Wann messen (Wochentag + Uhrzeit), wo die Daten für jeden Account abrufen (Klickpfad), wie Δ-Werte berechnen (`(Aktuell − Vorwoche) / Vorwoche × 100`), wie Alarm-Status setzen (🟢/🟡/🔴), was bei 🔴-Alarm tun (Content der letzten Woche analysieren). Füge Kalender-Erinnerungs-Template bei.

## Verifikation

- Alle 5 Accounts definiert: Handle, Plattform, Begründung, Baseline-Follower dokumentiert
- Baseline vorhanden: Alle 5 Accounts × 4 Metriken mit 2-Wochen-Baseline-Durchschnitt
- Monitoring-Tabelle: 12 Wochen-Zeilen angelegt (Woche 1+2 befüllt, Wochen 3–12 als Platzhalter)
- Alarm-Logik: Schwellen für 🟢/🟡/🔴 explizit definiert (% und Prozentpunkte)
- Failure-Indikator: Wenn weniger als 3 der 5 Accounts konsistent trackbar sind (z.B. Privat-Accounts / gelöschte Profile / keine Analytics-Daten verfügbar) → Skill gibt aus: "Weniger als 3 der 5 Accounts konsistent trackbar — Monitoring-System nicht operationsfähig. Bitte Accounts ersetzen durch öffentlich trackbare Alternative-Konkurrenten."
- Akzeptanzkriterium: Befüllte Monitoring-Tabelle (2 Wochen Baseline), Alarm-Trigger-Logik, monatlicher Benchmark-Report-Prozess und wöchentliche Monitoring-Anleitung

## Abhängigkeiten

- Input: Liste der 5 relevantesten Konkurrenz-Accounts und Zugang zu deren öffentlichen Profil-Daten (X Analytics / Social Blade / manuelle Erhebung)
- Empfohlene Vorgänger-Skills: /elvis-competitor-analysis (identifiziert die relevantesten 5 Accounts für das Monitoring), /elvis-performance-tracker (liefert Tracking-Framework-Muster)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) 5 Konkurrenz-Account-Steckbriefe (Handle, Plattform, Begründung, Baseline-Werte), (2) Wöchentliche Monitoring-Tabelle (21 Spalten × 12 Wochen, Woche 1+2 mit Baseline befüllt), (3) Alarm-Trigger-System (Schwellen-Definition, Alarm-Text-Template), (4) Monatlicher Benchmark-Report-Prozess (Ranking-Berechnung, Trend-Richtung), (5) Wöchentliche Monitoring-Anleitung. Sofort einsatzbereit als fortlaufendes Konkurrenz-Frühwarnsystem.
