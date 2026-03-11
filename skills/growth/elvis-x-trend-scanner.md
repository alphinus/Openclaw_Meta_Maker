# Skill

## Name

/elvis-x-trend-scanner

## Beschreibung

Scannt Nischen-Trends auf X/Twitter der letzten 48 Stunden. Identifiziert die meistdiskutierten Themen anhand von 10 vordefinierten Nischen-Keywords, bewertet Relevanz und Momentum, und liefert einen priorisierten Top-10 Trend-Report — fertig in einer einzigen Scan-Session.

## Ziele

- 10 Nischen-Keywords definiert und dokumentiert (Ausgangsbasis für den Scan)
- Top-20 Posts pro Keyword aus dem 48-Stunden-Zeitfenster abgerufen und ausgewertet
- Top-10 Trend-Themen aus Keyword-Überschneidungen extrahiert, sortiert nach Relevanz-Score
- Relevanz-Score 1–5 für jedes Trend-Thema vergeben (5 = höchste Relevanz)
- Markdown-Tabelle mit 4 Spalten: Rang, Trend-Thema, Score, Keyword-Überschneidungen

## Strategie

Der Skill priorisiert Überschneidungs-Signale: ein Thema, das in 4 von 10 Keywords auftaucht, ist relevanter als ein viraler Einzelpost. Relevanz-Score wird aus drei Faktoren berechnet — Keyword-Abdeckung (wie viele Keywords), Posting-Volumen (wie viele Posts), Aktualität (< 12h vs. 12–48h). Der Report ist bewusst knapp gehalten: 10 Themen, kein Rauschen.

## Einschränkungen

- Max. 10 Nischen-Keywords pro Scan-Durchlauf
- Max. 48 Stunden Zeitfenster — keine Trends älter als 2 Tage
- Max. 20 Posts pro Keyword abrufen (200 Posts gesamt als Datenbasis)
- Keine automatischen Post-Aktionen — reine Lese-Operation
- Nur öffentlich sichtbare Posts auswerten

## Ausführungsschritte

1. Definiere 10 Nischen-Keywords passend zur Zielgruppe des Accounts. Pro Keyword: Haupt-Begriff (1–3 Wörter), eine kurze Begründung (1 Satz warum relevant). Dokumentiere die 10 Keywords in einer nummerierten Liste als Scan-Grundlage.
2. Rufe für jedes der 10 Keywords die Top-20 Posts der letzten 48 Stunden ab (nach Engagement sortiert). Erfasse pro Post: Post-Text (Vorschau 60 Zeichen), Datum/Uhrzeit, Impressionen, Likes + Reposts (kombiniert), zugehöriges Keyword. Fehlende Impressionswerte als 0 markieren.
3. Extrahiere übergreifende Trend-Themen aus den 200 Posts (20 × 10 Keywords): Suche nach Themen-Clustern, die in mindestens 2 verschiedenen Keywords vorkommen. Bilde maximal 15 Themen-Cluster als Zwischenergebnis. Notiere pro Cluster: Thema-Label (3–5 Wörter), beteiligte Keywords (Liste), Anzahl Posts im Cluster.
4. Vergib Relevanz-Score 1–5 für jedes Themen-Cluster nach diesem Schlüssel: 5 = ≥5 Keywords + hohe Post-Dichte (>20 Posts); 4 = 3–4 Keywords oder hohe Post-Dichte; 3 = 2 Keywords + moderate Post-Dichte (10–20 Posts); 2 = 2 Keywords + geringe Post-Dichte (<10 Posts); 1 = Einzel-Keyword, schwaches Signal. Begründe jeden Score in einem Halbsatz.
5. Wähle die Top-10 Trend-Themen nach Relevanz-Score aus (bei Gleichstand: höhere Post-Zahl gewinnt). Erstelle den finalen Trend-Report als Markdown-Tabelle mit 4 Spalten: Rang (1–10), Trend-Thema, Score (1–5), Keyword-Abdeckung (Anzahl beteiligte Keywords / 10).

## Verifikation

- Vollständigkeit: Report enthält genau 10 Trend-Themen in der Tabelle
- Score-Verteilung: Mindestens 3 Themen mit Score ≥3 — andernfalls ist die Nische zu fragmentiert
- Failure-Indikator: Weniger als 3 Themen mit Score ≥3 → Skill gibt Meldung aus: "Trend-Signal schwach — weniger als 3 relevante Themen gefunden. Nischen-Keywords überprüfen oder Zeitfenster auf 72h erweitern."
- Datenintegrität: Jede Keyword-Abdeckung in der Tabelle ist aus den 10 definierten Keywords nachvollziehbar
- Akzeptanzkriterium: Tabelle vollständig (10 Zeilen, 4 Spalten), alle Scores begründet, kein Thema ohne Keyword-Referenz

## Abhängigkeiten

- Input: Zugang zu X/Twitter-Suche oder Analytics (öffentliche Timeline-Daten der letzten 48 Stunden) sowie eine Liste von 5–10 Nischen-Keywords als Eingabe vom Operator
- Empfohlene Vorgänger-Skills: elvis-market-scan (für Keyword-Grundlage), oder direkte Operator-Eingabe

## Output

Markdown-Tabelle (4 Spalten: Rang, Trend-Thema, Score 1–5, Keyword-Abdeckung) mit Top-10 Trend-Themen der letzten 48 Stunden. Ergänzt durch die 10 Keyword-Definitionen als Dokumentations-Block und Score-Begründungen als kurze Fußnoten-Liste. Gesamtlänge: max. 400 Wörter.
