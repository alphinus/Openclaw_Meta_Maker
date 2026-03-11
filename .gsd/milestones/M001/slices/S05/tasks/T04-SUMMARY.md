---
id: T04
parent: S05
milestone: M001
provides:
  - skills/strategy/elvis-decision-framework.md
  - skills/strategy/elvis-prioritization-engine.md
  - skills/strategy/elvis-scenario-planner.md
  - skills/strategy/elvis-okr-planner.md
  - skills/strategy/elvis-pivot-advisor.md
  - skills/strategy/elvis-resource-allocator.md
  - skills/strategy/elvis-monetization-strategy.md
key_files:
  - skills/strategy/elvis-decision-framework.md
  - skills/strategy/elvis-prioritization-engine.md
  - skills/strategy/elvis-scenario-planner.md
  - skills/strategy/elvis-okr-planner.md
  - skills/strategy/elvis-pivot-advisor.md
  - skills/strategy/elvis-resource-allocator.md
  - skills/strategy/elvis-monetization-strategy.md
key_decisions:
  - elvis-decision-framework Beschreibung nennt explizit "Entscheidungsrahmen für komplexe, folgenreiche Entscheidungen" — konsistent mit Forward-Referenz in agent/kirk.md
  - elvis-monetization-strategy differenziert sich in ## Beschreibung explizit von elvis-monetization-planner (Planner = 5 Modelle + ROI + 90-Tage-Plan; Strategy = Portfolio-Logik + Preis-Positionierung + CLV)
  - elvis-resource-allocator erzwingt 3 separate Budget-Dimensionen (Zeit / Geld / Energie je 100%) statt einer einzigen Ressourcen-Dimension — verhindert Dimension-Verwechslung
patterns_established:
  - Failure-Indikator mit konkretem Schwellenwert + Standard-Meldungstext in jeder ## Verifikation-Sektion (konsistent mit T01/T02/T03-Pattern)
  - Jeder Ausführungsschritt enthält Mengenangaben (D006): Faktoren (5 Kriterien, 3 Alternativen, 10 Items, ICE 1-10), Formeln (CLV = Kaufwert × Frequenz × Dauer), Prozent-Constraints (100%), Zeitangaben (30 Tage, Quartal), Matrixformate
  - Portfolio-Tier-Struktur (Einstieg/Kern/Premium) als konsistentes Muster für Angebots-Architekturen
observability_surfaces:
  - Reine Markdown-Dateien — kein Runtime, keine Log-Surfaces
  - "grep -c \"^## \" skills/strategy/DATEI.md" — Sektions-Vollständigkeits-Check (erwartet: 9)
  - "grep \"Failure-Indikator:\" skills/strategy/*.md" — Vollständigkeits-Check aller Failure-Indikatoren
  - "awk '/^## Abhängigkeiten/,/^## Output/' skills/strategy/elvis-monetization-strategy.md | grep \"elvis-\"" — Phantom-Referenz-Inspektion
  - "grep -r \"decision-framework\" agent/" — bestätigt Forward-Referenz-Konsistenz
duration: ~25min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T04: Strategy Skills S08–S14 erstellen

**7 Strategy Skills (S08–S14) vollständig erstellt: Decision Framework, Prioritization Engine, Scenario Planner, OKR Planner, Pivot Advisor, Resource Allocator und Monetization Strategy — alle mit 9 Sektionen, D006-konformen Schritten, Failure-Indikatoren und ohne Phantom-Referenzen.**

## What Happened

7 Strategy Skill-Dateien in `skills/strategy/` erstellt. Alle decken Entscheidungs- und Planungs-Methoden ab:

