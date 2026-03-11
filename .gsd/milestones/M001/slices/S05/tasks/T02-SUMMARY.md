---
id: T02
parent: S05
milestone: M001
provides:
  - skills/research/elvis-pain-point-finder.md
  - skills/research/elvis-research-synthesizer.md
  - skills/research/elvis-expert-finder.md
  - skills/research/elvis-case-study-analyzer.md
  - skills/research/elvis-data-collector.md
  - skills/research/elvis-problem-explorer.md
  - skills/research/elvis-insight-extractor.md
key_files:
  - skills/research/elvis-pain-point-finder.md
  - skills/research/elvis-research-synthesizer.md
  - skills/research/elvis-expert-finder.md
  - skills/research/elvis-case-study-analyzer.md
  - skills/research/elvis-data-collector.md
  - skills/research/elvis-problem-explorer.md
  - skills/research/elvis-insight-extractor.md
key_decisions:
  - elvis-research-synthesizer referenziert nur elvis-market-scan und elvis-audience-research (beide aus S01/T01) — keine Phantom-Referenzen
  - elvis-insight-extractor referenziert nur elvis-data-collector (aus diesem Task) — keine S06/S07-Vorgriffe
  - Dependency-Chain etabliert: elvis-data-collector → elvis-insight-extractor (innerhalb T02); elvis-pain-point-finder → elvis-problem-explorer (empfohlene Kette)
patterns_established:
  - Failure-Indikator mit konkretem Schwellenwert + Standard-Meldungstext in jeder ## Verifikation-Sektion (konsistent mit T01-Pattern)
  - Jeder Ausführungsschritt enthält Mengenangaben (D006): "30–40 Roh-Pain-Points", "5 Iterationen", "15 Einträge", "3 Datenpunkte pro Muster", "2×2 Matrix"
  - Differenzierungshinweise in ## Beschreibung eingebaut wo Skill-Überschneidung mit anderen Skills möglich ist
