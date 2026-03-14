# Project Research Summary

**Project:** OpenClaw Meta Maker — Meta-Agent Layer + Command System
**Domain:** Markdown-based AI Agent Factory (Meta-Agent Extension of Existing Ecosystem)
**Researched:** 2026-03-14
**Confidence:** HIGH

## Executive Summary

This is not a greenfield build. The project is 81% complete: 81 skills, 16 agents, 16 identities, and 10 souls already exist in a pure-Markdown system targeting the OpenClaw platform. The remaining work is precisely scoped: 8 meta skills (1 already exists), an infrastructure routing skill, and 10 command definitions across two milestones (S07 and S08). All structural conventions, naming patterns, and format requirements are fully defined by the existing codebase. The "stack" is Markdown with YAML front matter; the architecture is a four-layer system (base assets → meta skills → meta agents → commands); and the execution format is the established 9-section skill template. There are no technology decisions to make.

The recommended approach is generator-pattern-first within S07: build the individual generator skills (agent, soul, identity) before the composition skill (agent-creator), and build the command-router before S08 begins. All generator and autonomous skills must implement the four-safeguard quartet (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis) with concrete numbers and explicit execution-step halt points — not just as section declarations. Commands are routing declarations only; they contain no generation logic and must be architecturally distinct from skills to avoid the single largest structural risk in S08.

The primary risks are safeguard theater (safeguard sections that are formally present but operationally empty), command files that duplicate skill logic rather than routing to it, and orchestration skills that describe what they do without specifying how the LLM should execute each step. All three risks are preventable at write-time by following the existing `/elvis-skill-generator.md` as the canonical reference implementation. The approval gate pattern in that file — plan presented in step 2, explicit operator confirmation before step 3 executes — is the design standard that must propagate to all new autonomous skills.

## Key Findings

### Recommended Stack

The system's "stack" is entirely convention-based. OpenClaw injects Markdown files directly into the agent's system prompt; there is no compilation step, no framework, and no runtime code. Every artifact type (skill, agent, soul, identity, command) is a Markdown file following a defined template. The 9-section skill format is the binding contract across all 81 existing skills and must not be extended or modified for meta skills — not even for meta-specific concepts like routing or safeguard declarations. Those belong in the existing Einschränkungen and Strategie sections.

**Core conventions:**
- **9-section skill format** — Non-negotiable. Template at `templates/skill-template.md`. Deviations break Uhura's format validation.
- **YAML front matter** — Required for command registration via OpenClaw's slash command discovery system.
- **Two-phase execution (Plan → Approve → Execute)** — Canonical pattern from `skills/meta/elvis-skill-generator.md`. All generator and autonomous skills follow this.
- **Explicit safeguard quartet** — Max-Limit (number ≤ 10), Approval-Gate (named trigger word + halt point in steps), Stop-Bedingung (regular + early-exit), Rollback-Hinweis (concrete action, not "report error"). Required by R004.
- **Command-as-router** — Command files declare agent + skill chain only. No logic, no conditions, no step-by-step execution. Commands that contain generation logic become unmaintainable duplicates.
- **German language, English technical terms** — R011 requirement. All 81 existing skills are German. Skill/Soul/Agent/Command stay English. No mixing in meta layer.

### Expected Features

The feature scope is fully defined by agent definitions referencing non-existent skills and by M001-ROADMAP.md. There is no ambiguity about what S07 and S08 must deliver.

**Must have (table stakes — S07 core):**
- `/elvis-agent-generator` — Q's primary capability; without it, Q cannot fulfill its mission
- `/elvis-soul-generator` — Required by `/build-agent` command; foundational artifact layer
- `/elvis-identity-generator` — Completes the "new agent in under 2 minutes" promise
- `/elvis-agent-creator` — Assembly skill combining soul + identity + agent; the composition capstone of S07
- `/elvis-skill-expander` — Borg's core gap-detection + batch-generation capability
- `/elvis-system-analyzer` — Troi's read-only health check; primary skill referenced in Troi's agent definition
- `/elvis-library-manager` — Uhura's routing table maintenance; infrastructure for the command system
- `/elvis-command-router` — Hard S07/S08 boundary artifact; S08 cannot be written without it
- All 10 commands in `commands/` — Complete operator-facing command layer (S08)

**Should have (differentiators — S07 extended):**
- `/elvis-concept-design` — Q's framework-sketching capability; medium value, no command dependency
- `/elvis-agent-optimizer` — Backs the `/optimize-agent` command; needed only if that command is included in S08

**Defer (v2+):**
- `/elvis-pattern-assimilation` — Borg's external-pattern import; no current use case, highest implementation complexity
- Additional soul archetypes — Defer until operator encounters a gap the current 10 souls cannot fill
- Cross-ecosystem skill import — Speculative value, requires pattern-assimilation first

