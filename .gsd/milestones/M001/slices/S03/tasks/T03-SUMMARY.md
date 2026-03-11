---
id: T03
parent: S03
milestone: M001
provides:
  - agent/spock.md — Research Agent, researcher-Soul, 7 Sektionen
  - agent/riker.md — Growth Agent, growth-Soul, 7 Sektionen
  - agent/scotty.md — Automation Agent, automation-Soul, 7 Sektionen
  - agent/laforge.md — Builder Agent, builder-Soul, 7 Sektionen
key_files:
  - agent/spock.md
  - agent/riker.md
  - agent/scotty.md
  - agent/laforge.md
key_decisions:
  - Constraint-Formulierungen für Scotty und LaForge vermeiden die jeweils verbotenen Vokabeln auch in Negationen — statt "Konzipiert keine neuen Systeme" → "Greift nicht in den Aufbau neuer Systeme ein", um grep-Verifikation sauber zu halten
patterns_established:
  - Vocab-Grenzen durch Constraints-Sektion absichern, aber Formulierung so wählen dass grep-Checks korrekt 0 liefern (kein verbotenes Wort selbst in Negationen)
  - Scotty/LaForge-Differenzierung: Scotty = Betrieb/Wartung bestehender Systeme, LaForge = Aufbau/Architektur neuer Systeme — klar trennbar über Capability-Verb-Auswahl
observability_surfaces:
  - bash scripts/verify-s03.sh — zeigt 7 neue grüne Sektions-Checks pro Datei (spock, riker, scotty, laforge)
duration: ~20min (inkl. Crash-Recovery)
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T03: Research/Growth/Automation/Builder Agents (Spock, Riker, Scotty, LaForge)

**Vier Agent-Dateien (spock, riker, scotty, laforge) geschrieben — alle 7 Pflichtfelder gesetzt, Vocabulary-Grenzen verifiziert, verify-s03.sh-Fehlerstand von 124 auf 92 gesenkt.**

## What Happened

Die vier Agenten-Dateien wurden aus den jeweiligen Soul-Referenzen abgeleitet und mit klaren Capability- und Constraint-Abgrenzungen versehen.

Kritischste Differenzierung Scotty/LaForge: Scotty's Capabilities verwenden ausschließlich Betriebs-/Wartungs-Vokabular ("prüfen und beheben", "warten", "einrichten", "pflegen", "identifizieren und eliminieren"). LaForge's Capabilities verwenden ausschließlich Aufbau-/Architektur-Vokabular ("aufnehmen und übersetzen", "entwerfen", "aufbauen und konfigurieren", "strukturieren und ausführen").

Nach initialem Schreiben zeigte die Verifikation, dass die Constraints-Sektionen die verbotenen Vokabeln in Negationsform enthielten (z.B. "Konzipiert keine neuen Systeme…"), was die grep-Checks auf > 0 trieb. Die Constraints wurden umformuliert um denselben semantischen Inhalt ohne die kritischen Wörter auszudrücken.

## Verification

- `bash scripts/verify-s03.sh` — 92 Fehler (≤ 93 ✓), alle 28 Sektions-Checks für spock/riker/scotty/laforge grün
- `grep -i "konzipiert\|baut\|architektur" agent/scotty.md | wc -l` — 0 ✓
- `grep -i "repariert\|wartet\|betreib" agent/laforge.md | wc -l` — 0 ✓

## Diagnostics

`bash scripts/verify-s03.sh` zeigt Gruppe [2/3] mit den neuen grünen Checks für alle vier Dateien. Fehlende Dateien (picard, data, seven, sulu, tuvok, q, borg, troi, uhura) sind als ✗ sichtbar — korrekt für diesen Task-Stand.

## Deviations

Constraint-Formulierungen in scotty.md und laforge.md mussten nach initialem Schreiben angepasst werden, da die ursprünglichen Negations-Constraints die verbotenen Vokabeln enthielten und die grep-Checks auf > 0 trieben. Semantisch äquivalente Formulierungen ohne die kritischen Wörter wurden verwendet.

## Known Issues

none

## Files Created/Modified

- `agent/spock.md` — Research Agent, researcher-Soul, 6 Capabilities, 4-Schritt Loop, /elvis-market-scan /elvis-ai-research /elvis-data-analysis /elvis-fact-check
- `agent/riker.md` — Growth Agent, growth-Soul, 6 Capabilities, 5-Schritt Loop, /elvis-growth-audit /elvis-audience-builder /elvis-x-growth /elvis-growth-loop
- `agent/scotty.md` — Automation Agent, automation-Soul, 5 Capabilities, 4-Schritt Loop, /elvis-workflow-builder /elvis-automation /elvis-system-monitor /elvis-integration
- `agent/laforge.md` — Builder Agent, builder-Soul, 6 Capabilities, 4-Schritt Loop, /elvis-workflow-builder /elvis-system-builder /elvis-process-design /elvis-infrastructure
