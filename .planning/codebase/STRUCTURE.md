# Codebase Structure

**Analysis Date:** 2026-03-14

## Directory Layout

```
Openclaw_Meta_Maker/
├── agent/                 # Agent personas and their operating loops
├── commands/              # Command definitions and routing (placeholder)
├── identity/              # Character profiles and communication styles
├── scripts/               # Verification and automation scripts
├── skills/                # Capability catalog organized by domain
│   ├── analysis/         # Data analysis, testing, performance tracking
│   ├── automation/       # Workflow automation, process optimization
│   ├── content/          # Content creation (copywriting, hooks, scheduling)
│   ├── growth/           # Growth strategies, audience building, analytics
│   ├── research/         # Research and investigation capabilities
│   ├── strategy/         # Strategic planning and frameworks
│   └── meta/             # Meta-analysis and system optimization
├── soul/                  # Operating philosophies and value systems
├── templates/             # Template definitions for agent, identity, skill, soul
├── .planning/             # GSD planning and project state
│   ├── codebase/         # Codebase documentation (ARCHITECTURE.md, STRUCTURE.md, etc.)
│   ├── phases/           # Phase plans and summaries
│   └── PROJECT.md        # Project metadata and overview
└── .gitignore

```

## Directory Purposes

**`agent/` - Agent Personas**
- Purpose: Define specialized AI personas that coordinate work within their domain
- Contains: Markdown files with agent names as filenames (data.md, scotty.md, borg.md, etc.)
- Key files:
  - `agent/data.md`: Content creation agent - produces structured content following strict briefing workflow
  - `agent/borg.md`: Skills assimilation agent - identifies patterns and builds skill libraries
  - `agent/scotty.md`: Automation/systems agent - solves technical challenges through system understanding
