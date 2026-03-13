# S06: Automation + Analysis Skills (~20 Skills) — Research

**Date:** 2026-03-13

## Summary

S06 is fully implemented. All 20 skill files (10 Automation + 10 Analysis) already exist with complete content — not stubs. Each file has all 9 mandatory sections, follows the /elvis-* naming convention, contains D006-compliant execution steps with concrete quantities/formats/timeframes, and passes verify-s06.sh with exit code 0.

The verify script has a known limitation: its phantom-reference check reports "keine Referenzen" for all files because it doesn't parse `/elvis-*` references inside the `## Abhängigkeiten` block. Manual inspection confirms all 14 cross-references point to existing skills (no phantom references). The slice requires only verification and summary writing — no new file creation.

Total skill count after S06: 81 of ~100 target (15 Growth + 15 Content + 15 Research + 15 Strategy + 10 Automation + 10 Analysis + 1 Meta).

## Recommendation

Treat S06 as a verification-and-summary slice. All files exist with full content. The work is:
1. Spot-check 3-4 skills for D006 quality (concrete steps, failure indicators, meaningful constraints)
2. Manually verify the 14 dependency references point to real files (confirmed in research)
3. Note the verify-s06.sh phantom-check limitation for S09 integration
4. Write S06-SUMMARY.md

No file creation or editing needed unless quality spot-checks reveal issues.

## Don't Hand-Roll

| Problem | Existing Solution | Why Use It |
|---------|------------------|------------|
| Skill format compliance | `scripts/verify-s06.sh` | Automated 19-file × 9-section check, exit code = error count |
| Skill template reference | `templates/skill-template.md` | Zweistufiges Template with [PFLICHTFELD] markers |
| S01 benchmark quality bar | `skills/automation/elvis-workflow-builder.md` | Automation category benchmark from S01 |

## Existing Code and Patterns

- `scripts/verify-s06.sh` — 4-group verification: file existence (19), section completeness (171 checks), /elvis-* prefix (19), phantom references (19). Exit code 0 = all green. Already passing.
- `skills/automation/elvis-workflow-builder.md` — S01 benchmark skill for automation category; sets quality bar. Not counted in S06's 19 new skills (excluded by verify script).
- `skills/automation/elvis-automation-audit.md` — Representative S06 skill: 5-Kriterien-Score system, 8-column scoring table, concrete ROI calculation. Quality matches S01 benchmark.
- `skills/analysis/elvis-performance-tracker.md` — Representative S06 skill: 10-Kern-Metriken system, Ampel-System (🟢/🟡/🔴), explicit baseline/trend tracking. Quality matches S01 benchmark.

## Constraints

- **verify-s06.sh is the stopping condition** (per D015) — it's already passing with exit code 0
- **S06 dependency whitelist** (per S05 Forward Intelligence): may reference all S01-S05 skills. Confirmed all 14 references are valid.
- **D006 binding**: every Ausführungsschritt must have concrete Mengen, Formate, or Zeitangaben — spot-checked 3 files, all compliant (18-21 numeric references per file)
- **No S07/S08 forward references allowed** — confirmed none exist

## Common Pitfalls

- **Phantom-check false confidence** — verify-s06.sh [4/4] reports "keine Referenzen (ok)" for all files, but files DO contain /elvis-* references in their Abhängigkeiten blocks. The awk pattern doesn't extract them. Manual verification required (done: all 14 refs valid).
- **Circular dependency: elvis-performance-tracker ↔ elvis-kpi-dashboard** — Each references the other as "empfohlener Vorgänger". This is acceptable per D022 precedent (content-calendar/content-ideas pattern) since both are independently usable. Not a hard dependency cycle.

## Open Risks

- **Phantom-check gap carries to S09**: The integration verification in S09 will need a robust cross-slice phantom-reference check that actually parses `/elvis-*` references — verify-s06.sh's check is effectively a no-op for files with soft references.
- **analysis/ directory not in original R007 spec**: R007 mentions `skills/` with subcategories but the original CONTEXT.md structure shows `skills/automation/` without a separate `skills/analysis/`. The `analysis/` directory was created and is functional but should be noted in S09 verification.

## Skills Discovered

