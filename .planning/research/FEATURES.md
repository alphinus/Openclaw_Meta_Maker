# Feature Research

**Domain:** Meta-Agent System + Command Layer for Markdown-based AI Agent Ecosystem
**Researched:** 2026-03-14
**Confidence:** HIGH (derived from existing codebase, spec documents, agent definitions — no external research needed)

---

## Context

This is a subsequent milestone, not a greenfield project. 81 of ~100 skills already exist across 6 domains (growth, content, research, strategy, automation, analysis). The remaining work is:

- ~14 Meta Skills (skills/meta/) — Generator, Autonomous, and System categories
- ~10 Command definitions (commands/) — operator-facing shortcut layer
- Safeguards on all autonomous agents (Borg, Q, Picard, Troi, Uhura)

The "ecosystem" here is the meta-agent pattern: agents that operate on other agents, generators that create system artifacts, and a command layer that abstracts orchestration complexity from the operator.

---

## Feature Landscape

### Table Stakes (Users Expect These)

These are required for the meta-agent layer to be considered complete. Missing any of these makes the autonomous system non-functional or the command layer unusable.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Skill Generator (`/elvis-skill-generator`) | Entry point for all skill creation — meta-layer is useless without it | MEDIUM | Already exists as the one meta skill in S07 scope. Must be at quality parity with 81 existing skills. |
| Agent Generator (`/elvis-agent-generator`) | Q's primary capability — "create new agents" is Q's entire reason for existing | MEDIUM | Outputs agent.md in 7-section format (Name, Mission, Capabilities, Operating Loop, Constraints, Soul, Skills). Requires S03 agent definitions as format reference. |
| Soul Generator (`/elvis-soul-generator`) | Foundational artifact — new agents need new souls, not just recycled ones | LOW | Simpler than agent generator. 10 souls already exist as format templates. |
| Identity Generator (`/elvis-identity-generator`) | Completes the "new agent in < 2 minutes" promise — soul + identity + agent + skills | LOW | Most constrained scope: outputs a character persona, not behavioral logic. |
| Skill Expander (`/elvis-skill-expander`) | Borg's core function — gap detection + expansion is distinct from single-skill generation | MEDIUM | Gap analysis logic is what differentiates this from skill-generator. Requires library scan step. |
| System Analyzer (`/elvis-system-analyzer`) | Troi's table-stakes skill — "detect system weaknesses" is Troi's entire mission | MEDIUM | Read-only output. No mutations. Requires cross-referencing all agents, skills, dependencies. |
| Library Manager (`/elvis-library-manager`) | Uhura's primary skill — routing table maintenance is infrastructure for the command system | MEDIUM | Manages the command-routing relationship between /elvis-* skills and agents. |
| Agent Creator (`/elvis-agent-creator`) | Distinct from agent-generator: assembly of existing components vs. generating new ones from scratch | MEDIUM | Combines existing soul + identity + agent + skill list into a deployable agent. Under 2-minute workflow requirement. |
| Command Router (`/elvis-command-router`) | Infrastructure skill for the command layer — S08 depends on it | LOW | Routes `/build-agent`, `/generate-skills`, etc. to the correct meta-skill invocations. |
| Safeguards on all autonomous skills | Max-Limit + Approval-Gate + Stop-Bedingung + Rollback-Hinweis required per R004 | LOW | Already present in `/elvis-skill-generator`. Pattern must be replicated consistently in every meta skill. |
| `/build-agent` command | Primary operator entry point — the "< 2 minutes" promise depends on this | LOW | Invokes: identity selection → soul assignment → skill selection → agent assembly. No generation, pure orchestration. |
| `/generate-skills` command | Most frequent use case after setup — content creators need new skills regularly | LOW | Delegates to `/elvis-skill-generator` with category parameter. |
| `/expand-library` command | Borg-invocation shortcut — gap analysis + skill addition in one command | LOW | Delegates to `/elvis-skill-expander`. |
| `/analyze-system` command | Troi-invocation shortcut — health check on demand | LOW | Delegates to `/elvis-system-analyzer`. Read-only output. |
| `/create-skill` command | Single-skill creation shortcut, lower friction than `/generate-skills` | LOW | Minimal wrapper — delegates directly to `/elvis-skill-generator` for 1 skill. |

