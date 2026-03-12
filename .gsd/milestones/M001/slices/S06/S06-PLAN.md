# S06: Automation + Analysis Skills (~20 Skills)

**Goal:** 19 neue Skill-Dateien (9 Automation + 10 Analysis) vollständig ausgearbeitet mit allen 9 Pflicht-Sektionen, `/elvis-*`-Prefix, D006-konformen Ausführungsschritten und Failure-Indikatoren. `skills/analysis/` als neues Verzeichnis angelegt. `scripts/verify-s06.sh` läuft mit Exit-Code 0.
**Demo:** `bash scripts/verify-s06.sh` produziert `✅ S06 Verifikation bestanden — alle Checks grün` mit Exit-Code 0. Alle 19 neuen Dateien existieren. Zusammen mit dem S01-Benchmark `elvis-workflow-builder.md` ergibt das ~10 Automation + 10 Analysis = ~20 Skills für S06.

## Must-Haves

- `skills/analysis/` Verzeichnis existiert mit `.gitkeep` (neues Verzeichnis, in S01 bewusst ausgelassen)
- `scripts/verify-s06.sh` mit 4 Check-Gruppen (Datei-Existenz, Sektions-Vollständigkeit, /elvis-Prefix, Phantomreferenz) — Exit-Code = Fehleranzahl (D014)
- 9 neue Automation Skills in `skills/automation/` — vollständig, D006-konform, mit Failure-Indikator
- 10 neue Analysis Skills in `skills/analysis/` — vollständig, D006-konform, mit Failure-Indikator
- Alle 19 Skills: genau 9 Pflicht-Sektionen (`## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`)
- Alle 19 Skills: `/elvis-*`-Prefix im `## Name`-Block (D001)
- Alle 19 Skills: Inhalte auf Deutsch, Dateinamen auf Englisch (D002)
- Alle 19 Skills: `Failure-Indikator:` mit konkreter Schwelle und Meldungstext in `## Verifikation`
- Keine Phantom-Referenzen: alle in `## Abhängigkeiten` genannten Skills existieren als `.md`-Dateien (nur S01-Benchmark + S04 + S05 + andere S06-Skills erlaubt)
- Inhaltliche Differenzierung: Analysis-Skills enthalten explizit "fortlaufend", "wöchentlich" oder "Mess-System" (Abgrenzung zu einmaligen Growth-Skills)

## Proof Level

- This slice proves: contract
- Real runtime required: no
- Human/UAT required: no (Markdown-Generierung; `verify-s06.sh` ist maschinell ausführbar)

## Verification

```bash
# Objective stopping condition — muss Exit-Code 0 produzieren
bash scripts/verify-s06.sh

# Manuelle Spot-Checks nach T02 und T04
grep -c "Failure-Indikator" skills/analysis/elvis-performance-tracker.md
# → 1

grep -c "fortlaufend\|wöchentlich\|Mess-System" skills/analysis/elvis-growth-tracker.md
# → ≥1 (Differenzierungs-Pflicht)

grep -c "Failure-Indikator" skills/automation/elvis-automation-audit.md
# → 1

# Verzeichnis-Check
ls skills/analysis/.gitkeep
# → Datei existiert
```

## Observability / Diagnostics

- Runtime signals: none (reine Markdown-Generierung, kein Runtime)
- Inspection surfaces: `bash scripts/verify-s06.sh` — strukturierter Check-Report mit ✓/✗ pro Datei/Sektion; Exit-Code = Fehleranzahl; `grep -c "Failure-Indikator" skills/analysis/*.md skills/automation/elvis-automation-audit.md` für Qualitäts-Stichprobe
- Failure visibility: verify-s06.sh gibt `✗ [Dateiname]: [Sektion] — Sektion fehlt` oder `✗ [Dateiname]: Abhängigkeit '[dep]' — Phantomreferenz!` aus; Fehlerzähler als Exit-Code identifiziert exakte Fehleranzahl
- Redaction constraints: none (keine Secrets in Markdown-Dateien)

## Integration Closure

- Upstream surfaces consumed: `templates/skill-template.md` (S01), `skills/automation/elvis-workflow-builder.md` (S01-Benchmark), `scripts/verify-s05.sh` (Vorlage für verify-s06.sh), alle 28 S04-Skills + alle 28 S05-Skills (Abhängigkeits-Whitelist)
- New wiring introduced in this slice: `skills/analysis/` als neues Verzeichnis; `scripts/verify-s06.sh` registriert beide Unterordner im Phantom-Check; Analysis-Skills referenzieren S04/S05 Skills als Vorgänger
- What remains before the milestone is truly usable end-to-end: S07 (Meta-Agent System Skills), S08 (Command System), S09 (Integration und Verifikation + README)

