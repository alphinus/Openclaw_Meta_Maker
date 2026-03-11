# S01: Foundation — Templates, Format und Ordnerstruktur

**Goal:** Das vollständige Skill-Format ist definiert, alle 4 Templates existieren mit eingebetteten Beispielen, die Ordnerstruktur ist angelegt, und je ein vollständig ausgearbeiteter Beispiel-Skill pro Kategorie setzt den Qualitäts-Benchmark für alle nachfolgenden Slices.

**Demo:** `bash scripts/verify-s01.sh` läuft durch ohne Fehler — alle 11 Verzeichnisse, 4 Templates, 6 Beispiel-Skills und alle 9 Sektionen pro Skill sind vorhanden. Der Meta-Beispiel-Skill enthält nachweislich Safeguards.

## Must-Haves

- Ordnerstruktur exakt gemäß CONTEXT.md: `soul/`, `identity/`, `agent/`, `skills/{growth,content,research,strategy,automation,meta}/`, `commands/`, `templates/`
- `templates/skill-template.md` mit vollständigem 9-Sektionen-Format (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output) + eingebettetem Beispiel
- `templates/soul-template.md`, `templates/identity-template.md`, `templates/agent-template.md` — je mit Anweisungs-Kommentaren und vollständigem Beispiel
- 6 Beispiel-Skills (je einer pro Kategorie) mit konkreten Ausführungsschritten (spezifische Mengen, Zeitangaben, Formate — kein Abstraktionsniveau wie "analysiere Trends")
- Meta-Beispiel-Skill enthält alle 4 Safeguards: Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis
- Alle Skill-Namen tragen `/elvis-*` Prefix in der `## Name` Sektion
- Alle Inhalte auf Deutsch (Dateinamen/Verzeichnisse bleiben englisch)
- `scripts/verify-s01.sh` prüft alle Anforderungen und schlägt fehl wenn etwas fehlt

## Proof Level

- This slice proves: contract (Datei-Existenz, Sektion-Vollständigkeit, Format-Korrektheit)
- Real runtime required: no
- Human/UAT required: no — obwohl eine Review der Beispiel-Skills auf Konkretheit sinnvoll wäre

## Verification

```bash
# Ausführen aus dem Projekt-Root (C:\Dev\Openclaw_Meta_Maker):
bash scripts/verify-s01.sh
```

Der Skript prüft:
1. Alle 11 Verzeichnisse existieren
2. Alle 4 Template-Dateien existieren
3. `templates/skill-template.md` enthält alle 9 Sektions-Header (`## Name`, `## Beschreibung`, …, `## Output`)
4. Alle 6 Beispiel-Skills existieren in den richtigen Unterordnern
5. Jeder Beispiel-Skill enthält alle 9 Sektions-Header
6. Jeder Skill hat `/elvis-*` Prefix im `## Name` Block
7. `skills/meta/elvis-skill-generator.md` enthält Safeguard-Schlüsselwörter (Max-Limit, Approval-Gate, Stop-Bedingung, Rollback)

**Erwartetes Ergebnis nach T01 (Skript existiert, Inhalte fehlen):** Script schlägt fehl mit Fehlerzähler > 0.

**Erwartetes Ergebnis nach T04 (alle Inhalte erstellt):** Script läuft fehlerfrei durch, gibt `✅ S01 Verifikation bestanden` aus.

## Observability / Diagnostics

Dieser Slice ist reine Datei-Generierung ohne Runtime-Komponenten.

- Runtime signals: none (keine laufenden Prozesse)
- Inspection surfaces: `bash scripts/verify-s01.sh` — gibt strukturierten Check-Report aus mit ✓/✗ pro Datei/Sektion
- Failure visibility: Fehlerzähler + explizite ✗-Zeilen zeigen genau welche Datei oder Sektion fehlt
- Redaction constraints: none

## Integration Closure

- Upstream surfaces consumed: M001-CONTEXT.md (Skill-Format, Ordnerstruktur), DECISIONS.md (D001–D010)
- New wiring introduced in this slice: `templates/skill-template.md` als verbindlicher Skill-Contract für S04–S07; Ordnerstruktur als Datei-Layout-Contract für alle Slices
- What remains before the milestone is truly usable end-to-end: S02 (Souls + Identities), S03 (Agents), S04–S06 (Skills), S07 (Meta-Skills), S08 (Commands), S09 (Integration + README)

## Tasks

- [x] **T01: Ordnerstruktur anlegen und Verifikations-Skript schreiben** `est:30m`
  - Why: Legt das Datei-Layout des Ökosystems fest (R007) und etabliert die Stopping-Condition für S01 — der Skript schlägt initial fehl, alle folgenden Tasks machen ihn grün
  - Files: `soul/.gitkeep`, `identity/.gitkeep`, `agent/.gitkeep`, `skills/growth/.gitkeep`, `skills/content/.gitkeep`, `skills/research/.gitkeep`, `skills/strategy/.gitkeep`, `skills/automation/.gitkeep`, `skills/meta/.gitkeep`, `commands/.gitkeep`, `templates/.gitkeep`, `scripts/verify-s01.sh`
  - Do: Alle Verzeichnisse mit `.gitkeep` anlegen; `scripts/verify-s01.sh` schreiben das alle S01-Anforderungen prüft (Verzeichnisse, Templates, Skills, Sektionen, Prefix, Safeguards)
  - Verify: `bash scripts/verify-s01.sh` schlägt fehl (Fehler > 0) — erwartet, da Templates/Skills noch fehlen
  - Done when: Alle 11 Verzeichnisse existieren; `verify-s01.sh` ist ausführbar und gibt strukturierte ✓/✗ Ausgabe

