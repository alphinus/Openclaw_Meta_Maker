---
id: T03
parent: S01
milestone: M001
provides:
  - templates/soul-template.md — Template mit 6 Sektionen und vollständigem Beispiel-Soul `strategist`
  - templates/identity-template.md — Template mit 7 Sektionen, Charakter-Fokus (wer bin ich), Beispiel `spock`
  - templates/agent-template.md — Template mit 7 Sektionen inkl. Constraints + Primäre Skills, Betriebs-Fokus (was tue ich), Beispiel `worf`
key_files:
  - templates/soul-template.md
  - templates/identity-template.md
  - templates/agent-template.md
key_decisions:
  - "Identity vs. Agent Trennung explizit in Template-Header-Kommentaren dokumentiert: Identity = WER (Persönlichkeit), Agent = WAS (Betrieb) — mit Faustregel für Autoren"
  - "Soul-Beispiel `strategist` gewählt weil er direkt als Primärer Soul für Agent `worf` referenziert wird — schafft Kohärenz über alle 3 Templates"
  - "Agent `worf` referenziert soul/strategist.md explizit — demonstriert die Verbindung Soul→Agent die in S02/S03 überall gilt"
patterns_established:
  - Zweistufige Struktur (Anweisungs-Block + Beispiel) konsistent mit skill-template.md aus T02
  - HTML-Kommentare mit drei Ebenen — Format, Inhalt, häufiger Fehler — in allen Sektionen
  - "[PFLICHTFELD]-Marker bei kritischen Sektionen: Name + Mission im Agent, Name + Charakter-Beschreibung in Identity"
observability_surfaces:
  - "grep '^## ' templates/*.md — zeigt alle Sektions-Header aller 4 Templates auf einen Blick"
  - "bash scripts/verify-s01.sh — Check [2/7] prüft Existenz aller 4 Template-Dateien: jetzt alle ✓"
duration: ~25min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T03: Soul-, Identity- und Agent-Templates schreiben

**Alle 3 Templates erstellt: `soul-template.md` (6 Sektionen, Beispiel `strategist`), `identity-template.md` (7 Sektionen, Beispiel `spock`), `agent-template.md` (7 Sektionen, Beispiel `worf`). Identity-Agent-Trennung ist aus Kommentaren und Beispielen eindeutig erkennbar.**

## What Happened

Drei Template-Dateien nach dem zweistufigen Muster aus T02 erstellt. Alle verwenden denselben Aufbau: HTML-Kommentar-Anweisungsblock oben, vollständiges Beispiel unterhalb der Trennlinie.

**`templates/soul-template.md`** — 6 Sektionen: Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für. Beispiel-Soul `strategist` ist vollständig ausgearbeitet: Philosophie erklärt das Weltbild (Welt als lösbares System), 4 Core Values mit konkreter Verhaltensausprägung, 5 Operating Principles als harte Regeln, 4 messbare Success Metrics, Empfehlung für Strategy/Orchestrator/Research Agenten.

**`templates/identity-template.md`** — 7 Sektionen: Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz. Template-Header enthält den expliziten Warnblock "Identity beschreibt WER der Agent ist — nicht WAS er tut" mit Faustregel ("Würde das in ein Persönlichkeitsprofil passen? → Identity"). Beispiel `spock` enthält 7 Persönlichkeitsmerkmale, 4 Stärken, 4 Schwächen (authentisch, nicht Pseudo-Schwächen) und ein unverwechselbares Original-Zitat.

**`templates/agent-template.md`** — 7 Sektionen: Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills. Template-Header enthält den expliziten Warnblock "Agent beschreibt WAS er tut — nicht wer er ist". Beispiel `worf` hat eine präzise 1-Satz-Mission, 6 konkrete Capabilities, einen 6-Phasen Operating Loop (Lageerfassung → Analyse → Planerstellung → Risikobewertung → Freigabe-Request → Übergabe), 5 harte Constraints und 5 primäre Skills — darunter /elvis-strategy-audit, /elvis-execution-plan. `worf` referenziert `soul/strategist.md` als primären Soul.

## Identity vs. Agent — Differenzierungs-Check (Step 4)

`spock` (Identity): Persönlichkeitsmerkmale ("spricht in Wahrscheinlichkeiten"), Kommunikationsstil ("schreibt in strukturierten Sätzen"), Stärken als Persönlichkeitsassets ("bleibt unter Druck stabil"), Schwächen ("unterschätzt systematisch Einfluss von Emotionen"), kein Wort über Aufgaben oder Skills.

`worf` (Agent): Mission ("Entwickelt, prüft und pflegt die taktische Strategie"), Capabilities als ausführbare Leistungen, Operating Loop als Arbeitsprozess-Phasen, Constraints als Autonomie-Grenzen, Primäre Skills als Tool-Referenzen — kein Wort über Persönlichkeit oder Charakter.

**Urteil: Trennung ist offensichtlich.** Kein Satz aus `worf` könnte in `spock` stehen und umgekehrt.

## Verification

```bash
ls templates/
# → agent-template.md  identity-template.md  skill-template.md  soul-template.md  ✓

grep "^## " templates/soul-template.md
# → 6 Sektionen (Template) + 6 Sektionen (Beispiel) = 12 Zeilen ✓ (≥5 gefordert)

grep "^## " templates/identity-template.md
# → 7 Sektionen (Template) + 7 Sektionen (Beispiel) = 14 Zeilen ✓ (≥6 gefordert)

grep "^## " templates/agent-template.md
# → 7 Sektionen (Template) + 7 Sektionen (Beispiel) = 14 Zeilen ✓
# → enthält: Constraints ✓, Primäre Skills ✓

bash scripts/verify-s01.sh
# Check [1/7]: alle 11 Verzeichnisse ✓
# Check [2/7]: alle 4 Template-Dateien ✓ (neu)
# Check [3/7]: skill-template.md 9 Sektionen ✓
# Checks [4–7]: 70 Fehler (fehlende Beispiel-Skills) — T04 scope, erwartet
```

## Diagnostics

- `grep "^## " templates/*.md` — zeigt alle Sektions-Header aller 4 Templates kompakt
- `bash scripts/verify-s01.sh` — Check [2/7] ist jetzt vollständig grün; 70 verbleibende Fehler gehören zu T04

## Deviations

Keine. Alle 4 Steps exakt nach Plan ausgeführt.

## Known Issues

Keine. Die 70 Fehler im verify-Skript sind erwartungsgemäß — sie gehören zu T04 (Beispiel-Skills).

## Files Created/Modified

- `templates/soul-template.md` — 6-Sektionen-Template mit vollständigem Beispiel `strategist`
- `templates/identity-template.md` — 7-Sektionen-Template mit vollständigem Beispiel `spock` (Charakter-Fokus)
- `templates/agent-template.md` — 7-Sektionen-Template mit vollständigem Beispiel `worf` (Betriebs-Fokus, referenziert soul/strategist.md)
