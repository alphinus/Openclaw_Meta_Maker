---
phase: 02-composition-autonomous
plan: "02"
subsystem: meta-skills
tags: [skill-expander, concept-design, borg, q, meta-05, meta-12, safeguard-quartet]
dependency_graph:
  requires: []
  provides:
    - skills/meta/elvis-skill-expander.md
    - skills/meta/elvis-concept-design.md
  affects:
    - agent/borg.md
    - agent/q.md
    - skills/meta/elvis-command-router.md
tech_stack:
  added: []
  patterns:
    - Plan-Approve-Execute (Generator-Skill Pattern)
    - Safeguard-Quartet (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback)
    - D006 (konkrete Mengen, Formate, Zeitangaben in Ausführungsschritten)
key_files:
  created:
    - skills/meta/elvis-skill-expander.md
    - skills/meta/elvis-concept-design.md
  modified: []
decisions:
  - "Skill-Expander Approval-Gate nach Übersichts-Tabelle (Schritt 3): Operator bestätigt welche Richtungen sinnvoll sind bevor Ausarbeitungsaufwand entsteht"
  - "Concept-Design Approval-Gate nach Konzept-Entwurf (Schritt 4): Validierung erfolgt vor finaler Formatierung — Korrekturen kosten nichts wenn sie früh erkannt werden"
  - "Rollback-Strategie für beide Skills: vollständige Neu-Generierung statt iterative Korrektur — konsistent mit Phase-1-Pattern"
  - "Concept-Design: explizite Ökosystem-Prüfung (agent/*.md + soul/*.md) als Pflicht-Schritte 2-3 verhindert Duplikate und stellt Soul-Verfügbarkeit sicher"
metrics:
  duration: "4 minutes"
  completed_date: "2026-03-14"
  tasks_completed: 2
  files_created: 2
  files_modified: 0
---

# Phase 2 Plan 02: Skill-Expander + Concept-Design Summary

**One-liner:** Skill-Expander (Borg) generiert bis zu 5 vollständige 9-Sektionen-Varianten aus einem Basis-Skill; Concept-Design (Q) liefert ein validiertes Agent-Konzept-Dokument (Mission, Soul, Skill-Bedarf, Machbarkeit) als Vorstufe zu /elvis-agent-creator.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Skill-Expander Skill erstellen (Borg, META-05) | fcca65e | skills/meta/elvis-skill-expander.md |
| 2 | Concept-Design Skill erstellen (Q, META-12) | 46d7c5b | skills/meta/elvis-concept-design.md |

## What Was Built

### elvis-skill-expander.md (META-05)

Generator-Skill für Borg. Plan-Approve-Execute-Pattern mit einem bestehenden Skill als Basis-Input statt einer freien Anforderung.

- Approval-Gate nach Varianten-Übersichts-Tabelle (Schritt 3): 4-spaltige Tabelle (Name, Kategorie, Beschreibung, Abgrenzung) muss bestätigt werden
- Max. 5 Varianten pro Durchlauf — konsistent mit `agent/borg.md` Constraints
- Jede Variante wird als vollständige 9-Sektionen-Skill-Definition ausgearbeitet (nicht als Liste)
- Basis-Skill-Analyse in Schritt 2 bevor Varianten vorgeschlagen werden: Kategorie, Kernfunktion, 3 Erweiterungsrichtungen
- Rollback: fehlerhafte Variante vollständig neu generieren, max. 2 Versuche pro Variante

### elvis-concept-design.md (META-12)

Generator-Skill für Q. Plan-Approve-Execute-Pattern mit Output als Konzept-Dokument, nicht als fertiger Agent.

- Approval-Gate nach Konzept-Entwurf (Schritt 4): vollständiger Entwurf muss bestätigt werden
- Max. 1 Konzept pro Durchlauf — Konzeptvalidierung braucht Tiefe
- Pflicht-Ökosystem-Prüfung: `agent/*.md` auf Duplikate (Schritt 2), `soul/*.md` auf passenden Soul (Schritt 3)
- 6-Elemente-Konzept-Dokument: Mission, Soul-Empfehlung, Identity-Charakter, Skill-Bedarf (existiert/fehlt), Machbarkeits-Einschätzung, nächste Schritte
- Expliziter Verweis auf `/elvis-agent-creator` als nächsten Schritt nach Konzept-Freigabe
- Rollback: Entwurf komplett verwerfen, max. 3 Revisionsversuche

## Decisions Made

1. **Skill-Expander Approval-Gate nach Übersichts-Tabelle (Schritt 3):** Operator bestätigt welche Richtungen sinnvoll sind bevor Ausarbeitungsaufwand entsteht — identisches Pattern zum Skill-Generator aus Phase 1.

2. **Concept-Design Approval-Gate nach Konzept-Entwurf (Schritt 4):** Validierung erfolgt vor finaler Formatierung — Korrekturen kosten nichts wenn sie früh erkannt werden, kostenintensiv erst beim Agent-Creator.

3. **Rollback als vollständige Neu-Generierung:** Beide Skills verwenden dasselbe Rollback-Pattern aus Phase 1 — kein iteratives Patchen, präzisierte Anforderung + Neu-Generierung ist schneller.

4. **Ökosystem-Prüfung als Pflicht-Schritte in Concept-Design:** Duplikat-Erkennung und Soul-Verfügbarkeit werden vor dem Konzept-Entwurf geprüft — verhindert dass spät im Prozess auf fehlende Ressourcen gestoßen wird.

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- FOUND: skills/meta/elvis-skill-expander.md
- FOUND: skills/meta/elvis-concept-design.md
- FOUND: .planning/phases/02-composition-autonomous/02-02-SUMMARY.md
- FOUND: commit fcca65e (elvis-skill-expander)
- FOUND: commit 46d7c5b (elvis-concept-design)
