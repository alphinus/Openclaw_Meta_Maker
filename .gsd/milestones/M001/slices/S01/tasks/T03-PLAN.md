---
estimated_steps: 4
estimated_files: 3
---

# T03: Soul-, Identity- und Agent-Templates schreiben

**Slice:** S01 — Foundation — Templates, Format und Ordnerstruktur
**Milestone:** M001

## Description

Schreibt die drei übrigen Templates für das Ökosystem: `soul-template.md`, `identity-template.md`, `agent-template.md`. Diese Templates sind die Grundlage für S02 (10 Souls + 16 Identities) und S03 (16 Agents). 

Der kritische Punkt: Identity und Agent dürfen nicht verwechselt werden. Identity = Charakter-Persönlichkeit (wer bin ich, wie denke ich, wie kommuniziere ich). Agent = operationale Definition (was tue ich, wie arbeite ich, welche Skills nutze ich). Diese Trennung muss aus den Templates eindeutig erkennbar sein.

Jedes Template enthält: (1) Sektions-Definitionen mit Anweisungs-Kommentaren, (2) vollständiges Beispiel. Soul-Beispiel: `strategist`. Identity-Beispiel: `spock`. Agent-Beispiel: `worf`.

## Steps

1. `templates/soul-template.md` schreiben — Sektionen: Name, Philosophie, Core Values (3–5 Werte), Operating Principles (3–5 konkrete Handlungsprinzipien), Success Metrics (womit misst dieser Soul Erfolg), Geeignet für (für welche Agenten-Typen). Beispiel: Soul `strategist` vollständig ausfüllen.
2. `templates/identity-template.md` schreiben — Sektionen: Name, Charakter-Beschreibung, Persönlichkeitsmerkmale (Liste), Kommunikationsstil, Stärken (Liste), Schwächen (Liste), Star Trek Referenz (Zitat oder charakteristische Eigenschaft). Klarer Hinweis in Kommentaren: "Identity beschreibt WER der Agent ist — nicht WAS er tut". Beispiel: Identity `spock` vollständig ausfüllen.
3. `templates/agent-template.md` schreiben — Sektionen: Name, Mission (1 Satz), Capabilities (Liste konkreter Fähigkeiten), Operating Loop (step-by-step Arbeitsprozess), Constraints (Grenzen der Autonomie), Primärer Soul (Verweis auf soul/*.md), Primäre Skills (Liste von /elvis-* Skills). Klarer Hinweis: "Agent beschreibt WAS der Agent tut — nicht wer er ist (das ist Identity)". Beispiel: Agent `worf` vollständig ausfüllen.
4. Kurze Prüfung: Sind Identity `spock` und Agent `worf` so unterschiedlich strukturiert, dass die Trennung offensichtlich ist?

## Must-Haves

- [ ] Soul-Template hat mindestens 5 Sektions-Header
- [ ] Identity-Template hat mindestens 6 Sektions-Header
- [ ] Agent-Template hat mindestens 6 Sektions-Header inklusive `## Constraints`, `## Primärer Soul`, `## Primäre Skills`
- [ ] Identity und Agent sind inhaltlich klar unterscheidbar (Charakter vs. Betrieb)
- [ ] Alle 3 Templates haben vollständige Beispiele (kein Platzhalter-Text)
- [ ] Alle Inhalte auf Deutsch; Soul/Identity/Agent/Skill bleiben als Fachbegriffe englisch

## Verification

- `ls templates/` zeigt alle 4 Template-Dateien (soul, identity, agent, skill)
- `grep "^## " templates/soul-template.md` — mind. 5 Sektionen sichtbar
- `grep "^## " templates/identity-template.md` — mind. 6 Sektionen sichtbar
- `grep "^## " templates/agent-template.md` — mind. 6 Sektionen sichtbar; `Constraints` und `Primäre Skills` vorhanden

## Observability Impact

- Signals added/changed: Drei weitere Template-Dateien existieren; verify-Skript prüft nur skill-template.md (Sektion-Checks für Soul/Identity/Agent-Templates sind im verify-Skript nicht enthalten — das ist absichtlich, da deren Format weniger strikt standardisiert ist)
- How a future agent inspects this: `grep "^## " templates/*.md` — zeigt alle Sektions-Header aller Templates auf einen Blick
- Failure state exposed: Fehlende Template-Datei würde in S02/S03 sofort auffallen

## Inputs

- `M001-CONTEXT.md` — Agenten-Mapping (welche Star Trek Namen für welche Funktion)
- `DECISIONS.md` D004 (Star Trek Agenten-Namen), D002 (Deutsch)
- `templates/skill-template.md` (T02) — als formales Vorbild für Template-Aufbau

## Expected Output

- `templates/soul-template.md` — Template mit 5+ Sektionen; Beispiel `strategist`
- `templates/identity-template.md` — Template mit 6+ Sektionen; Beispiel `spock`; "wer bin ich" Charakter-Fokus
- `templates/agent-template.md` — Template mit 6+ Sektionen inkl. Constraints + Skills; Beispiel `worf`; "was tue ich" Betriebs-Fokus
