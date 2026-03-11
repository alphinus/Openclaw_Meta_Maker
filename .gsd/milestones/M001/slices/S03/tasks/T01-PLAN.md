---
estimated_steps: 4
estimated_files: 1
---

# T01: Stopping-Condition — scripts/verify-s03.sh schreiben

**Slice:** S03 — Agent Layer — 16 Star Trek Agenten
**Milestone:** M001

## Description

Das Verifikationsskript wird vor allen Agent-Dateien erstellt (D015-Prinzip). Es definiert die objektive Stopping-Condition für S03: 148 Checks in 3 Gruppen. Beim ersten Lauf zeigt es 148 Fehler — das ist korrekt und beweist, dass die Checks greifen. Jeder Task in S03 reduziert den Fehlerstand, bis T05 Exit-Code 0 erreicht.

Das Skript folgt exakt dem Muster von `scripts/verify-s02.sh`: ERRORS-Zähler, pass/fail-Hilfsfunktionen, 3 Gruppen mit Überschrift, abschließende Zusammenfassung, Exit-Code = ERRORS (D014).

## Steps

1. Lies `scripts/verify-s02.sh` als Referenz für Struktur, Funktionen und Stil
2. Erstelle `scripts/verify-s03.sh` via Bash-Heredoc mit:
   - Array `AGENT_FILES` mit allen 16 Dateinamen (kirk, spock, picard, data, worf, scotty, laforge, seven, sulu, tuvok, mccoy, riker, q, borg, troi, uhura)
   - Array `AGENT_SECTIONS` mit 7 Pflichtfeldern: `## Name`, `## Mission`, `## Capabilities`, `## Operating Loop`, `## Constraints`, `## Primärer Soul`, `## Primäre Skills`
   - Array `AUTONOMOUS_AGENTS` mit 5 Dateinamen (picard, q, borg, troi, uhura)
   - Array `SAFEGUARD_MARKERS` mit 4 fett-formatierten Markers: `**Max-Limit:**`, `**Approval-Gate:**`, `**Stop-Bedingung:**`, `**Rollback-Hinweis:**`
   - Gruppe [1/3]: 16 Datei-Existenz-Checks (für jede Datei in AGENT_FILES)
   - Gruppe [2/3]: 7×16=112 Sektions-Checks (für jede Datei × jede Sektion)
   - Gruppe [3/3]: 4×5=20 Safeguard-Checks (für jeden autonomen Agenten × jeden Marker)
3. Mache die Datei ausführbar: `chmod +x scripts/verify-s03.sh`
4. Führe das Skript aus: `bash scripts/verify-s03.sh`

## Must-Haves

- [ ] Skript enthält alle 16 Agent-Dateinamen
- [ ] Skript prüft alle 7 Pflichtfelder (`## Name`, `## Mission`, `## Capabilities`, `## Operating Loop`, `## Constraints`, `## Primärer Soul`, `## Primäre Skills`)
- [ ] Skript prüft alle 4 Safeguard-Marker für die 5 autonomen Agenten (Picard, Q, Borg, Troi, Uhura)
- [ ] Exit-Code = ERRORS (D014)
- [ ] Beim ersten Lauf: Exit-Code = 148 (alle fail)

## Verification

- `bash scripts/verify-s03.sh` — läuft ohne Bash-Syntaxfehler, zeigt 148 Fehler, Exit-Code = 148
- `echo $?` nach dem Lauf — gibt 148 aus
- `grep -c "fail " scripts/verify-s03.sh` — zeigt > 0 (fail-Funktion vorhanden)

## Observability Impact

- Signals added/changed: verify-s03.sh als primäre Inspection Surface für S03 — strukturierter Check-Report mit Haken/Kreuz
- How a future agent inspects this: `bash scripts/verify-s03.sh` — Exit-Code + Report zeigen exakt welche Dateien/Sektionen fehlen
- Failure state exposed: Jeder fehlende Agent oder jede fehlende Sektion wird mit Dateiname + Sektionsname benannt

## Inputs

- `scripts/verify-s02.sh` — Referenz für Skript-Struktur, ERRORS-Muster, pass/fail-Funktionen
- `templates/agent-template.md` — autoritative Liste der 7 Pflichtfelder

## Expected Output

- `scripts/verify-s03.sh` — lauffähiges 148-Check-Verifikationsskript, Exit-Code = 148 beim Erstlauf