## Tasks

- [x] **T01: skills/analysis/ anlegen + verify-s06.sh schreiben + 5 Analysis Skills** `est:45m`
  - Why: Das `skills/analysis/`-Verzeichnis ist S06-spezifisch und existiert noch nicht. `verify-s06.sh` muss als erstes geschrieben werden (zunächst mit Fehlern) um die Stopping-Condition zu definieren. Die ersten 5 Analysis Skills beginnen den Datei-Output.
  - Files: `skills/analysis/.gitkeep`, `scripts/verify-s06.sh`, `skills/analysis/elvis-performance-tracker.md`, `skills/analysis/elvis-kpi-dashboard.md`, `skills/analysis/elvis-funnel-analyzer.md`, `skills/analysis/elvis-content-analyzer.md`, `skills/analysis/elvis-ab-tester.md`
  - Do: (1) `mkdir skills/analysis && touch skills/analysis/.gitkeep`. (2) `verify-s06.sh` mit 4 Check-Gruppen schreiben (Datei-Existenz 19 Skills, Sektions-Vollständigkeit 19×9=171 Checks, /elvis-Prefix 19 Checks, Phantomreferenz über automation/ + analysis/ + growth/ + content/ + research/ + strategy/). (3) 5 Analysis Skills mit allen 9 Sektionen, Failure-Indikator, D006-konform und Differenzierungs-Formulierung ("fortlaufend" / "Mess-System" / "wöchentliche Cadence").
  - Verify: `ls skills/analysis/.gitkeep` → existiert; `bash scripts/verify-s06.sh` läuft durch (Exit-Code > 0 erwartet da restliche 14 Dateien fehlen, aber Skript selbst ist fehlerfrei)
  - Done when: `skills/analysis/.gitkeep` existiert, `verify-s06.sh` ist ausführbar ohne Syntax-Fehler, 5 Analysis Skills existieren mit allen 9 Pflicht-Sektionen und Failure-Indikator

- [x] **T02: Restliche 5 Analysis Skills** `est:35m`
  - Why: Vervollständigt die 10 Analysis Skills — die zweite Hälfte deckt Reporting, Growth-Tracking, Konversions-Analyse, Konkurrenz-Monitoring und Revenue-Tracking ab.
  - Files: `skills/analysis/elvis-reporting-system.md`, `skills/analysis/elvis-growth-tracker.md`, `skills/analysis/elvis-conversion-analyzer.md`, `skills/analysis/elvis-competitor-monitor.md`, `skills/analysis/elvis-revenue-tracker.md`
  - Do: 5 Analysis Skills mit allen 9 Sektionen, Failure-Indikator, D006-konform. Besonderer Fokus: `elvis-growth-tracker` muss explizit "fortlaufend" vs. einmaligem `elvis-growth-audit` abgrenzen; `elvis-competitor-monitor` muss sich von `elvis-competitor-analysis` (S04) und `elvis-competitor-deep-dive` (S05) durch Ongoing-System-Charakter unterscheiden. Phantom-Check: Abhängigkeiten nur aus S01-Benchmark + S04 + S05 + bereits erstellte S06 Analysis Skills.
  - Verify: `grep -c "fortlaufend\|wöchentlich\|Mess-System\|Monitoring-System" skills/analysis/elvis-growth-tracker.md` → ≥1; alle 5 Dateien haben 9 Sektionen; Failure-Indikatoren vorhanden
  - Done when: Alle 10 Analysis Skills existieren. `bash scripts/verify-s06.sh` meldet [1/4] 10/19 Dateien grün (Automation-Dateien noch fehlend).

- [x] **T03: Erste 5 neue Automation Skills** `est:35m`
  - Why: Beginnt die Automation-Skill-Erstellung. Diese 5 Skills decken die konzeptionellen Kern-Bausteine ab: Audit (was automatisieren?), Einzelaufgabe, Content-Scheduling, Trigger-Logik, Daten-Pipelines.
  - Files: `skills/automation/elvis-automation-audit.md`, `skills/automation/elvis-task-automator.md`, `skills/automation/elvis-content-scheduler.md`, `skills/automation/elvis-trigger-builder.md`, `skills/automation/elvis-data-pipeline.md`
  - Do: 5 Automation Skills mit allen 9 Sektionen, Failure-Indikator, D006-konform. Qualitäts-Benchmark: kein Skill darf abstrakter sein als `elvis-workflow-builder.md` (S01). Keine Code/API-Implementierungen — nur Prompt-Anweisungen für Workflow-Design. Differenzierung zu bestehenden Growth-Skills in `## Beschreibung` explizit.
  - Verify: `grep -c "Failure-Indikator" skills/automation/elvis-automation-audit.md` → 1; alle 5 Dateien haben 9 Sektionen; kein Python/JSON-Code in den Dateien
  - Done when: 5 Automation Skills existieren, alle D006-konform, alle mit Failure-Indikator, keine Phantom-Referenzen

