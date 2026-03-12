# S06 — Automation + Analysis Skills (~20 Skills) — Research

**Date:** 2026-03-12

## Summary

S06 has already been completed with all 20 skills (10 Automation + 10 Analysis) fully implemented and verified. All skills follow the 9-section format from S01, are D006-compliant with concrete execution steps, written in German, and have passed all verification checks (scripts/verify-s06.sh exit code 0).

The research validates that:
1. All 19 new skills (9 automation + 10 analysis) plus 1 S01 benchmark (elvis-workflow-builder) exist and are complete
2. A new `skills/analysis/` category has been established to differentiate continuous tracking systems (Analysis) from one-time investigations (Research in S05)
3. Skills use concrete scoring formulas (D028) and quantified metrics where applicable (5-criteria scores, CLV formulas, efficiency scores)
4. All skills have failure indicators with concrete thresholds and avoid phantom references to future skills

This research document provides forward intelligence for S07 and validates the architectural patterns established.

## Recommendation

**No action required** — S06 is complete and verified. The established patterns should be carried forward to S07:

1. **Continue the differentiation pattern**: Analysis skills are "continuous tracking/monitoring systems" with explicit cadences (weekly/monthly), while Research skills (S05) are one-time investigations. S07 Meta-skills should follow similar semantic differentiation.

2. **Maintain concrete scoring formulas**: Automation skills use objective scoring (5-criteria max 25, 4-dimension 1-10 avg), Analysis skills use specific formulas (CLV, conversion rates). S07 should maintain this quantitative rigor for Meta-agent evaluation metrics.

3. **Preserve the whitelist approach for dependencies**: S06 skills can reference S01/S04/S05 skills. S07 can reference all S01/S04/S05/S06 skills but must not forward-reference S08 or later slices.

4. **Apply the "Autopilot pattern"**: elvis-autopilot-setup demonstrates skill orchestration (combining workflow-builder, trigger-builder, batch-processor, integration-mapper into end-to-end systems). S07 Meta-skills should use similar orchestration patterns for agent/skill generation workflows.

## Don't Hand-Roll

| Problem | Existing Solution | Why Use It |
|---------|------------------|------------|
| Skill verification | `scripts/verify-s06.sh` | 4-group verification (file existence, section completeness, /elvis-* prefix, phantom references) with exit-code-as-error-count — proven reliable in S04/S05/S06 |
| Skill quality benchmark | `skills/automation/elvis-workflow-builder.md` (S01) | Demonstrates D006 compliance (concrete quantities, timeframes, formats) — all new Automation skills must meet or exceed this standard |
| Analysis vs. Research differentiation | Pattern from S06-SUMMARY Forward Intelligence | Analysis = continuous tracking with cadence, Research = one-time investigation — prevents semantic overlap between categories |
| Concrete scoring formulas (D028) | elvis-automation-audit (5-criteria), elvis-system-optimizer (4-dimension avg), elvis-revenue-tracker (CLV = Purchase × Frequency × Duration) | Reproducible, machine-verifiable metrics — prefer formulas over qualitative descriptions |

## Existing Code and Patterns

**Automation Skills (10 total):**
- `skills/automation/elvis-automation-audit.md` — 5-criteria scoring system (Häufigkeit/Volumen/Fehleranfälligkeit/Regelbasiert/Zeitaufwand 1–5, max 25) identifies top automation candidates; min. 10 processes, prioritizes Score >10
- `skills/automation/elvis-task-automator.md` — 5 repetition classes (daily/weekly/monthly/event-based/batch) with templates; focuses on repetition pattern as primary differentiator
- `skills/automation/elvis-content-scheduler.md` — 12-week content calendar, 5 content types, time-slot allocation, buffer slots; demonstrates long-range planning automation
- `skills/automation/elvis-trigger-builder.md` — 5 trigger categories (time/event/condition/threshold/webhook), trigger library ≥10 entries; foundational for workflow automation
- `skills/automation/elvis-data-pipeline.md` — 3-stage pipeline (Collect/Transform/Load), 5 data points per stage, error-rate tracking; classic ETL pattern
- `skills/automation/elvis-integration-mapper.md` — N×N integration matrix, visualizes tool connections, identifies gaps; overview skill for multi-tool ecosystems
- `skills/automation/elvis-system-optimizer.md` — 4-dimension audit (Speed/Reliability/Maintainability/Cost 1–10 each), Efficiency Score = average; quantitative system health check
- `skills/automation/elvis-batch-processor.md` — Batch workflows with batch size/time window/error-rate threshold; handles volume-based processing
- `skills/automation/elvis-autopilot-setup.md` — End-to-end "set & forget" automation; ≥3 monitoring metrics, ≥2 alarm rules, ≥2 override options, autonomy level <2 interventions/week; **demonstrates skill orchestration pattern for S07**
- `skills/automation/elvis-workflow-builder.md` — S01 benchmark; 5-step workflow format (Trigger → Action → Output → Condition → Error); foundational pattern for all automation skills

