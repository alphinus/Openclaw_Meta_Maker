# Project

## What This Is

OpenClaw Meta Maker ist ein vollständiges, modulares Agent-Ökosystem für OpenClaw — bestehend aus Markdown-Dateien die direkt importiert oder verwendet werden können. Es enthält Souls, Identities, Agents, Skills und ein Command System, die zusammen eine skalierbare Agent-Factory bilden.

Die Agenten tragen Namen aus dem Star Trek Universum (Kirk, Spock, Picard, Data, etc.) und sind auf Growth, Content, Research, Strategy, Automation und Meta-Agent-Aufgaben spezialisiert.

## Core Value

~100 vollständig ausgearbeitete Skills mit konkreten Execution Steps, Constraints, Verification und Dependencies — so dass ein AI-Agent jeden Skill ohne Interpretation ausführen kann.

## Current State

Projekt initialisiert. Noch keine Dateien außer GSD-Artefakten.

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
