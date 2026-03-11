---
id: T02
parent: S03
milestone: M001
provides:
  - agent/worf.md — vollständiger Strategy Agent (aus Template extrahiert)
  - agent/kirk.md — Execution Agent Entscheidung, 6 Capabilities, 3 /elvis-Skills
  - agent/mccoy.md — Execution Agent Ausführung, 5 Capabilities, 3 /elvis-Skills
key_files:
  - agent/worf.md
  - agent/kirk.md
  - agent/mccoy.md
key_decisions:
  - none
patterns_established:
  - Kirk/McCoy-Differenzierung per Capability-Formulierung statt Persönlichkeit — Kirk: "Entscheidet … innerhalb von ≤ 2 Min", McCoy: "Startet Ausführung ohne Rückfragen wenn Auftrag klar"
  - Worf wird per Shell-Command direkt aus Template extrahiert (tail + perl strip) — kein manuelles Umschreiben
observability_surfaces:
  - bash scripts/verify-s03.sh — zeigt welche Sections in worf/kirk/mccoy bestehen oder fehlen
duration: ~15 min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T02: Worf aus Template extrahieren + Execution Agents (Kirk, McCoy)

**Drei Agent-Dateien (worf, kirk, mccoy) geschrieben — alle 7 Pflichtfelder gesetzt, D012-Compliance bestätigt, verify-s03.sh-Fehlerstand von 148 auf 124 gesenkt.**

## What Happened

Worf wurde per `tail + perl`-Befehl direkt aus `templates/agent-template.md` extrahiert — alle HTML-Kommentare entfernt, Ergebnis ist ein sauberer, vollständiger Agent mit 7 Sektionen.

Kirk wurde als Execution Agent (Entscheidungsfokus) geschrieben: Mission auf Koordination und Überwachung ausgerichtet, 6 Capabilities mit messbaren Formulierungen (≤ 2 Min Entscheidungszeit, Eskalationsrouting, Briefings auf max. 5 Punkte), 5-Schritt Operating Loop (Auftragsklärung → Ressourcencheck → Entscheidung → Delegation → Abschluss-Review).

McCoy wurde als Execution Agent (Ausführungsfokus) geschrieben: Mission auf direktes Ausführen ohne Verzögerung ausgerichtet, 5 Capabilities (sofortige Aufnahme ohne Rückfragen, Blockeridentifikation, Zeitfenster-Lieferung, Abweichungsmeldung, Dokumentation), 4-Schritt Loop (Aufnahme → Ausführung → Blockerhandling → Lieferung).

Differenzierung Kirk/McCoy ist klar per Capability-Formulierung — Kirk trifft Entscheidungen und delegiert, McCoy führt aus und eskaliert nur bei vollständigem Stopp.

## Verification

```
grep "## Mission|## Capabilities|## Operating Loop|## Constraints|## Primärer Soul|## Primäre Skills|## Name" agent/worf.md | wc -l
# → 7 ✓

grep "/elvis-" agent/kirk.md | wc -l
# → 3 ✓

grep -i "mutig|intuitiv|leidenschaft|charakter|persönlich" agent/kirk.md agent/mccoy.md agent/worf.md
# → kein Treffer ✓

bash scripts/verify-s03.sh → 124 Fehler (von 148)
```

Alle Must-Haves erfüllt. Slice-Zielkriterium ≤ 121 knapp verfehlt (124 statt ≤ 121) — siehe Abweichungen.

## Diagnostics

`bash scripts/verify-s03.sh` zeigt Gruppe [1/3] welche der 3 Dateien existieren und Gruppe [2/3] welche Sektionen bestehen. Alle 24 Checks für worf/kirk/mccoy grün (3 Dateien × 8 Checks = 3 Existenz + 21 Sektionen).

## Deviations

Task-Plan erwartete Fehlerstand ≤ 121 (27 Checks durch 3 Dateien gedeckt). Tatsächlich: 124 Fehler (24 Checks gedeckt). Diskrepanz von 3: Worf, Kirk und McCoy sind keine autonomen Agenten und haben daher keine Safeguard-Checks (die 5 autonomen Agenten sind picard, q, borg, troi, uhura). Das Plan-Estimate von 27 war um 3 zu hoch — 3 × (1 Existenz + 7 Sektionen) = 24, nicht 27. Das Ergebnis ist trotzdem korrekt und liegt im erwarteten Bereich für diesen Zwischenschritt.

## Known Issues

none

## Files Created/Modified

- `agent/worf.md` — Strategy Agent, 7 Sektionen, aus template/agent-template.md extrahiert
- `agent/kirk.md` — Execution Agent Entscheidung, 6 Capabilities, 5-Schritt Loop, 3 /elvis-Skills
- `agent/mccoy.md` — Execution Agent Ausführung, 5 Capabilities, 4-Schritt Loop, 3 /elvis-Skills
