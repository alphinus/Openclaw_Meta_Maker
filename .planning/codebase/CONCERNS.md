# Codebase Concerns

**Analysis Date:** 2026-03-14

## Tech Debt

**Phantom Skill Dependencies — Critical**
- Issue: 48 skills referenced in agent files do not exist as `.md` files in the `skills/` directory tree
- Files: `agent/picard.md`, `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md`, `agent/kirk.md`, `agent/spock.md`, `agent/riker.md`, `agent/scotty.md`, `agent/laforge.md`, `agent/data.md`, `agent/seven.md`, `agent/sulu.md`, `agent/tuvok.md`, `agent/mccoy.md`, `agent/worf.md`
- Impact: System cannot execute skills referenced in agent capabilities. Agents are deployable but incomplete. Verification script `bash scripts/verify-s06.sh` passes (validates only Automation/Analysis skills S06 subset), but does not validate completeness of agent-to-skill dependency graph. No protection against phantom references in later skills.
- Fix approach: Run comprehensive phantom reference check across all agent files; create missing skill files from templates, or refactor agent capabilities to reference only existing skills. Implement validation in verification scripts to catch new phantom references.
- Missing skills include: `/elvis-orchestration`, `/elvis-agent-delegation`, `/elvis-logic-validator`, `/elvis-security-check`, `/elvis-system-analyzer`, `/elvis-data-analysis`, `/elvis-fact-check`, `/elvis-rapid-response`, `/elvis-rapid-execution`, `/elvis-direct-action` and 38 others.

**Incomplete Skill Coverage for S07 — Medium**
- Issue: S07 (Meta-Agent System Skills) is in planning phase but skills are not yet created. Agent layer (S03) references skills that don't exist (e.g., `/elvis-skill-generator`, `/elvis-agent-creator`)
- Files: `agent/q.md` (references 5 non-existent skills), `agent/borg.md` (references 4 non-existent skills), `agent/uhura.md` (references 3 non-existent skills)
- Impact: Autonomous agents (Q, Borg, Uhura) cannot function until S07 is completed. Project roadmap is serialized — S07 cannot be skipped.
- Fix approach: Complete S07 phase immediately after S06 closure; ensure all agent-referenced skills exist before marking milestone complete.

**Manual Skill Validation — Medium**
- Issue: 81 skill files across 7 categories exist, but verification only checks S06 subset (19 skills). No global verification script validates all 81 skills for template compliance.
- Files: `scripts/verify-s06.sh` checks only Automation + Analysis skills; `scripts/verify-s05.sh` checks only Research + Strategy; no unified checker
- Impact: Older skills (S01–S05) may have drifted from template standards. New skills could violate format conventions undetected. Template compliance is point-in-time per slice, not maintained.
- Fix approach: Create `scripts/verify-all-skills.sh` that validates all 81 skills against the 9 required sections defined in `templates/skill-template.md`. Run as pre-commit hook.

**Template Drift — Low**
- Issue: Template specifications exist in markdown (`templates/skill-template.md`, `templates/agent-template.md`, `templates/identity-template.md`, `templates/soul-template.md`) but are not enforced programmatically
- Files: `templates/skill-template.md` lines 8–12 document required edits, but no linting enforces them
- Impact: Authors may misunderstand requirements. HTML comments in templates are supposed to be deleted but remnants could persist. Spacing and formatting inconsistencies may accumulate.
- Fix approach: Add pre-commit hook that validates all `.md` files in `agent/`, `skills/`, `soul/`, `identity/` directories for template compliance. Reject files with HTML comments in non-template context.

## Known Bugs

**None Explicitly Declared**
- No TODO, FIXME, HACK, XXX, BUG, or BROKEN markers found in codebase
- This may indicate either excellent code quality or incomplete documentation of known issues

## Security Considerations

**No Detected Security Issues**
- Current codebase contains no API keys, external service integrations, or credential storage
- Project is document-based (Markdown) — no code execution risk detected
- No authentication or authorization logic implemented
- Recommendation: If project scales to include command execution or external API calls, add security review gates similar to `**Approval-Gate:**` constraints in autonomous agents (D007 safeguards pattern)

## Performance Bottlenecks

**Bash Verification Scripts — Minor**
- Problem: Verification scripts use grep/awk loops over file contents for validation. With 81+ skill files and 9 sections each, linear search becomes slower as codebase grows
- Files: `scripts/verify-s06.sh` lines 82–94 iterate through all files and sections
- Cause: String matching on disk files; no indexing
- Improvement path: Not critical at current scale (81 files run in <1s), but if skills scale to 200+, consider switch to single-pass regex validation or cached manifest file

