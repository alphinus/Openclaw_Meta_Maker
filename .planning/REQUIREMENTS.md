# Requirements: OpenClaw Meta Maker

**Defined:** 2026-03-14
**Core Value:** Komplettes, sofort importierbares Agent-Ökosystem für OpenClaw

## v1 Requirements

Requirements für die Fertigstellung. Jedes mappt auf Roadmap-Phasen.

### Meta Skills — Generatoren

- [ ] **META-01**: User kann mit `/elvis-soul-generator` eine neue Soul-Definition generieren die dem Template entspricht
- [ ] **META-02**: User kann mit `/elvis-identity-generator` eine neue Identity-Definition generieren die dem Template entspricht
- [ ] **META-03**: User kann mit `/elvis-agent-generator` eine neue Agent-Definition generieren die dem Template entspricht

### Meta Skills — Composition

- [ ] **META-04**: User kann mit `/elvis-agent-creator` einen kompletten Agenten aus Soul + Identity + Agent + Skills in < 2 Minuten zusammenstellen
- [ ] **META-05**: User kann mit `/elvis-skill-expander` bestehende Skills erweitern und neue Varianten ableiten (Borg)

### Meta Skills — System & Autonomous

- [ ] **META-06**: User kann mit `/elvis-system-analyzer` das gesamte Ökosystem auf Schwächen und Lücken analysieren (Troi)
- [ ] **META-07**: User kann mit `/elvis-library-manager` den Skill-Katalog organisieren, kategorisieren und durchsuchen (Uhura)
- [ ] **META-08**: User kann mit `/elvis-command-router` Anfragen an den richtigen Agent + Skill-Chain routen (Picard)
- [ ] **META-09**: User kann mit `/elvis-ecosystem-health` einen Gesundheitscheck des gesamten Systems durchführen

### Meta Skills — Erweitert

- [ ] **META-10**: User kann mit `/elvis-agent-optimizer` bestehende Agenten-Definitionen verbessern und optimieren
- [ ] **META-11**: User kann mit `/elvis-pattern-assimilation` Patterns aus externen Quellen ins Ökosystem integrieren (Borg)
- [ ] **META-12**: User kann mit `/elvis-concept-design` neue Agent-Konzepte entwerfen und validieren (Q)

### Safeguards

- [ ] **SAFE-01**: Alle autonomen Meta Skills (Q, Borg, Picard, Troi, Uhura) haben Max-Limit pro Durchlauf (≤ 10)
- [ ] **SAFE-02**: Alle autonomen Meta Skills haben Approval-Gate als nummerierter Ausführungsschritt
- [ ] **SAFE-03**: Alle autonomen Meta Skills haben explizite Stop-Bedingung
- [ ] **SAFE-04**: Alle autonomen Meta Skills haben Rollback-Hinweis

### Commands

- [ ] **CMD-01**: `/build-agent` — Routet zu Agent Creator Workflow
- [ ] **CMD-02**: `/generate-skills` — Routet zu Skill Generator + Expander
- [ ] **CMD-03**: `/analyze-system` — Routet zu System Analyzer
- [ ] **CMD-04**: `/optimize-agent` — Routet zu Agent Optimizer
- [ ] **CMD-05**: `/manage-library` — Routet zu Library Manager
- [ ] **CMD-06**: `/expand-skills` — Routet zu Skill Expander
- [ ] **CMD-07**: `/health-check` — Routet zu Ecosystem Health
- [ ] **CMD-08**: `/create-soul` — Routet zu Soul Generator
- [ ] **CMD-09**: `/create-identity` — Routet zu Identity Generator
- [ ] **CMD-10**: `/route-command` — Meta-Router für alle Commands (Picard)

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
| META-01 | Phase 1 | Pending |
| META-02 | Phase 1 | Pending |
| META-03 | Phase 1 | Pending |
| META-04 | Phase 2 | Pending |
| META-05 | Phase 2 | Pending |
| META-06 | Phase 2 | Pending |
| META-07 | Phase 2 | Pending |
| META-08 | Phase 1 | Pending |
| META-09 | Phase 2 | Pending |
| META-10 | Phase 2 | Pending |
| META-11 | Phase 2 | Pending |
| META-12 | Phase 2 | Pending |
| SAFE-01 | Phase 1 | Pending |
| SAFE-02 | Phase 1 | Pending |
| SAFE-03 | Phase 1 | Pending |
| SAFE-04 | Phase 1 | Pending |
| CMD-01 | Phase 3 | Pending |
| CMD-02 | Phase 3 | Pending |
| CMD-03 | Phase 3 | Pending |
| CMD-04 | Phase 3 | Pending |
| CMD-05 | Phase 3 | Pending |
| CMD-06 | Phase 3 | Pending |
| CMD-07 | Phase 3 | Pending |
| CMD-08 | Phase 3 | Pending |
| CMD-09 | Phase 3 | Pending |
| CMD-10 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 26 total
- Mapped to phases: 26
- Unmapped: 0 ✓

**Note on SAFE-01..04:** These safeguards apply to autonomous skills across Phase 1 and 2. Assigned to Phase 1 as the first instantiation point. Phase 2 success criteria verify the pattern is correctly maintained in composition and autonomous skills.

---
*Requirements defined: 2026-03-14*
*Last updated: 2026-03-14 after roadmap creation*
