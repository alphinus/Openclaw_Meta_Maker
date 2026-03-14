# Coding Conventions

**Analysis Date:** 2026-03-14

## Overview

This codebase is not traditional code — it is a meta-system written in Markdown and Bash. The "conventions" are structural and content rules for defining agents, souls, skills, and identities within the OpenClaw Meta Maker framework. All actual executables are Bash verification scripts.

## Naming Patterns

**Files:**
- Agent files: `agent/[lowercase-name].md` (e.g., `agent/kirk.md`, `agent/picard.md`)
  - Convention: Star Trek character names in lowercase, English only
  - Always a single file per agent

- Soul files: `soul/[lowercase-role].md` (e.g., `soul/strategist.md`, `soul/analyst.md`)
  - Represent philosophical operating principles

- Identity files: `identity/[lowercase-name].md` (e.g., `identity/kirk.md`)
  - Parallel to agents — describes personality and character traits

- Skill files: `skills/[category]/elvis-[kebab-case].md` (e.g., `skills/automation/elvis-automation-audit.md`)
  - Format: `/elvis-[skill-name]` — always lowercase, hyphens between words
  - Organized by category subdirectories: `automation/`, `analysis/`, etc.
  - The `/elvis-` prefix is mandatory for all skill references

**Python Scripts:**
- Generator/writer scripts follow pattern: `scripts/write_[s-number]_[purpose].py`
- Verification scripts: `scripts/verify-[s-number].sh` (e.g., `verify-s02.sh`, `verify-s03.sh`)

## Code Style

**Bash Scripts:**
- Shebang: `#!/usr/bin/env bash`
- Indentation: 4 spaces
- Comments: Using `#` for inline and block comments
- Variables: `UPPERCASE_WITH_UNDERSCORES` for constants
- Functions: defined using `function_name() { ... }` syntax
- Error handling: Use explicit `ERRORS=$((ERRORS + 1))` counter pattern

**Markdown Structure:**
- ATX headers (`##`, `###`) for all section headings
- Precise header names are mandatory — verification scripts grep for exact matches
- No HTML comments in final output (comments removed after template filling)
- List items use consistent `-` bullet points or numbered `1.` lists

**Python Scripts:**
- Format: Raw string triple-quoted content written as-is to files
- Encoding: UTF-8 with explicit `encoding='utf-8'`
- Pattern: Read template/reference → Generate markdown string → Write to file
- No actual Python classes or functions — purely generation scripts

## Critical Structural Rules

**Agent Files (`agent/*.md`) — 7 Mandatory Sections:**

1. `## Name` — Star Trek character name (lowercase)
2. `## Mission` — Single action-oriented sentence describing the agent's purpose
3. `## Capabilities` — 5-8 concrete, executable abilities (not personality traits)
4. `## Operating Loop` — Numbered steps showing how the agent works repeatedly
5. `## Constraints` — Hard boundaries of autonomy and scope
6. `## Primärer Soul` — Reference to `soul/[name].md` (German header)
7. `## Primäre Skills` — Bulleted list of `/elvis-*` skill references (German header)

**Critical Agent Rule D012:** No personality content in agents. Agents describe WHAT an agent does (tasks, capabilities, processes). Personality traits belong in `identity/*.md`.
- Wrong: "Kirk decides with bold confidence"
- Right: "Decides within 2 minutes on incomplete data and documents decision with reasoning"

**Soul Files (`soul/*.md`) — 6 Mandatory Sections:**

1. `## Name` — Role name (e.g., "analyst", "strategist")
2. `## Philosophie` — Operating philosophy (German: "Philosophie")
3. `## Core Values` — 4-5 bullet points of guiding principles
4. `## Operating Principles` — How this soul approaches work
5. `## Success Metrics` — How to measure success
6. `## Geeignet für` — List of agents and use cases (German header)

**Skill Files (`skills/[category]/elvis-[name].md`) — 9 Mandatory Sections:**

1. `## Name` — `/elvis-[kebab-case-name]`
2. `## Beschreibung` — 1-3 sentence description (German: "Beschreibung")
3. `## Ziele` — 3-5 measurable outcomes (German: "Ziele")
4. `## Strategie` — Conceptual approach explaining the "why" (German: "Strategie")
5. `## Einschränkungen` — Hard limits, forbidden actions, scope boundaries (German: "Einschränkungen")
6. `## Ausführungsschritte` — Numbered steps, each with concrete quantities and formats (German: "Ausführungsschritte")
7. `## Verifikation` — Acceptance criteria and failure indicators (German: "Verifikation")
8. `## Abhängigkeiten` — Input data and predecessor skills (German: "Abhängigkeiten")
9. `## Output` — Description of concrete deliverable (German: "Output")