observability_surfaces:
  - grep -c "^## " skills/research/DATEI.md — Sektions-Vollständigkeits-Check
  - grep "Failure-Indikator:" skills/research/*.md — Vollständigkeits-Check aller Failure-Indikatoren
  - awk '/^## Abhängigkeiten/,0' skills/research/elvis-research-synthesizer.md | grep "elvis-" — Phantom-Referenz-Inspektion
duration: ~25min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T02: Research Skills R08–R14 erstellen

**7 Analyse-Ebene Research Skills (R08–R14) vollständig erstellt: Pain Point Finder, Research Synthesizer, Expert Finder, Case Study Analyzer, Data Collector, Problem Explorer und Insight Extractor — alle mit 9 Sektionen, D006-konformen Schritten und Failure-Indikatoren.**

## What Happened

Alle 7 Research Skills für die "Analyse-Ebene" wurden nach dem etablierten T01-Format erstellt:

- **elvis-pain-point-finder**: Kartiert Pain Points auf 3 Tiefenebenen (oberflächlich/tief/latent), 10 Pain Points × 3 Ebenen + Häufigkeits-Score 1–5. Differenziert explizit von /elvis-audience-research (Fokus auf Problemtiefe, kein breites Profil).
- **elvis-research-synthesizer**: Verdichtet 3–5 Research-Inputs zu einem Insight-Brief: 5 übergreifende Erkenntnisse, 3 Widersprüche, 1 Handlungsempfehlung. Referenziert nur elvis-market-scan und elvis-audience-research (D021-konform).
- **elvis-expert-finder**: Top-10 Experten mit 4-Kriterien-Score (Veröffentlichungen, Reichweite, Praxis, Spezifität) je 1–5 Punkte (max. 20). Kontakt-Ansatz plattform-spezifisch pro Experte.
- **elvis-case-study-analyzer**: 3 Case Studies × Kontext + 5 Taktiken + 3 Metriken + Muster-Extraktion. Muster-Matrix klassifiziert kontextabhängig vs. universell anwendbar.
- **elvis-data-collector**: Strukturierte Daten aus 5 Quelltypen in Tabelle (Quelle, Typ, Datum, Datenpunkt, Relevanz 1–3). Vollständigkeits-Check ≥ 3 Einträge pro Quelltyp + Datenlücken-Report.
- **elvis-problem-explorer**: 5-Warum-Analyse (5 kausale Iterationen), 3 Problemebenen (Symptom/Ursache/Systemursache), 10 Sub-Probleme + Problem-Map + Priorisierungs-Empfehlung.
- **elvis-insight-extractor**: Muster aus ≥ 3 Datenpunkten, 2×2 Priorisierungs-Matrix (Konfidenz × Auswirkung), Top-5 Erkenntnisse mit Handlungsrelevanz-Einschätzung. Referenziert nur elvis-data-collector.

## Verification

```bash
# Datei-Existenz: alle 7 ✓
for f in elvis-pain-point-finder elvis-research-synthesizer elvis-expert-finder \
          elvis-case-study-analyzer elvis-data-collector \
          elvis-problem-explorer elvis-insight-extractor; do
  [ -f "skills/research/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done
# Output: alle 7 ✓

# Gesamtzahl: 15 ✓
ls skills/research/*.md | wc -l  # → 15

# Sektions-Checks: 9 ✓
grep -c "^## " skills/research/elvis-research-synthesizer.md  # → 9
grep -c "^## " skills/research/elvis-insight-extractor.md     # → 9
grep -c "^## " skills/research/elvis-pain-point-finder.md     # → 9

# Phantom-Referenz-Check research-synthesizer ✓
# Ergebnis: /elvis-market-scan + /elvis-audience-research (beide existieren)
awk '/^## Abhängigkeiten/,0' skills/research/elvis-research-synthesizer.md | grep "elvis-"

# Phantom-Referenz-Check insight-extractor ✓
# Ergebnis: /elvis-data-collector (aus diesem Task)
awk '/^## Abhängigkeiten/,0' skills/research/elvis-insight-extractor.md | grep "elvis-"

# Failure-Indikator Vollständigkeit: 15 ✓
grep -rl "Failure-Indikator:" skills/research/ | wc -l  # → 15
```

## Diagnostics

Reine Markdown-Dateien — kein Runtime, keine Log-Surfaces. Inspektion via:
- `grep -c "^## " skills/research/DATEI.md` — Sektions-Vollständigkeits-Check
- `grep "Failure-Indikator:" skills/research/*.md` — Vollständigkeits-Check aller Failure-Indikatoren
- `awk '/^## Abhängigkeiten/,0' skills/research/elvis-research-synthesizer.md | grep "elvis-"` — Phantom-Referenz-Inspektion für Synthesizer

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `skills/research/elvis-pain-point-finder.md` — 10 Pain Points × 3 Ebenen (oberflächlich/tief/latent) + Häufigkeits-Score 1–5
- `skills/research/elvis-research-synthesizer.md` — Insight-Brief aus 3–5 Research-Outputs; 5 Erkenntnisse + 3 Widersprüche + 1 Handlungsempfehlung
- `skills/research/elvis-expert-finder.md` — Top-10 Experten mit 4-Kriterien-Score (max. 20) + plattform-spezifischem Kontakt-Ansatz
- `skills/research/elvis-case-study-analyzer.md` — 3 Case Studies × Taktiken + Metriken + Muster-Matrix
- `skills/research/elvis-data-collector.md` — Daten aus 5 Quelltypen in Tabelle + Vollständigkeits-Check + Datenlücken-Report
- `skills/research/elvis-problem-explorer.md` — 5-Warum + 3 Ebenen + 10 Sub-Probleme + Problem-Map + Priorisierungs-Empfehlung
- `skills/research/elvis-insight-extractor.md` — Muster aus ≥ 3 Datenpunkten + 2×2 Priorisierungs-Matrix + Top-5 Erkenntnisse