| Technology | Skill | Status |
|------------|-------|--------|
| N/A (Markdown-only project) | N/A | No external technologies — pure Markdown file generation |

## Existing S06 Inventory

### Automation Skills (9 new + 1 S01 benchmark)

| File | Skill Name | Dependencies |
|------|-----------|-------------|
| elvis-automation-audit.md | /elvis-automation-audit | keine |
| elvis-task-automator.md | /elvis-task-automator | /elvis-workflow-builder |
| elvis-content-scheduler.md | /elvis-content-scheduler | /elvis-content-ideas |
| elvis-trigger-builder.md | /elvis-trigger-builder | /elvis-task-automator |
| elvis-data-pipeline.md | /elvis-data-pipeline | /elvis-kpi-dashboard |
| elvis-integration-mapper.md | /elvis-integration-mapper | keine |
| elvis-system-optimizer.md | /elvis-system-optimizer | keine |
| elvis-batch-processor.md | /elvis-batch-processor | keine |
| elvis-autopilot-setup.md | /elvis-autopilot-setup | keine |
| elvis-workflow-builder.md | /elvis-workflow-builder | S01 benchmark — not in S06 scope |

### Analysis Skills (10 new)

| File | Skill Name | Dependencies |
|------|-----------|-------------|
| elvis-performance-tracker.md | /elvis-performance-tracker | /elvis-growth-audit, /elvis-kpi-dashboard |
| elvis-kpi-dashboard.md | /elvis-kpi-dashboard | /elvis-performance-tracker |
| elvis-funnel-analyzer.md | /elvis-funnel-analyzer | /elvis-growth-audit |
| elvis-content-analyzer.md | /elvis-content-analyzer | /elvis-x-analytics |
| elvis-ab-tester.md | /elvis-ab-tester | /elvis-performance-tracker |
| elvis-reporting-system.md | /elvis-reporting-system | /elvis-kpi-dashboard |
| elvis-growth-tracker.md | /elvis-growth-tracker | /elvis-performance-tracker |
| elvis-conversion-analyzer.md | /elvis-conversion-analyzer | /elvis-performance-tracker |
| elvis-competitor-monitor.md | /elvis-competitor-monitor | /elvis-performance-tracker |
| elvis-revenue-tracker.md | /elvis-revenue-tracker | /elvis-performance-tracker |

## Requirements Coverage

### Owns/Supports

| Req | Role | Status in S06 |
|-----|------|--------------|
| R001 | co-owner (with S04, S05) | 19 new skills created → 81 total of ~100 target |
| R002 | supports | All 19 skills have 9-section format (171/171 checks green) |
| R003 | supports | D006-compliant execution steps verified (spot-check: 3 files, 18-21 numeric refs each) |
| R006 | supports | 19/19 /elvis-* prefix checks green |
| R011 | supports | All content in German (manual verification) |

### Dependency Validation

All 14 cross-skill references in S06 files verified against existing files:
- `/elvis-workflow-builder` → skills/automation/elvis-workflow-builder.md ✓
- `/elvis-content-ideas` → skills/content/elvis-content-ideas.md ✓
- `/elvis-kpi-dashboard` → skills/analysis/elvis-kpi-dashboard.md ✓ (circular-soft with performance-tracker)
- `/elvis-task-automator` → skills/automation/elvis-task-automator.md ✓
- `/elvis-performance-tracker` → skills/analysis/elvis-performance-tracker.md ✓
- `/elvis-x-analytics` → skills/growth/elvis-x-analytics.md ✓
- `/elvis-growth-audit` → skills/growth/elvis-growth-audit.md ✓

## Verification Command

```bash
bash scripts/verify-s06.sh
# Expected: Exit code 0, all checks green
# [1/4] 19/19 files exist
# [2/4] 171/171 section checks
# [3/4] 19/19 prefix checks
# [4/4] 19/19 phantom checks (note: doesn't actually parse refs)
```

## Sources

- verify-s06.sh output (source: local script execution, exit code 0)
- S05-SUMMARY.md Forward Intelligence (source: `.gsd/milestones/M001/slices/S05/S05-SUMMARY.md`)
- Manual file inspection of all 20 skill files (source: local filesystem)
