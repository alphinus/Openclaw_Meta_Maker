---
estimated_steps: 7
estimated_files: 7
---

# T04: Strategy Skills S08–S14 erstellen

**Slice:** S05 — Research + Strategy Skills (~30 Skills)
**Milestone:** M001

## Description

Erstellt die zweiten 7 Strategy Skills (S08–S14): Decision Framework, Prioritization Engine, Scenario Planner, OKR Planner, Pivot Advisor, Resource Allocator und Monetization Strategy. Diese Skills decken Entscheidungs- und Planungs-Methoden ab.

`elvis-decision-framework` ist in `agent/*.md` vorwärts-referenziert (STATE.md Forward References) — seine Beschreibung muss den Entscheidungsrahmen-Zweck klar machen. `elvis-monetization-strategy` differenziert sich explizit von `elvis-monetization-planner` (S04) durch meta-strategischen statt taktischen Fokus.

## Steps

1. Lies `skills/strategy/elvis-execution-plan.md` und `skills/growth/elvis-monetization-planner.md` als Format- und Grenzziehungs-Referenzen.
2. Erstelle `skills/strategy/elvis-decision-framework.md` — Strukturierter Entscheidungsrahmen für komplexe Entscheidungen: 5-Kriterien-Bewertungsmatrix (je Kriterium: Gewichtung 1–3 × Score 1–5), 3 Entscheidungsalternativen vergleichen, Sensitivitäts-Check (was ändert sich wenn ein Kriterium wegfällt?). Dieses Format ist in `agent/*.md` vorwärts-referenziert — Beschreibung muss den Entscheidungsrahmen-Zweck klar benennen. Failure-Indikator bei < 2 vollständig bewerteten Alternativen.
3. Erstelle `skills/strategy/elvis-prioritization-engine.md` — Aufgaben/Projekte/Ideen priorisieren: ICE-Score (Impact × Confidence × Ease, je 1–10), Liste von mindestens 10 Items bewerten, Top-3 Prioritäten mit Begründung, 30-Tage-Fokus-Plan auf Basis der Top-3. Failure-Indikator bei < 5 Items mit vollständigem ICE-Score.
4. Erstelle `skills/strategy/elvis-scenario-planner.md` — 3 Zukunftsszenarien entwickeln (Best Case / Base Case / Worst Case): je 5 Annahmen, 3 Konsequenzen, 1 Strategie-Anpassung. Entscheidungs-Trigger definieren: Ab welcher Metrik wechselt man in welches Szenario? Failure-Indikator bei fehlenden Entscheidungs-Triggern für alle 3 Szenarien.
5. Erstelle `skills/strategy/elvis-okr-planner.md` — OKR-Framework (Objectives and Key Results): 1 Quartal-Objective (inspirierend, qualitativ), 3 messbare Key Results pro Objective (Format: "Von X auf Y bis Datum Z"), wöchentlicher Check-in-Format (3 Fragen), Fortschritts-Score am Quartals-Ende (0.0–1.0). Failure-Indikator bei Key Results ohne messbare Ausgangszahlen.
6. Erstelle `skills/strategy/elvis-pivot-advisor.md` — Pivot-Entscheidung systematisch bewerten: 5 Pivot-Signale (Metriken die einen Pivot anzeigen), 3 Pivot-Optionen (Zielgruppe / Angebot / Kanal-Pivot), Pivot-Kosten-Abschätzung (Zeit in Wochen + Ressourcen), Go/No-Go-Kriterien (3 Bedingungen für einen Pivot). Failure-Indikator bei fehlenden Go/No-Go-Kriterien.
7. Erstelle `skills/strategy/elvis-resource-allocator.md` — Ressourcen-Aufteilung (Zeit, Geld, Energie): 5 strategische Aktivitäten priorisieren, 80/20-Analyse (welche 20% der Aktivitäten bringen 80% der Ergebnisse?), Ressourcen-Budget in % (muss zusammen 100% ergeben), monatliche Überprüfungs-Trigger (wann wird reallociert?). Failure-Indikator bei Ressourcen-Budget ≠ 100%.
8. Erstelle `skills/strategy/elvis-monetization-strategy.md` — Meta-Monetarisierungsstrategie: Angebots-Portfolio (3 Angebote mit Preispunkt × Zielgruppen-Segment), Preis-Positionierungs-Karte (günstiger Anker / Haupt-Angebot / Premium), Customer Lifetime Value Abschätzung (3 Kundensegmente × durchschnittlicher Wert). Differenzierung von `elvis-monetization-planner` (S04): Planner = 3 konkrete Modelle mit ROI; Strategy = Portfolio-Logik, Preis-Positionierung, CLV. Abhängigkeit: `elvis-monetization-planner` als empfohlener Vorgänger. Failure-Indikator bei fehlendem CLV für alle 3 Segmente.

