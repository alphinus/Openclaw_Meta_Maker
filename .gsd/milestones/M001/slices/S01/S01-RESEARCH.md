# S01: Foundation — Templates, Format und Ordnerstruktur — Research

**Date:** 2026-03-11

## Summary

S01 ist ein reiner Markdown-Authoring-Slice ohne Code, Libraries oder externe Dienste. Die Arbeit besteht ausschließlich aus: (1) Anlegen der Ordnerstruktur, (2) Schreiben von 4 Templates, (3) Schreiben von 6 Beispiel-Skills (einer pro Kategorie). Die einzigen "technischen" Entscheidungen sind Formatierungskonventionen, die dann für alle ~100 nachfolgenden Skills bindend gelten.

Das zentrale Risiko in S01 ist nicht technischer Natur, sondern inhaltlicher: Die Templates müssen präzise genug sein, dass zukünftige Slices (S02–S09) konsistent dasselbe Format produzieren — ohne in einem Slice abzuweichen und dadurch eine Korrekturwelle auszulösen. Das Skill-Template ist der kritischste Artefakt: Es definiert alle 9 Sektionen, legt konkrete Beispiele pro Sektion bei, und muss als Qualitäts-Benchmark die Messlatte für R003 (konkrete Execution Steps) setzen.

Die Empfehlung ist, alle Templates mit einem vollständig ausgefüllten Beispiel-Block zu liefern (kein Platzhalter-Dummy, sondern ein echter, funktionaler Skill / Soul / Identity / Agent). Das verhindert Fehlinterpretationen in S02–S09.

## Recommendation

**Templates mit eingebetteten Beispielen bauen, nicht nur leere Strukturen.**

Jedes Template enthält zwei Teile:
1. **Struktur-Definition** — die Sektionen mit Anweisungen in `<!-- Kommentaren -->`
2. **Ausgefülltes Beispiel** — ein realer Skill/Soul/etc. der das Format demonstriert

Das gilt besonders für `skill-template.md`. Die Beispiel-Skills pro Kategorie (einer pro Kategorie = 6 Skills) dienen als Qualitäts-Benchmark für alle nachfolgenden Slices.

Für die Ordnerstruktur: Alle Verzeichnisse mit `.gitkeep` anlegen, damit sie im Repo sichtbar sind. Die Struktur exakt so wie in CONTEXT.md spezifiziert — keine Abweichungen.

## Don't Hand-Roll

| Problem | Existing Solution | Why Use It |
|---------|------------------|------------|
| Konsistentes Markdown-Format ohne Parser | YAML-Frontmatter vermeiden | Einfachere Editierbarkeit, keine zusätzliche Parsing-Logik nötig — reine H2-Sektionen wie im finalen Skill-Format definiert |
| Skill-Namen Konsistenz | Naming Convention aus D001 | Alle Skills `/elvis-*` — keine Ausnahmen, auch Beispiel-Skills müssen diese Convention einhalten |

## Existing Code and Patterns

- `.gsd/milestones/M001/M001-CONTEXT.md` — Enthält das **finale, bindende Skill-Format** (9 Sektionen) und die **Ordnerstruktur** — diese sind die Grundlage für alle Templates, NICHT neu erfinden
- `.gsd/DECISIONS.md` — D001 bis D010 sind alle für S01 relevant; besonders D005 (Skill-Format), D006 (Granularität Execution Steps), D003 (Ordnerstruktur)

## Constraints

- **Sprache:** Alle Inhalte auf Deutsch (R011). Ausnahmen: Dateinamen, Verzeichnisnamen, Skill-Prefix `/elvis-*`, Fachbegriffe ohne gute Übersetzung (Skill, Soul, Agent, Identity) bleiben englisch.
- **Skill-Format ist fix:** Das 9-Sektionen-Format aus CONTEXT.md ist bindend (D005). Templates dürfen es nicht abwandeln.
- **Ordnerstruktur ist fix:** Exakt die Struktur aus CONTEXT.md — `soul/`, `identity/`, `agent/`, `skills/growth|content|research|strategy|automation|meta/`, `commands/`, `templates/` (D003).
- **Kein Code:** Nichts in S01 enthält ausführbaren Code. Templates sind reine Markdown-Dateien (R030).
- **Keine Stubs:** Templates sind vollständig ausgefüllt — kein Platzhalter-Inhalt der als echter Content durchgeht.
- **6 Beispiel-Skills (einer pro Kategorie):** growth, content, research, strategy, automation, meta — je ein voll ausgearbeiteter Skill als Qualitäts-Benchmark für nachfolgende Slices.