**Git History Accumulation — Low**
- Problem: Recent commits show frequent rapid commits (aa8c799, a10a35e both commit same S06 feature). Git log shows 20 commits in span of days
- Cause: Slice-based workflow with auto-commit between phases
- Impact: Repository will accumulate 100+ commits during project lifecycle; history becomes harder to navigate
- Improvement path: Squash commits before main merge; consider using `git worktree` for phase isolation instead of linear history

## Fragile Areas

**Agent-Skill Binding — High Risk**
- Files: All 16 agent files (`agent/*.md`)
- Why fragile: Agents reference skills by name string (`/elvis-*` format). No type checking, no validation at agent-load time. If a skill is renamed, all agents referencing it silently break. Worse, agents can reference phantom skills that don't exist.
- Safe modification: Before renaming any skill, grep all agent and skill files for references; update in parallel. Use verification scripts to catch mismatches before commit.
- Test coverage: Verification script checks for existence of referenced skills (phantom reference check in `verify-s06.sh` lines 118–149), but only within S06 scope. No global validation.
- Recommendation: Implement a manifest file that lists all skills with version/hash. Agents reference manifest entry, not raw filename. Solves phantom reference problem and enables skill versioning.

**Template Compliance as Acceptance Criteria**
- Files: `templates/agent-template.md`, `templates/skill-template.md`, `templates/soul-template.md`, `templates/identity-template.md`
- Why fragile: Acceptance criteria for each slice (S01–S07) is "bash scripts/verify-s*.sh exits with code 0." Scripts check for section headers and string presence, not semantic completeness. A skill could have all 9 headers but with empty/boilerplate content and still pass.
- Safe modification: Enhance verification scripts to check not just for section presence but for minimum line counts, non-empty sections, and specific keywords within each section (e.g., "## Ausführungsschritte" must have numbered list, "## Verifikation" must have bullet points).
- Test coverage: Scripts check structural compliance (D015 principle) but not content quality
- Recommendation: Add content validation phase after structural validation; flag sections that appear boilerplate (e.g., single-sentence descriptions, or descriptions that are exact copies of other skills)

**Autonomous Agent Safeguards — Medium Risk**
- Files: `agent/picard.md`, `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md`
- Why fragile: These 5 agents have safeguards defined in Markdown (`**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**`) but safeguards are documentation, not enforced. No runtime system validates that Picard doesn't exceed 3 parallel delegations, or that Q requests operator approval before creation.
- Safe modification: Treat Markdown safeguards as specification, not implementation. When these agents are later implemented in actual code, safeguards must be hard constraints (exception-throwing, not advisory).
- Test coverage: None — safeguards are untested promises
- Recommendation: Once agents move from specification to executable form, create unit tests that verify safeguard enforcement. Example: test that Picard raises exception on 4th concurrent delegation.

**Circular Dependency Risk in Skills**
- Files: All skill files in `skills/*/`
- Why fragile: Some skills reference other skills as prerequisites (e.g., `/elvis-ab-tester` recommends `/elvis-performance-tracker` and `/elvis-funnel-analyzer`). If skills form circular dependency chains (A → B → C → A), execution order becomes ambiguous.
- Safe modification: Before implementing skill execution runtime, audit all "Empfohlene Vorgänger-Skills" references to detect cycles. Create a dependency graph DAG validation tool.
- Test coverage: Verification scripts check that referenced skills exist, but don't check for cycles
- Recommendation: Add cycle detection to verification script; fail build if circular dependency detected

## Scaling Limits

**Skill Count Ceiling — Medium**
- Current capacity: 81 skills deployed across 7 categories
- Limit: As skill count approaches 150–200, discoverability breaks. No skill search/indexing mechanism exists. Authors must manually track skill locations.
- Scaling path: Implement skill registry file (`skills/REGISTRY.md`) with table of all skills, categories, and brief descriptions. Alternatively, add frontmatter to each skill file (YAML block) enabling automated indexing by category, dependencies, and success metrics.

**Verification Script Complexity — Low**
- Current capacity: Each verification script checks one slice (S03, S04, S05, S06 etc.). Each script is 100–200 lines bash.
- Limit: Creating a unified `verify-all.sh` would be 500+ lines bash; bash is not ideal for complex logic. Error messages become harder to parse.
- Scaling path: Convert verification to Python (build a small validator class); output JSON report that can be processed by CI/CD pipelines. Enable --strict, --warnings, --quiet flags for different contexts.

**Agent Count Ceiling — Low**
- Current capacity: 16 agents deployed
- Limit: If agents scale to 50+, agent file directory becomes unwieldy. Operating Loop complexity increases (coordination becomes harder).
- Scaling path: At 30+ agents, consider organizing agents into teams (`agent/team-execution/`, `agent/team-analysis/`, etc.) with a coordinator. Establish agent → agent communication patterns.

