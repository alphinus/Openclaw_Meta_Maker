---
estimated_steps: 4
estimated_files: 1
---

# T01: verify-s04.sh schreiben + Initial-Lauf

**Slice:** S04 — Growth + Content Skills (~30 Skills)
**Milestone:** M001

## Description

Objektive Stopping-Condition für S04 schreiben, bevor ein einziger Skill erstellt wird. Das Verifikations-Skript definiert den Vertrag: 28 neue Skill-Dateien (14 Growth + 14 Content), je 9 Pflichtsektion-Header, `/elvis-`-Prefix, keine Phantomreferenzen. Fehlerzähler als Exit-Code (D014). Der Initial-Lauf erwartungsgemäß mit ~284 Fehlern — das ist der Baseline-Beweis dass das Skript läuft und alle Checks registriert.

## Steps

1. Skript `scripts/verify-s04.sh` erstellen mit Shebang, `set -euo pipefail`, `ERRORS=0`-Zähler, `pass()`/`fail()`-Hilfsfunktionen und strukturiertem Output-Format analog zu `scripts/verify-s01.sh`.
2. **Check-Gruppe [1/4] — Datei-Existenz:** Array aller 28 neuen Skill-Dateipfade definieren (14 Growth + 14 Content exklusive elvis-growth-audit.md und elvis-x-hook-writer.md die aus S01 stammen); Schleife prüft Existenz jeder Datei.
3. **Check-Gruppe [2/4] — Sektions-Vollständigkeit:** Für jede der 28 Dateien alle 9 Pflichtsektion-Header prüfen: `## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`. Gesamtzahl: 252 Checks.
4. **Check-Gruppe [3/4] — /elvis-Prefix:** Für jede der 28 Dateien prüfen ob `/elvis-` im `## Name`-Block vorkommt (grep-basiert). 28 Checks.
5. **Check-Gruppe [4/4] — Phantomreferenz-Check:** Alle in `## Abhängigkeiten` genannten Skill-Dateinamen extrahieren (Pattern: `elvis-[a-z-]+`) und prüfen ob die referenzierten Dateien tatsächlich in `skills/` existieren. Fehler wenn ein referenzierter Skill nicht als Datei vorhanden ist.
6. Exit-Code auf `$ERRORS` setzen; Abschluss-Banner mit Gesamtergebnis ausgeben. Initial-Lauf ausführen und erwartete Fehleranzahl (~284) in Output-Kommentar notieren.

## Must-Haves

- [ ] Skript ist ausführbar (`chmod +x` oder `bash`-Aufruf funktioniert)
- [ ] Alle 28 Ziel-Dateipfade im Skript kodiert (keine fehlenden Einträge)
- [ ] 9 Pflichtsektion-Header im Skript explizit aufgelistet (identisch mit S01-Template)
- [ ] Fehlerzähler als Exit-Code (D014-konform)
- [ ] Initial-Lauf produziert strukturierten Output ohne Bash-Syntaxfehler

## Verification

- `bash scripts/verify-s04.sh; echo "Exit: $?"` → Exit-Code > 0 (viele Fehler erwartet), aber kein Bash-Syntaxfehler
- `grep -c "elvis-" scripts/verify-s04.sh` → Wert ≥ 28 (alle 28 Skill-Namen vorhanden)
- `bash scripts/verify-s04.sh 2>&1 | grep "\[1/4\]"` → Check-Gruppe-Header sichtbar

## Observability Impact

- Signals added/changed: Strukturierter ✓/✗-Output pro Datei und Sektion; Exit-Code als maschinenlesbarer Fehlerzähler
- How a future agent inspects this: `bash scripts/verify-s04.sh` — gibt für jede fehlende Datei/Sektion eine ✗-Zeile aus; Exit-Code = exakte Fehleranzahl
- Failure state exposed: Jede einzelne fehlende Sektion in jeder Datei wird explizit benannt

## Inputs

- `scripts/verify-s01.sh` — Referenz-Implementierung für Skript-Struktur und Output-Format
- `templates/skill-template.md` — Quelle der 9 Pflichtsektion-Header-Namen
- S04-RESEARCH.md Abschnitt 5 — autoritative Liste aller 28 neuen Skill-Dateinamen

## Expected Output

- `scripts/verify-s04.sh` — vollständiges Verifikations-Skript mit 4 Check-Gruppen, ausführbar, Initial-Lauf mit ~284 erwarteten Fehlern
