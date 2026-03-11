# Skill

## Name

/elvis-prioritization-engine

## Beschreibung

Priorisiert Aufgaben, Projekte oder Ideen mithilfe des ICE-Scoring-Modells (Impact × Confidence × Ease, je 1–10). Bewertet mindestens 10 Items, identifiziert die Top-3 Prioritäten mit Begründung und erstellt einen 30-Tage-Fokus-Plan auf Basis der Spitzenprioritäten. Verwandelt unstrukturierte Backlogs in klare Handlungsreihenfolgen.

## Ziele

- Mindestens 10 Items vollständig mit ICE-Score bewertet (Impact × Confidence × Ease je 1–10)
- Rangliste aller Items nach Gesamt-ICE-Score (absteigend) erstellt
- Top-3 Prioritäten mit je einer 3-Satz-Begründung (Impact-Argument, Confidence-Argument, Ease-Argument) dokumentiert
- 30-Tage-Fokus-Plan mit max. 6 konkreten Aktionen auf Basis der Top-3 erstellt
- Deprioritisierungsliste: Bottom-3 Items mit Grund für das Ausklammern benannt

## Strategie

ICE-Scoring verhindert "lautes Bauchgefühl" — Ideen die viel diskutiert werden landen nicht automatisch oben, weil alle 3 Dimensionen gleichwertig zählen. Confidence (Umsetzbarkeits-Sicherheit) diszipliniert gegen Wishful Thinking: hoher Impact ohne Grundlage (Confidence < 4) fällt in der Rangliste ab. Der 30-Tage-Plan enthält bewusst max. 6 Aktionen — mehr ist nicht fokussiert, sondern ein weiterer Backlog.

## Einschränkungen

- Mindestens 10 Items bewerten (weniger macht ICE-Ranking bedeutungslos)
- ICE-Scores: ganzzahlig 1–10, keine halben Punkte
- Top-3 Fokus-Plan: max. 6 Aktionen in 30 Tagen (2 pro Top-Priorität)
- Jede Aktion im 30-Tage-Plan muss einen Zeitrahmen (Tage 1–10 / 11–20 / 21–30) und ein konkretes Deliverable haben
- Items mit Confidence-Score < 3 werden zwar bewertet, aber mit "(Niedrige Sicherheit — validieren zuerst)" markiert

## Ausführungsschritte

1. Sammle alle Items die priorisiert werden sollen (Aufgaben, Projekte, Ideen, Initiativen). Ziel: mindestens 10, maximal 20 Items. Falls weniger als 10 vorhanden, generiere ergänzende Items aus dem Kontext des Operators (benenne diese als "Vorschlag"). Dokumentiere alle Items als nummerierte Liste mit je 1-Satz-Beschreibung.
2. Bewerte jedes Item nach dem ICE-Framework: Impact (1–10): Wie stark beeinflusst dieses Item das Hauptziel wenn es erfolgreich umgesetzt wird? Confidence (1–10): Wie sicher bist du dass es diesen Impact hat? Ease (1–10): Wie einfach ist die Umsetzung relativ zum verfügbaren Aufwand? Dokumentiere als Tabelle: Item | Impact | Confidence | Ease | ICE-Score (I×C×E) | Markierung.
3. Erstelle die Rangliste: Sortiere alle Items nach ICE-Score absteigend. Berechne den Median-ICE-Score (Mittelpunkt der Liste). Items unterhalb des Medians mit "(Niedrige Priorität)" markieren, Items mit Confidence < 3 mit "(Validieren zuerst)" markieren.
4. Analysiere die Top-3 Items tiefergehend: Für jedes Top-3 Item formuliere eine 3-Satz-Begründung — Satz 1: Impact-Argument (welches Ziel wird wie stark bewegt?), Satz 2: Confidence-Argument (welche Evidenz oder Vorerfahrung stützt den Score?), Satz 3: Ease-Argument (welche bestehenden Ressourcen oder Vorarbeiten erleichtern die Umsetzung?).
5. Erstelle den 30-Tage-Fokus-Plan: Je Top-3 Item 2 konkrete Aktionen. Jede Aktion enthält: Aktionsbeschreibung (1 Satz), Zeitrahmen (Tage 1–10, 11–20 oder 21–30), Deliverable (was liegt am Ende vor?), Aufwand-Schätzung in Stunden. Gesamtlimit: 6 Aktionen in 30 Tagen.
6. Erstelle die Deprioritisierungsliste: Benenne die Bottom-3 Items (niedrigster ICE-Score) und formuliere je 1 Satz Begründung warum sie jetzt ausgeblendet werden (zu niedrige Confidence, zu geringer Impact, zu hoher Aufwand ohne klaren Return). Diese Liste verhindert "Schublade vergessen" — Items bleiben sichtbar aber explizit zurückgestellt.

## Verifikation

- ICE-Tabelle: Alle Items haben 3 Scores (I, C, E) und berechneten Gesamt-Score (I×C×E)
- Rangliste: Absteigend sortiert, Median identifiziert, Markierungen korrekt gesetzt
- Top-3 Begründungen: Alle 3 Items mit je 3 Sätzen (Impact / Confidence / Ease) dokumentiert
- 30-Tage-Plan: Genau 6 Aktionen (2 pro Top-3), je mit Zeitrahmen, Deliverable und Aufwand-Schätzung
- Failure-Indikator: Wenn weniger als 5 Items einen vollständigen ICE-Score (alle 3 Dimensionen) aufweisen → Skill gibt aus: "ICE-Bewertung unvollständig: Mindestens 5 Items mit Impact, Confidence und Ease benötigt. Fehlende Scores bitte ergänzen oder Items entfernen."

## Abhängigkeiten

- Input: Liste von Items (Aufgaben, Projekte, Ideen) mit kurzer Beschreibung je Item, übergeordnetes Hauptziel (1 Satz)
- Empfohlene Vorgänger-Skills: /elvis-growth-strategy (definiert Hauptziel für Impact-Bewertung), /elvis-okr-planner (liefert Objectives als Bewertungsrahmen)

## Output

ICE-Scoring-Tabelle (≥10 Items × Impact/Confidence/Ease/Gesamt), Rangliste mit Median-Markierung, Top-3-Begründungen (je 3 Sätze), 30-Tage-Fokus-Plan (6 Aktionen mit Zeitrahmen + Deliverable), Deprioritisierungsliste (Bottom-3 mit Begründung). Gesamtlänge: max. 800 Wörter.
