# Architecture Research

**Domain:** Meta-Agent System + Command Routing Layer for Markdown-Based Agent Ecosystem
**Researched:** 2026-03-14
**Confidence:** HIGH (based on existing codebase + spec analysis)

## Standard Architecture

### System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     COMMAND LAYER                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ /build-agent │  │/generate-    │  │/analyze-     │  ...  │
│  │              │  │ skills       │  │ system       │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
│         └─────────────────┼─────────────────┘               │
│                           ↓ (command routes to agent+skill)  │
├──────────────────────────────────────────────────────────────┤
│                  META-AGENT LAYER                            │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐ │
│  │ Picard │  │   Q    │  │  Borg  │  │  Troi  │  │ Uhura  │ │
│  │Orchest.│  │Creator │  │Expander│  │Analyzer│  │Library │ │
│  └────┬───┘  └────┬───┘  └────┬───┘  └────┬───┘  └────┬───┘ │
│       └───────────┴───────────┴───────────┴───────────┘     │
│                           ↓                                  │
├──────────────────────────────────────────────────────────────┤
│                   META-SKILL LAYER (skills/meta/)            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │skill-generator│ │agent-generator│ │ system-      │  ...  │
│  │soul-generator │ │identity-gen. │ │ analyzer     │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│                           ↓                                  │
├──────────────────────────────────────────────────────────────┤
│               BASE SKILL + AGENT LAYERS (existing)           │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌──────────┐  │
│  │ skills/   │  │ agent/    │  │ identity/ │  │  soul/   │  │
│  │growth/    │  │ kirk.md   │  │ scotty.md │  │creator.md│  │
│  │content/   │  │ spock.md  │  │ data.md   │  │automation│  │
│  │research/  │  │ ...       │  │ ...       │  │  .md ... │  │
│  │strategy/  │  └───────────┘  └───────────┘  └──────────┘  │
│  │automation/│                                               │
│  │analysis/  │                                               │
│  └───────────┘                                               │
└──────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Location |
|-----------|----------------|----------|
| Command definitions | High-level operator entry points, each maps to one agent + one or more skills | `commands/*.md` |
| Command router skill | Resolves which agent and skill(s) a command invokes | `skills/meta/elvis-command-router.md` |
| Meta agents (Picard, Q, Borg, Troi, Uhura) | Orchestrate, generate, expand, analyze, and manage the ecosystem | `agent/*.md` (already exists) |
| Generator skills | Create new system artifacts (skills, agents, souls, identities) following templates | `skills/meta/elvis-*-generator.md` |
| Expander/Analyzer/Manager skills | Expand library, analyze system health, manage routing tables | `skills/meta/elvis-skill-expander.md`, `elvis-system-analyzer.md`, `elvis-library-manager.md` |
| Agent creator skill | Assembles complete agents from soul + identity + skill selection | `skills/meta/elvis-agent-creator.md` |
| Base skills (81 existing) | Domain capabilities invoked by agents | `skills/growth|content|research|strategy|automation|analysis/` |
| Agents (16 existing) | Domain specialists with defined missions and primary skills | `agent/*.md` |
| Souls (10 existing) | Philosophical operating frameworks | `soul/*.md` |
| Identities (16 existing) | Character context, communication style | `identity/*.md` |
| Templates (4 existing) | Canonical formats that all generators must use | `templates/*.md` |

## Recommended Project Structure

```
openclaw-meta-maker/
├── soul/                        # 10 Soul philosophies (complete)
├── identity/                    # 16 Star Trek identities (complete)
├── agent/                       # 16 Agent definitions (complete)
├── skills/
│   ├── growth/                  # ~15 Skills (complete)
│   ├── content/                 # ~15 Skills (complete)
│   ├── research/                # ~15 Skills (complete)
│   ├── strategy/                # ~15 Skills (complete)
│   ├── automation/              # ~10 Skills (complete)
│   ├── analysis/                # ~10 Skills (complete)
│   └── meta/                    # ~9 Skills (S07 — to build)
│       ├── elvis-skill-generator.md      # exists
│       ├── elvis-agent-generator.md      # to build
│       ├── elvis-soul-generator.md       # to build
│       ├── elvis-identity-generator.md   # to build
│       ├── elvis-agent-creator.md        # to build
│       ├── elvis-skill-expander.md       # to build
│       ├── elvis-system-analyzer.md      # to build
│       ├── elvis-library-manager.md      # to build
│       └── elvis-command-router.md       # to build (required by S08)
├── commands/                    # 10 Command definitions (S08 — to build)
│   ├── build-agent.md
│   ├── generate-skills.md
│   ├── expand-library.md
│   ├── analyze-system.md
│   ├── optimize-agent.md
│   ├── create-soul.md
│   ├── create-identity.md
│   ├── create-skill.md
│   ├── build-library.md
│   └── create-agent.md
└── templates/                   # 4 Templates (complete)
```

