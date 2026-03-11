---
id: S02
parent: M001
milestone: M001
provides:
  - soul/strategist.md — 6 Sektionen, taktisches Planen, strategische Weitsicht
  - soul/researcher.md — 6 Sektionen, Weltbild "Was ist wahr?", Spock als primärer Agent
  - soul/execution.md — 6 Sektionen, Weltbild "Ergebnis vor Prozess", Kirk + McCoy
  - soul/builder.md — 6 Sektionen, Engineering-Mindset, LaForge als primärer Agent
  - soul/growth.md — 6 Sektionen, Weltbild "Expansion als Grundhaltung", Riker
  - soul/automation.md — 6 Sektionen, Weltbild "Systeme > Einzellösungen", Scotty + Borg
  - soul/operator.md — 6 Sektionen, Weltbild "Erhält laufende Systeme", Sulu + Uhura
  - soul/analyst.md — 6 Sektionen, Weltbild "Was bedeutet das?", Seven + Troi
  - soul/creator.md — 6 Sektionen, Weltbild "Erschafft Neues", Data + Q
  - soul/minimalist.md — 6 Sektionen, Lens-Soul ohne primären Agenten
  - identity/spock.md — 7 Sektionen, researcher-Soul-Kohärenz, vulkanische Logik
  - identity/kirk.md — 7 Sektionen, execution-Soul-Kohärenz, Entscheidung unter Unsicherheit
  - identity/picard.md — 7 Sektionen, strategist-Soul-Kohärenz, "Make it so"
  - identity/riker.md — 7 Sektionen, growth-Soul-Kohärenz, Expansionsdenken
  - identity/worf.md — 7 Sektionen, strategist-Soul-Kohärenz, Ehre als Handlungsprinzip
  - identity/data.md — 7 Sektionen, creator-Soul-Kohärenz, Erschaffen ohne Ego
  - identity/scotty.md — 7 Sektionen, automation-Soul-Kohärenz, Systemcharakter
  - identity/laforge.md — 7 Sektionen, builder-Soul-Kohärenz, Ingenieursoptimismus
  - identity/mccoy.md — 7 Sektionen, execution-Soul-Kohärenz, "He's dead, Jim"
  - identity/seven.md — 7 Sektionen, analyst-Soul-Kohärenz, post-Borg-Perspektive
  - identity/sulu.md — 7 Sektionen, operator-Soul-Kohärenz, souveräne Ruhe
  - identity/tuvok.md — 7 Sektionen, strategist-Soul-Kohärenz, vulkanische Taktik
  - identity/q.md — 7 Sektionen, creator-Soul-Kohärenz, 5+ echte Schwächen aus Omnipotenz
  - identity/borg.md — 7 Sektionen, automation-Soul-Kohärenz, Singular-Sprecher/Kollektiv-Weltbild
  - identity/troi.md — 7 Sektionen, analyst-Soul-Kohärenz, empathisch-analytisch
  - identity/uhura.md — 7 Sektionen, operator-Soul-Kohärenz, Kommunikation als Weltbild
  - scripts/verify-s02.sh — 198-Check Verifikations-Skript, Exit-Code 0
requires:
  - slice: S01
    provides: templates/soul-template.md (6-Sektionen-Format + strategist-Beispiel), templates/identity-template.md (7-Sektionen-Format + spock-Beispiel)
affects:
  - S03
key_files:
  - soul/strategist.md
  - soul/researcher.md
  - soul/execution.md
  - soul/builder.md
  - soul/growth.md
  - soul/automation.md
  - soul/operator.md
  - soul/analyst.md
  - soul/creator.md
  - soul/minimalist.md
  - identity/spock.md
  - identity/kirk.md
  - identity/picard.md
  - identity/riker.md
  - identity/worf.md
  - identity/data.md
  - identity/scotty.md
  - identity/laforge.md
  - identity/mccoy.md
  - identity/seven.md
  - identity/sulu.md
  - identity/tuvok.md
  - identity/q.md
  - identity/borg.md
  - identity/troi.md
  - identity/uhura.md
  - scripts/verify-s02.sh