## Common Pitfalls

- **Zu abstrakte Beispiel-Skills** — Wenn der Beispiel-Skill für S01 vage Execution Steps hat (z.B. "Analysiere Trends"), werden alle ~100 nachfolgenden Skills dasselbe Niveau übernehmen. Beispiele müssen R003 vollständig erfüllen: spezifische Mengen, Zeitangaben, Formate.
- **Template-Kommentare vs. Inhalt verwechseln** — Templates brauchen klare visuelle Trennlinie zwischen "Anleitung für den Autor" (Kommentare) und "echtem Inhalt" (Beispiele). Sonst werden Anweisungen aus Versehen als Content behandelt.
- **Ordnerstruktur ohne `analysis/`** — Die CONTEXT.md Ordnerstruktur nennt `skills/automation/` aber in der Boundary Map von S06 erscheint auch `skills/analysis/`. Laut CONTEXT.md gibt es keine `analysis/`-Unterordner — es sind nur 6 Skill-Subkategorien: growth, content, research, strategy, automation, meta. Der `analysis/`-Begriff in S06 bezieht sich auf den *Inhalt*, nicht auf einen eigenen Unterordner. → `skills/analysis/` wird NICHT angelegt; Analysis-Skills gehen in `skills/strategy/` oder `skills/automation/`.
- **Soul-Template zu dünn** — Souls haben ein anderes Format als Skills. Soul-Sektionen sind: Name, Philosophie, Core Values, Operating Principles, Success Metrics, Für welche Agenten geeignet. Wenn das Soul-Template nur 2-3 Sektionen hat, werden die 10 Souls in S02 flach.
- **Identity-Template mit Agent-Template verwechseln** — Identity = Charakter-Persönlichkeit (wer bin ich?). Agent = operationale Definition (was tue ich?). Diese Trennung muss im Template klar erkennbar sein.
- **Meta-Skill Beispiel ohne Safeguards** — Der Beispiel-Meta-Skill muss bereits die Safeguard-Anforderungen (D007, R004) demonstrieren: Max-Limit, Approval-Gate, Stop-Bedingung, Rollback. Sonst wird S07 diese vergessen.

## Open Risks

- **`skills/analysis/` Verzeichnis-Ambiguität** — S06-Beschreibung im Roadmap erwähnt "~10 Analysis Skills" als eigene Gruppe neben Automation. CONTEXT.md zeigt aber nur 6 Unterordner in `skills/`. Entscheidung in S01: Ordnerstruktur folgt CONTEXT.md (6 Unterordner, kein separates `analysis/`). Analysis-Skills in `skills/strategy/` oder `skills/automation/` einordnen. → Klärung in S01-PLAN nötig, falls Abweichung gewünscht.
- **Template-Bindlichkeit für automatische Generierung** — In S07 wird der `elvis-skill-generator` Meta-Skill neue Skills generieren. Wenn das Template in S01 zu viele Freiheitsgrade lässt, wird die Generierung inkonsistent. Templates sollten wo möglich Pflichtfelder mit `[PFLICHTFELD]` markieren.
- **Deutsch + Fachbegriffe** — Einige Sektion-Titel im Template auf Deutsch könnten ungewohnt wirken (z.B. "Ausführungsschritte" statt "Execution Steps"). Konsistente Titel-Konvention festlegen und im Template dokumentieren.

## Skills Discovered

| Technology | Skill | Status |
|------------|-------|--------|
| Markdown Authoring | — | none found (nicht relevant — keine externe Library) |

*S01 ist technologie-frei. Es gibt keine relevanten Package-Skills für reine Markdown-Datei-Generierung.*

## Sources

- Finales Skill-Format und Ordnerstruktur (source: M001-CONTEXT.md — inline)
- Architektur-Entscheidungen D001–D010 (source: DECISIONS.md — inline)
- Requirement Coverage R002, R006, R007, R010, R011 (source: REQUIREMENTS.md — inline)