### Structure Rationale

- **skills/meta/:** Meta capabilities are skills, not agents — they follow the identical 9-section format. This is consistent with the existing pattern: agents *invoke* skills, skills *do* the work. A meta skill is simply a skill whose output is another system artifact.
- **commands/:** Commands are the public API of the ecosystem. They are one level of abstraction above the agent layer — each command declares which agent is responsible and which skills are invoked. This decouples the operator from knowing internal agent details.
- **No new top-level directories needed:** The full structure is already defined in M001-CONTEXT. The architecture is closed — only the `meta/` skills directory and `commands/` directory need population.

## Architectural Patterns

### Pattern 1: Generator Skill — Template-Constrained Creation

**What:** A meta skill that produces a new system artifact (skill, agent, soul, identity) strictly following a template. Output is always a fully populated markdown document in the established 9-section format. The skill never invents new sections.

**When to use:** Any time the system needs to create a new instance of a defined artifact type (skill, soul, identity, agent).

**Trade-offs:** Highly constrained output ensures consistency across ~100+ files; limits flexibility if requirements change mid-generation.

**Example:**
```
Invocation: /elvis-agent-generator
Input: Agent name, mission description, domain, soul reference
Output: Complete agent/*.md following agent-template.md
Key constraint: Approval-Gate before writing, max 3 agents per run
```

### Pattern 2: Safeguarded Autonomous Skill

**What:** A meta skill that can affect the ecosystem's own structure (expand, analyze, reorganize). Requires four explicit safeguards: Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis. These are non-negotiable per R004.

**When to use:** Any skill assigned to the autonomous meta agents (Borg, Q, Picard, Troi, Uhura). Applied to: elvis-skill-expander, elvis-system-analyzer, elvis-library-manager, elvis-agent-creator, elvis-command-router.

**Trade-offs:** Safeguards add friction to the operator interaction loop but prevent runaway generation. For a Markdown-only system, the "worst case" is redundant files — but safeguards are still required by the spec.

**Example safeguard structure:**
```markdown
## Einschränkungen
- **Max-Limit:** Maximal X Aktionen pro Durchlauf
- **Approval-Gate:** Operator-Bestätigung vor [Aktion]
- **Stop-Bedingung:** Endet wenn [condition]
- **Rollback-Hinweis:** [How to undo]
```

### Pattern 3: Command as Routing Declaration

**What:** A command file in `commands/` is not a skill and not an agent. It is a declarative routing document that answers: "When the operator says `/build-agent`, which agent handles it, and which skills are invoked in which order?" Commands are the single lookup table that binds the command name to the execution path.

**When to use:** For all 10 command definitions in S08.

**Trade-offs:** Keeping commands as separate files (rather than embedded in agents) makes routing explicit and auditable. The downside is an extra lookup step, but in a Markdown-only system this is negligible — OpenClaw handles the invocation chain.

**Example structure:**
```markdown
# Command: /build-agent

## Beschreibung
Erstellt einen vollständigen neuen Agenten im OpenClaw-Ökosystem.

## Verantwortlicher Agent
agent/q.md

## Invozierte Skills (in Reihenfolge)
1. /elvis-agent-generator — Generiert die Agent-Definition
2. /elvis-soul-generator (optional) — Falls neuer Soul benötigt
3. /elvis-identity-generator (optional) — Falls neue Identity benötigt

## Operator-Input benötigt
- Name des neuen Agenten
- Mission (1-2 Sätze)
- Ziel-Domäne
- Soul-Präferenz (oder "neu generieren")

## Safeguard-Hinweis
Q's Constraints gelten: Max. 3 Objekte pro Durchlauf, Approval-Gate vor Abschluss.
```

## Data Flow

### Command Invocation Flow

```
Operator: /build-agent [context]
    ↓
commands/build-agent.md
    ↓ (declares responsible agent)
agent/q.md (Q — Agent Creator)
    ↓ (invokes via /elvis-*)
skills/meta/elvis-agent-generator.md
    ↓ (reads)
templates/agent-template.md
    ↓ (approval-gate pause)
Operator confirms
    ↓
New agent/*.md produced as output text
```