**Analysis Skills (10 total):**
- `skills/analysis/elvis-performance-tracker.md` — KPI tracking system with 10 core metrics, weekly cadence, 4-week trend visualization, traffic-light status (🟢/🟡/🔴); continuous monitoring pattern
- `skills/analysis/elvis-kpi-dashboard.md` — Dashboard setup with 8 sections (Purpose/KPIs/DataSources/Visualizations/UpdateLogic/InterpretationGuide/AlarmThresholds/AccessControl), min. 5 KPIs; meta-template for all dashboards
- `skills/analysis/elvis-funnel-analyzer.md` — Conversion funnel ≥3 stages, drop-off analysis per stage, monthly cadence; conversion optimization focus
- `skills/analysis/elvis-content-analyzer.md` — 5 performance classes (Top/Solid/Average/Weak/Fail), monthly cadence; categorization-based performance review
- `skills/analysis/elvis-ab-tester.md` — A/B test system with 8 steps (Hypothesis/Variants/Metrics/Sample/Execution/Statistics/Interpretation/Documentation), min. 3 tests; rigorous experimentation framework
- `skills/analysis/elvis-reporting-system.md` — Reporting system with 7 components (ReportType/Audience/KPIs/DataSources/Visualizations/Cadence/DistributionLogic), min. 3 report types; reporting infrastructure
- `skills/analysis/elvis-growth-tracker.md` — 3 core growth metrics (Followers/Reach/Engagement), weekly cadence, 12-week tracking; **explicit differentiation from elvis-growth-audit (one-time snapshot)**
- `skills/analysis/elvis-conversion-analyzer.md` — 3 conversion types (Lead-to-Customer/Visitor-to-Lead/Awareness-to-Engagement), weekly cadence; multi-stage conversion tracking
- `skills/analysis/elvis-competitor-monitor.md` — 5 competitor accounts, 4 core metrics, weekly cadence, alarm triggers for significant deviations; **explicit differentiation from elvis-competitor-analysis/elvis-competitor-deep-dive**
- `skills/analysis/elvis-revenue-tracker.md` — CLV formula (Purchase Value × Purchase Frequency × Customer Duration), revenue segmentation, monthly cadence; **D028 compliance with explicit formula**

**Verification Infrastructure:**
- `scripts/verify-s06.sh` — 4 check groups: (1) File existence 19/19, (2) Section completeness 171/171 (19 files × 9 sections), (3) /elvis-* prefix 19/19, (4) Phantom reference check 19/19; exit code 0 = all green

**Patterns Established in S06:**
1. **Analysis = Continuous Tracking Systems**: All analysis skills positioned as "tracking/monitoring systems" with explicit cadence (weekly/monthly), not one-time analyses
2. **Differentiation via contrasts**: Skills with similar names include explicit "Im Gegensatz zu X..." statements in ## Beschreibung (e.g., elvis-growth-tracker vs. elvis-growth-audit)
3. **Concrete scoring formulas (D028)**: Automation skills use objective scoring (5-criteria max 25, 4-dimension avg 1–10), Analysis skills use explicit formulas (CLV = Purchase × Frequency × Duration)
4. **Failure indicators with thresholds**: All 19 skills have "Failure-Indikator:" with concrete threshold (e.g., "<5 processes with Score >10", "<4 weeks of data")
5. **Autopilot/orchestration pattern**: elvis-autopilot-setup shows how to combine multiple foundational skills into end-to-end systems — **critical pattern for S07 Meta-skills**

## Constraints

- **Phantom reference whitelist (S07)**: S07 Meta-skills may reference all S01/S04/S05/S06 skills but must NOT reference S08+ skills (future slices not yet implemented)
- **9-section format mandatory**: All skills must have: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output
- **D006 compliance (concrete execution steps)**: All Ausführungsschritte must include concrete quantities, timeframes, or formats (no abstract instructions like "analyze content" — must be "analyze Top-20 posts of last 7 days")
- **German content**: All skill content in German (file names remain English for compatibility)
- **No forward references**: Skills may only reference existing skills from S01/S04/S05/S06 — no references to S07/S08 skills not yet created
- **Failure indicators required**: Every skill must have at least one "Failure-Indikator:" with concrete threshold and failure message in ## Verifikation section

## Common Pitfalls

- **Analysis vs. Research confusion** — Analysis skills are continuous tracking systems (weekly/monthly cadence), Research skills (S05) are one-time investigations. Avoid mixing: a skill that "analyzes competitor strategy once" belongs in Research, not Analysis.
- **Phantom references in freetext** — verify-s06.sh only checks ## Abhängigkeiten block for phantom references; references in ## Strategie or ## Beschreibung are NOT validated. Manual review required if adding cross-references in prose.
- **Abstract scoring criteria** — Avoid "möglichst wenig" or qualitative thresholds. Use concrete numbers (Max 25, ≥10 entries, <2 interventions/week) for all scoring/limits (D019, D025, D028).
- **Missing differentiation for similar skills** — When creating a skill with a name similar to existing skills (e.g., elvis-growth-tracker vs. elvis-growth-audit), include explicit "Im Gegensatz zu X ist dieser Skill Y" statement in ## Beschreibung.
- **Failure indicator without threshold** — Generic failure indicators ("Wenn Daten fehlen") are insufficient. Must include concrete threshold ("Wenn <5 Prozesse erfasst") and exact failure message ("Skill bricht ab mit 'Datenbasis zu klein'").

