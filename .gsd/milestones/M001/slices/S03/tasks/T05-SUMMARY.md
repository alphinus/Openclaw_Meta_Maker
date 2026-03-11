---
id: T05
parent: S03
milestone: M001
provides:
  - agent/picard.md — Orchestrator Agent, strategist-Soul, 7 Sektionen, D007-Safeguards
  - agent/q.md — Agent Creator, creator-Soul, 7 Sektionen, D007-Safeguards
  - agent/borg.md — Skill Expander, automation-Soul, 7 Sektionen, D007-Safeguards
  - agent/troi.md — System Analyzer, analyst-Soul, 7 Sektionen, D007-Safeguards
  - agent/uhura.md — Library Manager, operator-Soul, 7 Sektionen, D007-Safeguards
key_files:
  - agent/picard.md
  - agent/q.md
  - agent/borg.md
  - agent/troi.md
  - agent/uhura.md
key_decisions:
  - none
patterns_established:
  - Alle 4 Safeguard-Marker (**Max-Limit:**, **Approval-Gate:**, **Stop-Bedingung:**, **Rollback-Hinweis:**) als eigene fett formatierte Absätze im Constraints-Block — grep-detektierbar per `grep -l "**Max-Limit:**" agent/`
  - Max-Limits immer als konkrete Zahlen (3, 5, 10) — keine vagen Formulierungen
  - Troi vs. Seven: Troi = schwache Signale + Kontext + Querverweise; Seven = strukturierte Datenanalyse + Kennzahlen
  - Picard vs. Worf/Tuvok: Picard orchestriert andere Agenten (delegiert, konsolidiert); Worf = Markt/Kampfstrategie; Tuvok = Sicherheit/Systemintegrität
observability_surfaces:
  - bash scripts/verify-s03.sh — 148-Check Report, Exit-Code 0 = vollständig grün
  - grep -rl "**Max-Limit:**" agent/ | wc -l — zeigt 5 (alle Safeguard-Agenten)
duration: <15min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T05: Autonome Agents mit Safeguards (Picard, Q, Borg, Troi, Uhura) + Final Verification

**5 autonome Agent-Dateien mit D007-konformen Safeguards geschrieben — verify-s03.sh erreicht Exit-Code 0, alle 148 Checks grün.**

## What Happened

Alle 5 verbleibenden Agent-Dateien wurden per Bash-Heredoc erstellt:

- **picard.md**: strategist-Soul, 6 Capabilities, 5-Schritt Loop (Aufgabenanalyse → Konsolidierung). Differenziert von Worf/Tuvok durch expliziten Orchestrierungs-Fokus — delegiert Teilaufgaben an andere Agenten und konsolidiert deren Ergebnisse. Max-Limit: 3 parallele Delegationen.
- **q.md**: creator-Soul, 6 Capabilities, 4-Schritt Loop. Erstellt neue Agent-Definitionen, Skills und Soul-Archetypes. Entwürfe bleiben bis zur Operator-Freigabe als Draft. Max-Limit: 3 neue Objekte.
- **borg.md**: automation-Soul, 5 Capabilities, 4-Schritt Loop. Systematische Erweiterung der Skill-Library — Scan → Lücken → Erstellen → Konformitäts-Check. Max-Limit: 5 neue Skills.
- **troi.md**: analyst-Soul, 6 Capabilities, 4-Schritt Loop. Differenziert von Seven durch Signal/Kontext-Fokus — schwache Signale, Querverweise, qualitative Faktoren die rein datenbasierte Analysen übersehen. Max-Limit: 1 vollständige System-Analyse.
- **uhura.md**: operator-Soul, 5 Capabilities, 4-Schritt Loop. Verwaltet Skill-Library als kommunikatives Rückgrat — Aufnahme, Archivierung, Routing-Pflege. Max-Limit: 10 Library-Änderungen.

Alle 5 Agenten enthalten alle 4 Safeguard-Marker fett formatiert im Constraints-Block.

## Verification

```
bash scripts/verify-s03.sh
# → ✅ S03 Verifikation bestanden — alle 148 Checks grün (Exit-Code 0)

grep -l "**Max-Limit:**" agent/picard.md agent/q.md agent/borg.md agent/troi.md agent/uhura.md | wc -l
# → 5

grep -rl "**Max-Limit:**" agent/ | wc -l      # → 5
grep -rl "**Approval-Gate:**" agent/ | wc -l  # → 5
grep -rl "**Stop-Bedingung:**" agent/ | wc -l # → 5
grep -rl "**Rollback-Hinweis:**" agent/ | wc -l # → 5
ls agent/*.md | wc -l                         # → 16
```

## Diagnostics

- `bash scripts/verify-s03.sh` — primäre Inspection Surface; zeigt [1/3] Datei-Existenz, [2/3] Sektions-Checks, [3/3] Safeguard-Marker; Exit-Code = Fehleranzahl
- `grep -rl "**Max-Limit:**" agent/` — zeigt alle 5 autonomen Agenten mit Safeguards

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `agent/picard.md` — Orchestrator Agent, strategist-Soul, 6 Capabilities, D007-Safeguards (Max: 3 Delegationen)
- `agent/q.md` — Agent Creator, creator-Soul, 6 Capabilities, D007-Safeguards (Max: 3 Objekte)
- `agent/borg.md` — Skill Expander, automation-Soul, 5 Capabilities, D007-Safeguards (Max: 5 Skills)
- `agent/troi.md` — System Analyzer, analyst-Soul, 6 Capabilities, D007-Safeguards (Max: 1 Analyse)
- `agent/uhura.md` — Library Manager, operator-Soul, 5 Capabilities, D007-Safeguards (Max: 10 Änderungen)
