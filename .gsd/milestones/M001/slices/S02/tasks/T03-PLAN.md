---
estimated_steps: 5
estimated_files: 4
---

# T03: 4 Souls schreiben — operator, analyst, creator, minimalist

**Slice:** S02 — Souls und Identities
**Milestone:** M001

## Description

Die 4 nuanciertesten Souls abschließen. `analyst` und `researcher` klingen ähnlich — die Abgrenzung muss in der `## Philosophie`-Sektion explizit und trennscharf gemacht werden. `creator` vs. `builder` ist ebenfalls eine kritische Unterscheidung. `minimalist` hat keinen primären Agenten und muss als Lens-Soul erklärt werden — mit besonders konkreten Success Metrics, um die Gefahr der Abstraktheit zu umgehen.

## Steps

1. `soul/operator.md` schreiben: Weltbild = navigiert und erhält laufende Systeme. Ordnung, Verlässlichkeit und Kontinuität sind Werte. Kein Erschaffen — Erhalten und Optimieren des Bestehenden. Primäre Agenten: Sulu (Operator Agent), Uhura (Library Manager). `## Geeignet für` explizit. 6 Sektionen. Abgrenzung zu `execution`: operator hält Systeme stabil, execution liefert Ergebnisse unter Druck.
2. `soul/analyst.md` schreiben: Weltbild = Muster in vorhandenen Daten erkennen und bewerten. Kernfrage: "Was bedeutet das?" (im Gegensatz zu researcher: "Was ist wahr?"). Bewertung und Interpretation statt Faktensuche. Primäre Agenten: Seven (Analysis Agent), Troi (System Analyzer). `## Geeignet für` explizit. 6 Sektionen. Die researcher-analyst-Abgrenzung muss in `## Philosophie` explizit artikuliert werden — ein Leser muss nach dem Lesen sofort wissen welcher Soul für welche Aufgabe geeignet ist.
3. `soul/creator.md` schreiben: Weltbild = erschafft Neues aus dem Nichts. Generativer Mindset: Leere ist kein Problem sondern Ausgangspunkt. Erschaffen ohne Ego (Data) oder mit spielerischer Leichtigkeit (Q) — beide Ausprägungen sind gültig. Primäre Agenten: Data (Content Agent), Q (Agent Creator). `## Geeignet für` explizit. 6 Sektionen. Abgrenzung zu `builder`: creator = generiert Neues; builder = verbessert Bestehendes durch Engineering.
4. `soul/minimalist.md` schreiben — Sonderfall: (A) Weltbild: maximale Wirkung mit minimalem Aufwand; Komplexität ist ein Fehler, nicht ein Feature; jede unnötige Schicht ist eine Fehlerquelle. (B) Kein primärer Agent → `## Geeignet für` beschreibt ihn als Lens-Soul ("kann jedem Agenten als sekundärer Soul dienen, der in Überproduktion oder Überplanung tendiert"). (C) Success Metrics müssen konkret sein: "Die Lösung braucht keine Dokumentation, weil sie sich selbst erklärt", "Drei Iterationen weniger als ursprünglich geplant", "Kollege versteht das Ergebnis ohne Einführung". 6 Sektionen.
5. `bash scripts/verify-s02.sh` ausführen — alle 10 Soul-Sektions-Checks müssen grün sein

## Must-Haves

- [ ] Alle 4 soul/*.md existieren mit exakt 6 Sektionen
- [ ] `soul/analyst.md` enthält in `## Philosophie` eine explizite Abgrenzung zu `researcher` (z.B. "Was bedeutet das?" vs. "Was ist wahr?")
- [ ] `soul/creator.md` enthält in `## Philosophie` eine explizite Abgrenzung zu `builder`
- [ ] `soul/minimalist.md` `## Geeignet für`-Sektion erklärt den Lens-Soul-Charakter (kein primärer Agent, sekundär für alle)
- [ ] `soul/minimalist.md` Success Metrics sind konkret und messbar — keine abstrakten Wünsche

## Verification

- `bash scripts/verify-s02.sh` — Soul-Sektions-Checks alle grün (60/60); Fehleranzahl ≤112 (nur noch Identity-Fehler)
- `grep -c "^## " soul/operator.md soul/analyst.md soul/creator.md soul/minimalist.md` — alle geben 6 zurück
- `grep "Was bedeutet" soul/analyst.md` — liefert mindestens einen Treffer (charakteristische Abgrenzungsformulierung)
- `grep "Lens-Soul\|sekundärer Soul\|kein primärer" soul/minimalist.md` — liefert mindestens einen Treffer
- `grep "## Geeignet für" soul/*.md | wc -l` = 10 (alle 10 Souls haben diese Sektion)

## Observability Impact

- Signals added/changed: `bash scripts/verify-s02.sh` — Soul-Block (60 Checks) vollständig grün nach diesem Task
- How a future agent inspects this: Skript-Gruppe `[2/3]` zeigt Soul-Vollständigkeit; grün = alle 10 Souls vollständig
- Failure state exposed: Fehlende Sektion in einem Soul wird mit exakter Datei und Sektionsname gemeldet

## Inputs

- `soul/strategist.md`, `soul/researcher.md`, ... (T01, T02) — Referenz für Qualitätsniveau und Abgrenzungs-Schreibweise
- `templates/soul-template.md` — verbindliches Format
- S02-RESEARCH.md — Soul-Abgrenzungs-Analyse (analyst vs. researcher, creator vs. builder, minimalist als Lens-Soul)
- S02-RESEARCH.md — Common Pitfalls: minimalist-Konkretheit, Operating Principles als Regeln

## Expected Output

- `soul/operator.md` — 6 Sektionen, Weltbild "Erhält laufende Systeme", Sulu + Uhura als primäre Agenten
- `soul/analyst.md` — 6 Sektionen, Weltbild "Was bedeutet das?", Seven + Troi als primäre Agenten, explizite researcher-Abgrenzung
- `soul/creator.md` — 6 Sektionen, Weltbild "Erschafft Neues", Data + Q als primäre Agenten, explizite builder-Abgrenzung
- `soul/minimalist.md` — 6 Sektionen, Lens-Soul ohne primären Agenten, konkrete Success Metrics
