# OpenClaw Meta Maker

## What This Is

Agent-Factory für OpenClaw: ein vollständiges, modulares Markdown-basiertes Agent-Ökosystem mit ~200 Dateien. Neue Agenten entstehen in unter 2 Minuten durch Kombination von Souls, Identities, Agents und Skills. Star Trek-Charaktere als Agenten-Personas. Alle Skills aufrufbar via `/elvis-[skill-name]`.

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

### Active

- [ ] ~14 Meta Skills (Generators, System, Autonomous Commands)
- [ ] ~10 Command-Definitionen (Command System als Markdown)
- [ ] Safeguards für autonome Agenten (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback)

### Out of Scope

- Ausführbarer Code jeglicher Art — reines Markdown-Projekt
- API-Verbindungen zu externen Diensten — kein Runtime
- Pixel Agents Visualisierung — separates Projekt
- Echte Social-Media-Automation — nur Skill-Definitionen

## Context

- Begonnen mit anderem GSD-Framework (`.gsd/`), jetzt mit neuem GSD-Workflow weitergeführt
- 81 von ~100 Skills existieren bereits, Qualität ist konsistent über alle Domänen
- Skill-Format ist bindend (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- Sprache: Deutsch, Fachbegriffe (Skill, Soul, Agent) bleiben Englisch
- Deduplizierung bereits durchgeführt (hook-writer, thread-writer, trend-scanner etc.)

## Constraints

- **Format**: Finales Skill-Format aus M001-CONTEXT bindend für alle neuen Skills
- **Sprache**: Deutsch mit englischen Fachbegriffen
- **Naming**: `/elvis-*` Convention für alle Skills
- **Safeguards**: Autonome Skills (Borg, Q, Picard, Troi, Uhura) brauchen explizite Limits
- **Konsistenz**: Neue Dateien müssen qualitativ zu den 81 existierenden Skills passen

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Star Trek Agenten-Mapping | Klare Funktions-Zuordnung, einprägsam | ✓ Good |
| 6 Skill-Domänen | Klare Trennung, keine Überlappung | ✓ Good |
| Erweitertes Skill-Format mit Verification | Skills müssen konkret genug für echte Ausführung sein | ✓ Good |
| Altes .gsd/ Framework verwerfen | Framework-Wechsel zu neuem GSD | ✓ Good |

---
*Last updated: 2026-03-14 after initialization*
