# Architecture

**Analysis Date:** 2026-03-14

## Pattern Overview

**Overall:** Multi-Agent Skill-Based System with Role-Based Personas and Soul-Driven Operating Principles

**Key Characteristics:**
- Agent-centric architecture where specialized AI personas handle distinct domains
- Skill-based capability framework allowing granular task delegation
- Philosophy-driven "Soul" layer defining operating principles and decision patterns
- Identity layer providing character context and communication style for agents
- Markdown-first knowledge representation (skills, souls, agents, identities)

## Layers

**Agent Layer:**
- Purpose: Define specialized AI personas that coordinate work across skill domains
- Location: `agent/` directory (markdown files defining agent missions, capabilities, constraints)
- Contains: Agent definitions with name, mission, operating loop, constraints, soul reference, and primary skills
- Depends on: Soul definitions, Skill catalog
- Used by: Orchestration system to delegate work to appropriate agents
- Example: `agent/data.md` - Content creation agent with structured workflow, `agent/borg.md` - Skills assimilation and process optimization

**Identity Layer:**
- Purpose: Provide character context, communication style, and behavioral patterns for agent personas
- Location: `identity/` directory (markdown files defining character profiles)
- Contains: Character descriptions, personality traits, strengths, weaknesses, communication styles
- Depends on: Soul layer for philosophical grounding
- Used by: Agent system to shape how agents think and communicate
- Example: `identity/scotty.md` - Systems engineer persona, `identity/data.md` - Precision-focused creator

**Soul Layer:**
- Purpose: Define core philosophical and operational principles that guide decision-making
- Location: `soul/` directory (markdown files defining operating philosophies)
- Contains: Philosophy statements, core values, operating principles, success metrics, suitability guidelines
- Depends on: None (foundational)
- Used by: All agents and identities to ground decisions in consistent worldview
- Example: `soul/automation.md` - Systems thinking, repeatability, friction reduction; `soul/execution.md` - Speed, adaptability, results-oriented

**Skill Layer:**
- Purpose: Encapsulate specialized, reusable capabilities organized by domain
- Location: `skills/` directory with subdirectories by domain (analysis, automation, content, growth, research, strategy, meta)
- Contains: Detailed skill definitions (goals, strategy, execution steps, verification criteria, dependencies)
- Depends on: None (skills are standalone)
- Used by: Agents to execute specific tasks, orchestration system for work distribution
- Execution: Each skill is invoked with `/elvis-[skill-name]` notation and produces deliverables following skill specifications
- Domains:
  - `skills/analysis/` - Data analysis, A/B testing, performance tracking, funnel analysis, KPI dashboards
  - `skills/automation/` - Workflow automation, task automation, batch processing, integration mapping
  - `skills/content/` - Content creation (hooks, copywriting, threads, calendar planning)
  - `skills/growth/` - Growth strategies, audience building, viral optimization, competitor analysis
  - `skills/research/` - Research and investigation tasks
  - `skills/strategy/` - Strategic planning and frameworks
  - `skills/meta/` - Meta-analysis and system optimization

**Orchestration/Command Layer:**
- Purpose: Coordinate agent selection and skill invocation
- Location: `commands/` directory (currently a placeholder)
- Contains: Command definitions that map high-level requests to agent+skill combinations
- Depends on: Agent, Identity, Soul, and Skill layers
- Used by: External interfaces to route work

**Planning Layer:**
- Purpose: Track project state, roadmaps, and execution phases
- Location: `.planning/` directory
- Contains: Project metadata (PROJECT.md), roadmap definitions (ROADMAP.md), state tracking (STATE.md), phase plans and summaries
- Depends on: GSD workflow system
- Used by: Lifecycle management and progress tracking

**Scripts/Tooling Layer:**
- Purpose: Automate verification and initialization tasks
- Location: `scripts/` directory
- Contains: Verification scripts (verify-sXX.sh), Python task generators
- Depends on: All layers above
- Used by: Development and deployment workflows

## Data Flow

**Request → Agent → Skill → Deliverable:**

1. **Request Intake**: High-level request arrives with context and constraints (e.g., "analyze A/B test results", "create growth strategy")
2. **Agent Selection**: Orchestration system identifies appropriate agent based on domain (Data for content, Scotty for automation, Worf for strategy)
3. **Brief Formation**: Agent reads full context, constraints, and identifies which skill(s) are needed
4. **Skill Invocation**: Agent invokes skill(s) with `/elvis-[skill-name]` notation and required inputs
5. **Skill Execution**: Skill follows its documented execution steps (typically 5-7 steps), produces structured output
6. **Verification**: Skill output checked against verification criteria defined in skill specification
7. **Deliverable**: Skill produces markdown document(s) following its output template specification
8. **Review Loop**: Agent reviews deliverable against original request constraints, may iterate if needed

**State Management:**
- Agent state is transient - no persistent state per agent
- Skill state is explicit - each skill documents what it requires as input and produces as output
- Request context is markdown-based and passed through the system
- Deliverables are self-documenting markdown that becomes new context for next request

