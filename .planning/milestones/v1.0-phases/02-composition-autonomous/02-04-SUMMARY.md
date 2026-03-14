---
phase: 02-composition-autonomous
plan: "04"
subsystem: meta
tags: [skill-management, library-manager, agent-optimizer, safeguard-quartet, approval-gate, uhura]

requires:
  - phase: 01-generators-router
    provides: elvis-skill-generator gold-standard für Safeguard-Quartet Pattern und 9-Sektionen-Format
  - phase: 02-composition-autonomous
    provides: elvis-agent-generator mit Querverweisvalidierungs-Pattern für Agent-Optimizer

provides:
  - skills/meta/elvis-library-manager.md — Skill-Katalog-Verwaltung mit Inventar, Vollständigkeits-Check, Duplikat-Erkennung, Approval-Gate vor Reorganisation
  - skills/meta/elvis-agent-optimizer.md — Agent-Schwächen-Analyse und optimierte Version-Generierung, Scope auf agent/*.md beschränkt

affects: [03-command-layer, Command-Router muss beide Skills in Routing-Tabelle aufnehmen]

tech-stack:
  added: []
  patterns:
    - "Inventar-vor-Änderung: Erst Ist-Stand erfassen und präsentieren, dann Approval-Gate, dann Änderungs-Anweisungen als Operator-Aktionen"
    - "Scope-Disziplin: Agent-Optimizer benennt Out-of-Scope-Issues (Soul/Skills) im Report aber verweist auf zuständige Skills"
    - "Approval-Gate als nummerierter Ausführungsschritt mit 'warte auf explizite Bestätigung' Halt-Punkt"

key-files:
  created:
    - skills/meta/elvis-library-manager.md
    - skills/meta/elvis-agent-optimizer.md
  modified: []

key-decisions:
  - "Approval-Gate für Library-Manager nach Schritt 4 (Änderungsvorschläge) — nicht nach Schritt 3 (Katalog): Katalog-Ausgabe ist lesend, strukturelle Änderungen brauchen Approval"
  - "Library-Manager Änderungen als Operator-Anweisungen ausgeben (nicht als automatische Dateioperationen): Operator behält Kontrolle über Dateisystem"
  - "Agent-Optimizer Scope hart auf agent/*.md beschränkt: Soul- und Skill-Korrekturen verweisen auf zuständige Skills statt selbst zu agieren"
  - "Original-Agent-Datei bleibt unverändert: Optimizer präsentiert Optimierung als Chat-Output, kein automatisches Überschreiben"

patterns-established:
  - "Verwaltungs-Skill Pattern: Inventar → Vollständigkeits-Check → Katalog-Ausgabe → Approval-Gate → Änderungs-Anweisungen als Operator-Aktionen"
  - "Analyse-vor-Generierung: Schwächen-Report präsentieren und bestätigen lassen bevor optimierte Version generiert wird"

requirements-completed: [META-07, META-10]

duration: 5min
completed: 2026-03-14
---

# Phase 2 Plan 04: Library-Manager und Agent-Optimizer Summary

**Library-Manager (Uhura, META-07) und Agent-Optimizer (META-10) als Verwaltungs-Skills mit Inventar-vor-Änderung-Prinzip und Scope-Disziplin auf definierten Verzeichnissen**

## Performance

- **Duration:** 5 min
- **Started:** 2026-03-14T18:56:15Z
- **Completed:** 2026-03-14T19:01:16Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- `skills/meta/elvis-library-manager.md` — inventarisiert `skills/`-Verzeichnis, erstellt 4-spaltigen Markdown-Katalog, prüft 9-Sektionen-Vollständigkeit, erkennt Duplikate, stellt Änderungsvorschläge vor Approval-Gate als Tabelle bereit, gibt bestätigte Änderungen als Operator-Anweisungen aus
- `skills/meta/elvis-agent-optimizer.md` — analysiert `agent/[name].md` gegen template, erstellt 5-spaltigen Schwächen-Report (Issue/Typ/Schwere/Empfehlung), generiert nach Approval optimierte Agent-Definition, präsentiert Vorher/Nachher-Diff als 4-spaltige Tabelle

## Task Commits

Each task was committed atomically:

1. **Task 1: Library-Manager Skill erstellen (Uhura, META-07)** - `672c572` (feat)
2. **Task 2: Agent-Optimizer Skill erstellen (META-10)** - `90c3c3a` (feat)

**Plan metadata:** `6fd4242` (docs: complete plan)

## Files Created/Modified

- `skills/meta/elvis-library-manager.md` — Meta-Skill zur Verwaltung und Kategorisierung des Skill-Katalogs mit Approval-Gate vor strukturellen Änderungen
- `skills/meta/elvis-agent-optimizer.md` — Meta-Skill zur Optimierung bestehender Agent-Definitionen, Scope auf agent/*.md beschränkt

## Decisions Made

- Approval-Gate im Library-Manager nach Schritt 4 (Änderungsvorschläge) platziert, nicht nach Schritt 3 (Katalog): Katalog-Ausgabe ist eine lesende Operation und braucht kein Approval — strukturelle Änderungen hingegen schon
- Library-Manager gibt Änderungen als Operator-Anweisungen aus (nicht als automatische Dateioperationen): Uhura hat keine Schreibrechte auf das Dateisystem, Operator führt Verschiebungen manuell aus
- Agent-Optimizer Scope hart auf `agent/*.md` beschränkt: wenn Soul- oder Skill-Probleme gefunden werden, benennt der Report sie als Issues und verweist auf `/elvis-soul-generator` bzw. `/elvis-skill-generator` — keine Scope-Ausweitung
- Original-Agent-Datei bleibt unverändert: Optimizer präsentiert optimierte Version als neuen Chat-Output, kein automatisches Überschreiben der Quelldatei

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Alle 7 Meta-Skills aus Phase 2 sind jetzt vollständig (elvis-agent-creator, elvis-skill-expander, elvis-concept-design, elvis-system-analyzer, elvis-ecosystem-health, elvis-library-manager, elvis-agent-optimizer)
- Phase 3 (Command Layer) kann starten: Command-Router Routing-Tabelle muss um alle Phase-2-Skills erweitert werden
- Kein Blocker für Phase 3

## Self-Check: PASSED

- FOUND: skills/meta/elvis-library-manager.md
- FOUND: skills/meta/elvis-agent-optimizer.md
- FOUND: .planning/phases/02-composition-autonomous/02-04-SUMMARY.md
- FOUND: commit 672c572 (Task 1)
- FOUND: commit 90c3c3a (Task 2)
- FOUND: commit 6fd4242 (Plan metadata)

---
*Phase: 02-composition-autonomous*
*Completed: 2026-03-14*
