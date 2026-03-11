---
id: T01
parent: S01
milestone: M001
provides:
  - Alle 11 Projektverzeichnisse mit .gitkeep
  - scripts/verify-s01.sh — ausführbares Verifikations-Skript für den gesamten S01
key_files:
  - scripts/verify-s01.sh
  - soul/.gitkeep
  - identity/.gitkeep
  - agent/.gitkeep
  - skills/growth/.gitkeep
  - skills/content/.gitkeep
  - skills/research/.gitkeep
  - skills/strategy/.gitkeep
  - skills/automation/.gitkeep
  - skills/meta/.gitkeep
  - commands/.gitkeep
  - templates/.gitkeep
key_decisions:
  - Verifikations-Skript prüft alle 7 Bedingungen sequenziell mit eigenem ✓/✗ pro Check-Item
  - Fehlerzähler als Exit-Code — ermöglicht CI-Integration und maschinelles Auslesen
patterns_established:
  - Jede Skript-Sektion beginnt mit einem nummerierten Header "[N/7] ..." für schnelle Navigation
  - Alle Pfade relativ zum Projekt-Root via BASH_SOURCE — portabel auf allen Systemen
observability_surfaces:
  - bash scripts/verify-s01.sh — strukturierter Check-Report mit ✓/✗ pro Item, Fehlerzähler als Exit-Code
duration: ~10 Minuten
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T01: Ordnerstruktur anlegen und Verifikations-Skript schreiben

**Alle 11 Projektverzeichnisse angelegt und `scripts/verify-s01.sh` geschrieben — schlägt erwartungsgemäß mit 83 Fehlern fehl wegen fehlender Templates und Skills.**

## What Happened

1. **11 Verzeichnisse mit .gitkeep** angelegt: `soul/`, `identity/`, `agent/`, `skills/growth/`, `skills/content/`, `skills/research/`, `skills/strategy/`, `skills/automation/`, `skills/meta/`, `commands/`, `templates/`. Exakt die Struktur aus M001-CONTEXT.md — kein `skills/analysis/`.

2. **`scripts/verify-s01.sh`** geschrieben — 7 Check-Gruppen sequenziell:
   - [1/7] Alle 11 Verzeichnisse existieren
   - [2/7] 4 Template-Dateien existieren
   - [3/7] `skill-template.md` hat alle 9 Sektions-Header
   - [4/7] 6 Beispiel-Skill-Dateien existieren
   - [5/7] Jeder Skill hat alle 9 Sektions-Header
   - [6/7] Jeder Skill enthält `/elvis-*` im `## Name` Block
   - [7/7] `skills/meta/elvis-skill-generator.md` enthält 4 Safeguard-Keywords

3. **Skript ausführbar** gemacht (`chmod +x`) und einmalig ausgeführt — bestätigt erwarteten Fehlzustand.

## Verification

```bash
bash scripts/verify-s01.sh
# Ergebnis: ❌ S01 Verifikation fehlgeschlagen — 83 Fehler gefunden
# Exit code: 83
# Check [1/7] vollständig grün: alle 11 ✓
# Checks [2/7]–[7/7] rot: Templates und Skills fehlen noch (Aufgabe von T02–T04)
```

```bash
ls skills/
# automation  content  growth  meta  research  strategy
# Exakt 6 Unterordner — kein analysis/
```

## Diagnostics

`bash scripts/verify-s01.sh` ist die primäre Inspection Surface für S01. Der strukturierte Output zeigt exakt welche Datei oder Sektion fehlt. Exit-Code = Anzahl Fehler, sodass CI-Systeme und nachfolgende Agenten den Status maschinell auslesen können.

## Deviations

none

## Known Issues

none — 83 Fehler sind der erwartete Anfangszustand; alle fehlenden Inhalte werden in T02–T04 erstellt.

## Files Created/Modified

- `soul/.gitkeep` — Marker für Versionierung
- `identity/.gitkeep` — Marker für Versionierung
- `agent/.gitkeep` — Marker für Versionierung
- `skills/growth/.gitkeep` — Marker für Versionierung
- `skills/content/.gitkeep` — Marker für Versionierung
- `skills/research/.gitkeep` — Marker für Versionierung
- `skills/strategy/.gitkeep` — Marker für Versionierung
- `skills/automation/.gitkeep` — Marker für Versionierung
- `skills/meta/.gitkeep` — Marker für Versionierung
- `commands/.gitkeep` — Marker für Versionierung
- `templates/.gitkeep` — Marker für Versionierung
- `scripts/verify-s01.sh` — Ausführbares Verifikations-Skript, 7 Check-Gruppen, Fehlerzähler als Exit-Code