## Open Risks

- **CLV formula oversimplification** — elvis-revenue-tracker uses simple CLV = Purchase Value × Purchase Frequency × Customer Duration without discounting future cashflows. Advanced CLV models use discount factors for time-value-of-money. Risk: Skill may be insufficient for sophisticated revenue tracking. **Mitigation**: Skill documentation explicitly states "einfache Formel" — future extension possible if needed.
- **Autonomy-level metric applicability** — elvis-autopilot-setup defines autonomy level as "<2 manual interventions/week." This threshold may not apply to all automation types (e.g., financial approvals may require more frequent human oversight). **Mitigation**: Constraint section includes "Keine Workflows automatisieren die eine menschliche Entscheidung erfordern ... ohne expliziten Approval-Schritt."
- **Integration-mapper scalability** — elvis-integration-mapper uses N×N matrix for visualizing tool connections. For ecosystems with >20 tools, the matrix becomes unwieldy. **Mitigation**: Skill targets "typical ecosystems with 5–15 tools" (implicit in 10-Min-Erfassungszeit); no explicit scale limit documented.
- **Analysis vs. Research boundary enforcement** — Semantic differentiation (continuous vs. one-time) is documented but not enforced by verify-s06.sh. Risk: Future contributors could create hybrid skills that blur the boundary. **Mitigation**: Forward Intelligence section documents the distinction; S07+ contributors must review S06-SUMMARY before creating new skills.

## Skills Discovered

| Technology | Skill | Status |
|------------|-------|--------|
| Markdown-based agent systems | N/A | No external skills — OpenClaw Meta Maker uses custom templates/patterns |
| Process automation scoring | N/A | Custom 5-criteria scoring (Häufigkeit/Volumen/Fehleranfälligkeit/Regelbasiert/Zeitaufwand) tailored to use case |
| Customer Lifetime Value (CLV) | N/A | Standard formula (Purchase Value × Purchase Frequency × Customer Duration) implemented inline |
| A/B testing frameworks | N/A | Custom 8-step framework (Hypothesis → Documentation) specific to skill format |

**No external skills required** — this is a pure content generation milestone using existing S01 templates.

## Sources

**S06 Completion Validation:**
- S06 fully implemented with 20 skills (source: `.gsd/milestones/M001/slices/S06/S06-SUMMARY.md`)
- All verification checks passed (source: `bash scripts/verify-s06.sh` exit code 0)
- 19 new skills created in T01–T04, verified in T05 (source: `.gsd/milestones/M001/slices/S06/tasks/*.md`)

**Pattern Documentation:**
- Analysis vs. Research differentiation established (source: S06-SUMMARY.md "Forward Intelligence (a)")
- Autopilot orchestration pattern documented (source: `skills/automation/elvis-autopilot-setup.md` and S06-SUMMARY "Forward Intelligence (e)")
- Concrete scoring formulas (D028) applied in multiple skills (source: `skills/automation/elvis-automation-audit.md`, `skills/automation/elvis-system-optimizer.md`, `skills/analysis/elvis-revenue-tracker.md`)
- Failure indicator pattern with thresholds validated (source: S06-SUMMARY "Verification" section, manual stichproben)

**Forward References Addressed:**
- `/elvis-automation` → `elvis-automation-audit.md` (source: S06-SUMMARY "Forward Intelligence (d)")
- `/elvis-integration` → `elvis-integration-mapper.md` (source: S06-SUMMARY "Forward Intelligence (d)")
- `/elvis-data-pipeline` → `elvis-data-pipeline.md` (source: S06-SUMMARY "Forward Intelligence (d)")
- Outstanding forward references deferred to S07/S08 (source: S06-SUMMARY "Forward Intelligence (d)" table)

**Template Compliance:**
- All skills follow skill-template.md 9-section format (source: `templates/skill-template.md`, verify-s06.sh section checks 171/171)
- D006 compliance validated against S01 benchmark elvis-workflow-builder (source: S06-SUMMARY "Verification" section)
- All skills in German with /elvis-* prefix (source: verify-s06.sh prefix checks 19/19)

**Architectural Decisions:**
- D028: Scoring formulas as explicit equations (source: `DECISIONS.md` row D028)
- D021: S04 dependency whitelist (source: `DECISIONS.md` row D021) — extended to S06 (S01/S04/S05 skills are valid references)
- D019: Concrete safeguard values in constraints (source: `DECISIONS.md` row D019) — applied to automation skills with Max-Limits

**Next Slice Requirements:**
- S07 can reference all S01/S04/S05/S06 skills (source: S06-SUMMARY "Forward Intelligence (c)" whitelist)
- S07 must NOT reference S08+ skills (source: same section, "S07 darf nicht referenzieren")
- S07 Meta-skills should apply autopilot orchestration pattern (source: S06-SUMMARY "Forward Intelligence (e)" pattern 2)
- S07 must differentiate similar Meta-skills explicitly (source: S06-SUMMARY "Forward Intelligence (e)" pattern 4)
