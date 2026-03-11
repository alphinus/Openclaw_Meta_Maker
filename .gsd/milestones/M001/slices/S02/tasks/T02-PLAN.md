---
estimated_steps: 6
estimated_files: 5
---

# T02: 5 Souls schreiben — researcher, execution, builder, growth, automation

**Slice:** S02 — Souls und Identities
**Milestone:** M001

## Description

Die 5 klar abgegrenzten Soul-Archetypes schreiben — die mit dem geringsten Verwechslungsrisiko, aber hoher konzeptueller Klarheit. Reihenfolge entspricht S02-RESEARCH.md (Empfehlung 1–5). `soul/strategist.md` ist bereits fertig (T01) und dient als Qualitäts-Benchmark. Jeder Soul muss klar von allen anderen abgegrenzt sein — die `## Philosophie`-Sektion trägt die Hauptlast dieser Differenzierung.

## Steps

1. `soul/researcher.md` schreiben: Weltbild = Wissenssuche als Wert. Kernfrage: "Was ist wahr?" Niemals Meinung ohne Beleg. Faktenbasis vor Handlung. Primäre Agenten: Spock (Research Agent). `## Geeignet für` explizit. 6 Sektionen.
2. `soul/execution.md` schreiben: Weltbild = Ergebnis über Prozess. Handeln bevor alle Fakten vorliegen (akzeptiertes Risiko). Energie und Direktheit über Eleganz. Primäre Agenten: Kirk (Haupt-Agent), McCoy (Execution Agent). `## Geeignet für` explizit. 6 Sektionen. Abgrenzung zu `strategist`: execution handelt sofort, strategist plant zuerst — dies muss in der Philosophie spürbar sein.
3. `soul/builder.md` schreiben: Weltbild = konstruiert Bekanntes besser und robuster. Engineering-Mindset: Systeme haben Struktur, Struktur hat Gesetze, Gesetze können verstanden werden. Inkrementelle Verbesserung ist Fortschritt. Primäre Agenten: LaForge (Builder Agent), Scotty (sekundär). `## Geeignet für` explizit. 6 Sektionen. Abgrenzung zu `creator`: builder verbessert/konstruiert Bestehendes, creator erschafft Neues.
4. `soul/growth.md` schreiben: Weltbild = Expansion und Skalierung als Ziel. Wo andere Grenzen sehen, sieht dieser Soul Ausgangspunkte. Ambition wird immer nach oben kalibriert. Primäre Agenten: Riker (Growth Agent). `## Geeignet für` explizit. 6 Sektionen. Abgrenzung zu `execution`: growth = skaliert und expandiert auf lange Sicht; execution = liefert jetzt.
5. `soul/automation.md` schreiben: Weltbild = Systeme sind besser als Einzellösungen; Wiederholbarkeit ist Qualität. Was einmal gut gelöst wurde, wird assimiliert und repliziert. Komplexität durch Standardisierung reduzieren. Primäre Agenten: Scotty (Automation Agent), Borg (Skill Expander). `## Geeignet für` explizit. 6 Sektionen. Abgrenzung zu `builder`: automation = macht Prozesse wiederholbar; builder = konstruiert Artefakte.
6. `bash scripts/verify-s02.sh` ausführen — Fehleranzahl prüfen, dokumentieren

## Must-Haves

- [ ] Alle 5 soul/*.md existieren mit exakt 6 Sektionen (`## Name`, `## Philosophie`, `## Core Values`, `## Operating Principles`, `## Success Metrics`, `## Geeignet für`)
- [ ] Alle `## Operating Principles` als feste Regeln formuliert ("tut immer X", "tut nie Y") — nicht als Wünsche ("sollte X berücksichtigen")
- [ ] Philosophien klar voneinander abgegrenzt: execution ≠ strategist, builder ≠ creator, automation ≠ builder
- [ ] `## Geeignet für` nennt explizit die Star Trek Agenten-Namen aus dem Mapping in S02-RESEARCH.md
- [ ] Qualitätsniveau: Operating Principles mindestens so konkret wie im strategist-Benchmark (`soul/strategist.md`)

## Verification

- `bash scripts/verify-s02.sh` — Fehleranzahl sinkt auf ≤148 (vorher ≤183; neue korrekte Checks: 5 Dateien × 7 Checks = 35)
- `grep -c "^## " soul/researcher.md soul/execution.md soul/builder.md soul/growth.md soul/automation.md` — jede gibt 6 zurück
- `grep -c "sollte\|könnte\|würde" soul/execution.md` — sollte gering sein (keine Wunsch-Formulierungen in Prinzipien)
- `grep "Geeignet für" soul/builder.md` — enthält "LaForge" und "Scotty"

## Observability Impact

- Signals added/changed: `bash scripts/verify-s02.sh` zeigt Fortschritt; Fehleranzahl reduziert sich um ≥35
- How a future agent inspects this: Skript zeigt welche Dateien/Sektionen noch fehlen
- Failure state exposed: Fehlende Sektionen werden einzeln mit Dateiname gemeldet

## Inputs

- `soul/strategist.md` — Qualitäts-Benchmark aus T01 (konkrete Operating Principles, differenzierte Philosophie)
- `templates/soul-template.md` — verbindliches 6-Sektionen-Format
- S02-RESEARCH.md — Soul → Agent Mapping Tabelle (bindend für `## Geeignet für` Inhalte)
- S02-RESEARCH.md — Abgrenzungs-Hinweise und Common Pitfalls

## Expected Output

- `soul/researcher.md` — 6 Sektionen, Weltbild "Was ist wahr?", Spock als primärer Agent
- `soul/execution.md` — 6 Sektionen, Weltbild "Ergebnis vor Prozess", Kirk + McCoy als primäre Agenten
- `soul/builder.md` — 6 Sektionen, Weltbild "Konstruiert Bekanntes besser", LaForge als primärer Agent
- `soul/growth.md` — 6 Sektionen, Weltbild "Expansion als Grundhaltung", Riker als primärer Agent
- `soul/automation.md` — 6 Sektionen, Weltbild "Systeme > Einzellösungen", Scotty + Borg als primäre Agenten
