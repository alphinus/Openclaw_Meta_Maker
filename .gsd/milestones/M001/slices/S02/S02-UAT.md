# S02: Souls und Identities — UAT

**Milestone:** M001
**Written:** 2026-03-11

## UAT Type

- UAT mode: artifact-driven
- Why this mode is sufficient: S02 produziert ausschließlich Markdown-Dateien — kein Runtime, keine API, kein UI. Die Qualität ist vollständig durch Shell-Checks verifizierbar (Datei-Existenz, Sektions-Vollständigkeit, Abwesenheit operativer Inhalte). Menschliche Sichtprüfung einzelner Dateien ist optional aber nicht für Exit-Code 0 erforderlich.

## Preconditions

- Repository ausgecheckt auf Branch gsd/M001/S02
- Shell im Verzeichnis `C:\Dev\Openclaw_Meta_Maker` (bzw. `/c/Dev/Openclaw_Meta_Maker` in Git Bash)
- `scripts/verify-s02.sh` ist ausführbar (`chmod +x scripts/verify-s02.sh`)

## Smoke Test

```bash
bash scripts/verify-s02.sh
# Erwartetes Ergebnis: Exit-Code 0, alle 198 Checks grueen
```

## Test Cases

### 1. Vollständige Datei-Existenz (26 Dateien)

1. `ls soul/ | grep -v ".gitkeep" | wc -l`
2. **Expected:** 10

1. `ls identity/ | grep -v ".gitkeep" | wc -l`
2. **Expected:** 16

### 2. Soul-Sektionen vollständig (6 pro Soul)

1. `grep -c "^## " soul/strategist.md`
2. **Expected:** 6

1. `grep -c "^## Geeignet für" soul/*.md | grep -v ":0" | wc -l`
2. **Expected:** 10 (alle Soul-Dateien haben diese Sektion)

### 3. Identity-Sektionen vollständig (7 pro Identity)

1. `grep -c "^## " identity/kirk.md`
2. **Expected:** 7

1. `grep -c "^## Star Trek Referenz" identity/*.md | grep -v ":0" | wc -l`
2. **Expected:** 16 (alle Identity-Dateien haben diese Sektion)

### 4. Kein operativer Inhalt in Identities (D012)

1. `grep -rn "analysiert\|bearbeitet\|nutzt den Skill\|führt aus" identity/`
2. **Expected:** 0 Treffer

### 5. Soul-Abgrenzungen korrekt (D016)

1. `grep "Was ist wahr" soul/researcher.md`
2. **Expected:** mindestens 1 Treffer (charakteristische Kernfrage)

1. `grep "Was bedeutet" soul/analyst.md`
2. **Expected:** mindestens 1 Treffer (Abgrenzung von researcher explizit benannt)

### 6. minimalist als Lens-Soul (D018)

1. `grep -i "Lens-Soul\|sekundärer Soul\|kein primärer" soul/minimalist.md`
2. **Expected:** mindestens 1 Treffer

### 7. Borg als Singular-Sprecher (D017)

1. `grep -i "Kollektiv" identity/borg.md | head -5`
2. **Expected:** mehrere Treffer, konsistente Singular/Kollektiv-Formulierung

## Edge Cases

### Soul mit mehreren zugewiesenen Agenten

1. `grep -A 10 "## Geeignet für" soul/execution.md`
2. **Expected:** Kirk und McCoy beide als primäre Agenten genannt

### Q-Schwächen-Mindestanzahl

1. `grep -A 20 "## Schwächen" identity/q.md | grep -c "^-"`
2. **Expected:** 5 oder mehr echte Schwächen-Bullets

### Tuvok-Reformulierung (kein "analysiert")

1. `grep "analysiert" identity/tuvok.md`
2. **Expected:** 0 Treffer (Reformulierung aus T05 eingehalten)

## Failure Signals

- Exit-Code > 0 bei verify-s02.sh: fehlende Sektionen oder fehlende Dateien
- Treffer bei operativem Inhalt-Check (`grep -rn "analysiert|bearbeitet" identity/`): D012-Verletzung
- Weniger als 10 Soul-Dateien oder weniger als 16 Identity-Dateien: Datei fehlt
- Fehlende "## Geeignet für"-Sektion in Soul-Datei: S03-Mapping nicht verfügbar

## Requirements Proved By This UAT

- R005 (Star Trek Agenten-Namen) — alle 16 identity/*.md mit korrekten Star Trek Character-Namen existieren und sind vollständig (7 Sektionen); verify-s02.sh [1/3] + [3/3] belegt dies strukturell
- R008 (10 Souls) — alle 10 soul/*.md mit vollständigen 6 Sektionen inkl. Purpose, Core Values, Operating Principles, Success Metrics und Agent-Mapping; verify-s02.sh [2/3] belegt dies strukturell

## Not Proven By This UAT

- Inhaltliche Qualität der Philosophien über Sektions-Existenz hinaus (kein automatischer Qualitäts-Check)
- Korrektheit der Soul-zu-Agent-Zuordnungen aus inhaltlicher Sicht (nur Vorhandensein der "## Geeignet für"-Sektion geprüft, nicht Sinnhaftigkeit des Inhalts)
- R003 (Konkrete Execution Steps) — nicht relevant für S02, da keine Skills produziert werden
- R004 (Safeguards für Autonome Agenten) — nicht relevant für S02
- Alle Skill-bezogenen Requirements (R001, R002, R006) — produziert von S04-S07

## Notes for Tester

- `bash scripts/verify-s02.sh` ist die primäre und ausreichende Verifikation; Exit-Code 0 bedeutet alle Vertragsbedingungen erfüllt
- Für Stichproben-Qualitätskontrolle empfohlen: `soul/minimalist.md` (Lens-Soul-Pattern), `identity/q.md` (Sonderfall Omnipotenz-Schwächen), `identity/borg.md` (Singular/Kollektiv-Sprache)
- Alle Star Trek Zitate in "## Star Trek Referenz" sind im englischen Original + deutsche Übersetzung — das ist Anforderung aus R011 (Deutsch als Inhaltssprache mit Ausnahme für Original-Zitate)