### Architecture Approach

The system uses a strict four-layer architecture with one-directional dependency flow: base assets (skills, agents, souls, identities) → meta skills (skills/meta/) → meta agents (agent/) → commands (commands/). Each layer has a defined responsibility boundary. Commands know who handles a request; agents know which skills to invoke; skills know how to execute. No layer implements the responsibility of a layer above or below it. This separation is what makes the system auditable and maintainable as it scales beyond 100 files.

**Major components:**
1. **Command Layer (commands/)** — Operator entry points; declarative routing only; one command = one primary agent + one skill chain
2. **Meta Skill Layer (skills/meta/)** — All generator, expander, analyzer, and orchestrator skills; follow identical 9-section format as domain skills
3. **Meta Agent Layer (agent/)** — Five autonomous agents (Picard, Q, Borg, Troi, Uhura); already complete; define which meta skills they invoke
4. **Base Asset Layer** — 81 skills, 16 agents, 16 identities, 10 souls, 4 templates; all complete; consumed by meta skills as reference and input

**Build order within S07:**
1. `elvis-command-router.md` — Build first; referenced by library-manager and all commands
2. Generator skills in parallel — `elvis-agent-generator`, `elvis-soul-generator`, `elvis-identity-generator` (no inter-dependencies)
3. `elvis-agent-creator.md` — Composition skill; depends on individual generators
4. Autonomous system skills in parallel — `elvis-skill-expander`, `elvis-system-analyzer`, `elvis-library-manager`

### Critical Pitfalls

1. **Safeguard-Washing** — Safeguard sections are formally present but contain vague language ("bei Bedarf", "möglichst") instead of concrete numbers and halt-point references. Prevention: every safeguard bullet must contain a number ≤ 10 (Max-Limit), an explicit trigger word and step reference (Approval-Gate), two exit conditions (Stop-Bedingung), and a named recoverable action (Rollback). The Approval-Gate must also appear as a numbered halt step in the Ausführungsschritte section — not only in Einschränkungen.

2. **Command Files as Skill Duplicates** — Commands built to feel "complete" by embedding generation logic become unmaintainable duplicates of skills. Prevention: define command architecture before generating any command. Every command must orchestrate at least two skills; if a command maps 1:1 to a single skill, it is an alias, not a command.

3. **Abstract Orchestration Steps** — Orchestrator skills (Picard, Borg coordination) describe intent ("delegiere", "koordiniere") without naming concrete sub-skill invocations. The LLM has no actionable step to execute. Prevention: every execution step of an orchestration skill must reference at least one `/elvis-*` skill by name, specify its input format, and define the expected output format.

4. **Autonomous Skills Without Error Exit Paths** — Multi-step autonomous skills define rollback in Einschränkungen but not in the execution flow itself. The LLM continues past failures. Prevention: every step in an autonomous skill must include a "Wenn [Fehler]: stoppe sofort, gib Schritt N/Status aus, warte auf Operator" clause. Last step must always output a status summary.

5. **Command Namespace Collision** — Commands and skills use different naming schemes but can describe identical functionality, creating operator confusion. Prevention: commands use plain verb-noun scheme (`/build-agent`), skills always use `/elvis-*`. Verify against all 81+ existing skill names before finalizing command names.

## Implications for Roadmap

Based on research, the natural phase structure is the existing S07 → S08 split, with S07 subdivided by dependency tier.

### Phase 1: Meta Infrastructure (S07-A)
**Rationale:** `elvis-command-router.md` is the single blocking dependency for the entire command layer. Building it first eliminates the risk of S08 starting with a forward-reference gap. This is the lowest-complexity skill in S07 but the highest-leverage.
**Delivers:** The routing infrastructure that every command in S08 will reference.
**Addresses:** Command-layer readiness, library-manager dependency
**Avoids:** Pitfall 5 (command namespace collision) — naming conventions are established here

### Phase 2: Individual Generator Skills (S07-B)
**Rationale:** Agent-creator depends on these three generators; they have no inter-dependencies and can be written in parallel. Building them before agent-creator is a hard dependency.
**Delivers:** `elvis-agent-generator`, `elvis-soul-generator`, `elvis-identity-generator`
**Uses:** `templates/agent-template.md`, `soul/*.md`, `identity/*.md` as format references
**Implements:** Generator pattern with two-phase approval gate
**Avoids:** Pitfall 1 (safeguard-washing) — each generator must have concrete numbers in all four safeguard fields