## Must-Haves

- [ ] 7 Dateien existieren in `skills/strategy/`
- [ ] Jede Datei enthält genau 9 Sektionen (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- [ ] Jeder `## Name` Block enthält `/elvis-*` Prefix
- [ ] Jeder Ausführungsschritt enthält mindestens 1 konkrete Zahl, Zeitangabe oder Matrixformat (D006)
- [ ] Jeder `## Verifikation` Block enthält `Failure-Indikator:` mit Schwelle + Standard-Meldungstext
- [ ] `elvis-decision-framework` beschreibt den Entscheidungsrahmen-Zweck in `## Beschreibung` klar (vorwärts-referenziert in agent/*.md)
- [ ] `elvis-monetization-strategy` differenziert sich in `## Beschreibung` explizit von `elvis-monetization-planner`
- [ ] Keine Phantom-Referenzen in `## Abhängigkeiten` — nur D021-Whitelist (S04-Skills und S05-Skills aus T03/T04)

## Verification

```bash
# Datei-Existenz (7 Checks)
for f in elvis-decision-framework elvis-prioritization-engine elvis-scenario-planner \
          elvis-okr-planner elvis-pivot-advisor \
          elvis-resource-allocator elvis-monetization-strategy; do
  [ -f "skills/strategy/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done

# Gesamtzahl Strategy Skills
ls skills/strategy/*.md | wc -l  # erwartet: 15

# Sektions-Check (Stichprobe)
grep -c "^## " skills/strategy/elvis-decision-framework.md  # erwartet: 9
grep -c "^## " skills/strategy/elvis-monetization-strategy.md  # erwartet: 9

# Phantom-Referenz-Check für monetization-strategy
awk '/^## Abhängigkeiten/,/^## /' skills/strategy/elvis-monetization-strategy.md | grep "elvis-"
# Darf nur: elvis-monetization-planner (existiert in S04)

# Failure-Indikator Vollständigkeit
grep -rl "Failure-Indikator:" skills/strategy/ | wc -l  # erwartet: 15

# Vorwärts-Referenz-Check: decision-framework wird in agents referenziert
grep -r "decision-framework" agent/  # zeigt welche Agenten diesen Skill referenzieren
```

## Observability Impact

- Signals added/changed: None
- How a future agent inspects this: `bash scripts/verify-s05.sh` nach T05; `grep "decision-framework" agent/*.md` bestätigt Referenz-Konsistenz
- Failure state exposed: Wenn `elvis-monetization-strategy` auf einen S04-Skill referenziert der nicht existiert, schlägt Phantom-Check fehl — Dateiname + Referenz werden angezeigt

## Inputs

- T03-Output: 7 Strategy Skills (S01–S07) für Abhängigkeits-Referenzen falls nötig
- `templates/skill-template.md` — verbindliches 9-Sektionen-Format
- `skills/strategy/elvis-execution-plan.md` — Qualitäts-Benchmark
- `skills/growth/elvis-monetization-planner.md` — Grenzziehungs-Referenz für elvis-monetization-strategy
- `agent/*.md` (STATE.md Forward References) — bestätigt dass `elvis-decision-framework` vorwärts-referenziert ist

## Expected Output

- `skills/strategy/elvis-decision-framework.md` — 5-Kriterien-Matrix, 3 Alternativen, Sensitivitäts-Check
- `skills/strategy/elvis-prioritization-engine.md` — ICE-Scoring für ≥10 Items, Top-3 Fokus-Plan
- `skills/strategy/elvis-scenario-planner.md` — Best/Base/Worst Case × Annahmen + Trigger
- `skills/strategy/elvis-okr-planner.md` — 1 Objective + 3 Key Results + Check-in-Format
- `skills/strategy/elvis-pivot-advisor.md` — 5 Signale + 3 Optionen + Go/No-Go-Kriterien
- `skills/strategy/elvis-resource-allocator.md` — 80/20-Analyse + Ressourcen-Budget (100%)
- `skills/strategy/elvis-monetization-strategy.md` — Portfolio + Preis-Positionierung + CLV
