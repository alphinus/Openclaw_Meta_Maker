---
estimated_steps: 5
estimated_files: 4
---

# T05: verify-s06.sh finalisieren, Lauf, S06-SUMMARY schreiben

**Slice:** S06 — Automation + Analysis Skills (~20 Skills)
**Milestone:** M001

## Description

Schließt Slice S06 ab. Führt `verify-s06.sh` aus und behebt alle verbleibenden Fehler bis Exit-Code 0 erreicht ist. Schreibt `S06-SUMMARY.md` nach dem Standardformat vorheriger Slices. Aktualisiert STATE.md und ROADMAP.md. Erstellt abschließenden Commit.

Nach diesem Task ist S06 offiziell abgeschlossen und S07 (Meta-Agent System Skills) kann beginnen.

## Steps

1. `bash scripts/verify-s06.sh` ausführen und alle Fehler beheben:
   - Fehlende Dateien: erstellen falls von T01–T04 ausgelassen
   - Fehlende Sektionen: ergänzen (typisch: `## Ziele` oder `## Einschränkungen` versehentlich weggelassen)
   - Fehlende `/elvis-*`-Prefix: `## Name`-Block korrigieren
   - Phantom-Referenzen: `## Abhängigkeiten`-Block auf existierende Dateien bereinigen
   - Skript läuft in Schleife bis Exit-Code 0

2. Finale Qualitätsstichprobe (manuell — maschinell nicht prüfbar):
   - `elvis-growth-tracker.md`: enthält "fortlaufend" + Abgrenzung zu `elvis-growth-audit`?
   - `elvis-competitor-monitor.md`: enthält "Monitoring-System" + Abgrenzung zu S04/S05?
   - `elvis-automation-audit.md`: nicht abstrakter als `elvis-workflow-builder` Benchmark?
   - `elvis-autopilot-setup.md`: alle referenzierten Skills in `## Abhängigkeiten` existieren?
   - 2 Failure-Indikatoren (je einer Automation + Analysis) auf Konkretheit prüfen: konkreter Schwellenwert + Meldungstext vorhanden?

3. `S06-SUMMARY.md` schreiben im Standard-Format (yaml-Frontmatter + Prosa-Abschnitte):
   - Frontmatter: `id`, `parent`, `milestone`, `provides`, `requires`, `affects`, `key_files`, `key_decisions`, `patterns_established`, `observability_surfaces`, `drill_down_paths`, `duration`, `verification_result`, `completed_at`
   - Prosa: What Happened (T01–T05), Verification (Skript-Output), Requirements Advanced, Requirements Validated, New Requirements Surfaced, Deviations, Known Limitations, Follow-ups, Files Created/Modified, **Forward Intelligence** (für S07: was sind fragile Punkte, was ändern sich Annahmen, authoritative diagnostics)

4. STATE.md aktualisieren:
   - `Active Slice`: S07
   - `Active Task`: —
   - `Phase`: S06 abgeschlossen (verify-s06.sh Exit-Code 0) — S07 startklar
   - Completed Slices: S06 ergänzen
   - S06 Ergebnis-Block: 9 neue Automation Skills + 10 neue Analysis Skills + verify-s06.sh Exit-Code 0
   - Forward References aus agent/*.md: vermerken welche S06-Skills jetzt existieren und welche agent/*.md Forward-Refs aus STATE.md erfüllt sind

5. M001-ROADMAP.md aktualisieren + Commit erstellen:
   - S06 als `[x]` markieren
   - Commit: `feat(S06): add automation and analysis skills (19 new skills, verify exit 0)`

## Must-Haves

- [ ] `bash scripts/verify-s06.sh` endet mit Exit-Code 0
- [ ] Alle 4 Check-Gruppen in verify-s06.sh grün: [1/4] 19/19 Dateien ✓, [2/4] 171/171 Sektions-Checks ✓, [3/4] 19/19 Prefix-Checks ✓, [4/4] 0 Phantom-Referenzen ✓
- [ ] Manuelle Qualitätsstichprobe: mindestens 2 Failure-Indikatoren mit konkreter Schwelle und Meldungstext verifiziert
- [ ] `S06-SUMMARY.md` existiert mit vollständigem YAML-Frontmatter und Forward Intelligence Section
- [ ] STATE.md zeigt S07 als Active Slice
- [ ] ROADMAP.md zeigt S06 als `[x]` abgeschlossen
- [ ] Commit `feat(S06): add automation and analysis skills` erstellt

## Verification

```bash
# Objektive Stopping-Condition
bash scripts/verify-s06.sh
# → ✅ S06 Verifikation bestanden — alle Checks grün
# → Exit-Code: 0

# Dateianzahl final
ls skills/automation/*.md | wc -l
# → 10 (9 neu + 1 S01-Benchmark)

ls skills/analysis/*.md | wc -l
# → 10 (alle 10 Analysis Skills)

# SUMMARY existiert
ls .gsd/milestones/M001/slices/S06/S06-SUMMARY.md

# ROADMAP S06 abgeschlossen
grep "\[x\].*S06" .gsd/milestones/M001/M001-ROADMAP.md
# → 1 Treffer

# STATE zeigt S07
grep "Active Slice.*S07" .gsd/STATE.md
# → 1 Treffer

# Failure-Indikator Stichprobe
grep -c "Failure-Indikator" skills/analysis/elvis-growth-tracker.md
# → 1

grep -c "Failure-Indikator" skills/automation/elvis-automation-audit.md
# → 1

# Differenzierungs-Check
grep -c "fortlaufend\|Monitoring-System\|wöchentlich" skills/analysis/elvis-competitor-monitor.md
# → ≥1
```

## Observability Impact

- Signals added/changed: `bash scripts/verify-s06.sh` als permanente Inspection Surface für S06-Vollständigkeit; Exit-Code 0 ist die verifizierbare Stopping-Condition
- How a future agent inspects this: `bash scripts/verify-s06.sh` für vollständigen S06-Status; S06-SUMMARY.md Forward Intelligence für S07-spezifische Hinweise
- Failure state exposed: Bei Exit-Code > 0 zeigt verify-s06.sh exakt welche Datei/Sektion/Referenz fehlt — keine Ambiguität

## Inputs

- Alle 19 Skill-Dateien aus T01–T04 (19 Dateien in `skills/automation/` und `skills/analysis/`)
- `scripts/verify-s06.sh` aus T01
- S04/S05 SUMMARY-Format als Vorlage für S06-SUMMARY.md
- `.gsd/STATE.md` aktueller Stand
- `.gsd/milestones/M001/M001-ROADMAP.md` aktueller Stand

## Expected Output

- `scripts/verify-s06.sh` (finalisiert) — Exit-Code 0, alle 4 Check-Gruppen grün
- `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md` — vollständige Slice-Dokumentation mit Forward Intelligence für S07
- `.gsd/STATE.md` — aktualisiert: S06 abgeschlossen, S07 startklar
- `.gsd/milestones/M001/M001-ROADMAP.md` — S06 als `[x]` markiert
