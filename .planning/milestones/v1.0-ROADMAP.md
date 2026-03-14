# Roadmap: OpenClaw Meta Maker

## Overview

Das Projekt ist zu 81% fertig: 81 Skills, 16 Agenten, 16 Identities, 10 Souls existieren bereits. Die verbleibende Arbeit ist präzise umgrenzt — drei Phasen liefern den Meta-Layer (Generatoren, autonome Skills, Command-System) der das Ökosystem von einem Skill-Archiv zu einer selbstverwaltenden Agent-Factory macht. Phase 1 baut die Generatoren und den Router (Fundament). Phase 2 baut die Kompositions- und autonomen Skills (volle Meta-Kapazität). Phase 3 baut den Command-Layer (Operator-Interface).

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Generators + Router** - Soul-, Identity-, Agent-Generatoren und Command-Router mit Safeguard-Quartet (completed 2026-03-14)
- [x] **Phase 2: Composition + Autonomous** - Agent-Creator, Skill-Expander, System-Analyzer, Library-Manager und erweiterte Meta-Skills (completed 2026-03-14)
- [x] **Phase 3: Command Layer** - Alle 10 Command-Definitionen als Markdown-Routing-Deklarationen (completed 2026-03-14)
- [x] **Phase 4: Integration Fixes + Tech Debt** - Agent-Zuweisungen korrigieren, Soul-Sektionsnamen fixen, Dokumentationslücken schliessen (completed 2026-03-14)

## Phase Details

### Phase 1: Generators + Router
**Goal**: User kann neue Souls, Identities und Agenten generieren, und alle Anfragen werden durch einen zentralen Router an das richtige Skill-Chain geleitet — mit vollständigem Safeguard-Quartet in jedem autonomen Skill
**Depends on**: Nothing (first phase)
**Requirements**: META-01, META-02, META-03, META-08, SAFE-01, SAFE-02, SAFE-03, SAFE-04
**Success Criteria** (what must be TRUE):
  1. User kann `/elvis-soul-generator` aufrufen und erhält eine vollständige Soul-Definition die dem 9-Abschnitt-Format entspricht
  2. User kann `/elvis-identity-generator` aufrufen und erhält eine vollständige Identity-Definition die dem Template entspricht
  3. User kann `/elvis-agent-generator` aufrufen und erhält eine vollständige Agent-Definition die dem Template entspricht
  4. User kann `/elvis-command-router` aufrufen und wird an den richtigen Agenten + Skill-Chain geleitet
  5. Jeder neue Skill in dieser Phase hat konkrete Zahlen in Max-Limit (≤ 10), einen benannten Halt-Punkt im Approval-Gate, zwei explizite Stop-Bedingungen und eine benannte Rollback-Aktion
**Plans:** 2/2 plans complete

Plans:
- [x] 01-01-PLAN.md — Soul-Generator und Identity-Generator erstellen (Wave 1)
- [x] 01-02-PLAN.md — Agent-Generator und Command-Router erstellen (Wave 2)

### Phase 2: Composition + Autonomous
**Goal**: User kann einen kompletten Agenten in unter 2 Minuten zusammenstellen, bestehende Skills expandieren, das Ökosystem auf Lücken analysieren, und den Skill-Katalog verwalten — alle autonomen Skills mit operativ vollständigen Safeguards
**Depends on**: Phase 1
**Requirements**: META-04, META-05, META-06, META-07, META-09, META-10, META-12
**Success Criteria** (what must be TRUE):
  1. User kann `/elvis-agent-creator` aufrufen und erhält in einem einzigen Workflow einen kompletten Agenten aus Soul + Identity + Agent-Definition
  2. User kann `/elvis-skill-expander` aufrufen und Borg generiert neue Skill-Varianten mit konkreten Sub-Skill-Referenzen in jedem Ausführungsschritt
  3. User kann `/elvis-system-analyzer` aufrufen und Troi liefert einen Gesundheitsbericht mit benannten Lücken und Empfehlungen
  4. User kann `/elvis-library-manager` aufrufen und der Skill-Katalog wird kategorisiert und durchsuchbar gemacht
  5. Alle autonomen Skills in dieser Phase enthalten einen Approval-Gate als numerierten Ausführungsschritt — nicht nur in Einschränkungen
