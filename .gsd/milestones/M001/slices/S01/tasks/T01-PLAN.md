---
estimated_steps: 3
estimated_files: 12
---

# T01: Ordnerstruktur anlegen und Verifikations-Skript schreiben

**Slice:** S01 — Foundation — Templates, Format und Ordnerstruktur
**Milestone:** M001

## Description

Legt die vollständige Ordnerstruktur des Ökosystems an (R007) und schreibt das Verifikations-Skript `scripts/verify-s01.sh`, das als objektive Stopping-Condition für den gesamten Slice dient. Nach diesem Task schlägt das Skript erwartungsgemäß fehl — Templates und Skills fehlen noch. Alle nachfolgenden Tasks (T02–T04) machen es schrittweise grüner bis der finale Exit-Code 0 ist.

## Steps

1. Alle 11 Verzeichnisse mit `.gitkeep` anlegen: `soul/`, `identity/`, `agent/`, `skills/growth/`, `skills/content/`, `skills/research/`, `skills/strategy/`, `skills/automation/`, `skills/meta/`, `commands/`, `templates/`
2. `scripts/` Verzeichnis anlegen und `scripts/verify-s01.sh` schreiben — das Skript prüft: (a) Alle 11 Dirs existieren, (b) 4 Template-Dateien existieren, (c) `skill-template.md` hat alle 9 Sektions-Header, (d) 6 Beispiel-Skill-Dateien existieren in den richtigen Unterordnern, (e) jeder Skill hat alle 9 Sektions-Header, (f) jeder Skill enthält `/elvis-*` in `## Name`, (g) `skills/meta/elvis-skill-generator.md` enthält Safeguard-Keywords (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback)
3. Skript ausführbar machen (`chmod +x scripts/verify-s01.sh`) und einmalig ausführen um den erwarteten Fehlzustand zu bestätigen

## Must-Haves

- [ ] Alle 11 Verzeichnisse existieren (exakt die Struktur aus M001-CONTEXT.md — kein `skills/analysis/`)
- [ ] `scripts/verify-s01.sh` ist ausführbar und gibt strukturierten ✓/✗ Report aus
- [ ] Skript schlägt beim ersten Ausführen fehl (Fehler > 0) — das ist das erwartete Verhalten
- [ ] Jede Prüfung im Skript gibt eine eigene ✓/✗ Zeile aus sodass genau erkennbar ist was fehlt

## Verification

- `bash scripts/verify-s01.sh` ausführen — Output enthält Fehler wegen fehlender Templates/Skills
- `ls soul/ identity/ agent/ skills/ commands/ templates/` — alle Verzeichnisse existieren
- `ls skills/` zeigt genau: `growth/ content/ research/ strategy/ automation/ meta/` (kein `analysis/`)

## Observability Impact

- Signals added/changed: `scripts/verify-s01.sh` ist die einzige Inspection Surface für den gesamten S01 — jeder Task kann damit seinen eigenen Fortschritt prüfen
- How a future agent inspects this: `bash scripts/verify-s01.sh` — liest alle Checks sequenziell, gibt strukturierten Report, endet mit Fehleranzahl
- Failure state exposed: Fehlerzähler + explizite ✗-Zeilen zeigen genau welche Datei oder Sektion fehlt; Exit-Code 1 bei Fehlern

## Inputs

- `M001-CONTEXT.md` — bindende Ordnerstruktur (6 Skill-Unterordner, keine `analysis/`)
- `DECISIONS.md` D003 — Ordnerstruktur-Entscheidung: integrierte Struktur, keine separaten Pakete

## Expected Output

- `soul/.gitkeep`, `identity/.gitkeep`, `agent/.gitkeep` — leere Marker-Dateien
- `skills/growth/.gitkeep`, `skills/content/.gitkeep`, `skills/research/.gitkeep`, `skills/strategy/.gitkeep`, `skills/automation/.gitkeep`, `skills/meta/.gitkeep`
- `commands/.gitkeep`, `templates/.gitkeep`
- `scripts/verify-s01.sh` — ausführbares Verifikations-Skript, schlägt initial fehl