### Differentiators (Competitive Advantage)

These are what make the OpenClaw Meta Maker genuinely useful rather than just formally complete.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Two-phase approval gate (plan → confirm → execute) | Prevents silent generation of wrong artifacts. Operator always sees the plan before any file is produced. | LOW | Already implemented in `/elvis-skill-generator`. Must be the standard pattern in all generator skills — not optional. |
| Explicit Max-Limit per autonomous agent | Without limits, Borg and Q can generate unbounded output in a single session. Limits create safe, auditable batches. | LOW | Borg: max 5 skills/run. Q: max 3 objects/run. Picard: max 3 parallel delegations. Already defined in agent files — skills must enforce the same limits. |
| Read-only boundary for Troi | System analysis that cannot mutate state is safe to run at any time. Makes health checks zero-risk. | LOW | Anti-mutation constraint must be in Troi's skill Einschränkungen section. Explicit. Not implied. |
| Draft-first workflow for Q | New objects created as drafts, only promoted after operator approval. Prevents partial-state contamination. | LOW | `/elvis-agent-creator` vs `/elvis-agent-generator` distinction: creator assembles existing parts (safe), generator creates new parts (needs draft-gate). |
| Command layer that names what it does, not how | `/build-agent` vs `/elvis-agent-creator` — operator commands express intent, not implementation. | LOW | All 10 commands route to meta-skills. The operator never needs to know which underlying skill runs. |
| `/optimize-agent` command | Agent improvement without full rebuild — swap soul, add/remove skills, adjust constraints | MEDIUM | No direct meta-skill equivalent — requires new skill or composition of `/elvis-system-analyzer` + `/elvis-agent-creator`. Needs a decision: build dedicated `/elvis-agent-optimizer` skill or compose. |
| Pattern assimilation skill (`/elvis-pattern-assimilation`) | Borg's differentiating capability: import patterns from external sources (other frameworks, structures) and normalize them to the OpenClaw format | HIGH | Listed as a Borg primary skill in agent/borg.md. Hardest meta skill to define concretely. Risk: too abstract. |
| Concept design skill (`/elvis-concept-design`) | Q can sketch frameworks, not just complete artifacts. Useful for exploring new skill categories before committing. | MEDIUM | Listed in agent/q.md. Lower stakes than agent/skill generation — no format compliance required. |

### Anti-Features (Commonly Requested, Often Problematic)

These are features that seem natural extensions but should be deliberately excluded from this milestone.

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| Automatic git commit from within a skill | Feels complete — skill generates file AND commits it | The system is pure Markdown. Skills produce text output in chat. Automatic commits bypass operator review and are impossible in pure Markdown format. Adding this creates a runtime dependency that violates the "no executable code" constraint. | Every skill ends with an explicit instruction to the operator: "Kopiere den Inhalt in [dateipfad] und führe git commit aus." Already implemented in `/elvis-skill-generator`. |
| Inter-skill API calls (skill calling skill) | Chaining feels powerful — skill generator calls skill expander automatically | Markdown skills cannot execute each other. This is a Markdown-format system, not a runtime. Describing inter-skill calls creates false expectations about what the system can do. | Commands serve this role at the operator level: `/build-agent` describes the multi-step workflow. The operator executes each step. |
| Versioning and rollback of individual skills | Library management feels incomplete without version history | Git is the version control system. Building a parallel versioning layer inside Markdown files duplicates git's role, adds complexity, and creates drift. | Rollback-Hinweis in every skill points to git: "Rückgängig durch `git revert` auf den entsprechenden Commit." |
| Cross-agent conflict resolution at runtime | Picard orchestrates — feels natural he should resolve skill conflicts automatically | Picard's Operating Loop already covers conflict resolution, but only in the planning/description sense. Real runtime conflict resolution requires code. In a Markdown system, Picard's skill produces a delegation plan; the operator executes and detects conflicts. | Picard's skills produce structured delegation plans with explicit dependency ordering. Conflicts are surfaced in the plan output for operator decision. |
| Natural language command parsing | `/build-agent create a growth-focused Kirk variant` vs. just `/build-agent` | Requires runtime NLP. This is a Markdown system. The commands are structured prompts, not a CLI. Natural language parsing belongs to the AI model layer (OpenClaw), not the skill definitions. | Each command definition includes a structured input template that guides the operator to provide the right parameters. |
| Skill quality scoring / automated rating | Library manager could auto-rate skills | Quality is subjective and context-dependent. Automated scoring would require runtime execution and produces false precision. Worse: a bad score metric could discourage good skills. | Verifikation section in every skill provides human-readable acceptance criteria. The operator judges quality at import time. |