key_decisions:
  - D016 — Soul-Abgrenzungs-Pflicht für researcher vs. analyst, builder vs. creator
  - D017 — Borg als Singular-Sprecher mit Kollektiv-Weltbild
  - D018 — minimalist als Lens-Soul ohne primären Agenten
patterns_established:
  - Template-Extraktion via tail + perl + sed + cat -s Pipeline (Heredoc für Windows-Pfad-Workaround)
  - Soul-Philosophien enthalten explizite Abgrenzungsformulierungen bei ähnlichen Souls
  - Operating Principles als feste Verhaltensregeln — keine Wunsch-Formulierungen
  - Schwächen in Identities entstehen immer als Kehrseite einer Stärke — keine Pseudo-Schwächen
  - Soul-Kohärenz durch Charakter-Fokus statt Aufgabenbeschreibung (Identity = WER, nicht WAS)
  - Zitate in Star Trek Referenz sind diagnostisch und erklären die Persönlichkeitslogik
observability_surfaces:
  - bash scripts/verify-s02.sh — 198 Checks (26 Datei-Existenz + 60 Soul-Sektionen + 112 Identity-Sektionen), strukturierter Report mit Haken/Kreuz pro Datei/Sektion, Exit-Code = Fehleranzahl
drill_down_paths:
  - .gsd/milestones/M001/slices/S02/tasks/T01-SUMMARY.md
  - .gsd/milestones/M001/slices/S02/tasks/T02-SUMMARY.md
  - .gsd/milestones/M001/slices/S02/tasks/T03-SUMMARY.md
  - .gsd/milestones/M001/slices/S02/tasks/T04-SUMMARY.md
  - .gsd/milestones/M001/slices/S02/tasks/T05-SUMMARY.md
duration: ~3h (5 Tasks)
verification_result: passed
completed_at: 2026-03-11
---

# S02: Souls und Identities

**10 Soul-Archetypes und 16 Star Trek Identity-Dateien vollständig geschrieben — verify-s02.sh Exit-Code 0, alle 198 Checks grün.**

## What Happened

S02 baute in 5 Tasks die philosophische und persönliche Grundlage für alle 16 Agenten auf.

**T01** etablierte die Stopping-Condition: `scripts/verify-s02.sh` mit 198 Checks in 3 Gruppen (Datei-Existenz, Soul-Sektionen, Identity-Sektionen). Exit-Code = Fehleranzahl nach D014. `soul/strategist.md` und `identity/spock.md` wurden direkt aus den S01-Templates extrahiert — Pipeline: `tail` → `perl -0777 -pe` (multi-line HTML-Kommentar-Entfernung) → `sed` → `cat -s`. Ausgangszustand: 183 Fehler. Technischer Workaround dokumentiert: Write-Tool schreibt auf diesem Windows-System in falschen Pfad (`C:\c\Dev\...`), daher Bash-Heredocs und Pipelines durchgehend verwendet.

**T02** schrieb die 5 klar abgrenzbaren Archetypes (researcher, execution, builder, growth, automation). Die kritische Herausforderung war konzeptuelle Abgrenzung: execution vs. strategist (handelt sofort vs. plant zuerst), builder vs. creator (konstruiert Bekanntes vs. erschafft Neues), automation vs. builder (macht Prozesse wiederholbar vs. konstruiert Artefakte), growth vs. execution (skaliert langfristig vs. liefert jetzt). Jede Abgrenzung ist explizit in der Philosophie-Sektion benannt. Fehleranzahl: 183 → 148.

**T03** schrieb die 4 nuanciertesten Archetypes (operator, analyst, creator, minimalist). Kernleistungen: analyst erhält die charakteristische Abgrenzungsformel "Was bedeutet das?" vs. researcher "Was ist wahr?"; creator trennt sich von builder durch "neue Entitäten erschaffen" vs. "mit bekannten Materialien konstruieren"; minimalist wird als Lens-Soul ohne primären Agenten implementiert, mit konkreten messbaren Success Metrics. Alle 60 Soul-Sektions-Checks grün. Fehleranzahl: 148 → 120.