### Meta Skill Self-Reference Flow

```
Operator: /generate-skills [requirements]
    ↓
commands/generate-skills.md
    ↓
agent/borg.md (Skill Expander)
    ↓
skills/meta/elvis-skill-generator.md (already exists)
    ↓ (reads)
templates/skill-template.md
    ↓ (produces)
New skills/[domain]/elvis-*.md content
```

### System Analysis Flow

```
Operator: /analyze-system
    ↓
commands/analyze-system.md
    ↓
agent/troi.md (System Analyzer)
    ↓
skills/meta/elvis-system-analyzer.md
    ↓ (reads all existing skills/agents)
skills/ + agent/ directories (inputs)
    ↓
Analysis report markdown (output, read-only — no writes)
```

### Key Data Flows

1. **Generator skills read templates, produce artifact text.** Templates in `templates/` are the authoritative format. Generators never define format — they always defer to templates.
2. **Commands declare routing, agents execute.** A command file answers "who and how." The agent answers "in what order." The skill answers "the actual steps."
3. **Library manager maintains routing tables.** Uhura + elvis-library-manager are responsible for keeping command-to-agent mappings current as new skills are added.

## Component Boundaries: Meta Skills vs. Commands

### Meta Skills (skills/meta/)

- Are invoked with `/elvis-*` like all other skills
- Follow the identical 9-section format as all 81 existing skills
- Produce a specific output artifact (a new skill file, an agent file, an analysis report)
- May be invoked directly by the operator OR by an agent
- Own the generation logic — templates, validation, safeguard enforcement
- **Boundary:** A meta skill knows HOW to generate an artifact. It does not know which command triggered it.

### Commands (commands/)

- Are operator-facing entry points with human-readable names (`/build-agent` not `/elvis-agent-generator`)
- Declare routing: responsible agent + skill invocation sequence
- Require no generation logic — purely declarative
- Each command maps to exactly one primary agent
- **Boundary:** A command knows WHO handles the request and WHAT sequence to follow. It delegates all generation logic to the agent and skills.

### Meta Agents (agent/ — existing, with autonomous behavior)

- Picard: orchestrates multi-agent workflows, delegates to domain specialists
- Q: creates new agents, skills, concepts (creator soul)
- Borg: expands skill library, assimilates new capabilities
- Troi: read-only system analysis, pattern detection
- Uhura: library management, routing table maintenance
- **Boundary:** Agents know WHICH skills to invoke for WHICH goals. They do not define skill execution steps.

## Build Order (Dependencies Between Meta Components)

S07 before S08 is the only hard constraint. Within S07, the following order minimizes forward-reference issues:

### S07 Internal Order

1. **elvis-command-router.md** — Build first. S08 depends on it, and all other meta skills reference routing concepts.
2. **Generator skills (parallel)** — No dependencies between them:
   - elvis-skill-generator.md (already exists — verify completeness)
   - elvis-agent-generator.md
   - elvis-soul-generator.md
   - elvis-identity-generator.md
3. **Composition skill** — Depends on individual generators:
   - elvis-agent-creator.md (assembles soul + identity + agent — references the three generators above)
4. **Autonomous system skills (parallel)** — Depend on generators existing:
   - elvis-skill-expander.md (Borg — expands library, calls skill-generator)
   - elvis-system-analyzer.md (Troi — read-only analysis across all existing skills/agents)
   - elvis-library-manager.md (Uhura — manages routing, calls command-router)

### S08 Internal Order

S08 can be built in any order once S07 is complete, because all 10 commands reference skills and agents that already exist. If any command file is written before `elvis-command-router.md` exists, note the forward reference but it does not block the file's creation.

Recommended: write `commands/build-agent.md` first as the canonical example, then use it as the pattern for the remaining 9 commands.

## Anti-Patterns

### Anti-Pattern 1: Meta Skill Inventing New Sections

**What people do:** A generator skill adds sections not in the template (e.g., "Beispiele", "Changelog") to make generated artifacts richer.
**Why it's wrong:** Breaks format consistency across 100+ files. OpenClaw may parse structure by header names. The binding constraint in PROJECT.md and M001-CONTEXT explicitly forbids inventing new sections.
**Do this instead:** Only the 9 defined sections. If a generator needs to communicate something extra, put it in the output text as a comment or note, not as a new section.

### Anti-Pattern 2: Command Files Containing Execution Logic

