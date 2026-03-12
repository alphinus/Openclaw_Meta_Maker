# Skill

## Name

/elvis-funnel-analyzer

## Beschreibung

Analysiert den Konversions-Funnel fortlaufend durch 5 Funnel-Stufen mit monatlicher Mess-Cadence: Conversion-Rate je Stufe, Drop-Off-Punkte und priorisierte Optimierungsmaßnahmen. Der Skill wird monatlich wiederholt um Trend-Verläufe zu erkennen — ob Optimierungen greifen oder ob neue Drop-Off-Punkte entstehen. Das Ergebnis ist ein klares Bild welche Funnel-Stufe den größten Return-on-Effort für Optimierungen bietet.

## Ziele

- Dokumentierter Funnel mit exakt 5 Stufen, je mit Besucher-Anzahl und Conversion-Rate zur nächsten Stufe
- Identifizierte Top-3 Drop-Off-Punkte (Stufen mit dem größten absoluten und relativen Verlust)
- Optimierungs-Prioritätsliste: 3 Maßnahmen nach Hebel-Größe sortiert (Aufwand vs. erwarteter Conversion-Gewinn)
- Benchmark-Vergleich: Einschätzung ob jede Conversion-Rate im branchenüblichen Bereich liegt

## Strategie

Der Skill arbeitet top-down durch den Funnel — von Awareness bis Conversion — weil eine Optimierung am Anfang des Funnels alle nachgelagerten Stufen verstärkt. Die Priorisierung folgt dem Hebel-Prinzip: Ein Drop-Off von 60 % auf Stufe 2 ist wichtiger als ein Drop-Off von 20 % auf Stufe 4, selbst wenn die absoluten Zahlen kleiner sind. Benchmark-Vergleiche dienen als Orientierung, nicht als Ziel — ein Funnel der 50 % besser als Benchmark ist, trotzdem Optimierungspotenzial hat wenn absolute Zahlen niedrig sind.

## Einschränkungen

- Exakt 5 Funnel-Stufen analysieren — bei mehr Stufen die wichtigsten 5 auswählen (Übersichtlichkeit)
- Nur Stufen analysieren für die tatsächliche Daten vorliegen (keine Schätzungen ohne Datenbasis)
- Keine Optimierungsmaßnahmen für Stufen die <50 Besucher hatten (zu kleine Stichprobe für valide Schlüsse)
- Benchmark-Werte nur als Richtwerte verwenden — keine verbindlichen Industrie-Standards ohne Quellenangabe
- Max. 3 priorisierte Optimierungsmaßnahmen ausgeben (mehr verwässern den Fokus)

## Ausführungsschritte

1. Definiere gemeinsam mit dem Operator die 5 Funnel-Stufen. Typisches Beispiel: Stufe 1 (Awareness: Unique Visitors / Impressionen), Stufe 2 (Interest: Klicks / Profilbesuche), Stufe 3 (Consideration: Anmeldungen / Lead-Erfassung), Stufe 4 (Intent: Checkout-Starts / Demo-Anfragen), Stufe 5 (Conversion: Käufe / Abschlüsse). Passe die Stufen-Bezeichnungen an das tatsächliche Geschäftsmodell an.
2. Erhebe für jede der 5 Stufen: Absoluten Wert (Anzahl Besucher / Nutzer / Aktionen in der Stufe), Zeitraum (immer 30 Tage für Vergleichbarkeit). Erstelle eine Rohdaten-Tabelle mit 3 Spalten: Stufe, Bezeichnung, Absoluter Wert.
3. Berechne für jede Stufen-Übergabe die Conversion-Rate: Stufe N+1 / Stufe N × 100 = Conversion-Rate in %. Berechne zusätzlich den absoluten Drop-Off: Stufe N − Stufe N+1 = verlorene Nutzer. Erstelle eine erweiterte Funnel-Tabelle mit 5 Spalten: Stufe, Wert, Conversion-Rate → nächste Stufe, Drop-Off absolut, Drop-Off %.
4. Identifiziere die Top-3 Drop-Off-Punkte nach zwei Kriterien: Höchster Drop-Off % (relativer Verlust) und Höchster Drop-Off absolut (absoluter Verlust). Markiere in der Tabelle die Top-3 mit "⚠️ Priorität". Begründe die Priorisierung in je einem Satz.
5. Vergleiche jede Conversion-Rate mit Branchen-Richtwerten. Typische Benchmarks: Awareness→Interest: 2–5 %, Interest→Consideration: 10–30 %, Consideration→Intent: 5–15 %, Intent→Conversion: 20–50 %. Markiere jede Rate als "✓ im Bereich", "⚡ über Benchmark" oder "⚠️ unter Benchmark". Füge einen Hinweis ein wenn Benchmarks für die spezifische Branche variieren können.
6. Erstelle die Optimierungs-Prioritätsliste für die Top-3 Drop-Off-Punkte. Für jeden Punkt: Beschreibung des Problems (1 Satz), 2 konkrete Optimierungsmaßnahmen (je 1–2 Sätze), geschätzter Aufwand (Niedrig / Mittel / Hoch), erwarteter Conversion-Gewinn in Prozentpunkten (konservative Schätzung), Prioritäts-Score = Erwarteter Gewinn / Aufwand.
7. Schreibe eine Zusammenfassung (max. 150 Wörter): Wo ist der Funnel am stärksten? Wo am schwächsten? Welche eine Maßnahme hätte den größten Impact? Welches sind die Quick Wins (Niedrig-Aufwand + hoher Gewinn)?

## Verifikation

- Datenintegrität: Alle Conversion-Rates nachvollziehbar berechnet aus den Rohdaten (keine runden Schätzungen ohne Grundlage)
- Top-3 identifiziert: Drop-Off-Punkte nach % und absolut markiert mit Priorisierungs-Begründung
- Maßnahmen konkret: Jede Optimierungsmaßnahme benennt eine spezifische Aktion (kein "mehr testen" oder "verbessern")
- Benchmark-Vergleich: Alle 4 Übergänge bewertet (✓ / ⚡ / ⚠️)
- Failure-Indikator: Wenn weniger als 3 der 5 Funnel-Stufen mit echten Daten (nicht Schätzungen) befüllt werden können → Skill gibt aus: "Zu wenige messbare Funnel-Stufen (< 3 mit echten Daten) — Funnel-Analyse nicht valide. Bitte Tracking für fehlende Stufen einrichten."
- Akzeptanzkriterium: Funnel-Tabelle vollständig, Top-3 Drop-Off-Punkte identifiziert, 3 priorisierte Optimierungsmaßnahmen mit Aufwand-Gewinn-Einschätzung

## Abhängigkeiten

- Input: Zahlen für alle 5 Funnel-Stufen aus dem letzten 30-Tage-Zeitraum (z.B. aus Google Analytics, Stripe, E-Mail-Plattform)
- Empfohlene Vorgänger-Skills: /elvis-performance-tracker (liefert Baseline-Metriken für den Funnel), /elvis-growth-audit (identifiziert relevante Funnel-Stufen vorab)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) Funnel-Visualisierung als Tabelle (5 Stufen × Conversion-Rates × Drop-Off-Punkte × Benchmark-Status), (2) Top-3 Drop-Off-Analyse mit Priorisierungs-Begründung, (3) Optimierungs-Prioritätsliste (3 Maßnahmen × Aufwand + Gewinn-Schätzung + Prioritäts-Score), (4) Zusammenfassung mit Quick-Win-Empfehlung (max. 150 Wörter). Einsatzbereit als Briefing für Conversion-Optimierung.
