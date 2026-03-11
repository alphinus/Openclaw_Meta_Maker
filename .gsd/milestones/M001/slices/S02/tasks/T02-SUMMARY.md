---
id: T02
parent: S02
milestone: M001
provides:
  - soul/researcher.md — 6 Sektionen, Weltbild "Was ist wahr?", Spock als primärer Agent
  - soul/execution.md — 6 Sektionen, Weltbild "Ergebnis vor Prozess", Kirk + McCoy als primäre Agenten
  - soul/builder.md — 6 Sektionen, Weltbild "Konstruiert Bekanntes besser", LaForge als primärer Agent
  - soul/growth.md — 6 Sektionen, Weltbild "Expansion als Grundhaltung", Riker als primärer Agent
  - soul/automation.md — 6 Sektionen, Weltbild "Systeme > Einzellösungen", Scotty + Borg als primäre Agenten
key_files:
  - soul/researcher.md
  - soul/execution.md
  - soul/builder.md
  - soul/growth.md
  - soul/automation.md
key_decisions:
  - none (alle Entscheidungen folgen bereits dokumentierten Patterns aus T01 und S02-RESEARCH.md)
patterns_established:
  - Abgrenzung execution vs. strategist explizit in Philosophie-Sektion (handelt sofort vs. plant zuerst)
  - Abgrenzung builder vs. creator explizit in Philosophie-Sektion (konstruiert Bekanntes vs. erschafft Neues)
  - Abgrenzung automation vs. builder explizit in Philosophie-Sektion (macht Prozesse wiederholbar vs. konstruiert Artefakte)
  - Abgrenzung growth vs. execution explizit in Philosophie-Sektion (skaliert langfristig vs. liefert jetzt)
  - Operating Principles durchgehend als feste Verhaltensregeln (tut X, verweigert Y) — keine Wunsch-Formulierungen
observability_surfaces:
  - bash scripts/verify-s02.sh — zeigt 148 Fehler (von 183); alle 6 neuen Soul-Sektionen grün
duration: ~30 min
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T02: 5 Souls schreiben — researcher, execution, builder, growth, automation

**5 Soul-Archetypes mit klaren Philosophien, konkreten Operating Principles und explizitem Agent-Mapping geschrieben — verify-s02.sh sinkt von 183 auf 148 Fehler (−35).**

## What Happened

Alle 5 Soul-Dateien nach dem strategist-Benchmark aus T01 geschrieben. Jede Datei enthält exakt 6 Sektionen im vorgeschriebenen Format. Die kritische Herausforderung war die konzeptuelle Abgrenzung zwischen ähnlichen Souls:

- **execution vs. strategist**: execution handelt sofort auf Basis unvollständiger Information, strategist analysiert zuerst und handelt dann — der Unterschied ist explizit in beiden Philosophie-Sektionen benannt.
- **builder vs. creator**: builder konstruiert Bekanntes besser/robuster (Engineering), creator erschafft Neues aus dem Nichts (generativ) — LaForge baut, Data erschafft.
- **automation vs. builder**: automation macht Prozesse wiederholbar (das Wie wird systematisiert), builder konstruiert Artefakte (das Was wird gebaut).
- **growth vs. execution**: growth skaliert auf lange Sicht mit Multiplikatoren, execution liefert jetzt mit direkter Handlung.

Operating Principles durchgehend als Verhaltensregeln formuliert ("Handelt auf Basis...", "Verweigert manuellen Aufwand...", "Identifiziert bei jeder Aufgabe...") — keine Wunsch-Formulierungen ("sollte", "könnte", "würde").

## Verification

```
bash scripts/verify-s02.sh → 148 Fehler (Ziel: ≤148 ✓)
  - researcher.md: alle 6 Sektionen ✓
  - execution.md: alle 6 Sektionen ✓
  - builder.md: alle 6 Sektionen ✓
  - growth.md: alle 6 Sektionen ✓
  - automation.md: alle 6 Sektionen ✓

grep -c "^## " soul/*.md → alle 5 neuen Dateien geben 6 zurück ✓
grep -c "sollte|könnte|würde" soul/execution.md → 0 ✓
grep "Geeignet für" soul/builder.md → enthält LaForge und Scotty ✓
```

## Diagnostics

`bash scripts/verify-s02.sh` — zeigt strukturierten Check-Report. Fortschritt: 198→183→148→(T03+T04+T05 folgen). Exit-Code = Fehleranzahl.

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `soul/researcher.md` — 6 Sektionen, Wissenssuche als Weltbild, Spock als primärer Agent
- `soul/execution.md` — 6 Sektionen, Ergebnis über Prozess, Kirk + McCoy als primäre Agenten
- `soul/builder.md` — 6 Sektionen, Engineering-Mindset, LaForge (primär) + Scotty (sekundär)
- `soul/growth.md` — 6 Sektionen, Expansion und Skalierung, Riker als primärer Agent
- `soul/automation.md` — 6 Sektionen, Systeme > Einzellösungen, Scotty + Borg als primäre Agenten