- [x] **T04: Letzte 4 neue Automation Skills** `est:30m`
  - Why: Vervollständigt die 9 neuen Automation Skills — Integration-Mapper, System-Optimizer, Batch-Processor und Autopilot-Setup runden das Automation-Ökosystem ab.
  - Files: `skills/automation/elvis-integration-mapper.md`, `skills/automation/elvis-system-optimizer.md`, `skills/automation/elvis-batch-processor.md`, `skills/automation/elvis-autopilot-setup.md`
  - Do: 4 Automation Skills mit allen 9 Sektionen, Failure-Indikator, D006-konform. `elvis-autopilot-setup` als End-to-End-Setup-Skill darf andere bereits existierende S06-Automation-Skills in `## Abhängigkeiten` referenzieren (sind dann bereits vorhanden). Phantom-Check vor dem Schreiben der Abhängigkeiten manuell durchführen.
  - Verify: `grep -c "Failure-Indikator" skills/automation/elvis-autopilot-setup.md` → 1; alle 4 Dateien haben 9 Sektionen
  - Done when: Alle 9 neuen Automation Skills existieren (zusammen mit S01-Benchmark = 10 total in `skills/automation/`)

- [x] **T05: verify-s06.sh finalisieren, Lauf, S06-SUMMARY schreiben** `est:25m`
  - Why: Schließt S06 mit der objektiven Stopping-Condition ab. verify-s06.sh muss Exit-Code 0 erreichen. SUMMARY dokumentiert Ergebnisse für nachfolgende Slices.
  - Files: `scripts/verify-s06.sh` (ggf. finale Korrekturen), `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md`, `.gsd/STATE.md`, `.gsd/milestones/M001/M001-ROADMAP.md` (S06 als [x] markieren)
  - Do: (1) `bash scripts/verify-s06.sh` ausführen — alle Fehler beheben. (2) S06-SUMMARY.md mit Standard-Frontmatter schreiben (provides, requires, affects, key_files, key_decisions, patterns_established, Forward Intelligence für S07). (3) STATE.md aktualisieren: S06 abgeschlossen, S07 als nächste Slice. (4) ROADMAP.md: S06 als `[x]` markieren. (5) Commit `feat(S06): add automation and analysis skills`.
  - Verify: `bash scripts/verify-s06.sh` → Exit-Code 0, alle 4 Check-Gruppen grün; `grep "\[x\].*S06" .gsd/milestones/M001/M001-ROADMAP.md` → 1 Treffer
  - Done when: verify-s06.sh Exit-Code 0, S06-SUMMARY.md existiert, STATE.md zeigt S07 als nächste Slice, Commit erstellt

## Files Likely Touched

- `skills/analysis/.gitkeep` — neues Verzeichnis
- `skills/analysis/elvis-performance-tracker.md`
- `skills/analysis/elvis-kpi-dashboard.md`
- `skills/analysis/elvis-funnel-analyzer.md`
- `skills/analysis/elvis-content-analyzer.md`
- `skills/analysis/elvis-ab-tester.md`
- `skills/analysis/elvis-reporting-system.md`
- `skills/analysis/elvis-growth-tracker.md`
- `skills/analysis/elvis-conversion-analyzer.md`
- `skills/analysis/elvis-competitor-monitor.md`
- `skills/analysis/elvis-revenue-tracker.md`
- `skills/automation/elvis-automation-audit.md`
- `skills/automation/elvis-task-automator.md`
- `skills/automation/elvis-content-scheduler.md`
- `skills/automation/elvis-trigger-builder.md`
- `skills/automation/elvis-data-pipeline.md`
- `skills/automation/elvis-integration-mapper.md`
- `skills/automation/elvis-system-optimizer.md`
- `skills/automation/elvis-batch-processor.md`
- `skills/automation/elvis-autopilot-setup.md`
- `scripts/verify-s06.sh`
- `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md`
- `.gsd/STATE.md`
- `.gsd/milestones/M001/M001-ROADMAP.md`
