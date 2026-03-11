# S01: Foundation — Templates, Format und Ordnerstruktur — UAT

**Milestone:** M001
**Written:** 2026-03-11

## UAT Type

- UAT mode: artifact-driven
- Why this mode is sufficient: S01 produziert ausschließlich Markdown-Dateien und ein Bash-Skript — kein Runtime-System, keine Web-Oberfläche, keine Datenbank. Die Qualität ist vollständig durch Datei-Existenz, Sektions-Vollständigkeit und Format-Korrektheit prüfbar. Das Verifikations-Skript ist die primäre Inspection Surface.

## Preconditions

- Projekt-Root: `C:\Dev\Openclaw_Meta_Maker`
- Bash verfügbar (Git Bash auf Windows oder WSL)
- Alle 4 Tasks (T01–T04) abgeschlossen

## Smoke Test

```bash
bash scripts/verify-s01.sh
# Erwartetes Ergebnis: ✅ S01 Verifikation bestanden — alle Checks grün
# Exit-Code: 0
```

## Test Cases

### 1. Verzeichnisstruktur vollständig

1. Führe `ls -la soul/ identity/ agent/ skills/` aus
2. Führe `ls -la skills/growth/ skills/content/ skills/research/ skills/strategy/ skills/automation/ skills/meta/` aus
3. Führe `ls -la commands/ templates/` aus
4. **Expected:** Alle 11 Verzeichnisse existieren mit mindestens einer Datei (.gitkeep oder Skill-Datei)

### 2. Alle 4 Template-Dateien vorhanden und vollständig

1. Führe `ls templates/` aus
2. Führe `grep "^## " templates/skill-template.md | wc -l` aus
3. Führe `grep "^## " templates/soul-template.md | wc -l` aus
4. Führe `grep "^## " templates/identity-template.md | wc -l` aus
5. Führe `grep "^## " templates/agent-template.md | wc -l` aus
6. **Expected:** 4 Template-Dateien vorhanden; skill-template.md ≥18 Sektions-Header (9 Template + 9 Beispiel); soul-template.md ≥12; identity-template.md ≥14; agent-template.md ≥14

### 3. skill-template.md enthält alle 9 Pflicht-Sektionen

1. Führe `grep "^## " templates/skill-template.md` aus
2. **Expected:** ## Name, ## Beschreibung, ## Ziele, ## Strategie, ## Einschränkungen, ## Ausführungsschritte, ## Verifikation, ## Abhängigkeiten, ## Output — alle 9 vorhanden (je mindestens einmal)

### 4. Alle 6 Benchmark-Skills vollständig

1. Führe `bash scripts/verify-s01.sh` aus und prüfe Check [4/7] und [5/7]
2. **Expected:** 6 Skills vorhanden (✓); 54/54 Sektions-Checks grün (✓)

### 5. /elvis-* Prefix in allen Skills

1. Führe `grep -h "^/elvis-" skills/**/*.md` aus (oder bash scripts/verify-s01.sh Check [6/7])
2. **Expected:** Jeder der 6 Skills enthält `/elvis-` im `## Name` Block

### 6. Meta-Skill enthält alle 4 Safeguards

1. Führe `grep -E "Max-Limit|Approval-Gate|Stop-Bedingung|Rollback" skills/meta/elvis-skill-generator.md` aus
2. **Expected:** ≥4 Treffer (je ein Treffer pro Safeguard-Keyword)

### 7. D006-Konformität prüfen (manuell)

1. Öffne `skills/growth/elvis-growth-audit.md`
2. Prüfe `## Ausführungsschritte` auf konkrete Mengen (Zahlen), Zeitangaben und Formate
3. Öffne `skills/meta/elvis-skill-generator.md`
4. Prüfe `## Einschränkungen` auf fettgedruckte Safeguard-Definitionen
5. **Expected:** Jeder Ausführungsschritt enthält mindestens eine konkrete Zahl oder Zeitangabe; alle 4 Safeguards sind fettgedruckt mit Doppelpunkt-Trennung