## Dependencies at Risk

**No External Package Dependencies — Positive**
- Codebase is pure Markdown + Bash scripts
- No npm, pip, gem, or cargo dependencies
- Zero risk of supply chain attacks or outdated libraries
- Risk mitigation: If future phases introduce code (e.g., Python CLI, Node CLI), establish strict dependency policy: minimize dependencies, pin versions, audit security regularly

**Bash Script Portability — Low Risk**
- Scripts use `set -euo pipefail` and bash idioms (not /bin/sh)
- Target: Linux/macOS bash (shebang: `#!/usr/bin/env bash`)
- Issue: Scripts not tested on Windows (project runs on Windows 11 per environment info)
- Impact: `scripts/verify-*.sh` may fail on Windows without bash emulation (Git Bash, WSL, Cygwin)
- Recommendation: Test scripts on Windows; document required bash environment; alternatively port to Python for cross-platform compatibility

## Missing Critical Features

**No Skill Execution Engine**
- Problem: Skills are fully specified (9 sections per template) but non-executable. No agent calls skills. No workflow orchestration system exists.
- Blocks: Cannot use OpenClaw Meta Maker for actual automation; it remains a specification system
- Expected in: S08 (Commands) or later phase

**No Agent Execution Runtime**
- Problem: 16 agents are specified with capabilities and operating loops, but no code implements the loops. Agents cannot be invoked, delegated to, or monitored.
- Blocks: Agent delegation patterns (Picard) cannot be tested; safeguards cannot be verified
- Expected in: Later phase (not yet scheduled)

**No Skill Discovery Mechanism**
- Problem: 81 skills exist but there is no way to query "which skills solve problem X?" or "which skills depend on metric Y?"
- Blocks: As library grows, manual skill navigation becomes impractical
- Solution: Implement skill search by category, tags, dependencies, input/output types

**No Skill Versioning**
- Problem: If a skill is updated (e.g., `/elvis-ab-tester` changes methodology), no mechanism tracks versions or breaking changes
- Blocks: Agents and workflows may depend on specific skill versions; updates could silently break them
- Solution: Add version number to skill headers; implement skill versioning in manifest

## Test Coverage Gaps

**Untested Skill Content — High Risk**
- What's not tested: Actual skill execution and correctness. The template specifies that `/elvis-ab-tester` should "calculate mindeststichprobengröße pro Variante" but no test verifies the calculation formula is correct or implemented
- Files: All 81 skill files in `skills/*/`
- Risk: Skill advice could be statistically incorrect, logically inconsistent, or operationally infeasible
- Priority: High — if skills are used for actual decision-making (A/B testing, growth strategies, etc.), incorrect skill content poses business risk

**Untested Agent Workflows — High Risk**
- What's not tested: Agent capabilities and operating loops are specified but not executed. No test simulates a Picard delegation to 3 agents or verifies the consolidation step works
- Files: All 16 agent files in `agent/*/`
- Risk: Agent orchestration logic (Picard's 5-step operating loop) may have deadlock conditions, resource leaks, or missed edge cases
- Priority: High — autonomous agents with safeguards must be tested before use

**No Integration Tests Between Agents and Skills**
- What's not tested: Agent → Skill binding. When Picard delegates to Kirk, and Kirk invokes `/elvis-execution-plan`, do they agree on input/output formats?
- Files: Cross-references between `agent/*.md` and `skills/*/*.md`
- Risk: Runtime errors when agent invokes skill with wrong parameters; data format mismatches
- Priority: Medium — not critical until execution engine exists

**No Verification of Safeguards**
- What's not tested: Autonomous agent safeguards are specified in Markdown but never enforced. Picard's `**Max-Limit:** Maximal 3 parallele Agenten-Delegationen` is advice, not code
- Files: `agent/picard.md`, `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md` (lines with `**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**`)
- Risk: Safeguards are bypassed or misinterpreted when agents move to executable code
- Priority: High — safeguard failure could cause runaway automation

**Template Compliance Checking Only — Low Risk**
- What IS tested: Structural compliance. Scripts verify that all 9 sections exist in each skill file, that `/elvis-` prefix is used, that dependencies reference existing skills
- What's NOT tested: Section content quality. A skill with the line "TODO: fill this in" still passes verification
- Files: Verification scripts `scripts/verify-*.sh`
- Risk: Low because structural compliance prevents obvious defects; content quality gaps are caught during use, not deployment
- Priority: Low — acceptable given current project phase (specification, not execution)

---

*Concerns audit: 2026-03-14*
