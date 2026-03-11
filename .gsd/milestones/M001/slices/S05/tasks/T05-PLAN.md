---
estimated_steps: 5
estimated_files: 2
---

# T05: verify-s05.sh schreiben + S05-SUMMARY.md erstellen

**Slice:** S05 — Research + Strategy Skills (~30 Skills)
**Milestone:** M001

## Description

Erstellt das Verifikations-Skript `scripts/verify-s05.sh` analog zu `verify-s04.sh` (4 Check-Gruppen: Datei-Existenz, Sektions-Vollständigkeit, /elvis-Prefix, Phantom-Referenzen) und führt es aus bis Exit-Code 0 erreicht ist. Danach wird `S05-SUMMARY.md` geschrieben mit vollständiger Forward Intelligence für S06.

Dieser Task ist die objektive Stopping-Condition für S05 — er transformiert alle vorherigen Tasks in einen maschinenverifizierten Abschluss.

## Steps

1. Kopiere `scripts/verify-s04.sh` als Ausgangsbasis für `scripts/verify-s05.sh`. Ersetze S04 durch S05, ersetze die GROWTH_SKILLS/CONTENT_SKILLS Arrays durch RESEARCH_SKILLS (14 Dateien) und STRATEGY_SKILLS (14 Dateien). Passe die Check-Gruppen-Header und Zusammenfassungs-Texte an. Fehlerzähler als Exit-Code (D014) beibehalten.

   **RESEARCH_SKILLS (14 Dateien):**
   ```
   skills/research/elvis-ai-research.md
   skills/research/elvis-opportunity-finder.md
   skills/research/elvis-trend-analyzer.md
   skills/research/elvis-source-validator.md
   skills/research/elvis-competitor-deep-dive.md
   skills/research/elvis-audience-research.md
   skills/research/elvis-keyword-researcher.md
   skills/research/elvis-pain-point-finder.md
   skills/research/elvis-research-synthesizer.md
   skills/research/elvis-expert-finder.md
   skills/research/elvis-case-study-analyzer.md
   skills/research/elvis-data-collector.md
   skills/research/elvis-problem-explorer.md
   skills/research/elvis-insight-extractor.md
   ```

   **STRATEGY_SKILLS (14 Dateien):**
   ```
   skills/strategy/elvis-growth-strategy.md
   skills/strategy/elvis-positioning-strategy.md
   skills/strategy/elvis-content-strategy.md
   skills/strategy/elvis-go-to-market.md
   skills/strategy/elvis-platform-strategy.md
   skills/strategy/elvis-risk-assessment.md
   skills/strategy/elvis-competitive-strategy.md
   skills/strategy/elvis-decision-framework.md
   skills/strategy/elvis-prioritization-engine.md
   skills/strategy/elvis-scenario-planner.md
   skills/strategy/elvis-okr-planner.md
   skills/strategy/elvis-pivot-advisor.md
   skills/strategy/elvis-resource-allocator.md
   skills/strategy/elvis-monetization-strategy.md
   ```

2. Führe `bash scripts/verify-s05.sh` aus und notiere alle Fehler. Behebe fehlende Sektionen, fehlende Failure-Indikatoren oder Phantom-Referenzen in den betroffenen Skill-Dateien. Wiederhole bis Exit-Code 0.

3. Führe abschließende Validierung durch:
   ```bash
   bash scripts/verify-s05.sh
   ls skills/research/*.md | wc -l   # erwartet: 15
   ls skills/strategy/*.md | wc -l   # erwartet: 15
   grep -rl "Failure-Indikator:" skills/research/ skills/strategy/ | wc -l  # erwartet: 30
   ```