- Structure: Each agent file contains: Name, Mission, Capabilities list, Operating Loop (numbered steps), Constraints, Primary Soul, Primary Skills
- How they work: Agents define a mission (what they do), operating loop (how they work step-by-step), constraints (what they won't do), and which soul drives their decision-making

**`identity/` - Character Profiles**
- Purpose: Provide character context that shapes how agents think, communicate, and decide
- Contains: Markdown files defining character personas (scotty.md, data.md, etc.) from Star Trek universe
- Key aspects per file:
  - Character Description: How the person sees the world and approaches problems
  - Personality Traits: Specific behavioral patterns
  - Communication Style: Word choice, tone, metaphors, directness level
  - Strengths/Weaknesses: What they excel at and where they struggle
  - Star Trek Reference: Canonical quote showing the core philosophy
- How they're used: Each agent or soul is associated with an identity that colors its thinking and communication

**`soul/` - Operating Philosophies**
- Purpose: Define core value systems and operating principles that guide all decisions
- Contains: Markdown files with philosophy names (automation.md, execution.md, creator.md, etc.)
- Key aspects per file:
  - Philosophy: Core belief about how work should be done
  - Core Values: 3-4 fundamental principles
  - Operating Principles: Specific decision rules (typically 5-6)
  - Success Metrics: How to know if the soul's approach worked
  - Suitability: Which agents/tasks benefit from this soul
- Examples:
  - `soul/automation.md`: Prioritizes repeatability, systemization, friction reduction
  - `soul/execution.md`: Prioritizes speed, adaptability, results over process
  - `soul/creator.md`: Prioritizes originality, generative thinking, exploration
- How they're used: Agents are assigned a Primary Soul which shapes their decision-making

**`skills/` - Capability Catalog**
- Purpose: Encapsulate reusable, domain-specific capabilities with clear execution procedures
- Structure: Organized into 7 domains (analysis, automation, content, growth, research, strategy, meta)
- Each skill file contains:
  - Name: Invoked as `/elvis-[skill-name]` (e.g., `/elvis-ab-tester`)
  - Description: 1-2 sentence overview
  - Goals: What the skill produces (5-8 specific outputs)
  - Strategy: Philosophy and approach
  - Constraints: Hard limits (what the skill won't do)
  - Execution Steps: Numbered procedure (typically 5-7 steps)
  - Verification: Specific checklist for quality assurance
  - Dependencies: Required inputs and recommended predecessor skills
  - Output: Template and format of deliverable
- Example skill from `skills/analysis/elvis-ab-tester.md`:
  - Tests exactly one variable at a time
  - Calculates sample size with statistical rigor (95% confidence, 80% power)
  - Produces test design, sample calculation, execution checklist, result template, scenario planning
  - Failure indicator: "Sample size < 100 per variant" → outputs error and stops

**Subdomains within `skills/`:**

- `skills/analysis/` - Data analysis and optimization:
  - elvis-ab-tester.md: A/B testing with scientific methodology
  - elvis-performance-tracker.md: KPI and performance dashboards
  - elvis-funnel-analyzer.md: Conversion funnel analysis
  - elvis-revenue-tracker.md: Revenue and monetization analysis
  - (9 total skills in this domain)

- `skills/automation/` - Process and workflow automation:
  - elvis-workflow-builder.md: Identify and document repetitive tasks for automation
  - elvis-automation-audit.md: Audit existing automation for optimization
  - elvis-task-automator.md: Automate specific repetitive tasks
  - elvis-data-pipeline.md: Build data processing pipelines
  - (10 total skills in this domain)

- `skills/content/` - Content creation across formats:
  - elvis-x-hook-writer.md: Write attention-grabbing opening lines
  - elvis-copywriting.md: General copywriting for various formats
  - elvis-content-calendar.md: Plan content distribution schedule
  - elvis-headline-writer.md: Write compelling headlines
  - elvis-story-writer.md: Create narrative-driven content
  - (15 total skills in this domain)

- `skills/growth/` - Growth strategy and audience building:
  - elvis-growth-audit.md: Audit current growth strategy
  - elvis-audience-builder.md: Build and engage audience
  - elvis-competitor-analysis.md: Analyze competitor strategies
  - elvis-viral-formula.md: Design viral distribution patterns
  - (12 total skills in this domain)

- `skills/research/`, `skills/strategy/`, `skills/meta/` - Additional domains with similar structure

**`scripts/` - Verification and Automation**
- Purpose: Automate verification, initialization, and task generation
- Contains:
  - `verify-s01.sh` through `verify-s06.sh`: Verify slice completion for milestones M001-S01 through S06
  - `write_s03_plan.py`, `write_s03_tasks.py`: Generate task and plan files for S03
- How they're used: Execute during phase initialization to ensure completeness, during verification to check deliverables

**`templates/` - Definition Templates**
- Purpose: Provide structure templates for new skills, agents, identities, and souls
- Contains:
  - `skill-template.md`: Boilerplate for new skill definition
  - `agent-template.md`: Boilerplate for new agent definition
  - `identity-template.md`: Boilerplate for new identity definition
  - `soul-template.md`: Boilerplate for new soul definition
- How they're used: When creating new capabilities, copy the appropriate template and fill in the structure

**`.planning/` - Project Planning and State**
- Purpose: Track project context, roadmap, and execution phases
- Contains:
  - `.planning/PROJECT.md`: Project metadata, vision, scope
  - `.planning/ROADMAP.md`: Milestone and phase definitions
  - `.planning/STATE.md`: Current execution state and position
  - `.planning/codebase/`: Codebase analysis documents (this document, ARCHITECTURE.md, etc.)
  - `.planning/phases/`: Phase plans and summary files
- How they're used: GSD workflow system reads these to understand project state and execution context

## Key File Locations

**Entry Points:**
- Agent definitions: `agent/[name].md` - Start here to understand how work is coordinated
- Skill definitions: `skills/[domain]/elvis-[skill-name].md` - Start here to understand how to execute specific tasks
- Soul definitions: `soul/[name].md` - Start here to understand decision-making philosophy
- Identity definitions: `identity/[name].md` - Start here to understand communication and personality

**Configuration:**
- Project config: `.planning/PROJECT.md` - Project scope and metadata
- Roadmap: `.planning/ROADMAP.md` - Milestone and phase definitions
- State: `.planning/STATE.md` - Current execution context

**Core Logic:**
- Agent operating loops: `agent/*.md` - Defines step-by-step how agents work
- Skill execution steps: `skills/[domain]/*.md` - Defines step-by-step how skills execute
- Soul decision patterns: `soul/*.md` - Defines philosophical decision framework

**Testing/Verification:**
- Slice verification: `scripts/verify-s0X.sh` - Bash scripts that verify slice completeness
- Task generation: `scripts/write_s0X_*.py` - Python scripts that generate task definitions

## Naming Conventions

**Files:**
- Agent files: lowercase-with-hyphens for character names (data.md, scotty.md)
- Identity files: lowercase character names (scotty.md, data.md)
- Soul files: lowercase philosophy names (automation.md, execution.md, creator.md)
- Skill files: `elvis-[kebab-case-skill-name].md` (elvis-ab-tester.md, elvis-workflow-builder.md)
- Script files: `verify-s[slice-number].sh` (verify-s01.sh), `write_s[slice]_[type].py`
- Directory names: lowercase-with-hyphens for multi-word directories (skills/analysis, .planning/codebase)

**Directories:**
- Domain directories: lowercase (analysis, automation, content)
- System directories: prefixed with dot for hidden/system use (.planning, .gsd)
- Concept groupings: English noun form (agent, skills, identity, soul, commands, templates)

**Within Markdown Files:**
- Section headers: Title Case with # hierarchy
- Subsection headers: Title Case with ## or ### hierarchy
- Code references: Backticks for file paths (`skills/analysis/elvis-ab-tester.md`)
- Numbered lists: For execution steps (1. First step, 2. Second step)
- Bullet lists: For items and constraints

## Where to Add New Code

**New Skill:**
- Implementation: Create file in `skills/[domain]/elvis-[skill-name].md` where domain is one of: analysis, automation, content, growth, research, strategy, meta
- Structure: Copy from `templates/skill-template.md` and fill in all sections (Name, Description, Goals, Strategy, Constraints, Execution Steps, Verification, Dependencies, Output)
- Naming: Use `/elvis-` prefix, describe skill in kebab-case (elvis-engagement-analyzer, elvis-campaign-scheduler)
- Registration: Update agent's "Primary Skills" section if this skill is a primary capability for that agent

**New Agent:**
- Implementation: Create file in `agent/[agent-name].md`
- Structure: Copy from `templates/agent-template.md` and fill in Mission, Capabilities list, Operating Loop, Constraints, Soul, Primary Skills
- Character name: Use Star Trek character name or new persona
- Dependencies: Must reference existing Soul and existing Skills
- Registration: Can be invoked once file exists - orchestration system discovers agents from agent/ directory

**New Soul:**
- Implementation: Create file in `soul/[soul-name].md`
- Structure: Copy from `templates/soul-template.md` and fill in Philosophy, Core Values, Operating Principles, Success Metrics, Suitability
- Philosophy: Should be orthogonal to existing souls (not duplicate of automation, execution, creator, builder, analyst, etc.)
- Impact: Once created, can be assigned as Primary Soul to agents

**New Identity:**
- Implementation: Create file in `identity/[character-name].md`
- Structure: Copy from `templates/identity-template.md` and fill in Character Description, Personality Traits, Communication Style, Strengths, Weaknesses, Star Trek Reference
- Character: Use Star Trek character (preferred) or new persona
- Assignment: Can be assigned to agents to shape their communication and thinking style

**New Domain within Skills:**
- Create directory: `skills/[new-domain]/`
- Add skills: Start with first skill file `elvis-[first-skill].md`
- Purpose: Domains should be roughly orthogonal (analysis vs. automation, not analysis vs. ab-testing)

**Utilities and Helpers:**
- Shared verification logic: `scripts/verify-[phase].sh`
- Shared generation logic: `scripts/write_[phase]_[type].py`
- These are called by the GSD verification system

## Special Directories

**`.planning/`:**
- Purpose: GSD system state and project context
- Generated: Partially (created by gsd:new-project, updated by gsd:plan-phase)
- Committed: Yes (critical for project continuity)
- Contents:
  - `PROJECT.md`: Project scope and metadata (created once, updated rarely)
  - `ROADMAP.md`: Milestone and phase definitions (created once, updated for replanning)
  - `STATE.md`: Current execution position (updated frequently by GSD system)
  - `phases/`: Plans and summaries for each phase (created during planning, updated during execution)
  - `codebase/`: This document and architecture analysis files (created by gsd:map-codebase)

**`.gsd/`:**
- Purpose: GSD internal runtime state and activity tracking
- Generated: Yes (created and managed by GSD system)
- Committed: Yes (needed for state continuity between sessions)
- Contents: Activity logs, milestone tracking, slice and task state

**`templates/`:**
- Purpose: Structural templates for new components
- Generated: No (hand-written templates)
- Committed: Yes (foundational)
- How to use: Copy template file to actual location, replace placeholders

**`commands/`:**
- Purpose: Command routing definitions (future use)
- Generated: No (placeholder for now)
- Committed: Yes (prepared for future expansion)
- Future role: Will map high-level requests to agent+skill combinations

## Adding Files - Decision Tree

```
What are you adding?

├─ A new capability to execute
│  └─ → Add skill to skills/[domain]/elvis-[name].md
│
├─ A new coordinator/domain expert
│  └─ → Add agent to agent/[name].md
│
├─ A new operating philosophy
│  └─ → Add soul to soul/[name].md
│
├─ A new personality/character
│  └─ → Add identity to identity/[name].md
│
├─ Verification/automation script
│  └─ → Add script to scripts/
│
└─ Project/planning documentation
   └─ → Add to .planning/ (rarely - mostly GSD manages this)
```

---

*Structure analysis: 2026-03-14*
