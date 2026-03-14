---
phase: 03-command-layer
plan: 01
subsystem: command-layer
tags: [commands, routing, command-router, phase-3]
dependency_graph:
  requires: [skills/meta/elvis-*.md]
  provides: [commands/*.md, expanded routing table]
  affects: [skills/meta/elvis-command-router.md]
tech_stack:
  added: []
  patterns: [routing-declaration, 5-field-format, keyword-routing]
key_files:
  created:
    - commands/build-agent.md
    - commands/generate-skills.md
    - commands/analyze-system.md
    - commands/optimize-agent.md
    - commands/manage-library.md
    - commands/expand-skills.md
    - commands/health-check.md
    - commands/create-soul.md
    - commands/create-identity.md
    - commands/route-command.md
  modified:
    - skills/meta/elvis-command-router.md
decisions:
  - "10 command files as pure routing declarations — no execution logic, max 15 lines each"
  - "commands/ directory at root level parallel to skills/, agent/, soul/, identity/"
  - "CMD-02 generate-skills.md lists both Elvis and Borg agents with per-skill assignment"
  - "Command-router routing table expanded from 4 to 12 entries covering all Phase-1 and Phase-2 skills"
  - "Phase-2 forward references removed from router — table is now complete"
metrics:
  duration: "2 minutes"
  completed_date: "2026-03-14"
  tasks_completed: 2
  files_created: 10
  files_modified: 1
requirements_completed: [CMD-01, CMD-02, CMD-03, CMD-04, CMD-05, CMD-06, CMD-07, CMD-08, CMD-09, CMD-10]
---

# Phase 3 Plan 01: Command Layer — Routing Declarations Summary

**One-liner:** 10 minimal command routing declarations in commands/ plus elvis-command-router routing table expanded from 4 to 12 entries covering all Phase-1 and Phase-2 skills.

## What Was Built

### Task 1: 10 Command Files (CMD-01 through CMD-10)

All 10 command files created in `commands/` as pure routing declarations using the locked 5-field format (Command, Beschreibung, Agent, Skill-Chain, optional Hinweis). No execution logic — each file is 10-15 lines.

| Command | Agent | Skill-Chain | File |
|---------|-------|-------------|------|
| /build-agent | Q | /elvis-agent-creator | commands/build-agent.md |
| /generate-skills | Elvis / Borg | /elvis-skill-generator + /elvis-skill-expander | commands/generate-skills.md |
| /analyze-system | Troi | /elvis-system-analyzer | commands/analyze-system.md |
| /optimize-agent | Picard | /elvis-agent-optimizer | commands/optimize-agent.md |
| /manage-library | Uhura | /elvis-library-manager | commands/manage-library.md |
| /expand-skills | Borg | /elvis-skill-expander | commands/expand-skills.md |
| /health-check | Picard | /elvis-ecosystem-health | commands/health-check.md |
| /create-soul | Elvis | /elvis-soul-generator | commands/create-soul.md |
| /create-identity | Elvis | /elvis-identity-generator | commands/create-identity.md |
| /route-command | Picard | /elvis-command-router | commands/route-command.md |

### Task 2: Command-Router Routing Table Expansion

`skills/meta/elvis-command-router.md` updated:
- Routing table expanded from 4 to 12 entries
- Added 8 Phase-2 skills: elvis-agent-creator, elvis-skill-expander, elvis-system-analyzer, elvis-library-manager, elvis-ecosystem-health, elvis-agent-optimizer, elvis-concept-design, elvis-command-router (self-reference)
- Verifikation acceptance criterion updated from "4 Eintraege" to "12 Eintraege"
- Completeness check updated to list all 12 skills
- All Phase-2 forward references removed — router is now the complete source of truth

## Commits

| Task | Commit | Description |
|------|--------|-------------|
| Task 1 | c66c0fd | feat(03-01): create 10 command routing declaration files |
| Task 2 | 7388fa8 | feat(03-01): expand command-router routing table from 4 to 12 entries |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Stale "Phase 2" reference in Ausfuehrungsschritte**

- **Found during:** Task 2
- **Issue:** Step 5 of Ausfuehrungsschritte contained "kann die Routing-Tabelle in Phase 2 erweitert werden" — a stale forward reference now that the table is complete
- **Fix:** Updated to "kann die Routing-Tabelle bei Bedarf erweitert werden" — neutral, forward-compatible wording
- **Files modified:** skills/meta/elvis-command-router.md
- **Commit:** 7388fa8 (included in same commit)

## Decisions Made

- 10 command files as pure routing declarations — no execution logic, max 15 lines each per CONTEXT.md spec
- commands/ directory at root level parallel to skills/, agent/, soul/, identity/
- CMD-02 generate-skills.md lists both Elvis and Borg agents with explicit per-skill assignment ("Elvis (fuer /elvis-skill-generator) / Borg (fuer /elvis-skill-expander)")
- Command-router routing table now the single complete source of truth for all 12 skills

## Self-Check: PASSED

All 11 artifacts verified (10 command files + 1 modified router). Both commits present (c66c0fd, 7388fa8).