- [x] **T02: Skill-Template mit vollständigem Beispiel schreiben** `est:45m`
  - Why: Das Skill-Template ist der kritischste Artefakt in S01 — es setzt den Qualitäts-Standard für alle ~100 Skills in S04–S07 und liefert R002 (erweitertes Format) und R010 (Templates)
  - Files: `templates/skill-template.md`
  - Do: Template mit zwei Teilen schreiben: (1) Anweisungs-Block mit `<!-- Kommentaren -->` pro Sektion, (2) vollständig ausgefülltes Beispiel-Skill `/elvis-x-growth` als erstes Beispiel in der Datei (kein Platzhalter); alle 9 Sektionen präzise; Execution Steps mit spezifischen Mengen/Zeitangaben
  - Verify: `bash scripts/verify-s01.sh` zeigt ✓ für alle 9 Sektionen in `templates/skill-template.md`
  - Done when: Template enthält alle 9 `## Sektions-Header`; eingebettetes Beispiel hat konkrete (nicht abstrakte) Ausführungsschritte; Kommentare und Beispiel sind visuell klar getrennt

- [x] **T03: Soul-, Identity- und Agent-Templates schreiben** `est:45m`
  - Why: Diese drei Templates bilden die Grundlage für S02 (Souls + Identities) und S03 (Agents) — ohne sie produzieren diese Slices inkonsistente Strukturen (R010)
  - Files: `templates/soul-template.md`, `templates/identity-template.md`, `templates/agent-template.md`
  - Do: Je Template mit Anweisungs-Kommentaren + vollständigem Beispiel. Soul: Sektionen Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für. Identity: Sektionen Name, Charakter, Persönlichkeit, Stärken, Schwächen, Kommunikationsstil, Star Trek Referenz. Agent: Sektionen Name, Mission, Capabilities, Operating Loop, Constraints, Primärer Soul, Primäre Skills. Identity ≠ Agent klar trennen (Charakter vs. operationale Definition)
  - Verify: `bash scripts/verify-s01.sh` schlägt weiterhin fehl wegen fehlender Beispiel-Skills — aber die 3 Template-Dateien existieren (✓ in Ausgabe)
  - Done when: 3 Template-Dateien existieren; jede hat mindestens 5 Sektions-Header; Soul/Identity/Agent-Unterschied ist aus dem Template-Inhalt eindeutig erkennbar

- [x] **T04: 6 Beispiel-Skills schreiben und Verifikation abschließen** `est:60m`
  - Why: Die Beispiel-Skills sind der Qualitäts-Benchmark — sie zeigen für S04–S07 exakt welches Konkretheitsniveau erwartet wird (R003); der Meta-Skill demonstriert Safeguard-Pattern (R004); nach diesem Task muss `verify-s01.sh` vollständig grün sein
  - Files: `skills/growth/elvis-x-growth.md`, `skills/content/elvis-x-content.md`, `skills/research/elvis-ai-research.md`, `skills/strategy/elvis-growth-strategy.md`, `skills/automation/elvis-automation.md`, `skills/meta/elvis-skill-generator.md`
  - Do: Je ein vollständig ausgearbeiteter Skill pro Kategorie mit allen 9 Sektionen. Execution Steps müssen spezifisch sein (z.B. "Analysiere die Top-20 Posts der letzten 7 Tage", nicht "Analysiere Posts"). Meta-Skill `/elvis-skill-generator` muss alle 4 Safeguards enthalten: Max-Limit (z.B. max. 10 Skills pro Durchlauf), Approval-Gate (Operator bestätigt vor Ausführung), Stop-Bedingung (wann endet der Prozess), Rollback-Hinweis (was bei Fehler). Alle Skills auf Deutsch, alle `/elvis-*` Prefix
  - Verify: `bash scripts/verify-s01.sh` läuft vollständig durch mit 0 Fehlern; Ausgabe endet mit `✅ S01 Verifikation bestanden`
  - Done when: 6 Skill-Dateien existieren; verify-s01.sh: exit code 0; Meta-Skill enthält alle 4 Safeguard-Typen; kein Skill hat abstrakte Schritte wie "analysiere Daten" ohne Menge/Format/Zeitangabe

## Files Likely Touched

- `scripts/verify-s01.sh`
- `soul/.gitkeep`, `identity/.gitkeep`, `agent/.gitkeep`
- `skills/growth/.gitkeep`, `skills/content/.gitkeep`, `skills/research/.gitkeep`, `skills/strategy/.gitkeep`, `skills/automation/.gitkeep`, `skills/meta/.gitkeep`
- `commands/.gitkeep`, `templates/.gitkeep`
- `templates/skill-template.md`
- `templates/soul-template.md`
- `templates/identity-template.md`
- `templates/agent-template.md`
- `skills/growth/elvis-x-growth.md`
- `skills/content/elvis-x-content.md`
- `skills/research/elvis-ai-research.md`
- `skills/strategy/elvis-growth-strategy.md`
- `skills/automation/elvis-automation.md`
- `skills/meta/elvis-skill-generator.md`
