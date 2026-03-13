---
estimated_steps: 5
estimated_files: 2
---

# T01: Spot-check Qualität, verifiziere Dependencies und schreibe S06-SUMMARY.md

**Slice:** S06 — Automation + Analysis Skills (~20 Skills)
**Milestone:** M001

## Description

Alle 19 S06-Skills existieren bereits mit vollständigem Inhalt. Diese Aufgabe führt Qualitätssicherung durch (D006 Spot-Checks, D030 Ongoing-Marker, Dependency-Verifikation) und schreibt das abschließende S06-SUMMARY.md mit Forward Intelligence für S07/S09.

## Steps

1. Spot-check 4 Skills auf D006-Konformität: elvis-automation-audit.md, elvis-performance-tracker.md, elvis-data-pipeline.md, elvis-kpi-dashboard.md — prüfe dass jeder Ausführungsschritt konkrete Mengen, Zeitangaben oder Formate enthält (≥1 numerische Referenz pro Schritt)
2. grep-Check D030: Alle 10 `skills/analysis/elvis-*.md` müssen in `## Beschreibung` mindestens eines von "fortlaufend", "wöchentlich", "Mess-System", "Monitoring-System" enthalten
3. Manuell alle 14 `/elvis-*`-Referenzen aus den Abhängigkeiten-Blöcken extrahieren und gegen existierende Dateien im Projekt prüfen — jede Referenz muss auf eine reale .md-Datei zeigen
4. `bash scripts/verify-s06.sh` als finale Stopping-Condition ausführen — muss Exit-Code 0 liefern
5. S06-SUMMARY.md schreiben mit: provides, requires, affects, key_files, key_decisions, patterns_established, Forward Intelligence (Phantom-Check-Gap, analysis/-Verzeichnis, Skill-Count 81/~100)

## Must-Haves

- [ ] 4 Skills D006-spot-checked mit ≥15 numerischen Referenzen je Datei
- [ ] 10/10 Analysis-Skills D030-konform (Ongoing-Marker in Beschreibung)
- [ ] 14/14 Dependency-Referenzen zeigen auf existierende Dateien
- [ ] verify-s06.sh Exit-Code 0
- [ ] S06-SUMMARY.md existiert mit Forward Intelligence

## Verification

- `bash scripts/verify-s06.sh` — Exit-Code 0
- `test -f .gsd/milestones/M001/slices/S06/S06-SUMMARY.md && echo OK`
- D030-Check: `for f in skills/analysis/elvis-*.md; do grep -l -E "fortlaufend|wöchentlich|Mess-System|Monitoring" "$f" || echo "FAIL: $f"; done`

## Inputs

- `scripts/verify-s06.sh` — automatisierte 4-Gruppen-Verifikation
- `skills/automation/*.md` — 9 Automation-Skills (+ 1 S01-Benchmark)
- `skills/analysis/*.md` — 10 Analysis-Skills
- S05-SUMMARY.md Forward Intelligence — Dependency-Whitelist und Kontext

## Expected Output

- `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md` — vollständige Slice-Dokumentation mit Forward Intelligence
- `.gsd/milestones/M001/slices/S06/tasks/T01-SUMMARY.md` — Task-Abschluss-Dokumentation
