# S06: Automation + Analysis Skills (~20 Skills)

**Goal:** Alle 19 S06-Skills (9 Automation + 10 Analysis) sind vollständig, qualitätsgeprüft und mit verifiziertem Dependency-Graph — S06-SUMMARY.md dokumentiert das Ergebnis.
**Demo:** `bash scripts/verify-s06.sh` gibt Exit-Code 0; S06-SUMMARY.md existiert mit vollständiger Forward Intelligence für S07/S09.

## Must-Haves

- verify-s06.sh Exit-Code 0 (19/19 Dateien, 171/171 Sektionen, 19/19 Prefix, 19/19 Phantom)
- D006-Konformität spot-checked an 3–4 Skills (konkrete Mengen, Zeitangaben, Formate in Ausführungsschritten)
- Alle 14 Dependency-Referenzen manuell verifiziert gegen existierende Dateien
- D030-Konformität: alle 10 Analysis-Skills enthalten Ongoing-Marker in ## Beschreibung
- S06-SUMMARY.md mit Forward Intelligence für S07/S09 (inkl. Phantom-Check-Limitation)

## Verification

- `bash scripts/verify-s06.sh` — Exit-Code 0
- S06-SUMMARY.md existiert und enthält alle Pflicht-Sektionen (provides, requires, affects, key_files, verification_result, completed_at)

## Tasks

- [x] **T01: Spot-check Qualität, verifiziere Dependencies und schreibe S06-SUMMARY.md** `est:25m`
  - Why: Alle 19 Skill-Dateien existieren bereits mit vollständigem Inhalt — kein Authoring nötig. Die Aufgabe ist Qualitätssicherung und Dokumentation.
  - Files: `skills/automation/elvis-automation-audit.md`, `skills/analysis/elvis-performance-tracker.md`, `skills/analysis/elvis-kpi-dashboard.md`, `skills/automation/elvis-data-pipeline.md`, `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md`
  - Do: (1) Spot-check 4 Skills auf D006-Konformität (Mengen/Zeitangaben/Formate in jedem Ausführungsschritt). (2) grep-Check D030 Ongoing-Marker in allen 10 Analysis-Skills. (3) Manuell alle 14 /elvis-*-Referenzen aus Abhängigkeiten-Blöcken gegen existierende Dateien prüfen. (4) verify-s06.sh als finale Stopping-Condition ausführen. (5) S06-SUMMARY.md schreiben mit Forward Intelligence (Phantom-Check-Gap für S09, analysis/ Verzeichnis-Hinweis, Skill-Count 81/~100).
  - Verify: `bash scripts/verify-s06.sh` Exit-Code 0 + `test -f .gsd/milestones/M001/slices/S06/S06-SUMMARY.md`
  - Done when: verify-s06.sh grün, alle 14 Dependencies auf existierende Dateien geprüft, D030-Check bestanden, S06-SUMMARY.md geschrieben

## Files Likely Touched

- `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md`
- `.gsd/milestones/M001/slices/S06/tasks/T01-SUMMARY.md`
