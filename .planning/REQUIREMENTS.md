# Requirements: OpenClaw Meta Maker

**Defined:** 2026-03-14
**Core Value:** Komplettes, sofort importierbares Agent-Ökosystem für OpenClaw

## v1 Requirements

Requirements für die Fertigstellung. Jedes mappt auf Roadmap-Phasen.

### Meta Skills — Generatoren

- [x] **META-01**: User kann mit `/elvis-soul-generator` eine neue Soul-Definition generieren die dem Template entspricht
- [x] **META-02**: User kann mit `/elvis-identity-generator` eine neue Identity-Definition generieren die dem Template entspricht
- [x] **META-03**: User kann mit `/elvis-agent-generator` eine neue Agent-Definition generieren die dem Template entspricht

### Meta Skills — Composition

- [x] **META-04**: User kann mit `/elvis-agent-creator` einen kompletten Agenten aus Soul + Identity + Agent + Skills in < 2 Minuten zusammenstellen
- [x] **META-05**: User kann mit `/elvis-skill-expander` bestehende Skills erweitern und neue Varianten ableiten (Borg)

### Meta Skills — System & Autonomous

- [x] **META-06**: User kann mit `/elvis-system-analyzer` das gesamte Ökosystem auf Schwächen und Lücken analysieren (Troi)
- [x] **META-07**: User kann mit `/elvis-library-manager` den Skill-Katalog organisieren, kategorisieren und durchsuchen (Uhura)
- [x] **META-08**: User kann mit `/elvis-command-router` Anfragen an den richtigen Agent + Skill-Chain routen (Picard)
- [x] **META-09**: User kann mit `/elvis-ecosystem-health` einen Gesundheitscheck des gesamten Systems durchführen

### Meta Skills — Erweitert

- [x] **META-10**: User kann mit `/elvis-agent-optimizer` bestehende Agenten-Definitionen verbessern und optimieren
- [ ] **META-11**: User kann mit `/elvis-pattern-assimilation` Patterns aus externen Quellen ins Ökosystem integrieren (Borg)
- [x] **META-12**: User kann mit `/elvis-concept-design` neue Agent-Konzepte entwerfen und validieren (Q)

### Safeguards

- [x] **SAFE-01**: Alle autonomen Meta Skills (Q, Borg, Picard, Troi, Uhura) haben Max-Limit pro Durchlauf (≤ 10)
- [x] **SAFE-02**: Alle autonomen Meta Skills haben Approval-Gate als nummerierter Ausführungsschritt
- [x] **SAFE-03**: Alle autonomen Meta Skills haben explizite Stop-Bedingung
- [x] **SAFE-04**: Alle autonomen Meta Skills haben Rollback-Hinweis

### Commands

- [x] **CMD-01**: `/build-agent` — Routet zu Agent Creator Workflow
- [x] **CMD-02**: `/generate-skills` — Routet zu Skill Generator + Expander
- [x] **CMD-03**: `/analyze-system` — Routet zu System Analyzer
- [x] **CMD-04**: `/optimize-agent` — Routet zu Agent Optimizer
- [x] **CMD-05**: `/manage-library` — Routet zu Library Manager
- [x] **CMD-06**: `/expand-skills` — Routet zu Skill Expander
- [x] **CMD-07**: `/health-check` — Routet zu Ecosystem Health
- [x] **CMD-08**: `/create-soul` — Routet zu Soul Generator
- [x] **CMD-09**: `/create-identity` — Routet zu Identity Generator
- [x] **CMD-10**: `/route-command` — Meta-Router für alle Commands (Picard)

## v2 Requirements

### Erweiterte Autonomie

- **AUTO-01**: Agenten können eigenständig Sub-Agenten spawnen
- **AUTO-02**: Borg kann automatisch das Skill-Repertoire erweitern basierend auf Nutzungsmustern
- **AUTO-03**: Troi kann proaktiv Systemprobleme melden

## Out of Scope

| Feature | Reason |
|---------|--------|
| Ausführbarer Code | Reines Markdown-Projekt — kein Runtime |
| API-Verbindungen | Keine externen Dienste |
| Pixel Agents Visualisierung | Separates Projekt |
| Multi-User Support | Single-User Workflow |
| Versionierung von Skills | Git übernimmt das |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| META-01 | Phase 1 | Complete |
| META-02 | Phase 1 | Complete |
| META-03 | Phase 1 | Complete |
| META-04 | Phase 2 | Complete |
| META-05 | Phase 2 | Complete |
| META-06 | Phase 2 | Complete |
| META-07 | Phase 2 | Complete |
| META-08 | Phase 1 | Complete |
| META-09 | Phase 2 | Complete |
| META-10 | Phase 2 | Complete |
| META-11 | Phase 2 | Pending |
| META-12 | Phase 2 | Complete |
| SAFE-01 | Phase 1 | Complete |
| SAFE-02 | Phase 1 | Complete |
| SAFE-03 | Phase 1 | Complete |
| SAFE-04 | Phase 1 | Complete |
| CMD-01 | Phase 3 | Complete |
| CMD-02 | Phase 3 | Complete |
| CMD-03 | Phase 3 | Complete |
| CMD-04 | Phase 3 | Complete |
| CMD-05 | Phase 3 | Complete |
| CMD-06 | Phase 3 | Complete |
| CMD-07 | Phase 3 | Complete |
| CMD-08 | Phase 3 | Complete |
| CMD-09 | Phase 3 | Complete |
| CMD-10 | Phase 3 | Complete |

**Coverage:**
- v1 requirements: 26 total
- Mapped to phases: 26
- Unmapped: 0 ✓

**Note on SAFE-01..04:** These safeguards apply to autonomous skills across Phase 1 and 2. Assigned to Phase 1 as the first instantiation point. Phase 2 success criteria verify the pattern is correctly maintained in composition and autonomous skills.

---
*Requirements defined: 2026-03-14*
*Last updated: 2026-03-14 after roadmap creation*
