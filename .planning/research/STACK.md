# Stack Research

**Domain:** Markdown-based AI Agent Factory — Meta-Agent Layer + Command System
**Researched:** 2026-03-14
**Confidence:** HIGH (existing system patterns are observable; OpenClaw platform behavior verified via official docs and community sources)

---

## Context

This is not a greenfield technology decision. The project is 81% complete: 81 skills, 16 agents, 16 identities, 10 souls already built in a pure-Markdown system with no runtime code. The "stack" here means: **patterns, conventions, and structural decisions** for the 14 missing meta skills and 10 commands. There are no npm packages, no frameworks, no code.

The platform target is OpenClaw. Its skill system is Markdown files injected into the agent's system prompt on demand. Its command system is Markdown files that become the agent's instructions when invoked.

---

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Markdown (CommonMark) | — | All skill, command, soul, identity, agent definitions | OpenClaw's native format — files are injected directly into system prompt. No conversion layer. |
| YAML front matter | — | Command metadata (name, description, argument-hint) | OpenClaw's command registration uses YAML frontmatter in SKILL.md. Enables platform-native slash command discovery. |
| 9-section skill format | (project-defined) | All meta skills | Already validated over 81 skills. Template exists in `templates/skill-template.md`. Deviating creates inconsistency in the library that Uhura/Borg cannot manage. |
| German language + English technical terms | — | All file content | R011 requirement. Established pattern across all 81 existing skills. Fachbegriffe (Skill, Soul, Agent, Command) stay English. |

### Structural Patterns (the actual "stack" decisions)

| Pattern | What It Is | Why Use It |
|---------|-----------|------------|
| Generator-first meta skills | Skills that produce other skills/agents/identities/souls as their output | Q, Borg, and Picard agents are already defined referencing skills like `/elvis-agent-generator`, `/elvis-agent-creator`, `/elvis-concept-design` — these skills do not yet exist. The generator pattern is the architecture's growth mechanism. |
| Two-phase execution (Plan → Approve → Execute) | Every autonomous skill presents a plan and waits for explicit operator confirmation before creating or modifying anything | The existing `/elvis-skill-generator` establishes this as the canonical pattern. Approval gate in step 2 (overview table) before step 3 (generation) is the proven safeguard. All S07 meta skills must follow this. |
| Explicit safeguard quartet | Every autonomous skill declares: Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis in the Einschränkungen section | R004 requirement. Already implemented in all 5 autonomous agents (Borg, Q, Picard, Troi, Uhura). Skills that serve these agents must mirror their constraints at the skill level. |
| Command-as-router | Command files dispatch to the correct agent + skill pair; they do not contain logic themselves | OpenClaw slash commands become the agent's instructions. A command like `/build-agent` should route to Picard + the relevant skill chain, not re-implement agent creation logic. Separation prevents duplication. |
| Read-only analysis skills | Troi and Uhura skills operate in read-only mode by default; any write action requires explicit operator confirmation | Already defined in Troi's agent constraints ("Analyse-Ergebnisse sind read-only"). Skills for these agents must enforce this at the Einschränkungen level. |

### Supporting Conventions