---

## Feature Dependencies

```
[/elvis-skill-generator] (exists)
    └──enables──> [/build-agent command]
    └──enables──> [/generate-skills command]
    └──enables──> [/create-skill command]

[/elvis-agent-generator]
    └──requires──> [agent/*.md] (S03 — complete)
    └──requires──> [templates/agent-template.md] (S01 — complete)
    └──enables──> [/create-agent command]

[/elvis-soul-generator]
    └──requires──> [soul/*.md] (S02 — complete)
    └──enables──> [/create-soul command]

[/elvis-identity-generator]
    └──requires──> [identity/*.md] (S02 — complete)
    └──enables──> [/create-identity command]

[/elvis-agent-creator]
    └──requires──> [/elvis-agent-generator] (or soul + identity + agent assembly without generation)
    └──requires──> [/elvis-soul-generator]
    └──requires──> [/elvis-identity-generator]
    └──enables──> [/build-agent command]

[/elvis-skill-expander]
    └──requires──> [/elvis-skill-generator]
    └──enables──> [/expand-library command]

[/elvis-system-analyzer]
    └──requires──> [all agent/*.md] (S03 — complete)
    └──requires──> [all skills/*] (S04-S06 — complete)
    └──enables──> [/analyze-system command]

[/elvis-library-manager]
    └──requires──> [/elvis-system-analyzer]
    └──enables──> [/build-library command]

[/elvis-command-router]
    └──requires──> [all meta skills above]
    └──enables──> [all 10 commands]
    └──must exist before S08]

[S08 commands]
    └──all require──> [/elvis-command-router] (S07)
    └──all require──> [all meta skills] (S07)
```

### Dependency Notes

- **`/elvis-agent-creator` is the key orchestration skill:** It is the only meta skill that combines multiple other meta-skill outputs. It must be the last generator skill defined in S07.
- **`/elvis-command-router` is the S07/S08 boundary artifact:** Nothing in S08 can be written until command-router exists. This is why S08 depends on S07.
- **`/optimize-agent` command has no direct meta-skill backing:** Either a new `/elvis-agent-optimizer` skill needs to be created in S07, or `/optimize-agent` must route to a composition of `/elvis-system-analyzer` + manual operator step + `/elvis-agent-creator`. The simpler path is a dedicated optimizer skill.
- **`/elvis-pattern-assimilation` is a Borg skill with no command equivalent:** It is a direct-invocation skill, not exposed via the command layer. Low priority within S07 if skill count needs trimming.

---

## MVP Definition

This milestone has a fixed, pre-defined scope (S07 + S08 from the roadmap). "MVP" here means: what is the minimum set of S07 meta skills that unlocks the full command layer in S08?

### Launch With (v1 = S07 + S08 complete)

- [ ] `/elvis-skill-generator` — already exists, verify format compliance
- [ ] `/elvis-agent-generator` — Q's primary output capability
- [ ] `/elvis-soul-generator` — needed by `/build-agent` and `/create-soul`
- [ ] `/elvis-identity-generator` — needed by `/build-agent` and `/create-identity`
- [ ] `/elvis-agent-creator` — the assembly skill that makes the < 2 min promise real
- [ ] `/elvis-skill-expander` — Borg's gap-detection capability
- [ ] `/elvis-system-analyzer` — Troi's read-only health check
- [ ] `/elvis-library-manager` — Uhura's routing table maintenance
- [ ] `/elvis-command-router` — infrastructure for all commands
- [ ] All 10 commands in `commands/` — complete command layer