**What people do:** Embed detailed step-by-step instructions in a command file to make it self-contained.
**Why it's wrong:** Commands become unmaintainable duplicates of skills. When a skill changes, the command becomes stale. Commands must be routing declarations only.
**Do this instead:** Command files declare agent + skill references. All execution steps live in the skill files.

### Anti-Pattern 3: Autonomous Skills Without All Four Safeguards

**What people do:** Add a Max-Limit but omit Stop-Bedingung or Rollback-Hinweis because the scenario seems simple.
**Why it's wrong:** R004 is non-negotiable per M001-CONTEXT. All four safeguards (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis) are required for Borg, Q, Picard, Troi, Uhura skills.
**Do this instead:** Treat the four safeguards as a checklist in the Einschränkungen section. If a safeguard seems trivial (e.g., Rollback is "delete the generated file"), write it explicitly anyway.

### Anti-Pattern 4: Commands That Bypass Agent Layer

**What people do:** Command file directly lists skills to invoke, without naming a responsible agent.
**Why it's wrong:** Breaks the layered architecture. Agents provide domain expertise and constraint enforcement (especially safeguards). A command that skips the agent layer also skips the agent's operating loop and constraints.
**Do this instead:** Every command must name exactly one primary agent. The agent then decides which skills to invoke.

## Integration Points

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Command → Agent | Command file declares `agent/[name].md` as responsible | Declarative reference, not invocation code |
| Agent → Meta Skill | Agent's "Primäre Skills" list includes `/elvis-*` meta skills | Same invocation pattern as domain skills |
| Meta Skill → Template | Generator skill reads `templates/[type]-template.md` | Template is the authoritative format source |
| Meta Skill → Library | Generator output references `skills/[domain]/` path | Convention-based path, no runtime lookup |
| Command Router Skill → Command files | elvis-command-router.md maintains the routing table | This skill is referenced by Uhura for maintenance |
| Uhura → Library State | Uhura reads all skill/agent files to verify completeness | Read-only scan, no mutation |

### Dependency Graph (S07/S08 components)

```
templates/skill-template.md
    └─ consumed by → elvis-skill-generator.md (exists)
                  → elvis-agent-generator.md
                  → elvis-soul-generator.md
                  → elvis-identity-generator.md

agent/*.md (all 16, S03 complete)
    └─ referenced by → elvis-agent-creator.md
                    → elvis-system-analyzer.md

skills/meta/elvis-skill-generator.md (exists)
    └─ invoked by → elvis-skill-expander.md (Borg)
                 → commands/generate-skills.md

skills/meta/elvis-command-router.md
    └─ invoked by → elvis-library-manager.md (Uhura)
                 → all commands/*.md (reference it for routing logic)

skills/meta/[all generators]
    └─ consumed by → elvis-agent-creator.md (composition)

skills/meta/[all S07 skills]
    └─ consumed by → commands/*.md (S08)
```

## Scaling Considerations

This is a Markdown-only system with no runtime. "Scaling" means file count and cognitive load, not users or traffic.

| Scale | Architecture Adjustments |
|-------|--------------------------|
| Current (~100 skills, 16 agents) | Single flat directory per domain — works well |
| 200+ skills | Consider domain subdirectories within skills/[domain]/ — not needed now |
| 500+ skills | Index file per domain (skills/growth/INDEX.md) for navigation — defer to later milestone |

### Scaling Priority

1. **First bottleneck:** Skill discoverability — with 100 skills, /elvis-* names become hard to navigate. Uhura + elvis-library-manager address this by maintaining routing tables.
2. **Second bottleneck:** Format drift — as skills multiply, generators diverge from templates. Verification in S09 catches this.

## Sources

- Codebase analysis: existing `agent/`, `skills/meta/`, `templates/` directories (HIGH confidence)
- M001-CONTEXT.md: canonical spec for file list, safeguard requirements, skill format (HIGH confidence)
- M001-ROADMAP.md: S07/S08 boundary map and slice dependencies (HIGH confidence)
- Existing skill `skills/meta/elvis-skill-generator.md`: reference implementation for meta skill pattern (HIGH confidence)
- Existing agents `agent/q.md`, `agent/borg.md`, `agent/troi.md`, `agent/uhura.md`, `agent/picard.md`: reference implementation for meta agent constraints (HIGH confidence)

---
*Architecture research for: Meta-Agent System + Command Routing Layer*
*Researched: 2026-03-14*
