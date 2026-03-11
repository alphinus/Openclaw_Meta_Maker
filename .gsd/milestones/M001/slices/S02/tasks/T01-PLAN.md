---
estimated_steps: 5
estimated_files: 3
---

# T01: verify-s02.sh erstellen + strategist.md + spock.md aus Templates extrahieren

**Slice:** S02 — Souls und Identities
**Milestone:** M001

## Description

Die Stopping-Condition für S02 definieren bevor Inhalt erstellt wird: `scripts/verify-s02.sh` mit 198 Checks (26 Datei-Existenz + 60 Soul-Sektionen + 112 Identity-Sektionen). Danach die zwei Dateien extrahieren, die bereits fertig in den Templates ausgearbeitet sind: `soul/strategist.md` und `identity/spock.md`. Der initiale Skript-Lauf soll fast alle Checks fehlschlagen — das ist korrekt und dokumentiert den Ausgangszustand.

## Steps

1. `scripts/verify-s02.sh` schreiben — 3 Check-Gruppen mit `[1/3]`, `[2/3]`, `[3/3]`-Header:
   - `[1/3] Datei-Existenz (26 Dateien)`: Alle 10 soul/*.md und 16 identity/*.md mit exakten Dateinamen auf Existenz prüfen. Fehlerzähler erhöhen wenn fehlt.
   - `[2/3] Soul-Sektionen (10 × 6 = 60 Checks)`: Für jede der 10 soul/*.md prüfen ob `## Name`, `## Philosophie`, `## Core Values`, `## Operating Principles`, `## Success Metrics`, `## Geeignet für` vorhanden sind (via `grep`).
   - `[3/3] Identity-Sektionen (16 × 7 = 112 Checks)`: Für jede der 16 identity/*.md prüfen ob `## Name`, `## Charakter-Beschreibung`, `## Persönlichkeitsmerkmale`, `## Kommunikationsstil`, `## Stärken`, `## Schwächen`, `## Star Trek Referenz` vorhanden sind.
   - Exit-Code = Fehleranzahl (D014-konform). Skript ausführbar machen: `chmod +x scripts/verify-s02.sh`
2. Initialen Lauf ausführen: `bash scripts/verify-s02.sh` — dokumentiert den Ausgangszustand (erwartet ~196 Fehler da alle 26 Dateien fehlen)
3. `soul/strategist.md` erstellen: Inhalt aus `templates/soul-template.md` unterhalb der Trennlinie (`---`) extrahieren. Alle HTML-Kommentare (`<!-- ... -->`) entfernen. Nur den reinen Soul-Inhalt behalten (beginnt mit `# Soul`). Prüfen: `grep -c "^## " soul/strategist.md` muss 6 zurückgeben.
4. `identity/spock.md` erstellen: Inhalt aus `templates/identity-template.md` unterhalb der Trennlinie extrahieren. Alle HTML-Kommentare entfernen. Nur den reinen Identity-Inhalt behalten. Prüfen: `grep -c "^## " identity/spock.md` muss 7 zurückgeben.
5. `bash scripts/verify-s02.sh` erneut ausführen — Fehleranzahl muss auf ≤183 gesunken sein (strategist: 1 Existenz + 6 Sektionen = 7 korrekte Checks; spock: 1 Existenz + 7 Sektionen = 8 korrekte Checks → 198 - 15 = 183 verbleibend)

## Must-Haves

- [ ] `scripts/verify-s02.sh` ist ausführbar und prüft exakt 198 Checks (26 Existenz + 60 Soul + 112 Identity)
- [ ] Exit-Code des Skripts = Fehleranzahl (0 = alles grün, N = N Fehler)
- [ ] `soul/strategist.md` enthält exakt 6 `##`-Sektionen, kein Template-Kommentar-Inhalt
- [ ] `identity/spock.md` enthält exakt 7 `##`-Sektionen, kein Template-Kommentar-Inhalt
- [ ] Skript-Sektionen mit `[1/3]`, `[2/3]`, `[3/3]`-Header für schnelle Navigation im Output

## Verification

- `bash scripts/verify-s02.sh` läuft ohne Bash-Fehler (korrekte Syntax)
- `echo $?` nach dem Lauf gibt eine Zahl zurück (kein Bash-Absturz)
- `grep -c "^## " soul/strategist.md` = 6
- `grep -c "^## " identity/spock.md` = 7
- `grep -c "<!-- " soul/strategist.md` = 0 (keine Template-Kommentare in der Ausgabe)
- `grep -c "<!-- " identity/spock.md` = 0

## Observability Impact

- Signals added/changed: `bash scripts/verify-s02.sh` — strukturierter Check-Report mit ✓/✗ pro Datei/Sektion; Exit-Code = Fehleranzahl
- How a future agent inspects this: `bash scripts/verify-s02.sh` gibt Checkpoint-Status für S02 aus; Exit-Code 0 = vollständig grün
- Failure state exposed: Jede fehlende Datei oder fehlende Sektion wird mit Dateiname und Sektion einzeln gemeldet

## Inputs

- `templates/soul-template.md` — vollständiges strategist-Beispiel unterhalb der Trennlinie wird extrahiert
- `templates/identity-template.md` — vollständiges spock-Beispiel unterhalb der Trennlinie wird extrahiert
- `scripts/verify-s01.sh` — Referenz-Muster für Skript-Struktur und Exit-Code-Konvention (D014)
- S02-RESEARCH.md — Dateiliste mit exakten Namen aller 26 Dateien

## Expected Output

- `scripts/verify-s02.sh` — ausführbares Verifikations-Skript, 198 Checks, Fehlerzähler als Exit-Code
- `soul/strategist.md` — vollständig ausgearbeiteter strategist-Soul (aus Template-Beispiel extrahiert), 6 Sektionen
- `identity/spock.md` — vollständig ausgearbeitetes spock-Identity (aus Template-Beispiel extrahiert), 7 Sektionen