## Edge Cases

### Skript-Ausführbarkeit auf Windows

1. Führe `bash scripts/verify-s01.sh` in Git Bash oder WSL aus (nicht PowerShell)
2. **Expected:** Skript läuft durch; kein "permission denied"

### Deutsch-Only-Inhalte

1. Öffne eine beliebige Skill-Datei (z.B. `skills/growth/elvis-growth-audit.md`)
2. Prüfe ob Sektions-Inhalte auf Deutsch sind (nicht Englisch)
3. **Expected:** Alle Prose-Inhalte auf Deutsch; Dateinamen und Header-Schlüsselwörter (## Name etc.) bleiben englisch-ähnlich

## Failure Signals

- `bash scripts/verify-s01.sh` gibt Exit-Code > 0 zurück — fehlende Dateien oder Sektionen
- ✗ Zeilen im Skript-Output zeigen welche Datei oder Sektion fehlt
- `grep "^## " templates/skill-template.md` zeigt weniger als 9 eindeutige Sektions-Header
- `grep -E "Max-Limit|Approval-Gate|Stop-Bedingung|Rollback" skills/meta/elvis-skill-generator.md` gibt weniger als 4 Treffer zurück
- Skill-Datei in der falschen Kategorie (z.B. growth-Skill in content/)

## Requirements Proved By This UAT

- R002 — Erweitertes Skill-Format (9 Sektionen incl. Constraints, Verification, Dependencies) ist in templates/skill-template.md und allen 6 Benchmark-Skills implementiert und durch verify-s01.sh maschinell verifiziert
- R003 — Konkrete Execution Steps demonstriert in allen 6 Benchmark-Skills (spezifische Mengen, Zeitangaben, Formate) — Qualitäts-Benchmark für S04–S07
- R004 — Safeguard-Pattern für autonome Agenten: elvis-skill-generator.md enthält alle 4 Typen (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback) — nachweisbar per grep
- R006 — /elvis-* Naming Convention: alle 6 Skills haben Prefix im ## Name Block (verifiziert durch Skript)
- R007 — Ordnerstruktur: alle 11 Verzeichnisse gemäß CONTEXT.md (verifiziert durch Skript)
- R010 — 4 wiederverwendbare Templates mit Anweisungs-Block und vollständigem Beispiel
- R011 — Alle Markdown-Inhalte auf Deutsch

## Not Proven By This UAT

- R001 — ~100 vollständige Skills: nur 6 Benchmark-Skills existieren; volle Umsetzung in S04–S06
- R003 (vollständig) — D006-Konformität aller ~100 Skills: nur 6 Benchmark-Skills als Qualitäts-Benchmark; der Rest folgt in S04–S07
- R004 (vollständig) — Safeguards aller autonomen Agenten (Borg, Q, Picard, Troi, Uhura): nur Skill-Generator demonstriert das Muster; vollständige Implementierung in S07
- R005 — Star Trek Agenten-Namen: keine Agent-Dateien in S01 — wird in S02/S03 bewiesen
- R008 — 10 Souls: keine Soul-Dateien in S01 — wird in S02 bewiesen
- R009 — Command System: keine Command-Dateien in S01 — wird in S08 bewiesen
- Templates auf Praxis-Tauglichkeit: erst nachgewiesen wenn S02/S03 die Templates für 10 Souls + 16 Identities + 16 Agents verwenden

## Notes for Tester

- Das Verifikations-Skript ist die primäre und vollständige Prüfinstanz für S01 — manuelle Checks sind optional
- Exit-Code 0 = vollständig grün; jeder Fehler erhöht den Exit-Code um 1
- Bei Windows: das Skript nur in Git Bash oder WSL ausführen, nicht in PowerShell oder CMD
- D006-Konformität (Schritt-Konkretheit) kann nicht maschinell geprüft werden — manuelles Review der Benchmark-Skills empfohlen als Kalibrierung für S04–S07
