---
id: T01
parent: S02
milestone: M001
provides:
  - scripts/verify-s02.sh — 198-Check Stopping-Condition für S02 (TDD-Äquivalent)
  - soul/strategist.md — vollständig ausgearbeiteter strategist-Soul (6 Sektionen)
  - identity/spock.md — vollständig ausgearbeitetes spock-Identity (7 Sektionen)
key_files:
  - scripts/verify-s02.sh
  - soul/strategist.md
  - identity/spock.md
key_decisions:
  - Heredoc statt Write-Tool für Skript-Erstellung (Write-Tool schreibt in Windows-Pfad C:\c\Dev\... statt C:\Dev\...)
  - perl -0777 -pe für multi-line HTML-Kommentar-Entfernung aus Templates
  - cat -s zur Normalisierung mehrfacher Leerzeilen
patterns_established:
  - Template-Extraktion via tail + perl + sed + cat -s Pipeline
  - Exit-Code = Fehleranzahl (D014-konform), max 255 nicht erreicht bei S02
observability_surfaces:
  - bash scripts/verify-s02.sh — strukturierter Check-Report [1/3]/[2/3]/[3/3] mit ✓/✗ pro Datei/Sektion; Exit-Code = Fehleranzahl
duration: ~15m
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T01: verify-s02.sh erstellen + strategist.md + spock.md aus Templates extrahieren

**198-Check Verifikations-Skript erstellt und Ausgangszustand mit 183 Fehlern dokumentiert; strategist.md (6 Sektionen) und spock.md (7 Sektionen) aus Template-Beispielen extrahiert.**

## What Happened

`scripts/verify-s02.sh` nach dem Muster von verify-s01.sh geschrieben — 3 Check-Gruppen mit `[1/3]`, `[2/3]`, `[3/3]`-Headern: Datei-Existenz (26 Dateien), Soul-Sektionen (10×6=60 Checks), Identity-Sektionen (16×7=112 Checks). Exit-Code = Fehleranzahl (D014-konform).

Technischer Hinweis: Das Write-Tool schreibt in einen falschen Windows-Pfad (`C:\c\Dev\...`). Alle Dateien wurden daher mit bash-Heredocs (Skript) und perl-Pipelines (Markdown) erstellt — diese schreiben korrekt nach `/c/Dev/Openclaw_Meta_Maker/`.

`soul/strategist.md` und `identity/spock.md` wurden aus den Template-Dateien unterhalb der `---`-Trennlinie extrahiert. Pipeline: `tail -n +<line>` → `perl -0777 -pe 's/<!--.*?-->//gs'` (multi-line HTML-Kommentar-Entfernung) → `sed '/./,$!d'` (führende Leerzeilen entfernen) → `cat -s` (mehrfache Leerzeilen normalisieren).

Initialer Lauf (alle 26 Dateien fehlend): 198 Fehler. Nach Extraktion der 2 Dateien: 183 Fehler (198 − 15 korrekte Checks: 1+6 für strategist, 1+7 für spock).

## Verification

```
grep -c "^## " soul/strategist.md   → 6 ✓
grep -c "^## " identity/spock.md   → 7 ✓
grep -c "<!-- " soul/strategist.md  → 0 ✓
grep -c "<!-- " identity/spock.md   → 0 ✓
bash scripts/verify-s02.sh → Exit-Code 183 ✓ (erwarteter Ausgangszustand)
```

## Diagnostics

`bash scripts/verify-s02.sh` gibt strukturierten Check-Report aus. Fehlende Dateien werden in allen 3 Gruppen gemeldet (Existenz + alle Sektions-Checks). Exit-Code direkt als Fortschrittsindikator nutzbar: 198→183→127→91→35→0.

## Deviations

Write-Tool-Bug: Schreibt nach `C:\c\Dev\...` statt `C:\Dev\...` auf diesem Windows-System. Workaround: bash-Heredoc für Skript, bash-Pipeline für Markdown-Extraktion.

## Known Issues

Keine.

## Files Created/Modified

- `scripts/verify-s02.sh` — ausführbares Verifikations-Skript, 198 Checks, Exit-Code = Fehleranzahl
- `soul/strategist.md` — vollständig ausgearbeiteter strategist-Soul, 6 Sektionen, kein Template-Inhalt
- `identity/spock.md` — vollständig ausgearbeitetes spock-Identity, 7 Sektionen, kein Template-Inhalt