**Philosophy-Driven Decision Points:**
- Agents apply their Soul's operating principles when choosing how to work
- For example, an Automation Soul agent (Scotty) prioritizes repeatability and systemization
- An Execution Soul agent (McCoy) prioritizes speed and direct action over planning
- A Creator Soul agent (Data, Q) prioritizes originality and generative thinking
- These souls are consulted at decision points within skill execution

## Key Abstractions

**Skill:**
- Purpose: Encapsulate a specific, reusable capability with clear inputs, execution steps, verification, and outputs
- Examples: `elvis-ab-tester.md` (A/B testing with statistical rigor), `elvis-workflow-builder.md` (automation discovery and documentation)
- Pattern: Name → Description → Goals → Strategy → Constraints → Execution Steps → Verification → Dependencies → Output
- Invocation: `/elvis-[skill-name]` with required context as input
- Output: Markdown document(s) ready for immediate use or as input to next skill

**Agent:**
- Purpose: A specialized AI persona that coordinates work across a domain
- Examples: `data` (content creation), `borg` (skill assimilation), `scotty` (automation/systems)
- Pattern: Name → Mission → Capabilities → Operating Loop → Constraints → Soul → Primary Skills
- Role: Acts as domain expert, decides which skills to invoke, reviews deliverables against requirements
- Communication: Uses identity profile to shape how it thinks and communicates

**Soul:**
- Purpose: Define a philosophical operating framework that guides decision-making
- Examples: `execution` (speed, adaptability, results), `automation` (repeatability, systemization), `creator` (originality, generativity)
- Pattern: Name → Philosophy → Core Values → Operating Principles → Success Metrics → Suitability
- Application: Agents are assigned a Primary Soul that shapes their decision patterns
- Decision influence: When a skill has multiple valid approaches, the soul determines which is chosen

**Identity:**
- Purpose: Provide character context that affects communication style and personality expression
- Examples: `scotty` (systems engineer with humor and pessimistic time estimates), `data` (precise, ego-free, learning-focused)
- Pattern: Name → Character Description → Personality Traits → Communication Style → Strengths → Weaknesses → Star Trek Reference
- Application: Agents are assigned an Identity that shapes how they interact
- Expression: Visible in communication tone, word choice, metaphors, and decision emphasis

## Entry Points

**Agent Invocation:**
- Location: Agent files in `agent/` directory
- Triggers: System-level request for capability in a specific domain
- Responsibilities:
  1. Understand the full request and constraints
  2. Identify relevant skill(s) needed
  3. Prepare skill invocation with correct context
  4. Execute skill(s) in sequence or parallel as appropriate
  5. Review deliverable(s) against original requirements
  6. Return final deliverable or iterate if needed

**Skill Invocation:**
- Location: Skill files in `skills/[domain]/` directories
- Triggers: Agent-initiated with `/elvis-[skill-name]` notation
- Responsibilities:
  1. Execute documented execution steps (typically 5-7 steps)
  2. Verify outputs meet verification criteria
  3. Produce markdown deliverable following output template
  4. Document any failure indicators
  5. Return structured output ready for next stage

**Command/Orchestration:**
- Location: `commands/` directory (currently placeholder)
- Triggers: External system requests
- Responsibilities: Parse requests, select appropriate agent, invoke agent with context

## Error Handling

**Strategy:** Explicit error definition within skill/agent specifications

**Patterns:**
- **Skill-level failures**: Each skill defines "Failure Indicator" - specific condition that means skill cannot proceed (e.g., "If sample size calculation < 100, skill outputs error message and stops")
- **Agent-level iteration**: Agent reviews skill output against requirements, can re-invoke skill with adjusted context if needed
- **Soul-based recovery**: Automation soul (Scotty) improvises workarounds; Execution soul (McCoy) acts directly; Creator soul (Data) adjusts approach
- **Constraint violation**: If deliverable violates documented constraints, agent loops back rather than accepting substandard output
- **Missing dependencies**: Skills document required inputs - if not provided, skill outputs "Input missing: [X]" and does not execute

## Cross-Cutting Concerns

**Logging:**
- Implicit through markdown deliverables - each skill output documents its own process and results
- Verification steps explicitly record what passed/failed
- Agent operating loop includes "Review" phase where decisions are documented

**Validation:**
- Skill-level: Verification criteria explicitly checked before output is marked complete
- Agent-level: Agent reviews skill output against original requirements
- Format-level: All outputs must be markdown documents following template patterns
- Data-level: Skills like `/elvis-ab-tester` include statistical validation (p-values, confidence intervals)

**Authentication:**
- Not applicable - single-user workflow with no external auth required
- Agents are logical personas, not external identities

**Consistency:**
- Soul definitions ensure consistent decision patterns across agents
- Identity definitions ensure consistent communication style
- Skill templates ensure consistent output format and quality
- Markdown-first approach enables easy version control and auditability

---

*Architecture analysis: 2026-03-14*
