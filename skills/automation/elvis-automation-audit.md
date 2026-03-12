# Skill

## Name

/elvis-automation-audit

## Beschreibung

Scannt systematisch alle Geschäftsprozesse auf Automatisierungspotenzial und bewertet jeden Prozess mit einem 5-Kriterien-Score (Häufigkeit, Volumen, Fehleranfälligkeit, Regelbasiert, Zeitaufwand — je 1-5 Punkte, Max 25). Liefert eine priorisierte Liste von mindestens 5 Prozessen mit Score >10 als Automatisierungs-Roadmap für die nächsten 3 Monate.

## Ziele

- Identifizierte mindestens 10 Prozesse mit dokumentiertem 5-Kriterien-Score (je 1-25 Punkte)
- Priorisierte Roadmap: mindestens 5 Prozesse mit Score >10, sortiert nach Gesamt-Score absteigend
- Jeder Prozess mit Zeit-Ersparnis-Schätzung (Stunden pro Woche) und ROI-Zeitraum (Wochen bis Break-Even)
- Konkrete nächste Schritte für die Top-3 Prozesse: jeweils empfohlener Automatisierungs-Ansatz (Tool-Kategorie und grober Workflow-Typ)

## Strategie

Der Skill nutzt ein objektives Bewertungssystem statt Bauchgefühl: Jedes der 5 Kriterien wird unabhängig bewertet, die Summe ist die Automatisierungs-Priorität. Häufigkeit + Volumen identifizieren Skalierungs-Potenzial (viele Wiederholungen), Fehleranfälligkeit + Regelbasiert identifizieren Qualitäts-Verbesserung (weniger menschliche Fehler), Zeitaufwand identifiziert Kosten-Reduktion. Prozesse unter Score 10 sind "Parking Lot" — nicht automatisierungs-würdig oder zu komplex. Der Audit ist die Entscheidungsgrundlage, nicht die Implementierung.

## Einschränkungen

- Min. 10 Prozesse erfassen — weniger ist nicht aussagekräftig für Priorisierung
- Jeder Prozess muss alle 5 Kriterien bewertet haben — keine Lücken in der Scoring-Matrix
- Nur Prozesse aufnehmen die messbar sind (Häufigkeit zählbar, Zeitaufwand schätzbar) — keine abstrakten Tätigkeiten wie "strategisches Denken"
- Keine Implementierungsdetails liefern — nur Prozess-Beschreibung und Automatisierungs-Ansatz (Tool-Kategorie)
- Automatisierung von Prozessen mit rechtlichen oder finanziellen Konsequenzen erfordert expliziten Freigabe-Schritt im Score-Kommentar

## Ausführungsschritte

1. Erfasse alle relevanten Prozesse: Bitte den Operator mindestens 10 Prozesse zu nennen die regelmäßig ausgeführt werden (täglich, wöchentlich, monatlich). Für jeden Prozess dokumentiere: Prozess-Name (max. 50 Zeichen), Kurzbeschreibung (1-2 Sätze), Häufigkeit (täglich/wöchentlich/monatlich), aktueller Zeitaufwand in Minuten pro Durchlauf.
2. Bewerte jeden Prozess mit dem 5-Kriterien-Score: Häufigkeit (1=monatlich, 3=wöchentlich, 5=täglich/mehrmals täglich); Volumen (1=1-5 Einheiten, 3=6-50 Einheiten, 5=>50 Einheiten pro Durchlauf); Fehleranfälligkeit (1=kaum Fehler, 3=gelegentlich Fehler, 5=häufig Fehler oder hohe Fehler-Kosten); Regelbasiert (1=viele Ausnahmen/Ermessensentscheidungen, 3=grob strukturiert, 5=vollständig regelbasiert ohne Ermessen); Zeitaufwand (1=<10 Min, 3=10-60 Min, 5=>60 Min pro Durchlauf). Berechne Gesamt-Score: Summe aller 5 Kriterien (Max 25 Punkte).
3. Erstelle die Scoring-Tabelle mit 8 Spalten: Prozess-Name, Häufigkeit (Pkt), Volumen (Pkt), Fehleranfälligkeit (Pkt), Regelbasiert (Pkt), Zeitaufwand (Pkt), Gesamt-Score, Zeitaufwand/Woche (Min). Berechne Zeitaufwand/Woche: Häufigkeit × Minuten pro Durchlauf. Sortiere die Tabelle absteigend nach Gesamt-Score.
4. Identifiziere die Top-5 Prozesse mit Score >10 als Automatisierungs-Roadmap. Für jeden der Top-5 schätze: Zeitersparnis nach Automatisierung (% des aktuellen Zeitaufwands — meistens 80-95%), Implementierungs-Aufwand (Einfach 1-4h / Mittel 1-3 Tage / Komplex >3 Tage), ROI-Zeitraum in Wochen (Implementierungs-Aufwand in Stunden / wöchentliche Zeitersparnis in Stunden).
5. Empfehle für die Top-3 Prozesse jeweils einen Automatisierungs-Ansatz: Tool-Kategorie (No-Code-Workflow / Zapier-Integration / Custom-Script / API-Integration), grober Workflow-Typ (z.B. "Zeit-basierter Trigger → Daten abrufen → in Tabelle eintragen → Slack-Benachrichtigung"), kritische Abhängigkeiten (z.B. "benötigt API-Zugang zu Tool X"). Keine Code-Implementierung — nur konzeptionelle Beschreibung in 2-3 Sätzen.

## Verifikation

- Vollständigkeit: Alle erfassten Prozesse (min. 10) haben alle 5 Kriterien-Scores dokumentiert, keine Lücken
- Scoring-Tabelle: Gesamt-Score ist korrekt berechnet (Summe der 5 Einzel-Scores), Sortierung absteigend
- Roadmap: Mindestens 5 Prozesse mit Score >10 identifiziert und mit ROI-Zeitraum dokumentiert
- Automatisierungs-Ansätze: Top-3 Prozesse haben jeweils Tool-Kategorie und Workflow-Typ dokumentiert
- Failure-Indikator: Wenn weniger als 5 Prozesse Score >10 haben → Meldung "Automatisierungs-Potenzial gering — nur [N] Prozesse mit Score >10. Empfehle Prozess-Optimierung vor Automatisierung oder Erfassung weiterer Prozesse."
- Akzeptanzkriterium: Scoring-Tabelle mit min. 10 Prozessen, min. 5 Prozesse mit Score >10 in Roadmap, ROI-Zeiträume berechnet, Top-3 mit Automatisierungs-Ansätzen dokumentiert

## Abhängigkeiten

- Input: Liste von mindestens 10 regelmäßigen Geschäftsprozessen (Name, Häufigkeit, grobe Zeitschätzung) — kann auch unstrukturiert sein, der Skill strukturiert sie
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für systematische Automatisierungs-Planung)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) Scoring-Tabelle (alle erfassten Prozesse, sortiert nach Gesamt-Score), (2) Automatisierungs-Roadmap (Top-5 Prozesse mit Score >10, ROI-Zeiträume), (3) Top-3 Empfehlungen (je Tool-Kategorie und Workflow-Typ), (4) Parking Lot (Prozesse mit Score ≤10 zur späteren Überprüfung). Einsatzbereit als Entscheidungsgrundlage für Automatisierungs-Investitionen.