**T04** schrieb die 8 klassischen Identities (kirk, picard, riker, worf, data, scotty, laforge, mccoy). Kernprinzip: Soul-Kohärenz durch Charakter-Fokus — Kirk (execution) zeigt "entscheidet ohne alle Fakten" als Persönlichkeit, nicht als Stellenbeschreibung. Schwächen entstehen als Kehrseite der Stärken: Kirks Impulsivität ist die Kehrseite seiner Entscheidungsstärke, Worfs Inflexibilität die seiner Prinzipientreue. D012 (kein operativer Inhalt in Identities) konsequent eingehalten. Fehleranzahl: 120 → 56.

**T05** schrieb die 7 verbleibenden Identities (seven, sulu, tuvok, q, borg, troi, uhura) inklusive der Sonderfälle. Q erhielt 5+ echte Schwächen aus der Omnipotenz selbst (Langeweile-Anfälligkeit, struktureller Empathiemangel, Unzuverlässigkeit, Blindheit für Konsequenzen zweiter Ordnung, Selbstbezogenheit). Borg wurde nach D017 als Singular-Sprecher mit Kollektiv-Weltbild implementiert. Ein False-Positive beim operativen-Inhalt-Check (Tuvok: "analysiert" in Charakter-Beschreibung — nicht operational gemeint aber literal gematcht) wurde durch Umformulierung behoben. Finaler Lauf: Exit-Code 0.

## Verification

```bash
bash scripts/verify-s02.sh
# Exit-Code 0 — alle 198 Checks grün
# [1/3] 26/26 Datei-Existenz-Checks
# [2/3] 60/60 Soul-Sektions-Checks
# [3/3] 112/112 Identity-Sektions-Checks

grep -c "^## Geeignet für" soul/*.md
# Alle 10 Soul-Dateien: je 1

grep -rn "analysiert|bearbeitet|nutzt den Skill|führt aus" identity/
# 0 Treffer (kein operativer Inhalt in Identities)

ls soul/ | grep -v ".gitkeep" | wc -l    # 10
ls identity/ | grep -v ".gitkeep" | wc -l   # 16
```

## Requirements Advanced

- R005 (Star Trek Agenten-Namen) — alle 16 Identity-Dateien mit exakten Star Trek Namen und authentischen Charakter-Profilen geschrieben; Soul-Kohärenz belegt die Persönlichkeits-zu-Funktion-Zuordnung
- R008 (10 Souls) — alle 10 Souls vollständig ausgearbeitet mit 6 Sektionen inkl. Purpose, Core Values, Operating Principles, Success Metrics und Agent-Mapping

## Requirements Validated

