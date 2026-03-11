# Skill

## Name

/elvis-execution-plan

## Beschreibung

Entwickelt einen strukturierten 90-Tage-Wachstumsplan mit messbaren Zielen, priorisierten Taktiken nach Impact/Aufwand-Matrix und einem konkreten Aktionsplan für die ersten 30 Tage. Wandelt eine Wachstums-Ambition in ein ausführbares Dokument um das klar zeigt was wann zu tun ist.

## Ziele

- 3 messbare, zeitgebundene Wachstumsziele für die nächsten 90 Tage (Ziel, Metrik, Messmethode)
- Priorisierte Taktiken-Liste nach 2×2 Impact/Aufwand-Matrix (Quick Wins, Big Bets, Fill-ins, Vermeiden)
- Aktionsplan mit max. 10 Maßnahmen für die ersten 30 Tage, mit Verantwortlichkeit und Fälligkeitsdatum
- Risiko-Register mit 3 identifizierten Risiken und je einer Gegenmaßnahme

## Strategie

Der Skill arbeitet rückwärts: erst das 90-Tage-Ziel definieren, dann die Taktiken identifizieren die es erreichen, dann die ersten 30 Tage konkret planen. Die Impact/Aufwand-Matrix stellt sicher dass Quick Wins zuerst kommen — sie bauen Momentum auf und liefern frühzeitig Daten. Big Bets werden geplant aber erst nach Quick-Win-Validation gestartet. Alles in der "Vermeiden"-Kategorie wird explizit benannt um Energie-Verschwendung zu verhindern.

## Einschränkungen

- Max. 3 Wachstumsziele (mehr führt zu Fragmentierung und mangelnder Fokussierung)
- Aktionsplan enthält max. 10 Maßnahmen für 30 Tage (mehr ist nicht umsetzbar ohne dediziertes Team)
- Jede Maßnahme muss eine Verantwortlichkeit (Operator / Tool / Agentur / offen) und ein Fälligkeitsdatum haben
- Keine strategischen Ziele ohne messbare KPI — "besser werden" ist kein Ziel
- Keine Taktiken aufnehmen die mehr als 20 Stunden/Woche Aufwand erfordern ohne explizite Ressourcen-Bestätigung durch den Operator

## Ausführungsschritte

1. Kläre den Ausgangspunkt: Dokumentiere den aktuellen Ist-Stand in 5 Metriken (z.B. für X/Twitter: Follower, Posts/Woche, Durchschnitts-Engagement-Rate, monatliche Impressionen, Conversion-Rate wenn bekannt). Falls Daten fehlen, markiere sie als "unbekannt" und weise im Output darauf hin.
2. Definiere 3 Wachstumsziele für die nächsten 90 Tage. Jedes Ziel im Format: "Von [Ist-Wert] auf [Soll-Wert] in [Metrik] bis [konkretes Datum], gemessen über [Messmethode]." Mindestens 2 der 3 Ziele müssen quantifizierbare Metriken haben.
3. Sammle alle Taktiken die potenziell zu den 3 Zielen beitragen — mindestens 10, max. 20 Ideen. Für jede Taktik: kurze Beschreibung (1 Satz), geschätzter wöchentlicher Aufwand in Stunden (1h / 2–5h / 5–10h / >10h), erwarteter Impact (niedrig / mittel / hoch).
4. Ordne alle Taktiken in die 2×2 Impact/Aufwand-Matrix ein: Quick Wins (hoher Impact, niedriger Aufwand ≤2h/Woche), Big Bets (hoher Impact, hoher Aufwand >5h/Woche), Fill-ins (niedriger Impact, niedriger Aufwand), Vermeiden (niedriger Impact, hoher Aufwand). Erstelle die Matrix als Markdown-Tabelle mit 4 Spalten.
5. Wähle aus Quick Wins und Big Bets die Top-10 Maßnahmen für den 30-Tage-Aktionsplan. Reihenfolge: Quick Wins zuerst (Tage 1–14), dann erste Big-Bet-Vorbereitung (Tage 15–30). Für jede Maßnahme: Nummer, Beschreibung, Verantwortlichkeit (Operator / Extern / Tool), Fälligkeitsdatum (Tag X oder konkretes Datum), Erfolgsindikator.
6. Identifiziere 3 Risiken die den Plan gefährden könnten. Format: "Risiko: [Beschreibung]. Eintrittswahrscheinlichkeit: hoch/mittel/niedrig. Gegenmaßnahme: [konkrete Aktion wenn Risiko eintritt]."
7. Schreibe den vollständigen Execution-Plan im Markdown-Format mit 5 Abschnitten: (1) Ist-Stand (5 Metriken), (2) 3 Wachstumsziele (SMART-Format), (3) Impact/Aufwand-Matrix (alle Taktiken), (4) 30-Tage-Aktionsplan (Tabelle mit 10 Maßnahmen), (5) Risiko-Register (3 Risiken mit Gegenmaßnahmen). Gesamtlänge: max. 1.200 Wörter.

## Verifikation

- Ziele-Qualität: Alle 3 Ziele enthalten Ist-Wert, Soll-Wert, Metrik, Datum und Messmethode — kein einziges vages Ziel wie "mehr Reichweite"
- Aktionsplan-Vollständigkeit: Alle 10 Maßnahmen haben Verantwortlichkeit und Fälligkeitsdatum
- Matrix-Abdeckung: Alle 4 Quadranten der Impact/Aufwand-Matrix sind befüllt (mindestens 1 Eintrag pro Quadrant)
- Failure-Indikator: Wenn der Operator keine Ist-Metriken liefert und alle 5 als "unbekannt" markiert sind → Skill gibt Warnung aus: "Kritische Datenlücke: Ohne Ist-Werte ist der Plan Spekulation. Empfehle: /elvis-growth-audit zuerst ausführen."
- Akzeptanzkriterium: 3 SMART-Ziele, vollständige Matrix, 10 Maßnahmen mit Fälligkeitsdaten, 3 Risiken mit Gegenmaßnahmen

## Abhängigkeiten

- Input: Aktueller Ist-Stand (Metriken, auch "unbekannt" möglich) und übergeordnete Wachstums-Ambition (1–3 Sätze)
- Empfohlene Vorgänger-Skills: /elvis-growth-audit (liefert Ist-Metriken und Muster), /elvis-market-scan (liefert Marktkontext für Ziel-Kalibrierung)

## Output

Markdown-Dokument (max. 1.200 Wörter) mit 5 Abschnitten: Ist-Stand, 3 SMART-Wachstumsziele, Impact/Aufwand-Matrix, 30-Tage-Aktionsplan mit 10 Maßnahmen, Risiko-Register. Einsatzbereit als Arbeits- und Review-Dokument.