| Convention | Purpose | When to Use |
|-----------|---------|-------------|
| `/elvis-*` skill naming | All skills callable via OpenClaw command interface | Every skill in the meta category — no exceptions. R006. |
| `skills/meta/` placement | All generator/system/autonomous skills live here | Any skill whose primary function is creating, auditing, or managing the ecosystem itself (not producing external content or analysis for the operator's business). |
| `commands/` placement | All command definitions live here | Files that are invoked as `/[command-name]` top-level commands, not `/elvis-*` skills. Commands dispatch; skills execute. |
| Agent-skill cross-reference in Abhängigkeiten | Each meta skill references the agent it belongs to | Enables Uhura's routing table maintenance and ensures no orphaned skills. |
| Max-limit ladder | Generator = max 10, Expander (Borg) = max 5, Orchestrator (Picard) = max 3 parallel delegations | Already established in agent definitions. Skills must not exceed the ceiling set by their parent agent's constraints. |

---

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Code blocks with executable logic in skill files | OpenClaw injects Markdown as instructions, not as executable code. R014 (Out of Scope: Ausführbarer Code). Any "code" in skill files is illustrative example only. | Concrete procedural natural-language steps in Ausführungsschritte that describe what the agent does, not runnable scripts |
| Abstract execution steps ("Analysiere das System") | These pass format validation but fail in practice — the agent has no concrete action to take. The existing 81 skills establish the D006 standard (Menge + Format + Zeitangabe). | Steps like "Erstelle eine Tabelle mit 3 Spalten (Name, Kategorie, Status) für alle Skills in `skills/meta/` — max. 15 Einträge" |
| Catch-all autonomous behavior without stop conditions | Meta skills that loop indefinitely or generalize too broadly become unpredictable. The safeguard quartet exists because this was identified as a critical risk (CONTEXT.md Risiken). | Explicit Stop-Bedingung in every autonomous skill — "stoppt wenn X" must name a concrete exit condition |
| Separate command logic for routing vs. execution | If command files contain skill-level logic, they become unsynchronized with skills when skills are updated. | Commands contain only: trigger context, which agent to activate, which skill to call, what input format to expect |
| New skill sections beyond the 9-section format | Tempting for meta skills to add "Meta-Konfiguration" sections — breaks Uhura's format validation, breaks the skill template. | Use the Einschränkungen section for safeguard declarations and the Strategie section for meta-context |

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| Two-phase Plan→Approve→Execute | Single-pass autonomous generation | Never for this system — OpenClaw has no native sandboxing. The approval gate is the only circuit breaker before the agent writes files or gives instructions that cannot be undone. |
| Command-as-router (thin command files) | Command files with embedded skill logic | If the project had only 2-3 commands and no dedicated skill layer. At 10 commands + 14 meta skills, the routing separation prevents duplication. |
| Explicit safeguard quartet in Einschränkungen | Implicit safeguards in Strategie section | Never — Strategie is narrative, Einschränkungen is checked. The operator reads Einschränkungen to know what the skill will and won't do. Hiding safeguards in Strategie means they get skipped. |
| German language throughout | English for meta/technical skills | If the operator base were international. Current project is single-operator (Mario), German is specified in R011, and all 81 existing skills are German. Mixing languages in the meta layer creates cognitive overhead. |

---

## Stack Patterns by Variant

**If the skill creates new ecosystem files (generator pattern — Q, Borg):**
- Cap at max 10 new objects per run
- Require overview-table confirmation before any object is generated
- Output: generated content in chat only (no auto-save) + instruction to manually copy to correct path
- Reason: OpenClaw agents operate in the conversation — they cannot write to disk without explicit tool calls. The "no auto-save" pattern from `/elvis-skill-generator` is architecturally correct, not a limitation.

**If the skill audits or analyzes existing ecosystem files (inspector pattern — Troi, Uhura):**
- Read-only by default
- Output: structured report (Markdown table format) with findings only
- Write actions (archiving, reorganizing) require a separate explicit invocation
- Reason: Inspection and modification are different cognitive modes. Separating them prevents "analysis that accidentally restructures your library."

**If the skill orchestrates other agents/skills (orchestrator pattern — Picard):**
- Cap at max 3 parallel delegations
- Each delegation must name the target agent AND the target skill
- Consolidation step is mandatory — raw delegation outputs without synthesis are useless
- Reason: Picard's agent definition already establishes this ceiling. Skills serving Picard must not exceed it.

**If the file is a command (not a skill):**
- One command = one primary agent + one skill chain
- Command file contains: trigger description, input expectations, which agent to activate, which skill to invoke
- No logic, no conditions, no branching in the command file itself
- Reason: Commands in OpenClaw become the agent's system instructions at invocation time. A command that contains conditional routing logic becomes a prompt that asks the agent to decide its own routing — this degrades to unpredictable behavior.

---

## Version Compatibility

| Pattern | Compatible With | Notes |
|---------|----------------|-------|
| 9-section skill format | All 81 existing skills + templates | Non-negotiable. The skill-template.md is the contract. |
| `/elvis-*` naming | All existing agent `Primäre Skills` references | Agent definitions reference skills by name. A skill named differently than what the agent references creates dead links — detectable by `/elvis-library-audit`. |
| Approval-gate in Schritt 2 | Existing `/elvis-skill-generator` pattern | S07 skills must mirror this — operators learn the "Schritt 2 = confirmation" expectation from the existing skill. |
| `commands/` flat directory | M001-CONTEXT.md folder spec | Commands are flat files, not nested. CONTEXT.md shows `commands/` at root level with no subdirectories. |

---

## Meta Skill Inventory (what S07 must build)

Based on agent definitions referencing non-existent skills:

| Skill Name | Parent Agent | Pattern | Priority |
|-----------|-------------|---------|---------|
| `/elvis-agent-generator` | Q | Generator | High — Q's primary skill, referenced in agent def |
| `/elvis-agent-creator` | Q | Generator | High — referenced in Q agent def |
| `/elvis-concept-design` | Q | Generator | Medium — Q's experimental/PoC skill |
| `/elvis-identity-generator` | Q/Borg | Generator | High — needed for "agent in 2 minutes" workflow |
| `/elvis-soul-generator` | Q/Borg | Generator | High — completes the generation layer |
| `/elvis-skill-expander` | Borg | Generator | High — Borg's core library-growth skill |
| `/elvis-library-audit` | Uhura/Troi | Inspector | High — validates all skill dependencies |
| `/elvis-system-analyzer` | Troi | Inspector | High — Troi's primary skill, referenced in agent def |
| `/elvis-library-manager` | Uhura | Inspector + Writer | Medium — library structure management |
| `/elvis-orchestrator` | Picard | Orchestrator | High — Picard's coordination skill |
| `/elvis-agent-team-builder` | Picard | Orchestrator | Medium — assembles agent teams for tasks |
| `/elvis-ecosystem-health` | Troi | Inspector | Medium — system-wide health check |
| `/elvis-skill-validator` | Uhura | Inspector | Medium — format compliance checking |
| `/elvis-template-generator` | Q | Generator | Low — generates new templates |

Note: `/elvis-skill-generator` already exists in `skills/meta/`. Do not recreate it.

## Command Inventory (what S08 must build)

Based on CONTEXT.md and agent capabilities:

| Command | Routes To | Purpose |
|---------|-----------|---------|
| `/build-agent` | Picard + Q | Full agent creation workflow |
| `/generate-skills` | Q + Borg | Skill generation batch run |
| `/expand-library` | Borg | Add skills to fill identified gaps |
| `/audit-library` | Uhura + Troi | Inspect library for issues |
| `/analyze-system` | Troi | System health check |
| `/manage-library` | Uhura | Library reorganization |
| `/create-concept` | Q | PoC / experimental definition |
| `/delegate-task` | Picard | Multi-agent task delegation |
| `/validate-skills` | Uhura | Format compliance run |
| `/assemble-team` | Picard | Build agent team for a goal |

---

## Sources

- OpenClaw official docs (https://docs.openclaw.ai/concepts/system-prompt) — System prompt injection behavior, bootstrap file handling, skills format. Confidence: HIGH.
- OpenClaw DeepWiki Skills System (https://deepwiki.com/openclaw/openclaw/6.4-skills-system) — Three-tier skill loading, YAML frontmatter, gating rules. Confidence: HIGH.
- Jason Liu, Context Engineering: Slash Commands vs Subagents (https://jxnl.co/writing/2025/08/29/context-engineering-slash-commands-subagents/) — Command routing architecture, context pollution rationale for thin command files. Confidence: HIGH.
- HuggingFace: Design Patterns for Agentic Workflows (https://huggingface.co/blog/dcarpintero/design-patterns-for-building-agentic-workflows) — Orchestrator-Workers, Evaluator-Optimizer, Parallelization patterns. Confidence: MEDIUM (academic framing applied to Markdown system).
- ByteBridge: Human-in-the-Loop vs Human-on-the-Loop (https://bytebridge.medium.com/from-human-in-the-loop-to-human-on-the-loop-evolving-ai-agent-autonomy-c0ae62c3bf91) — Approval gate patterns, governance without micromanagement. Confidence: MEDIUM.
- Existing project files: `skills/meta/elvis-skill-generator.md`, `agent/q.md`, `agent/borg.md`, `agent/picard.md`, `agent/troi.md`, `agent/uhura.md`, `templates/skill-template.md` — Primary source for all pattern recommendations. Confidence: HIGH (observable ground truth).
- M001-CONTEXT.md — Skill format spec, safeguard requirements, command system scope. Confidence: HIGH (binding project spec).

---
*Stack research for: OpenClaw Meta Maker — Meta-Agent Layer + Command System (S07/S08)*
*Researched: 2026-03-14*