4. Schreibe `.gsd/milestones/M001/slices/S05/S05-SUMMARY.md` im YAML-Frontmatter + Markdown-Format (analog zu S04-SUMMARY.md). Pflicht-Sektionen: What Happened, Verification, Requirements Advanced, Requirements Validated, Deviations, Known Limitations, Follow-ups, Files Created/Modified, Forward Intelligence. Forward Intelligence muss beschreiben: (a) was S06 über S05-Skills wissen muss, (b) was fragil ist, (c) Referenz-Whitelist für S06, (d) welche agent/*.md Forward References durch S05 abgedeckt werden.

5. Aktualisiere `.gsd/STATE.md`: S05 als abgeschlossen markieren, S06 als nächsten Slice eintragen, S05-Ergebnis dokumentieren (28 Skills + verify-s05.sh Exit-Code 0).

## Must-Haves

- [ ] `scripts/verify-s05.sh` existiert und ist ausführbar (`chmod +x` falls nötig)
- [ ] `bash scripts/verify-s05.sh` gibt Exit-Code 0 zurück (0 Fehler)
- [ ] Alle 4 Check-Gruppen grün: [1/4] 28 Dateien, [2/4] 252 Sektions-Checks, [3/4] 28 Prefix-Checks, [4/4] 0 Phantom-Referenzen
- [ ] `S05-SUMMARY.md` existiert mit allen Pflicht-Sektionen und Forward Intelligence
- [ ] `STATE.md` zeigt S05 als abgeschlossen und S06 als nächsten Slice

## Verification

```bash
# Haupt-Verifikation
bash scripts/verify-s05.sh
echo "Exit-Code: $?"  # muss 0 sein

# Zusammenfassung Research
ls skills/research/*.md | wc -l  # 15

# Zusammenfassung Strategy
ls skills/strategy/*.md | wc -l  # 15

# Failure-Indikator in allen 28 neuen Skills (ohne S01-Benchmarks)
grep -rl "Failure-Indikator:" \
  skills/research/elvis-ai-research.md \
  skills/research/elvis-opportunity-finder.md \
  skills/research/elvis-trend-analyzer.md \
  skills/research/elvis-source-validator.md \
  skills/research/elvis-competitor-deep-dive.md \
  skills/research/elvis-audience-research.md \
  skills/research/elvis-keyword-researcher.md \
  skills/research/elvis-pain-point-finder.md \
  skills/research/elvis-research-synthesizer.md \
  skills/research/elvis-expert-finder.md \
  skills/research/elvis-case-study-analyzer.md \
  skills/research/elvis-data-collector.md \
  skills/research/elvis-problem-explorer.md \
  skills/research/elvis-insight-extractor.md \
  skills/strategy/elvis-growth-strategy.md \
  skills/strategy/elvis-positioning-strategy.md \
  skills/strategy/elvis-content-strategy.md \
  skills/strategy/elvis-go-to-market.md \
  skills/strategy/elvis-platform-strategy.md \
  skills/strategy/elvis-risk-assessment.md \
  skills/strategy/elvis-competitive-strategy.md \
  skills/strategy/elvis-decision-framework.md \
  skills/strategy/elvis-prioritization-engine.md \
  skills/strategy/elvis-scenario-planner.md \
  skills/strategy/elvis-okr-planner.md \
  skills/strategy/elvis-pivot-advisor.md \
  skills/strategy/elvis-resource-allocator.md \
  skills/strategy/elvis-monetization-strategy.md | wc -l  # 28

# SUMMARY existiert
[ -f ".gsd/milestones/M001/slices/S05/S05-SUMMARY.md" ] && echo "✓ SUMMARY" || echo "✗ SUMMARY fehlt"
```

## Observability Impact

- Signals added/changed: `scripts/verify-s05.sh` — neues Verifikations-Skript mit 4 Check-Gruppen, Exit-Code = Fehleranzahl; ist von S09 referenzierbar für abschließende Gesamt-Verifikation
- How a future agent inspects this: `bash scripts/verify-s05.sh` — liefert strukturierten ✓/✗ Report + Exit-Code; `grep -E "✗" <(bash scripts/verify-s05.sh 2>&1)` für Fehler-only View
- Failure state exposed: verify-s05.sh zeigt genau welche Datei welche Sektion fehlt; Forward Intelligence in SUMMARY macht fragile Punkte für S06 explizit

## Inputs

- T01-Output: 7 Research Skills R01–R07
- T02-Output: 7 Research Skills R08–R14
- T03-Output: 7 Strategy Skills S01–S07
- T04-Output: 7 Strategy Skills S08–S14
- `scripts/verify-s04.sh` — Vorlage für verify-s05.sh (4 Check-Gruppen, Fehlerzähler-Pattern)
- `.gsd/milestones/M001/slices/S04/S04-SUMMARY.md` — Format-Referenz für S05-SUMMARY.md

## Expected Output

- `scripts/verify-s05.sh` — ausführbares 4-Gruppen-Verifikations-Skript, Exit-Code = Fehleranzahl
- `.gsd/milestones/M001/slices/S05/S05-SUMMARY.md` — vollständige Slice-Summary mit Forward Intelligence
- `bash scripts/verify-s05.sh` → Exit-Code 0, alle 4 Check-Gruppen grün
- `STATE.md` aktualisiert: S05 completed, S06 next