Total: 9 meta skills (1 exists) + 10 commands = 18 files for S07+S08.

### Add After Validation (v1.x)

- [ ] `/elvis-concept-design` — Q's experimental framework sketching. Not needed for any command. Add when operator requests it.
- [ ] `/elvis-pattern-assimilation` — Borg's import capability. Only needed when external patterns exist to assimilate. Defer until first real use case appears.
- [ ] `/elvis-agent-optimizer` — Supports `/optimize-agent` command. Build if `/optimize-agent` command is included in S08.

### Future Consideration (v2+)

- [ ] Additional Soul archetypes beyond the 10 existing — defer until operator encounters a use case the current 10 souls cannot cover.
- [ ] Cross-ecosystem import (import skills from other agent ecosystems) — requires `/elvis-pattern-assimilation` plus format normalization logic. Complex, speculative value.

---

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| `/elvis-agent-generator` | HIGH | LOW | P1 |
| `/elvis-soul-generator` | HIGH | LOW | P1 |
| `/elvis-identity-generator` | HIGH | LOW | P1 |
| `/elvis-agent-creator` | HIGH | MEDIUM | P1 |
| `/elvis-skill-expander` | HIGH | MEDIUM | P1 |
| `/elvis-system-analyzer` | HIGH | MEDIUM | P1 |
| `/elvis-library-manager` | MEDIUM | MEDIUM | P1 |
| `/elvis-command-router` | HIGH | LOW | P1 |
| All 10 commands (S08) | HIGH | LOW | P1 |
| `/elvis-concept-design` | MEDIUM | LOW | P2 |
| `/elvis-agent-optimizer` | MEDIUM | MEDIUM | P2 |
| `/elvis-pattern-assimilation` | LOW | HIGH | P3 |

**Priority key:**
- P1: Required for S07/S08 milestone completion
- P2: Should have — add if skill count allows (target: ~14-15 meta skills total)
- P3: Nice to have, future consideration

---

## Competitor Feature Analysis

This is not a traditional software product with competitors. The relevant comparison is: how do other AI agent prompt-systems handle meta-agent and command features?

| Feature | Auto-GPT / similar runtime systems | LangGraph / code-based agent frameworks | Our Approach (OpenClaw Markdown) |
|---------|-------------------------------|----------------------------------------|----------------------------------|
| Agent creation | Programmatic — agents defined in code | Nodes defined in graph DSL | Markdown templates — human-readable, no runtime |
| Skill/tool registration | Runtime registration, function signatures | Tool nodes with typed inputs | Skill files with natural language steps |
| Command routing | Code dispatch table | Graph edge routing | Command Markdown files referencing meta-skills |
| Safeguards | Environment-level (sandboxing, rate limits) | Code-level (guards, validators) | Constraint sections in Markdown — enforced by the LLM reading the skill |
| Audit trail | Logs | Execution traces | Git history + approval-gate output in chat |
| Portability | Tied to runtime | Python/JS ecosystem | Any system that can import Markdown (OpenClaw, Claude, others) |

**Implication:** The Markdown approach trades runtime enforcement for portability and readability. Safeguards must be extremely explicit in the Einschränkungen section because there is no code layer to enforce them — the LLM is the runtime.

---

## Sources

- `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md`, `agent/picard.md` — agent definitions confirm which meta-skills each agent expects to invoke
- `.gsd/milestones/M001/M001-ROADMAP.md` — S07 boundary map defines exact meta-skill file list
- `.gsd/milestones/M001/M001-CONTEXT.md` — R004 safeguard requirements, 6-layer system definition
- `skills/meta/elvis-skill-generator.md` — existing meta skill sets quality and safeguard pattern
- `.planning/PROJECT.md` — "no executable code" constraint, naming convention, language rules

---

*Feature research for: Meta-Agent System + Command Layer (OpenClaw Meta Maker, M001 S07+S08)*
*Researched: 2026-03-14*
