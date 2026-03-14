# OpenClaw Meta Maker

## What This Is

Agent-Factory für OpenClaw: ein vollständiges, modulares Markdown-basiertes Agent-Ökosystem mit ~300 Dateien. Neue Agenten entstehen in unter 2 Minuten durch Kombination von Souls, Identities, Agents und Skills. Star Trek-Charaktere als Agenten-Personas. Alle Skills aufrufbar via `/elvis-[skill-name]`, alle Commands via `/[command-name]`. Der Meta-Layer (Generatoren, autonome Skills, Command-System) macht das Ökosystem zu einer selbstverwaltenden Agent-Factory.

## Core Value

Ein komplettes, sofort importierbares Agent-Ökosystem für OpenClaw — jede Datei nutzbar, jeder Agent einsatzbereit, jeder Skill ausführbar.

## Requirements

### Validated

- ✓ 10 Souls (analyst, automation, builder, creator, execution, growth, minimalist, operator, researcher, strategist) — S01
- ✓ 16 Identities (Star Trek Charaktere) — S02
- ✓ 16 Agent-Definitionen (Star Trek Charaktere) — S03
- ✓ 4 Templates (soul, identity, agent, skill) — S01
- ✓ 15 Content Skills — S04
- ✓ 15 Growth Skills — S04
- ✓ 15 Research Skills — S05
- ✓ 15 Strategy Skills — S05
- ✓ 10 Analysis Skills — S06
- ✓ 10 Automation Skills — S06
- ✓ META-01: Soul-Generator — v1.0
- ✓ META-02: Identity-Generator — v1.0
- ✓ META-03: Agent-Generator — v1.0
- ✓ META-04: Agent-Creator (Concept→Approve→Orchestrate) — v1.0
- ✓ META-05: Skill-Expander (Borg) — v1.0
- ✓ META-06: System-Analyzer (Troi) — v1.0
- ✓ META-07: Library-Manager (Uhura) — v1.0
- ✓ META-08: Command-Router (Picard) — v1.0
- ✓ META-09: Ecosystem-Health — v1.0
- ✓ META-10: Agent-Optimizer (Picard) — v1.0
- ✓ META-12: Concept-Design (Q) — v1.0
- ✓ SAFE-01..04: Safeguard-Quartet für alle autonomen Meta-Skills — v1.0
- ✓ CMD-01..10: 11 Command-Routing-Deklarationen — v1.0

### Active

(Next milestone — TBD via `/gsd:new-milestone`)

### Out of Scope

- Ausführbarer Code jeglicher Art — reines Markdown-Projekt
- API-Verbindungen zu externen Diensten — kein Runtime
- Pixel Agents Visualisierung — separates Projekt
- Echte Social-Media-Automation — nur Skill-Definitionen
- Multi-User Support — Single-User Workflow
- Versionierung von Skills — Git übernimmt das
- META-11 (pattern-assimilation) — kein aktueller Use Case, v2 Kandidat

## Context

- Shipped v1.0 mit ~300 Markdown-Dateien (246 Projekt + Planning)
- 93 Skills (81 Content + 12 Meta), 16 Agenten, 16 Identities, 10 Souls
- 11 Command-Routing-Deklarationen, 1 Command-Router mit 12-Einträge-Tabelle
- Skill-Format bindend (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- Sprache: Deutsch, Fachbegriffe (Skill, Soul, Agent) bleiben Englisch
- Alle autonomen Skills haben Safeguard-Quartet (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback)

## Constraints

- **Format**: Finales Skill-Format bindend für alle neuen Skills
- **Sprache**: Deutsch mit englischen Fachbegriffen
- **Naming**: `/elvis-*` Convention für alle Skills
- **Safeguards**: Autonome Skills brauchen explizite Limits (Safeguard-Quartet)
- **Konsistenz**: Neue Dateien müssen qualitativ zu den bestehenden Skills passen
- **Commands**: Reine Routing-Deklarationen, max 15 Zeilen, keine Ausführungslogik

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Star Trek Agenten-Mapping | Klare Funktions-Zuordnung, einprägsam | ✓ Good |
| 6 Skill-Domänen | Klare Trennung, keine Überlappung | ✓ Good |
| Erweitertes Skill-Format mit Verification | Skills müssen konkret genug für echte Ausführung sein | ✓ Good |
| Plan-Approve-Execute für Generatoren | Konsistentes Pattern, Operator behält Kontrolle | ✓ Good |
| Match-Clarify-Route für Router | Router generiert nichts, spiegelt nur Routing-Tabelle | ✓ Good |
| Concept→Approve→Orchestrate für Agent-Creator | Ein Gate statt drei — erhält <2-Min-Constraint | ✓ Good |
| Safeguard-Quartet als Pflicht | Autonome Skills brauchen explizite Grenzen | ✓ Good |
| Commands als reine Routing-Deklarationen | Keine Logik-Duplikation, max 15 Zeilen | ✓ Good |
| Generator-Bypass in Agent-Creator | Intern implementiert by design — kein separater Skill-Aufruf | ✓ Good |
| META-11 deferred → v2 | Kein aktueller Use Case für pattern-assimilation | ✓ Good |

---
*Last updated: 2026-03-14 after v1.0 milestone*
