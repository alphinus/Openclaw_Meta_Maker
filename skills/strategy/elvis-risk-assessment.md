# Skill

## Name

/elvis-risk-assessment

## Beschreibung

Identifiziert und bewertet 10 Risiken für ein Creator-Business oder eine Wachstumsstrategie entlang von 3 Dimensionen (Eintrittswahrscheinlichkeit 1–5, Auswirkung 1–5, Erkennbarkeit 1–5), priorisiert die Top-3 kritischen Risiken und definiert je 1 Mitigation-Maßnahme mit Frühwarnsignal. Liefert eine strukturierte Risiko-Übersicht für strategische Entscheidungen.

## Ziele

- 10 identifizierte Risiken mit vollständiger 3-Dimensionen-Bewertung (je 1–5 Score)
- Risiko-Priorisierungs-Score: Eintrittswahrscheinlichkeit × Auswirkung × (6 − Erkennbarkeit) = RPS
- Top-3 kritische Risiken mit je 1 konkreten Mitigation-Maßnahme und 1 Frühwarnsignal
- Risiko-Heatmap: 2×2 Matrix (Wahrscheinlichkeit × Auswirkung) mit allen 10 Risiken

## Strategie

Risiko-Assessment nutzt das Prinzip der gewichteten Priorisierung: Nicht jedes Risiko verdient gleich viel Aufmerksamkeit. Der Risiko-Priorisierungs-Score (RPS) berücksichtigt neben Wahrscheinlichkeit und Auswirkung auch die Erkennbarkeit — ein Risiko das spät erkennbar ist, ist gefährlicher als eines das früh sichtbar wird. Frühwarnsignale machen den Plan aktionierbar: Man wartet nicht bis ein Risiko eintritt, sondern erkennt es im Entstehen.

## Einschränkungen

- Genau 10 Risiken — weniger ist zu wenig für einen vollständigen Risikoraum, mehr wird unübersichtlich
- Alle 3 Dimensionen müssen für jedes Risiko bewertet sein (kein leeres Feld)
- Score-Skala ist 1–5 für alle Dimensionen: 1 = niedrig/leicht erkennbar, 5 = hoch/schwer erkennbar
- Top-3 Mitigation-Maßnahmen müssen konkret und ausführbar sein (keine "mehr aufpassen"-Aussagen)
- Frühwarnsignal muss messbar oder beobachtbar sein (z.B. Metrik fällt unter Schwellenwert)

## Ausführungsschritte

1. Identifiziere 10 Risiken verteilt auf 5 Risiko-Kategorien: (1) Plattform-Risiken (2 Risiken: z.B. Algorithmus-Änderung, Account-Sperrung), (2) Markt-Risiken (2 Risiken: z.B. Nischen-Sättigung, neue Konkurrenz), (3) Ressourcen-Risiken (2 Risiken: z.B. Burn-out, Budget-Engpass), (4) Produkt-/Angebots-Risiken (2 Risiken: z.B. Angebots-Fehler, mangelnde Nachfrage), (5) Reputations-Risiken (2 Risiken: z.B. Shitstorm, Kontroverser Post). Für jedes Risiko: kurze Beschreibung (1 Satz), betroffener Bereich.
2. Bewerte jedes der 10 Risiken auf 3 Dimensionen: (A) Eintrittswahrscheinlichkeit (1=sehr unwahrscheinlich bis 5=sehr wahrscheinlich), (B) Auswirkung bei Eintreten (1=kaum spürbar bis 5=business-kritisch), (C) Erkennbarkeit (1=sofort sichtbar bis 5=kaum erkennbar bis zu spät). Erstelle eine Tabelle mit 7 Spalten: Rang | Risiko | Kategorie | Wahrscheinlichkeit | Auswirkung | Erkennbarkeit | RPS.
3. Berechne den Risiko-Priorisierungs-Score (RPS) für jedes Risiko: RPS = Eintrittswahrscheinlichkeit × Auswirkung × (6 − Erkennbarkeit). Maximaler RPS = 5 × 5 × 5 = 125. Sortiere die 10 Risiken absteigend nach RPS.
4. Erstelle die Risiko-Heatmap als 5×5-Matrix: Achse X = Auswirkung (1–5), Achse Y = Eintrittswahrscheinlichkeit (1–5). Trage alle 10 Risiken als [R1]–[R10] in die Matrix ein. Markiere den kritischen Bereich (Auswirkung ≥4 UND Wahrscheinlichkeit ≥3) als Hochrisiko-Zone.
5. Definiere für die Top-3 Risiken (höchster RPS) je 1 Mitigation-Maßnahme: Format: "Maßnahme: [konkrete Aktion]. Zeitpunkt: [Wann wird die Maßnahme ergriffen — präventiv vor Eintreten oder reaktiv nach Eintreten?]. Aufwand: [niedrig/mittel/hoch]. Verantwortlich: [Operator/Tool/Extern]."
6. Definiere für jedes Top-3-Risiko 1 Frühwarnsignal: Format: "Frühwarnsignal: Wenn [messbare oder beobachtbare Bedingung] eintritt, ist das ein Indikator für [Risiko]. Kontrollintervall: [täglich/wöchentlich/monatlich prüfen]."
7. Schreibe den vollständigen Risiko-Assessment-Report: Executive Summary (3 Sätze: Gesamtrisiko-Einschätzung), vollständige Risiko-Tabelle (10 Risiken, RPS-sortiert), Risiko-Heatmap, Top-3-Mitigation-Pläne mit Frühwarnsignalen, Gesamtempfehlung (1 Satz: Was ist die dringlichste Risiko-Priorität?). Max. 1.000 Wörter.

## Verifikation

- Risiko-Vollständigkeit: Genau 10 Risiken mit vollständiger 3-Dimensionen-Bewertung (alle 30 Score-Felder ausgefüllt)
- Kategorien-Abdeckung: Alle 5 Risiko-Kategorien vertreten (Plattform, Markt, Ressourcen, Produkt, Reputation)
- RPS-Berechnung: Alle 10 RPS-Werte rechnerisch korrekt (Wahrscheinlichkeit × Auswirkung × (6−Erkennbarkeit))
- Failure-Indikator: Wenn weniger als 5 Risiken mit vollständiger 3-Dimensionen-Bewertung vorliegen → "Risiko-Assessment unvollständig: Nur [N]/10 Risiken vollständig bewertet. Min. 5 vollständige Bewertungen erforderlich für valide Priorisierung."
- Akzeptanzkriterium: 10 Risiken vollständig bewertet, RPS berechnet und sortiert, Top-3 mit Mitigation + Frühwarnsignal

## Abhängigkeiten

- Input: Beschreibung der aktuellen Strategie, des Geschäftsmodells oder des zu bewertenden Vorhabens (3–5 Sätze)
- Empfohlene Vorgänger-Skills: /elvis-growth-strategy (liefert zu bewertenden Strategiekontext), /elvis-competitive-strategy (liefert Markt-Risiko-Kontext)

## Output

Markdown-Dokument (max. 1.000 Wörter) mit 5 Abschnitten: Executive Summary, Risiko-Tabelle (10 Risiken × 3 Dimensionen + RPS, sortiert), Risiko-Heatmap (5×5-Matrix), Top-3-Mitigation-Pläne mit Frühwarnsignalen, strategische Gesamtempfehlung.