**Plans:** 4/4 plans complete

Plans:
- [ ] 02-01-PLAN.md — Agent-Creator Skill erstellen (Wave 1)
- [ ] 02-02-PLAN.md — Skill-Expander und Concept-Design erstellen (Wave 1)
- [ ] 02-03-PLAN.md — System-Analyzer und Ecosystem-Health erstellen (Wave 1)
- [ ] 02-04-PLAN.md — Library-Manager und Agent-Optimizer erstellen (Wave 1)

### Phase 3: Command Layer
**Goal**: User kann alle Kern-Workflows über kurze, einprägsame Commands starten — jeder Command routet deklarativ an Agenten + Skill-Chain ohne eigene Ausführungslogik
**Depends on**: Phase 2
**Requirements**: CMD-01, CMD-02, CMD-03, CMD-04, CMD-05, CMD-06, CMD-07, CMD-08, CMD-09, CMD-10
**Success Criteria** (what must be TRUE):
  1. User kann `/build-agent` aufrufen und wird an den Agent-Creator-Workflow weitergeleitet
  2. User kann `/generate-skills`, `/expand-skills`, `/create-soul`, `/create-identity` aufrufen und landet jeweils beim richtigen Skill
  3. User kann `/analyze-system`, `/health-check`, `/manage-library`, `/optimize-agent` aufrufen und landet jeweils beim richtigen autonomen Skill
  4. Kein Command-File enthält Ausführungslogik — jedes File ist eine reine Routing-Deklaration (Agent + Skill-Chain)
**Plans:** 1/1 plans complete

Plans:
- [ ] 03-01-PLAN.md — 10 Command-Dateien erstellen + Router-Tabelle erweitern (Wave 1)

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Generators + Router | 2/2 | Complete   | 2026-03-14 |
| 2. Composition + Autonomous | 4/4 | Complete   | 2026-03-14 |
| 3. Command Layer | 1/1 | Complete   | 2026-03-14 |
| 4. Integration Fixes + Tech Debt | 2/2 | Complete   | 2026-03-14 |

### Phase 4: Integration Fixes + Tech Debt
**Goal**: Alle Wiring-Inkonsistenzen aus dem Milestone-Audit bereinigen — Agent-Zuweisungen vereinheitlichen, fehlerhafte Sektionsnamen korrigieren, Dokumentationslücken schliessen
**Depends on**: Phase 3
**Requirements**: (gap closure — no new requirements)
**Gap Closure**: Closes INT-01, INT-02 and 5 tech debt items from v1.0-MILESTONE-AUDIT.md
**Success Criteria** (what must be TRUE):
  1. Agent-Zuweisung für create-soul und create-identity ist konsistent zwischen Commands und Router-Tabelle
  2. elvis-ecosystem-health prüft korrekte Soul-Sektionsnamen (Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für)
  3. elvis-agent-creator dokumentiert explizit dass Generator-Logik intern implementiert ist (kein separater Skill-Aufruf)
  4. elvis-agent-optimizer Step 2c ist konsistent mit Scope-Beschränkung auf agent/*.md
  5. Dedizierter Command für /elvis-concept-design existiert
  6. /generate-skills Dual-Agent-Routing ist klar dokumentiert
**Plans:** 2/2 plans complete

Plans:
- [ ] 04-01-PLAN.md — Router-Tabelle + Command-Layer bereinigen (Wave 1)
- [ ] 04-02-PLAN.md — Skill-Dokumentation korrigieren (Wave 1)
