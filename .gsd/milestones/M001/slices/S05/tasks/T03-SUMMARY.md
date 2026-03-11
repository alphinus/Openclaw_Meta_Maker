---
id: T03
parent: S05
milestone: M001
provides:
  - skills/strategy/elvis-growth-strategy.md
  - skills/strategy/elvis-positioning-strategy.md
  - skills/strategy/elvis-content-strategy.md
  - skills/strategy/elvis-go-to-market.md
  - skills/strategy/elvis-platform-strategy.md
  - skills/strategy/elvis-risk-assessment.md
  - skills/strategy/elvis-competitive-strategy.md
key_files:
  - skills/strategy/elvis-growth-strategy.md
  - skills/strategy/elvis-positioning-strategy.md
  - skills/strategy/elvis-content-strategy.md
  - skills/strategy/elvis-go-to-market.md
  - skills/strategy/elvis-platform-strategy.md
  - skills/strategy/elvis-risk-assessment.md
  - skills/strategy/elvis-competitive-strategy.md
key_decisions:
  - Risiko-Priorisierungs-Score (RPS) = Wahrscheinlichkeit × Auswirkung × (6−Erkennbarkeit) als messbare Priorisierungsformel etabliert
  - GTM-Plan verwendet 7-Wochen-Rahmen (Pre-Launch 2W / Launch-Woche / Post-Launch 4W) statt generischem Phasen-Modell
  - Plattform-Strategie verwendet 60/15/15/10-Ressourcenteilung als feste Aufteilung
patterns_established:
  - Failure-Indikator mit konkretem Schwellenwert + Standard-Meldungstext in jeder ## Verifikation-Sektion (konsistent mit T01/T02-Pattern)
  - Jeder Ausführungsschritt enthält Mengenangaben (D006): Prozent-Werte, Matrizen, Zeiträume, Anzahlen
  - Differenzierungs-Aussage in ## Beschreibung: Explizit benannter Vergleich mit ähnlichem taktischen S04-Skill
  - Ressourcen-%-Aufteilungen summieren sich auf 100% (Arithmetik-Check als Verifikations-Kriterium)
observability_surfaces:
  - "grep -l \"Failure-Indikator:\" skills/strategy/*.md | wc -l  # erwartet: 8"
  - "grep -c \"^## \" skills/strategy/elvis-<name>.md  # erwartet: 9 pro Datei"
  - "bash scripts/verify-s05.sh  # nach T05: alle 4 Checks inkl. diese 7 Skills"
duration: ~25min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T03: Strategy Skills S01–S07 erstellen

**7 Strategy Skills (S01–S07) vollständig erstellt: Growth Strategy, Positioning Strategy, Content Strategy, Go-to-Market, Platform Strategy, Risk Assessment und Competitive Strategy — alle mit 9 Sektionen, D006-konformen Schritten, expliziter Differenzierung von S04-Skills und Failure-Indikatoren.**

## What Happened

Alle 7 Strategy Skills wurden auf Basis des Qualitäts-Benchmarks `skills/strategy/elvis-execution-plan.md` erstellt (SMART-Ziele, 2×2-Matrizen, konkrete Zeiträume, Prozent-Aufteilungen). Jede Datei enthält genau 9 Sektionen, mindestens eine Mengenangabe/Zeitangabe/Prozent pro Ausführungsschritt (D006) und einen Failure-Indikator mit Schwelle und Standard-Meldungstext.

