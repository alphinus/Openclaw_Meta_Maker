---
estimated_steps: 4
estimated_files: 2
---

# T06: Verifikation + S04-SUMMARY.md

**Slice:** S04 — Growth + Content Skills (~30 Skills)
**Milestone:** M001

## Description

Objektive Verifikation des Slice-Ergebnisses: `bash scripts/verify-s04.sh` → Exit-Code 0. Manuelle D006-Stichproben auf Konkretheitsgrad. S04-SUMMARY.md als Forward Intelligence für S09. STATE.md aktualisieren.

Dies ist die Schlussprüfung — erst wenn alle 4 Check-Gruppen grün und die manuellen Stichproben bestanden sind, ist S04 offiziell abgeschlossen. R003 (Konkrete Execution Steps) wird hier als Proof Level "contract" bestätigt.

## Steps

1. **Automatisierte Verifikation:** `bash scripts/verify-s04.sh` ausführen. Exit-Code 0 ist die Mindestanforderung. Falls Exit-Code > 0: Fehlerausgabe analysieren, fehlende Sektionen in betroffenen Skills nachpflegen, erneut ausführen bis Exit-Code 0.

2. **Manuelle D006-Stichproben (6 Skills):**
   - Growth: `elvis-viral-formula.md`, `elvis-growth-loop.md`, `elvis-niche-finder.md`
   - Content: `elvis-x-thread-writer.md`, `elvis-headline-writer.md`, `elvis-content-brief.md`
   - Für jeden Skill prüfen: (a) ≥4 nummerierte Ausführungsschritte, (b) ≥1 Mengenangabe pro Schritt (Zahl, Zeitraum, Zeichenlimit), (c) Failure-Indikator in `## Verifikation` benannt. Abweichungen direkt im Skill korrigieren.

3. **S04-SUMMARY.md schreiben:** Nach Standard-Format mit Sektionen: YAML-Header (id, parent, provides, requires, affects, key_files, key_decisions, patterns_established, observability_surfaces, drill_down_paths, duration, verification_result, completed_at), narrativen Sektionen (What Happened, Verification, Requirements Advanced, Requirements Validated, Deviations, Known Limitations, Follow-ups, Files Created/Modified, Forward Intelligence).

4. **STATE.md + DECISIONS.md aktualisieren:** Active Slice → S05, S04 als abgeschlossen markieren, Requirements Status aktualisieren (R001 teilweise erfüllt, R003 contract-proof erbracht).

## Must-Haves

- [ ] `bash scripts/verify-s04.sh` → Exit-Code 0
- [ ] 6 Stichproben-Skills dokumentiert in S04-SUMMARY.md (Ergebnis: pass/fail pro Kriterium)
- [ ] S04-SUMMARY.md existiert mit vollständigem YAML-Header + Forward Intelligence
- [ ] Forward Intelligence beschreibt mindestens: erlaubte/nicht erlaubte Cross-Referenzen für S05, bekannte Phantom-Referenz-Risiken, D006-Erkenntnisse

## Verification

- `bash scripts/verify-s04.sh; echo "Exit: $?"` → "Exit: 0"
- `ls .gsd/milestones/M001/slices/S04/S04-SUMMARY.md` → Datei existiert
- `grep "completed_at" .gsd/milestones/M001/slices/S04/S04-SUMMARY.md` → vorhanden
- `grep "R003" .gsd/milestones/M001/slices/S04/S04-SUMMARY.md` → vorhanden (Requirements Advanced)

## Observability Impact

- Signals added/changed: S04-SUMMARY.md als strukturierte Inspektion-Surface für S09; STATE.md zeigt aktualisierten Slice-Status
- How a future agent inspects this: `bash scripts/verify-s04.sh` + S04-SUMMARY.md
- Failure state exposed: Falls Exit-Code > 0 nach Korrekturen → Summary notiert welche Skills nachgebessert wurden

## Inputs

- Alle 28 Skill-Dateien aus T02–T05
- `scripts/verify-s04.sh` aus T01
- `S01-SUMMARY.md` — Format-Referenz für YAML-Header und Narrativ-Struktur
- `.gsd/STATE.md` — aktueller Zustand

## Expected Output

- `.gsd/milestones/M001/slices/S04/S04-SUMMARY.md` — vollständige Slice-Zusammenfassung mit Forward Intelligence für S05/S09
- `.gsd/STATE.md` — aktualisiert: S04 abgeschlossen, S05 als next slice
