---
estimated_steps: 4
estimated_files: 1
---

# T02: Skill-Template mit vollständigem Beispiel schreiben

**Slice:** S01 — Foundation — Templates, Format und Ordnerstruktur
**Milestone:** M001

## Description

Schreibt das kritischste Template des gesamten Projekts: `templates/skill-template.md`. Dieses Template ist für alle ~100 Skills in S04–S07 bindend (R002, R010). Es enthält zwei klar getrennte Teile: (1) Anweisungs-Block mit HTML-Kommentaren pro Sektion, der dem Autor sagt was in jede Sektion gehört, (2) ein vollständig ausgearbeitetes Beispiel-Skill das das Qualitäts-Niveau demonstriert.

Das Template legt das 9-Sektionen-Format aus CONTEXT.md fest: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output. Es markiert Pflichtfelder mit `[PFLICHTFELD]` damit der `elvis-skill-generator` in S07 weiss, welche Felder er immer befüllen muss.

## Steps

1. Ersten Teil schreiben: Template-Struktur mit `<!-- Anweisung -->` Kommentaren pro Sektion. Jede Sektion erklärt: was hingehört, welches Format, was ein häufiger Fehler ist. `[PFLICHTFELD]` bei Name, Beschreibung, Ausführungsschritte, Verifikation, Output einfügen.
2. Visuelle Trennlinie zwischen Template-Teil und Beispiel-Teil einfügen (`---` + Kommentar `<!-- BEISPIEL BEGINS BELOW — KEIN TEMPLATE-INHALT -->`)
3. Vollständiges Beispiel-Skill schreiben: `/elvis-x-growth` (X/Twitter Growth Analysis). Alle 9 Sektionen ausfüllen. Ausführungsschritte müssen R003 erfüllen: spezifische Mengen (z.B. "Top-20 Posts der letzten 7 Tage"), Formate (z.B. "Excel-Tabelle mit 4 Spalten"), Zeitangaben (z.B. "innerhalb von 2 Stunden"). Einschränkungen müssen konkrete Limits haben (z.B. "max. 20 Posts pro Analyse-Durchlauf").
4. Prüfen: `bash scripts/verify-s01.sh` zeigt ✓ für alle 9 Sektionen in `templates/skill-template.md`

## Must-Haves

- [ ] Alle 9 Sektions-Header exakt so: `## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`
- [ ] Template-Kommentare und Beispiel-Inhalt sind visuell klar getrennt (kein Mischmasch)
- [ ] Pflichtfelder mit `[PFLICHTFELD]` markiert in den Kommentaren
- [ ] Beispiel-Skill `/elvis-x-growth` hat konkrete Steps (Mengen + Zeitangaben + Formate)
- [ ] Kein Platzhalter-Text der als echter Content durchgehen könnte (z.B. kein "[Ihr Skill hier]")

## Verification

- `bash scripts/verify-s01.sh` — Sektion-Checks für `templates/skill-template.md` alle ✓
- Manueller Check: Lese `## Ausführungsschritte` im Beispiel — enthält mindestens eine Zahl/Menge und mindestens eine Zeitangabe

## Observability Impact

- Signals added/changed: `verify-s01.sh` kann jetzt Sektion-Checks für das Skill-Template passieren
- How a future agent inspects this: `grep "^## " templates/skill-template.md` listet alle Sektions-Header
- Failure state exposed: Fehlende Sektion wird in verify-Ausgabe mit ✗ markiert

## Inputs

- `M001-CONTEXT.md` — finales Skill-Format (9 Sektionen, exakte Header-Namen)
- `DECISIONS.md` D005 (Skill-Format), D006 (Execution Steps Granularität)
- `scripts/verify-s01.sh` — zeigt welche Checks das Template bestehen muss

## Expected Output

- `templates/skill-template.md` — zweistufiges Template (Anweisungen + Beispiel) mit allen 9 Sektionen; Beispiel `/elvis-x-growth` vollständig ausgearbeitet mit konkreten Execution Steps
