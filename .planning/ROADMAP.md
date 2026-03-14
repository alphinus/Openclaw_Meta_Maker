# Roadmap: OpenClaw Meta Maker

## Overview

Das Projekt ist zu 81% fertig: 81 Skills, 16 Agenten, 16 Identities, 10 Souls existieren bereits. Die verbleibende Arbeit ist präzise umgrenzt — drei Phasen liefern den Meta-Layer (Generatoren, autonome Skills, Command-System) der das Ökosystem von einem Skill-Archiv zu einer selbstverwaltenden Agent-Factory macht. Phase 1 baut die Generatoren und den Router (Fundament). Phase 2 baut die Kompositions- und autonomen Skills (volle Meta-Kapazität). Phase 3 baut den Command-Layer (Operator-Interface).

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Generators + Router** - Soul-, Identity-, Agent-Generatoren und Command-Router mit Safeguard-Quartet
- [ ] **Phase 2: Composition + Autonomous** - Agent-Creator, Skill-Expander, System-Analyzer, Library-Manager und erweiterte Meta-Skills
- [ ] **Phase 3: Command Layer** - Alle 10 Command-Definitionen als Markdown-Routing-Deklarationen

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
**Plans**: TBD

### Phase 2: Composition + Autonomous
**Goal**: User kann einen kompletten Agenten in unter 2 Minuten zusammenstellen, bestehende Skills expandieren, das Ökosystem auf Lücken analysieren, und den Skill-Katalog verwalten — alle autonomen Skills mit operativ vollständigen Safeguards
**Depends on**: Phase 1
**Requirements**: META-04, META-05, META-06, META-07, META-09, META-10, META-11, META-12
**Success Criteria** (what must be TRUE):
  1. User kann `/elvis-agent-creator` aufrufen und erhält in einem einzigen Workflow einen kompletten Agenten aus Soul + Identity + Agent-Definition
  2. User kann `/elvis-skill-expander` aufrufen und Borg generiert neue Skill-Varianten mit konkreten Sub-Skill-Referenzen in jedem Ausführungsschritt
  3. User kann `/elvis-system-analyzer` aufrufen und Troi liefert einen Gesundheitsbericht mit benannten Lücken und Empfehlungen
  4. User kann `/elvis-library-manager` aufrufen und der Skill-Katalog wird kategorisiert und durchsuchbar gemacht
  5. Alle autonomen Skills in dieser Phase enthalten einen Approval-Gate als numerierten Ausführungsschritt — nicht nur in Einschränkungen
**Plans**: TBD

### Phase 3: Command Layer
**Goal**: User kann alle Kern-Workflows über kurze, einprägsame Commands starten — jeder Command routet deklarativ an Agenten + Skill-Chain ohne eigene Ausführungslogik
**Depends on**: Phase 2
**Requirements**: CMD-01, CMD-02, CMD-03, CMD-04, CMD-05, CMD-06, CMD-07, CMD-08, CMD-09, CMD-10
**Success Criteria** (what must be TRUE):
  1. User kann `/build-agent` aufrufen und wird an den Agent-Creator-Workflow weitergeleitet
  2. User kann `/generate-skills`, `/expand-skills`, `/create-soul`, `/create-identity` aufrufen und landet jeweils beim richtigen Skill
  3. User kann `/analyze-system`, `/health-check`, `/manage-library`, `/optimize-agent` aufrufen und landet jeweils beim richtigen autonomen Skill
  4. Kein Command-File enthält Ausführungslogik — jedes File ist eine reine Routing-Deklaration (Agent + Skill-Chain)
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Generators + Router | 0/TBD | Not started | - |
| 2. Composition + Autonomous | 0/TBD | Not started | - |
| 3. Command Layer | 0/TBD | Not started | - |
