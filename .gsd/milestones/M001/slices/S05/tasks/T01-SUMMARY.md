---
id: T01
parent: S05
milestone: M001
provides:
  - skills/research/elvis-ai-research.md
  - skills/research/elvis-opportunity-finder.md
  - skills/research/elvis-trend-analyzer.md
  - skills/research/elvis-source-validator.md
  - skills/research/elvis-competitor-deep-dive.md
  - skills/research/elvis-audience-research.md
  - skills/research/elvis-keyword-researcher.md
key_files:
  - skills/research/elvis-ai-research.md
  - skills/research/elvis-opportunity-finder.md
  - skills/research/elvis-trend-analyzer.md
  - skills/research/elvis-source-validator.md
  - skills/research/elvis-competitor-deep-dive.md
  - skills/research/elvis-audience-research.md
  - skills/research/elvis-keyword-researcher.md
key_decisions:
  - Dependency-Whitelist eingehalten: alle 7 Skills referenzieren nur S04-Skills (elvis-competitor-analysis, elvis-audience-builder, elvis-x-trend-scanner, elvis-market-scan) oder "keine (Einstiegs-Skill)" — keine Phantom-Referenzen
  - Differenzierungs-Notizen in Beschreibung/Strategie eingebaut: elvis-trend-analyzer vs. elvis-x-trend-scanner, elvis-competitor-deep-dive vs. elvis-competitor-analysis, elvis-audience-research vs. elvis-audience-builder
patterns_established:
  - Failure-Indikator mit konkretem Schwellenwert + Standard-Meldungstext in jeder ## Verifikation-Sektion
  - Jeder Ausführungsschritt enthält Mengenangaben (D006: z.B. "5 Prompt-Templates", "12 Wochen", "20 Pain Points", "30 Keywords")
  - Abgrenzungsnotizen in Skills die ähnliche Vorgänger haben (Scope-Clarity-Muster)
observability_surfaces:
  - none (reine Markdown-Dateien, kein Runtime)
duration: ~35m
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T01: Research Skills R01–R07 erstellen

**7 Research Skills (R01–R07) vollständig erstellt: KI-Recherche, Opportunity-Finder, Trend-Analyzer, Source-Validator, Competitor-Deep-Dive, Audience-Research, Keyword-Researcher — alle mit 9 Sektionen, D006-konformen Schritten und Failure-Indikatoren.**

## What Happened

Alle 7 Skill-Dateien wurden nach dem Qualitäts-Benchmark `skills/research/elvis-market-scan.md` und dem verbindlichen 9-Sektionen-Format aus `templates/skill-template.md` erstellt. Vor dem Schreiben wurden die Benchmark-Datei, das Template, sowie `skills/growth/elvis-competitor-analysis.md` und `skills/growth/elvis-audience-builder.md` gelesen, um Grenzziehungen korrekt zu dokumentieren.

Jeder Skill wurde mit folgenden Qualitäts-Merkmalen ausgestattet:
- **Konkrete Zahlen in jedem Schritt** (D006): z.B. "5 Prompt-Templates mit je 3 Parametern", "12-Wochen-Zeitraum", "20 Pain Points", "30 Keywords in 3 Kategorien"
- **Failure-Indikator** mit Schwellenwert und Standard-Meldungstext in `## Verifikation`
- **D021-konforme Abhängigkeiten**: nur S04-Skills und S01-Benchmarks referenziert

Differenzierungen zu bestehenden Skills wurden explizit dokumentiert:
- `elvis-trend-analyzer` vs. `/elvis-x-trend-scanner`: Multi-Plattform, kausal, prädiktiv (Abgrenzungsnotiz im Output-Block)
- `elvis-competitor-deep-dive` vs. `/elvis-competitor-analysis`: Einzel-Fokus 12 Wochen tief vs. 5 Accounts × 5 Metriken Oberfläche
- `elvis-audience-research` vs. `/elvis-audience-builder`: Qualitativ-tiefgehend (5 Quellentypen, Originalzitate) vs. quantitatives 5-Dimensionen-Profil

## Verification

```bash
# Datei-Existenz (7/7)
for f in elvis-ai-research elvis-opportunity-finder elvis-trend-analyzer \
          elvis-source-validator elvis-competitor-deep-dive \
          elvis-audience-research elvis-keyword-researcher; do
  [ -f "skills/research/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done
# Ergebnis: 7/7 ✓

# Sektions-Vollständigkeit (alle 9 Sektionen)
# elvis-ai-research: 9 sections ✓
# elvis-opportunity-finder: 9 sections ✓
# elvis-trend-analyzer: 9 sections ✓
# elvis-source-validator: 9 sections ✓
# elvis-competitor-deep-dive: 9 sections ✓
# elvis-audience-research: 9 sections ✓
# elvis-keyword-researcher: 9 sections ✓

# /elvis-* Prefix: 7/7 ✓
# Failure-Indikator: 7/7 ✓
```

## Diagnostics

Reine Markdown-Dateien — kein Runtime, keine Log-Surfaces. Inspektion via:
- `grep -c "^## " skills/research/DATEI.md` — Sektions-Vollständigkeits-Check
- `grep "Failure-Indikator:" skills/research/*.md` — Vollständigkeits-Check aller Failure-Indikatoren

## Deviations

Keine Abweichungen vom Task-Plan.

## Known Issues

Keine.

## Files Created/Modified

- `skills/research/elvis-ai-research.md` — KI-gestützte Recherche mit 5 Prompt-Templates, 3-Kriterien-Matrix
- `skills/research/elvis-opportunity-finder.md` — Gap-Analyse, 5 Lücken aus 3 Quellentypen, Gap-Scoring
- `skills/research/elvis-trend-analyzer.md` — 3 Trends × 5 Dimensionen, Kausalität + 6-Monate-Prognose
- `skills/research/elvis-source-validator.md` — 5-Kriterien-Scoring, Schwelle 15/25
- `skills/research/elvis-competitor-deep-dive.md` — 12-Wochen-Tiefenanalyse, Top-5 Posts, 3+3 Stärken/Schwächen
- `skills/research/elvis-audience-research.md` — 20 Pain Points + 5 Jobs-to-be-done aus 5 Quellentypen
- `skills/research/elvis-keyword-researcher.md` — 30 Keywords in 3 Kategorien, 3×3 Content-Matrix
- `.gsd/milestones/M001/slices/S05/S05-PLAN.md` — T01 als [x] markiert