**Identity Files (`identity/*.md`) — 7 Mandatory Sections:**

1. `## Name` — Character name (lowercase)
2. `## Charakter-Beschreibung` — Detailed personality description
3. `## Persönlichkeitsmerkmale` — 6-8 bullet points of traits
4. `## Kommunikationsstil` — How this character speaks/communicates
5. `## Stärken` — Personal strengths (5 bullet points)
6. `## Schwächen` — Personal weaknesses (5 bullet points)
7. `## Star Trek Referenz` — Quote from Star Trek with German translation

## Language

**Rule D002:** All content is in German (Deutsch) EXCEPT:
- File names: Always English lowercase (kirk, data, automation-audit)
- Skill prefixes: Always `/elvis-[english-kebab-case]`
- Code/commands: Bash, Python — standard syntax
- Section headers: Mix of German and English per template (e.g., `## Primärer Soul` is German, `## Name` is English)

## Import Organization

**Skill References (Operating Loop and Capabilities):**
- Use `/elvis-[skill-name]` format
- Skills are referenced (never defined inline)
- No relative paths — always absolute skill references
- Order by frequency/importance of use

**Soul References:**
- Single reference per agent: `soul/[soul-name].md`
- Must match exactly one file in `soul/` directory
- Used as philosophical foundation, not execution logic

## Error Handling

**Exit Codes:**
- Bash verification scripts: Exit code = number of errors found (D014)
- Exit 0 = all checks passed
- Exit N = N checks failed, detailed output shows which ones
- Pattern: `exit $ERRORS` at script end

**Failure Messages:**
- Format: `fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }`
- Always include filename and missing section name
- Success format: `pass() { echo "  ✓ $1"; }`

**Verification Pattern:**
- Bash scripts use `grep -qF` to check for exact header presence
- Case-sensitive header matching
- One check per mandatory section per file
- Combinatorial: N files × M sections = N×M checks

## Comments

**Bash Scripts:**
- Use `#` for inline comments
- Section headers use special format:
  ```bash
  # ─────────────────────────────────────
  # [N/3] Section Name (X Checks)
  # ─────────────────────────────────────
  ```
- Comments before functions explaining purpose

**Markdown Templates:**
- HTML comments `<!-- ... -->` used in templates to explain WHAT to fill in
- All comments deleted after template is filled
- No comments in final output files

**Python Generation Scripts:**
- No comments — only docstrings in triple-quoted content
- Clear variable names like `plan`, `tasks`, `base` explain intent

## Module Design

**Exports/References:**
- Agents reference exactly 1 Soul (primary philosophy)
- Agents reference 3-5 Skills (primary operational toolkit)
- Skills reference predecessor skills by `/elvis-*` name
- Identity and Agent files are parallel — same character name, different content

**Barrel Files:**
- No barrel files or aggregators
- Each entity (agent, soul, skill, identity) is a single self-contained file
- Cross-references by filename, not by aggregated exports

**Monolithic vs. Modular:**
- Each file is a self-documenting contract
- Skill files define complete execution steps with concrete outputs
- Agent files define complete operating loops
- Soul files define complete philosophical frameworks
- No partial definitions across files

## Directory Structure Rules

**Organizational Principle:**
- Files are organized by TYPE, not by feature or domain
- `agent/` contains all agents regardless of specialization
- `soul/` contains all souls
- `skills/[category]/` separates skills by functional area (automation, analysis, etc.)
- `identity/` contains all personality definitions
- `templates/` contains binding templates for each file type

## Key Documentation Standards

**Rule D001 (Skill Prefix):** All skill references use `/elvis-` prefix — non-negotiable.

**Rule D006 (Concrete Steps):** Execution steps must include:
- Concrete quantities (e.g., "Top-20", "the last 7 days", "3 variants") — never "some" or "several"
- Concrete format (e.g., "Markdown table with 4 columns", "JSON array")
- Time estimates where relevant

**Rule D013 (Safeguard Formatting):** Autonomous agents' safeguard markers must be bold:
- `**Max-Limit:** [specific number]`
- `**Approval-Gate:** [condition]`
- `**Stop-Bedingung:** [automatic halt condition]`
- `**Rollback-Hinweis:** [undo mechanism]`

**Rule D015 (Verification-First):** Verification script defines contract BEFORE any files are created — scripts show all checks failing on first run (this proves checks work).

---

*Convention analysis: 2026-03-14*