### Phase 3: Composition + Autonomous Skills (S07-C)
**Rationale:** Agent-creator depends on S07-B generators. Skill-expander, system-analyzer, and library-manager can be built in parallel after generators exist (they reference generator skills in their dependency declarations).
**Delivers:** `elvis-agent-creator`, `elvis-skill-expander`, `elvis-system-analyzer`, `elvis-library-manager`
**Implements:** Composition pattern (agent-creator) + safeguarded autonomous skill pattern (expander, analyzer, manager)
**Avoids:** Pitfall 3 (abstract orchestration) — system-analyzer and skill-expander must reference concrete sub-skills in execution steps; Pitfall 4 (no error exit paths)

### Phase 4: Command Layer (S08)
**Rationale:** All S07 skills must exist before S08 begins. Commands are declarative routing files — low complexity per file, but the architecture (which command maps to which agent and skill chain) must be decided before writing any individual command file.
**Delivers:** All 10 command definitions in `commands/`
**Uses:** All meta skills from S07 as routing targets
**Avoids:** Pitfall 2 (command-as-skill-duplicate) — each command must orchestrate 2+ skills; Pitfall 5 (namespace collision) — use verb-noun scheme, no `/elvis-*` in command names

### Phase Ordering Rationale

- S07-A before S07-B/C: command-router is a dependency for library-manager, and establishing naming conventions early prevents namespace collisions during command generation
- S07-B before S07-C: agent-creator is a composition skill; it cannot be written without the individual generator skills being defined first
- S07-C skills can be written in parallel once generators exist
- S08 after all S07: every command references a meta skill and an agent; no forward references allowed in command files
- No phase benefits from deeper `/gsd:research-phase` — all patterns are defined by the existing codebase and spec

### Research Flags

Phases that can skip `/gsd:research-phase` (standard patterns, well-documented):
- **S07-A (command-router):** Routing declaration pattern fully defined in ARCHITECTURE.md
- **S07-B (generators):** Generator pattern fully defined by `elvis-skill-generator.md` reference implementation
- **S07-C (autonomous skills):** Safeguarded autonomous skill pattern fully defined; the pitfalls are known and preventable
- **S08 (commands):** Command routing declaration pattern fully defined; low complexity

No phase requires external research. All required patterns are observable in the existing codebase.

One decision point that needs explicit operator input before S08: whether `/optimize-agent` command is in scope. If yes, `/elvis-agent-optimizer` must be added to S07-C. If no, S08 has 9 commands instead of 10. This is a scope decision, not a research question.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Conventions observable directly from 81 existing skills, agent definitions, and spec documents |
| Features | HIGH | Scope fully defined by agent definitions referencing named non-existent skills and M001-ROADMAP.md |
| Architecture | HIGH | Four-layer structure verified against existing codebase and M001-CONTEXT.md |
| Pitfalls | HIGH | Pitfalls derived from direct analysis of existing artifacts and the one existing meta skill |

**Overall confidence:** HIGH

### Gaps to Address

- **`/optimize-agent` scope:** Is this command in S08 or deferred? Requires an `/elvis-agent-optimizer` skill in S07-C if included. Resolve before S07-C begins.
- **`/elvis-pattern-assimilation` placement:** Borg's agent definition references this skill, but it has no command equivalent and no current use case. Confirm deferral to v2 before finalizing S07 file list.
- **Command count confirmation:** 10 commands assumes `/optimize-agent` is included. If deferred, the count is 9. The command list should be confirmed before S08 starts.

## Sources

### Primary (HIGH confidence)
- `skills/meta/elvis-skill-generator.md` — Canonical reference implementation for meta skill pattern, two-phase approval gate, safeguard quartet
- `agent/q.md`, `agent/borg.md`, `agent/picard.md`, `agent/troi.md`, `agent/uhura.md` — Meta agent definitions; establish which skills each agent expects and what constraints apply
- `templates/skill-template.md` — Binding format contract for all 9-section skill files
- `.gsd/milestones/M001/M001-CONTEXT.md` — R004 safeguard requirements, naming conventions, out-of-scope constraints
- `.gsd/milestones/M001/M001-ROADMAP.md` — S07/S08 boundary, file inventory
- OpenClaw docs (https://docs.openclaw.ai/concepts/system-prompt) — System prompt injection behavior, skill loading
- OpenClaw DeepWiki (https://deepwiki.com/openclaw/openclaw/6.4-skills-system) — YAML frontmatter, three-tier skill loading

### Secondary (MEDIUM confidence)
- Jason Liu, Context Engineering: Slash Commands vs Subagents — Command routing architecture rationale
- HuggingFace: Design Patterns for Agentic Workflows — Orchestrator-Workers and Evaluator-Optimizer pattern framing
- ByteBridge: Human-in-the-Loop vs Human-on-the-Loop — Approval gate governance patterns

---
*Research completed: 2026-03-14*
*Ready for roadmap: yes*
