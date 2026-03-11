# Project

## What This Is

OpenClaw Meta Maker ist ein vollständiges, modulares Agent-Ökosystem für OpenClaw — bestehend aus Markdown-Dateien die direkt importiert oder verwendet werden können. Es enthält Souls, Identities, Agents, Skills und ein Command System, die zusammen eine skalierbare Agent-Factory bilden.

Die Agenten tragen Namen aus dem Star Trek Universum (Kirk, Spock, Picard, Data, etc.) und sind auf Growth, Content, Research, Strategy, Automation und Meta-Agent-Aufgaben spezialisiert.

## Core Value

~100 vollständig ausgearbeitete Skills mit konkreten Execution Steps, Constraints, Verification und Dependencies — so dass ein AI-Agent jeden Skill ohne Interpretation ausführen kann.

## Current State

S01, S02 und S03 abgeschlossen. Foundation + philosophische Grundlage + Agent Layer vollständig:
- **11 Verzeichnisse** angelegt (soul/, identity/, agent/, skills/{growth,content,research,strategy,automation,meta}/, commands/, templates/)
- **4 Templates** mit Anweisungs-Block + vollständigem Beispiel: skill-template.md, soul-template.md, identity-template.md, agent-template.md
- **6 Benchmark-Skills** (je einer pro Kategorie): elvis-growth-audit, elvis-x-hook-writer, elvis-market-scan, elvis-execution-plan, elvis-workflow-builder, elvis-skill-generator
- **10 Soul-Dateien** (soul/*.md) — vollständig mit 6 Sektionen, klaren Philosophie-Abgrenzungen und Agent-Mapping in "## Geeignet für"
- **16 Identity-Dateien** (identity/*.md) — vollständig mit 7 Sektionen, authentischen Star Trek Charakter-Profilen, Soul-Kohärenz und originalen Zitaten
- **16 Agent-Dateien** (agent/*.md) — vollständig mit 7 Pflichtfeldern (Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills); 5 autonome Agenten mit D007-Safeguards
- **verify-s03.sh** läuft mit Exit-Code 0 (alle 148 Checks grün)
- Nächster Schritt: S04 (Growth + Content Skills, ~30 Skills)

## Architecture / Key Patterns

- **Integrierte Ordnerstruktur**: Ein Root-Verzeichnis mit `soul/`, `identity/`, `agent/`, `skills/`, `meta-agent/`, `commands/`, `templates/`
- **Skill-Format**: `Name → Description → Objectives → Strategy → Constraints → Execution Steps → Verification → Dependencies → Output`
- **Naming Convention**: Alle Skills verwenden `/elvis-*` Prefix
- **Agenten-Namen**: Ausschließlich Star Trek Charaktere (Kirk, Spock, Picard, Data, Worf, Scotty, LaForge, Seven, Sulu, Tuvok, McCoy, Riker, Q, Borg, Troi, Uhura)
- **Sprache**: Deutsch
- **Safeguards**: Autonome Agenten haben Max-Limits, Approval-Gates und Stop-Bedingungen

## Capability Contract

Siehe `.gsd/REQUIREMENTS.md`

## Milestone Sequence

- [ ] M001: OpenClaw Meta Maker — Vollständiges Agent-Ökosystem mit 16 Star Trek Agenten, ~100 Skills und Command System