- **elvis-decision-framework**: 5-Kriterien-Bewertungsmatrix (Gewichtung 1–3 × Score 1–5), 3 Alternativen vergleichen, Sensitivitäts-Check (5 Szenarien "Ohne Kriterium X"), Entscheidungs-Log (6 Felder). Forward-Referenz in agent/kirk.md bestätigt — Beschreibung nennt explizit "Entscheidungsrahmen für komplexe, folgenreiche Entscheidungen".
- **elvis-prioritization-engine**: ICE-Scoring (Impact × Confidence × Ease, je 1–10) für ≥10 Items, Rangliste mit Median, Top-3-Begründungen (3 Sätze je Item), 30-Tage-Fokus-Plan (6 Aktionen), Deprioritisierungsliste (Bottom-3).
- **elvis-scenario-planner**: Best/Base/Worst Case je 5 Annahmen (5 Kategorien: Markt, Ressourcen, Zielgruppe, Wettbewerb, extern), 3 Konsequenzen, 1 Strategie-Anpassung, Entscheidungs-Trigger (Metrik + Schwellenwert + Zeitfenster), Szenario-Monitoring-Plan (3 KPIs).
- **elvis-okr-planner**: 1 qualitatives Quartal-Objective, 3 Key Results (Von-X-auf-Y-bis-Z-Format), wöchentliches Check-in (3 Fragen), Fortschritts-Scoring (0.0–1.0 mit 4 Bewertungsankern inkl. Google-Standard 0.7), Retrospektive-Template.
- **elvis-pivot-advisor**: 5 messbare Pivot-Signale mit Aktivitäts-Status (aktiv/nicht aktiv), 3 Pivot-Optionen (Zielgruppe/Angebot/Kanal) mit Kosten-Vergleichs-Tabelle (3×3), 3 Go/No-Go-Kriterien, Empfehlung (Pivot/Kein Pivot/Mehr Daten).
- **elvis-resource-allocator**: Ist-Ressourcen-Tabelle (5×3), 80/20-Analyse mit definierbarer Ergebnis-Metrik, Soll-Budget (je Dimension exakt 100%), Delta-Analyse, 3 monatliche Überprüfungs-Trigger.
- **elvis-monetization-strategy**: Angebots-Portfolio (3 Tiers × 5 Felder), Preis-Positionierungs-Karte (Tier-Ratio + psychologische Funktionen), CLV-Tabelle (3 Segmente + gewichteter Durchschnitt, Formel: Kaufwert × Frequenz × Dauer), Portfolio-Logik (Customer Journey + Churn-Punkte), Strategische Differenzierung. Explizite Abgrenzung von elvis-monetization-planner in ## Beschreibung.

## Verification

```bash
# Alle 7 Dateien existieren ✓
for f in elvis-decision-framework elvis-prioritization-engine elvis-scenario-planner \
          elvis-okr-planner elvis-pivot-advisor \
          elvis-resource-allocator elvis-monetization-strategy; do
  [ -f "skills/strategy/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done

# Gesamtzahl Strategy Skills: 15 ✓
ls skills/strategy/*.md | wc -l  # → 15

# Sektions-Check: alle 7 mit exakt 9 Sektionen ✓
for f in elvis-decision-framework elvis-prioritization-engine elvis-scenario-planner \
          elvis-okr-planner elvis-pivot-advisor \
          elvis-resource-allocator elvis-monetization-strategy; do
  grep -c "^## " "skills/strategy/$f.md"  # → je 9
done

# Failure-Indikator Vollständigkeit: 15/15 ✓
grep -l "Failure-Indikator:" skills/strategy/*.md | wc -l  # → 15

# Phantom-Referenz-Check elvis-monetization-strategy ✓
awk '/^## Abhängigkeiten/,/^## Output/' skills/strategy/elvis-monetization-strategy.md | grep "elvis-"
# → /elvis-monetization-planner (existiert in S04) — keine Phantom-Referenz

# Forward-Referenz-Check ✓
grep -r "decision-framework" agent/  # → agent/kirk.md
```

Alle Must-Haves erfüllt.

## Diagnostics

Reine Markdown-Dateien — kein Runtime, keine Log-Surfaces.

Inspection commands:
- `grep -c "^## " skills/strategy/elvis-decision-framework.md` — Sektions-Vollständigkeits-Check (erwartet: 9)
- `grep "Failure-Indikator:" skills/strategy/*.md` — Vollständigkeits-Check aller Failure-Indikatoren
- `awk '/^## Abhängigkeiten/,/^## Output/' skills/strategy/elvis-monetization-strategy.md | grep "elvis-"` — Phantom-Referenz-Inspektion für monetization-strategy
- `grep -r "decision-framework" agent/` — Forward-Referenz-Konsistenz

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `skills/strategy/elvis-decision-framework.md` — 5-Kriterien-Matrix, 3 Alternativen, Sensitivitäts-Check, Entscheidungs-Log; vorwärts-referenziert in agent/kirk.md
- `skills/strategy/elvis-prioritization-engine.md` — ICE-Scoring (≥10 Items), Rangliste mit Median, 30-Tage-Fokus-Plan (6 Aktionen)
- `skills/strategy/elvis-scenario-planner.md` — Best/Base/Worst Case × 5 Annahmen + Entscheidungs-Trigger (Metrik+Schwellenwert+Zeitfenster)
- `skills/strategy/elvis-okr-planner.md` — 1 Objective + 3 Key Results (Von-X-auf-Y-bis-Z) + Check-in-Format + Scoring 0.0–1.0
- `skills/strategy/elvis-pivot-advisor.md` — 5 Pivot-Signale + 3 Optionen (Zielgruppe/Angebot/Kanal) + Go/No-Go-Kriterien
- `skills/strategy/elvis-resource-allocator.md` — 80/20-Analyse + Ressourcen-Budget (3 Dimensionen je 100%) + Überprüfungs-Trigger
- `skills/strategy/elvis-monetization-strategy.md` — Portfolio (3 Tiers) + Preis-Positionierungs-Karte + CLV (3 Segmente); explizit von elvis-monetization-planner abgegrenzt
