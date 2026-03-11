---
id: T04
parent: S03
milestone: M001
provides:
  - agent/data.md — Content Agent, creator-Soul, 7 Sektionen
  - agent/seven.md — Analysis Agent, analyst-Soul, 7 Sektionen
  - agent/sulu.md — Operator Agent, operator-Soul, 7 Sektionen
  - agent/tuvok.md — System/Security Agent, strategist-Soul, 7 Sektionen, kein Delegations-Vokabular
key_files:
  - agent/data.md
  - agent/seven.md
  - agent/sulu.md
  - agent/tuvok.md
key_decisions:
  - none
patterns_established:
  - Tuvok-Differenzierung von Worf durch Capabilities-Fokus auf Sicherheit/Systemintegrität statt Markt/Kampfstrategie; verbotenes Vokabular (delegier/orchestrier/koordinier) komplett vermieden durch Formulierung "Tuvok analysiert und berichtet, andere setzen um"
  - Data/Seven-Abgrenzung per expliziten Constraints — Data: "keine Datenanalyse", Seven: "keinen Content produzieren"
observability_surfaces:
  - bash scripts/verify-s03.sh — zeigt grüne Checks für alle 4 neuen Dateien (data, seven, sulu, tuvok)
  - grep -i "delegier\|orchestrier\|koordinier" agent/tuvok.md | wc -l — muss 0 bleiben
duration: ~15min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T04: Creator/Analyst/Operator/Strategist Agents (Data, Seven, Sulu, Tuvok)

**Vier Agent-Dateien (data, seven, sulu, tuvok) geschrieben — alle 7 Pflichtfelder gesetzt, verify-s03.sh-Fehlerstand von 92 auf 60 gesenkt.**

## What Happened

Alle vier Agent-Dateien wurden per direktem Write erstellt:

- **data.md** (creator-Soul): 6 Capabilities (Hooks, Langform, Varianten, Kalender, Ideen, Review), 4-Schritt-Loop, Constraints grenzen klar zu Seven (keine Analyse) und Worf (keine Strategie) ab.
- **seven.md** (analyst-Soul): 6 Capabilities (Metriken, Audits, Muster, Benchmarks, Reporting, Schwachstellen), 5-Schritt-Loop (Daten erfassen → bereinigen → Muster analysieren → Bedeutung extrahieren → Report erstellen), Constraints grenzen klar zu Data (kein Content) und Worf (keine Pläne) ab.
- **sulu.md** (operator-Soul): 5 Capabilities (Routing, Tracking, Queue, Status-Reports, Eskalation), 4-Schritt-Loop, Constraints verbieten strategische Planung und inhaltliche Task-Bearbeitung.
- **tuvok.md** (strategist-Soul): 6 Capabilities (Integrität, Sicherheitsanalyse, Logik-Validierung, Risiko-Assessment, Sicherheitspläne, Schwachstellen-Dokumentation), 4-Schritt-Loop. Kein Delegierungs- oder Orchestrierungsvokabular. Differenzierung von Worf durch Security/Systemintegrität-Fokus statt Markt/Kampfstrategie; Differenzierung von Picard durch fehlendes Delegations-Vokabular.

## Verification

- `bash scripts/verify-s03.sh` → **60 Fehler** (Ziel: ≤ 65) ✓
- `grep -i "delegier\|orchestrier\|koordinier" agent/tuvok.md | wc -l` → **0** ✓
- `grep "## Primärer Soul" agent/tuvok.md` + Inhalt → **soul/strategist.md** ✓

## Diagnostics

- `bash scripts/verify-s03.sh` zeigt Gruppe [1/3] mit grünen Existenz-Checks für data/seven/sulu/tuvok
- Gruppe [2/3] zeigt grüne Sektions-Checks für alle 4 Dateien (Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills)
- Verbleibende 60 Fehler betreffen noch nicht erstellte Agenten (picard, q, borg, troi, uhura) — korrekt für diesen Task-Stand

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `agent/data.md` — Content Agent, creator-Soul, 6 Capabilities, 4-Schritt-Loop, 7 Sektionen
- `agent/seven.md` — Analysis Agent, analyst-Soul, 6 Capabilities, 5-Schritt-Loop, 7 Sektionen
- `agent/sulu.md` — Operator Agent, operator-Soul, 5 Capabilities, 4-Schritt-Loop, 7 Sektionen
- `agent/tuvok.md` — System/Security Agent, strategist-Soul, 6 Capabilities, 4-Schritt-Loop, 7 Sektionen, kein Delegations-Vokabular
