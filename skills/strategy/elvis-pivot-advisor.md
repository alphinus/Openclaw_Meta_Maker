# Skill

## Name

/elvis-pivot-advisor

## Beschreibung

Bewertet systematisch ob ein Pivot sinnvoll ist: identifiziert 5 messbare Pivot-Signale, analysiert 3 Pivot-Optionen (Zielgruppe / Angebot / Kanal-Pivot), schätzt die Pivot-Kosten (Zeit in Wochen + Ressourcen) und definiert Go/No-Go-Kriterien (3 Bedingungen). Verhindert vorschnelle Pivots aus Ungeduld und verschleppte Pivots aus Angst.

## Ziele

- 5 messbare Pivot-Signale identifiziert (Metriken mit Schwellenwerten die einen Pivot anzeigen)
- 3 Pivot-Optionen analysiert: Zielgruppen-Pivot, Angebots-Pivot, Kanal-Pivot
- Pivot-Kosten-Abschätzung für jede Option (Zeit in Wochen + Ressourcen-Aufwand)
- Go/No-Go-Entscheidung: 3 definierte Bedingungen die erfüllt sein müssen für einen Pivot
- Empfehlung: Pivot (welche Option) / Kein Pivot / Mehr Daten sammeln — mit Begründung

## Strategie

Der Pivot-Advisor arbeitet in zwei Phasen: Diagnose (Signale + Optionen) und Entscheidung (Go/No-Go). Signale allein rechtfertigen keinen Pivot — erst wenn die Go/No-Go-Kriterien erfüllt sind, ist ein Pivot angemessen. Die 3 Pivot-Optionen (Zielgruppe / Angebot / Kanal) werden strukturiert bewertet, nicht intuitiv — jede Option bekommt eine Kosten-Nutzen-Schätzung. Eine "Mehr Daten sammeln"-Empfehlung ist ein legitimes Ergebnis wenn die Signallage unklar ist.

## Einschränkungen

- Genau 5 Pivot-Signale (Metriken mit konkreten Schwellenwerten — keine qualitativen Signale ohne Zahl)
- Genau 3 Pivot-Optionen analysieren (Zielgruppe / Angebot / Kanal — keine anderen Kategorien)
- Pivot-Kosten: Zeit in Wochen (Ganzzahl) und Ressourcen-Aufwand (niedrig/mittel/hoch mit 1-Satz-Begründung)
- Go/No-Go-Kriterien: genau 3, messbar formuliert, alle 3 müssen gleichzeitig erfüllt sein
- Empfehlung muss eine der 3 Optionen benennen wenn Pivot empfohlen — kein "irgendwie pivoten"

## Ausführungsschritte

1. Erfasse den aktuellen Stand: Dokumentiere das bisherige Modell (Zielgruppe, Angebot, Hauptkanal) in je 1 Satz. Notiere die aktuellen Werte der 3 wichtigsten Performance-Metriken (z.B. Follower-Wachstum/Woche, Engagement-Rate, Conversion-Rate oder Umsatz). Diese Baseline ist Referenz für die Pivot-Signal-Bewertung.
2. Identifiziere 5 Pivot-Signale: Messbare Metriken die bei Unterschreitung/Überschreitung auf einen nötigen Pivot hinweisen. Format je Signal: "Signal [N]: [Metrik] [unter/über] [Schwellenwert] über [Zeitraum] = Pivot-Warnung." Beispiel: "Signal 1: Follower-Wachstum unter 1 % pro Woche über 6 aufeinanderfolgende Wochen = Pivot-Warnung." Prüfe welche Signale aktuell aktiv sind (✓ aktiv / ✗ nicht aktiv).
3. Analysiere 3 Pivot-Optionen: Option A — Zielgruppen-Pivot: Selbes Angebot, neues Segment. Welches alternative Segment und warum? Option B — Angebots-Pivot: Selbe Zielgruppe, anderes Angebot (Format, Preis oder Nutzenversprechen ändern). Was genau ändert sich? Option C — Kanal-Pivot: Selbe Zielgruppe + selbes Angebot, anderen Distributions-Kanal. Welcher Kanal und warum? Je Option: 2–3 Sätze Begründung + Potenzial-Schätzung (niedrig/mittel/hoch).
4. Schätze die Pivot-Kosten für jede Option: Option A / B / C je: Zeit in Wochen bis erste Ergebnisse sichtbar, Ressourcen-Aufwand (niedrig = <5h/Woche, mittel = 5–15h/Woche, hoch = >15h/Woche), Haupt-Risiko (1 Satz). Erstelle Kosten-Vergleichs-Tabelle: 3 Spalten (Zeit / Ressourcen / Risiko) × 3 Optionen.
5. Definiere 3 Go/No-Go-Kriterien: Bedingungen die alle gleichzeitig erfüllt sein müssen damit ein Pivot gerechtfertigt ist. Format: "Bedingung [N]: [Messbare Beschreibung]." Beispiel: "Bedingung 1: Mindestens 3 der 5 Pivot-Signale sind aktiv." Bedingungen sollen sicherstellen dass Signale konsistent sind (nicht zufällig), Ressourcen für den Pivot vorhanden sind und mindestens 1 Pivot-Option ein klares Potenzial-Signal hat.
6. Formuliere die Empfehlung: "Pivot (Option X)" oder "Kein Pivot" oder "Mehr Daten sammeln (Zeitraum: N Wochen)". Begründung in 3 Sätzen: (1) Anzahl aktiver Signale (N von 5), (2) erfüllte Go/No-Go-Kriterien (N von 3) und (3) empfohlene Option mit wichtigstem Argument. Ergänze den konkreten nächsten Schritt (1 Aktion mit Zeitrahmen).

## Verifikation

- Pivot-Signale: 5 Signale mit Metrik, Schwellenwert und Zeitraum, jedes mit aktivem Status markiert
- Optionen-Analyse: Alle 3 Pivot-Optionen (Zielgruppe / Angebot / Kanal) bewertet mit Potenzial-Schätzung
- Kosten-Tabelle: 3 × 3 Matrix (Optionen × Zeit/Ressourcen/Risiko) vollständig ausgefüllt
- Empfehlung: Eine von 3 Optionen benannt (falls Pivot), Begründung enthält Anzahl aktiver Signale
- Failure-Indikator: Wenn keine Go/No-Go-Kriterien definiert sind → Skill gibt aus: "Pivot-Entscheidung nicht möglich: 3 messbare Go/No-Go-Kriterien sind Pflicht. Ohne definierte Kriterien wird jede Empfehlung zur Spekulation."

## Abhängigkeiten

- Input: Aktuelles Modell (Zielgruppe, Angebot, Kanal), aktuelle Werte von 2–3 Performance-Metriken
- Empfohlene Vorgänger-Skills: /elvis-risk-assessment (Risiko-Kontext für Go/No-Go), /elvis-growth-strategy (Wachstumsziele als Referenz für Signalwertung)

## Output

5 Pivot-Signale (mit Aktivitäts-Status), 3 Pivot-Optionen mit Potenzial-Schätzung, Kosten-Vergleichs-Tabelle (3×3), Go/No-Go-Kriterien (3 Bedingungen), Pivot-Empfehlung (Pivot/Kein Pivot/Mehr Daten + Begründung + nächster Schritt). Gesamtlänge: max. 800 Wörter.