Besonderheiten pro Skill:
- **elvis-growth-strategy**: 3-Horizonte-Modell (30/90/365 Tage × 3 SMART-Ziele), 4 Go/No-Go-Checkpoints alle 30 Tage, Differenzierung von elvis-growth-audit (Ist vs. Soll)
- **elvis-positioning-strategy**: 5-Dimensionen-Map × 4 Akteure (Selbst + 3 Konkurrenten), 1-Satz-USP-Template, Failure bei <3 Konkurrenten
- **elvis-content-strategy**: 3 Säulen 40/40/20%, min. 15 Themen-Cluster, 90-Tage-Phasenplan, Differenzierung von elvis-content-calendar (taktisch vs. strategisch)
- **elvis-go-to-market**: 7-Wochen-Rahmen, 4-stufiges Botschafts-Framework, Failure bei fehlenden Erfolgsmetriken pro Phase
- **elvis-platform-strategy**: 2×2-Portfolio-Matrix (min. 5 Plattformen), 60/15/15/10%-Aufteilung, 3 messbare Migrations-Trigger, Failure bei fehlenden Ressourcen-%
- **elvis-risk-assessment**: 10 Risiken × 3 Dimensionen + RPS-Formel, 5×5-Heatmap, Failure bei <5 vollständigen Bewertungen
- **elvis-competitive-strategy**: Porter-Auswahl-Pflicht (1 von 3), 5-Punkte-Differenzierungs-Tabelle, Failure bei fehlender Strategie-Auswahl

## Verification

```
# Datei-Existenz: 7/7 ✓
for f in elvis-growth-strategy elvis-positioning-strategy elvis-content-strategy \
          elvis-go-to-market elvis-platform-strategy \
          elvis-risk-assessment elvis-competitive-strategy; do
  [ -f "skills/strategy/$f.md" ] && echo "✓ $f"
done
# Ergebnis: alle 7 ✓

# Sektions-Check (alle 7): 9/9 ✓ pro Datei

# Failure-Indikator: 7/7 Dateien ✓
grep -l "Failure-Indikator:" skills/strategy/elvis-*.md | wc -l  # = 7

# Phantom-Referenz competitive-strategy:
# elvis-competitor-deep-dive → skills/research/elvis-competitor-deep-dive.md ✓
# elvis-competitor-analysis → skills/growth/elvis-competitor-analysis.md ✓

# Strategy files gesamt: 8 (7 neu + 1 Benchmark) ✓
# Research files gesamt: 15 (14 neu + 1 Benchmark) ✓
```

Slice-Level-Checks (Stand nach T03):
- [1/4] Datei-Existenz: 22/28 (7 Strategy neu, T04–T05 stehen noch aus)
- [2/4] Sektions-Checks: 22×9 = 198/252 (T04–T05 ausstehend)
- [3/4] /elvis-* Prefix: 22/28 ✓
- [4/4] Phantom-Referenzen: 0 ✓

## Diagnostics

Reine Markdown-Dateien — kein Runtime, keine Log-Surfaces.

- `grep -c "^## " skills/strategy/DATEI.md` — Sektions-Vollständigkeits-Check (erwartet: 9)
- `grep "Failure-Indikator:" skills/strategy/*.md` — Vollständigkeits-Check aller Failure-Indikatoren
- `awk '/^## Abhängigkeiten/,/^## Output/' skills/strategy/elvis-competitive-strategy.md | grep "elvis-"` — Phantom-Referenz-Inspektion

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `skills/strategy/elvis-growth-strategy.md` — 3-Horizonte-Wachstumsstrategie (30/90/365 Tage), 4 Go/No-Go-Checkpoints, Kanal-Portfolio mit %-Aufteilung
- `skills/strategy/elvis-positioning-strategy.md` — 5-Dimensionen-Map × 3 Konkurrenten, 1-Satz-USP-Template, Tonalitäts-Profil
- `skills/strategy/elvis-content-strategy.md` — 90-Tage-Content-Strategie, 3 Säulen 40/40/20%, 15+ Themen-Cluster
- `skills/strategy/elvis-go-to-market.md` — GTM mit 7-Wochen-Plan, Botschafts-Framework Problem→Lösung→Beweis→CTA
- `skills/strategy/elvis-platform-strategy.md` — Plattform-Portfolio-Matrix (min. 5 Plattformen), 3 Migrations-Trigger, Content-Synergy-Regeln
- `skills/strategy/elvis-risk-assessment.md` — 10 Risiken × 3 Dimensionen + RPS-Formel, 5×5-Heatmap, Top-3 Mitigation
- `skills/strategy/elvis-competitive-strategy.md` — Porter-Basis-Strategie-Auswahl, 5-Punkte-Differenzierungs-Tabelle, 3 Verteidigungs-Maßnahmen
