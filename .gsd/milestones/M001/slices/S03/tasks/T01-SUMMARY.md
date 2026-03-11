---
id: T01
parent: S03
milestone: M001
provides:
  - scripts/verify-s03.sh — 148-Check Verifikationsskript für S03
key_files:
  - scripts/verify-s03.sh
key_decisions:
  - none
patterns_established:
  - verify-s03.sh folgt exakt dem Muster von verify-s02.sh (ERRORS-Zähler, pass/fail-Hilfsfunktionen, 3 Gruppen, Zusammenfassung, Exit-Code = ERRORS)
observability_surfaces:
  - bash scripts/verify-s03.sh — strukturierter 148-Check Report mit ✓/✗ pro Datei und Sektion; Exit-Code = Fehleranzahl
duration: ~10m
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T01: Stopping-Condition — scripts/verify-s03.sh schreiben

**`scripts/verify-s03.sh` erstellt — 148 Checks in 3 Gruppen, erster Lauf zeigt Exit-Code 148 (alle fail, beweist korrekte Checks).**

## What Happened

Das Verifikationsskript wurde nach dem Muster von `scripts/verify-s02.sh` erstellt. Zuerst wurden die Referenzdatei `scripts/verify-s02.sh` und `templates/agent-template.md` gelesen, um Struktur und die 7 Pflichtfelder zu verifizieren.

Das Skript enthält:
- Array `AGENT_FILES` mit 16 Dateinamen (kirk, spock, picard, data, worf, scotty, laforge, seven, sulu, tuvok, mccoy, riker, q, borg, troi, uhura)
- Array `AGENT_SECTIONS` mit 7 Pflichtfeldern aus dem Template
- Array `AUTONOMOUS_AGENTS` mit 5 Dateinamen (picard, q, borg, troi, uhura)
- Array `SAFEGUARD_MARKERS` mit 4 fett-formatierten D007-Markern

## Verification

```
bash scripts/verify-s03.sh
# → 148 Fehler, Exit-Code 148 ✓

grep -c "fail " scripts/verify-s03.sh
# → 3 (fail-Funktion vorhanden) ✓

echo $?  # nach bash scripts/verify-s03.sh
# → 148 ✓
```

Alle 3 Must-Have-Verifikationen bestanden:
- Skript läuft ohne Bash-Syntaxfehler durch
- Zeigt exakt 148 Fehler (16 Datei-Existenz + 112 Sektions + 20 Safeguard)
- Exit-Code = 148

## Diagnostics

Inspection surface: `bash scripts/verify-s03.sh`
- Jeder fehlgeschlagene Check zeigt `Dateiname: SektionsName — Datei fehlt / Sektion fehlt`
- Exit-Code = Fehleranzahl — maschinenlesbar für weitere Automatisierung
- Gruppe [1/3] zeigt welche Agent-Dateien fehlen
- Gruppe [2/3] zeigt welche Sektionen fehlen (pro Datei)
- Gruppe [3/3] zeigt welche Safeguard-Marker fehlen (nur autonome Agenten)

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `scripts/verify-s03.sh` — 148-Check Verifikationsskript, lauffähig, Exit-Code = ERRORS (D014)