- R005 (Star Trek Agenten-Namen) — alle 16 identity/*.md existieren mit exakten Character-Namen aus der R005-Liste; verify-s02.sh 26/26 Existenz-Checks und 112/112 Identity-Sektions-Checks beweisen Vollständigkeit
- R008 (10 Souls) — alle 10 soul/*.md existieren mit vollständigen 6 Sektionen; verify-s02.sh 60/60 Soul-Sektions-Checks beweisen Format-Konformität; grep -c auf "## Geeignet für" = 10 bestätigt Agent-Mapping

## New Requirements Surfaced

- none

## Requirements Invalidated or Re-scoped

- none

## Deviations

Write-Tool schreibt auf diesem Windows-System in falschen Pfad (C:\c\Dev\... statt C:\Dev\...). Workaround: alle Dateien via bash-Heredocs und Pipelines erstellt. Kein inhaltlicher Impact, dokumentiert in T01-SUMMARY.md.

## Known Limitations

- Soul-zu-Agenten-Mappings in "## Geeignet für" sind verbindliche Vorgaben für S03 — S03 muss diese Referenzen korrekt aufnehmen
- Identities enthalten bewusst keine Skills oder Capabilities — das ist architektonisch korrekt (D012), aber S03 muss die operative Schicht aufbauen

## Follow-ups

- S03 konsumiert alle 26 Dateien: 16 Identity-Dateien als Persönlichkeitsgrundlage, 10 Soul-Dateien als Weltbild-Zuweisung pro Agent

## Files Created/Modified

- `scripts/verify-s02.sh` — 198-Check Stopping-Condition, Exit-Code = Fehleranzahl
- `soul/strategist.md` — aus S01-Template extrahiert, 6 Sektionen
- `soul/researcher.md` — "Was ist wahr?", 6 Sektionen, Spock als primärer Agent
- `soul/execution.md` — "Ergebnis vor Prozess", 6 Sektionen, Kirk + McCoy
- `soul/builder.md` — Engineering-Mindset, 6 Sektionen, LaForge primär
- `soul/growth.md` — "Expansion als Grundhaltung", 6 Sektionen, Riker
- `soul/automation.md` — "Systeme > Einzellösungen", 6 Sektionen, Scotty + Borg
- `soul/operator.md` — "Erhält laufende Systeme", 6 Sektionen, Sulu + Uhura
- `soul/analyst.md` — "Was bedeutet das?", 6 Sektionen, Seven + Troi
- `soul/creator.md` — "Erschafft Neues", 6 Sektionen, Data + Q
- `soul/minimalist.md` — Lens-Soul, 6 Sektionen, kein primärer Agent
- `identity/spock.md` — aus S01-Template extrahiert, 7 Sektionen
- `identity/kirk.md` — execution-Soul, 7 Sektionen
- `identity/picard.md` — strategist-Soul, 7 Sektionen
- `identity/riker.md` — growth-Soul, 7 Sektionen
- `identity/worf.md` — strategist-Soul, 7 Sektionen
- `identity/data.md` — creator-Soul, 7 Sektionen
- `identity/scotty.md` — automation-Soul, 7 Sektionen
- `identity/laforge.md` — builder-Soul, 7 Sektionen
- `identity/mccoy.md` — execution-Soul, 7 Sektionen
- `identity/seven.md` — analyst-Soul, 7 Sektionen
- `identity/sulu.md` — operator-Soul, 7 Sektionen
- `identity/tuvok.md` — strategist-Soul, 7 Sektionen
- `identity/q.md` — creator-Soul, 7 Sektionen, 5+ echte Schwächen
- `identity/borg.md` — automation-Soul, 7 Sektionen, Singular-Kollektiv
- `identity/troi.md` — analyst-Soul, 7 Sektionen
- `identity/uhura.md` — operator-Soul, 7 Sektionen

## Forward Intelligence

### What the next slice should know
- "## Geeignet für" in den Soul-Dateien ist das verbindliche Agent-Mapping — S03 liest diese Sektionen um Primary-Soul und Secondary-Soul pro Agent zuzuweisen
- Jeder Agent in S03 braucht genau eine Identity-Referenz (identity/name.md) und genau einen Primary-Soul (soul/name.md)
- minimalist ist sekundärer Soul für alle Agenten — S03 kann ihn als optionalen zweiten Soul bei jedem Agenten erwähnen
- Tuvok teilt den strategist-Soul mit Picard und Worf — S03 muss die Agents trotzdem klar durch Capabilities differenzieren (Tuvok = Security/Taktik, Picard = Orchestrierung, Worf = Kampfbereitschaft)
- Q und Borg sind die kreativsten Sonderfälle: Q omnipotent-spielerisch (creator), Borg effizient-assimilierend (automation) — ihre Agent-Definitionen in S03 werden die komplexesten

### What's fragile
- Soul-zu-Agent-Mapping ist nur in "## Geeignet für" dokumentiert — wenn S03 diese Sektionen nicht liest entsteht inkonsistente Zuweisung
- Der literale grep-Check auf operative Sprache in identity/ ist nicht exhaustiv — neue operative Verben die in Charakter-Beschreibungen landen würden unbemerkt bleiben

### Authoritative diagnostics
- `bash scripts/verify-s02.sh` — primäre Inspection Surface; Exit-Code 0 bedeutet alle 26 Dateien existieren mit vollständigen Sektionen
- `grep "## Geeignet für" soul/*.md -A 10` — zeigt Agent-Mapping pro Soul schnell ohne alle Dateien zu lesen

### What assumptions changed
- Ursprüngliche Planung sah 183 initiale Fehler vor (nach T01) — tatsächlich waren es auch 183: korrekte Baseline
- Write-Tool-Bug war bekannt aus T01 — konsequent via Heredocs umgangen in allen Tasks
