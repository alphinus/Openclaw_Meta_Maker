---
estimated_steps: 7
estimated_files: 6
---

# T04: 6 Beispiel-Skills schreiben und Verifikation abschließen

**Slice:** S01 — Foundation — Templates, Format und Ordnerstruktur
**Milestone:** M001

## Description

Schreibt einen vollständig ausgearbeiteten Beispiel-Skill pro Kategorie (growth, content, research, strategy, automation, meta). Diese 6 Skills sind der Qualitäts-Benchmark für alle ~90–100 Skills in S04–S07 — sie zeigen exakt welches Konkretheitsniveau bei Execution Steps erwartet wird (R003).

Der Meta-Skill `/elvis-skill-generator` ist besonders kritisch: er muss alle 4 Safeguard-Typen demonstrieren (R004), die alle autonomen Agenten in S07 benötigen: Max-Limit, Approval-Gate, Stop-Bedingung, Rollback-Hinweis.

Nach diesem Task muss `bash scripts/verify-s01.sh` mit Exit-Code 0 enden.

**Skill-Zuordnung:**
- `skills/growth/elvis-x-growth.md` — X/Twitter Growth Analyse
- `skills/content/elvis-x-content.md` — X/Twitter Content-Erstellung
- `skills/research/elvis-ai-research.md` — KI-gestützte Marktrecherche
- `skills/strategy/elvis-growth-strategy.md` — Wachstumsstrategie-Entwicklung
- `skills/automation/elvis-automation.md` — Workflow-Automatisierung
- `skills/meta/elvis-skill-generator.md` — Neuen Skill generieren (mit Safeguards)

## Steps

1. `skills/growth/elvis-x-growth.md` schreiben — alle 9 Sektionen. Ausführungsschritte: konkret mit Zahlen (z.B. "Analysiere die Top-20 Posts der letzten 14 Tage im Ziel-Nischen-Bereich", "Extrahiere die 5 häufigsten Engagement-Muster", "Erstelle eine Liste von 10 Wachstums-Hypothesen mit je einer Begründung"). Einschränkungen: max. 20 Posts pro Analyse.
2. `skills/content/elvis-x-content.md` schreiben — alle 9 Sektionen. Ausführungsschritte konkret: z.B. "Schreibe 5 Tweet-Varianten zu einem Thema, jede mit max. 280 Zeichen", "Jede Variante nutzt einen anderen Hook-Typ (Frage, Aussage, Kontrast, Liste, Story)". 
3. `skills/research/elvis-ai-research.md` schreiben — alle 9 Sektionen. Ausführungsschritte: z.B. "Identifiziere 10 relevante Quellen (Blogs, Paper, Competitor-Seiten) zum Thema", "Extrahiere pro Quelle: Kernaussage, Datum, Relevanz-Score 1–5", "Erstelle eine strukturierte Zusammenfassung mit 3 Schlüssel-Erkenntnissen".
4. `skills/strategy/elvis-growth-strategy.md` schreiben — alle 9 Sektionen. Ausführungsschritte: z.B. "Definiere 3 Wachstumsziele für die nächsten 90 Tage (messbar, zeitgebunden)", "Priorisiere Taktiken nach Impact/Aufwand-Matrix (2×2)", "Erstelle Aktionsplan mit max. 10 Maßnahmen für die ersten 30 Tage".
5. `skills/automation/elvis-automation.md` schreiben — alle 9 Sektionen. Ausführungsschritte: z.B. "Identifiziere repetitive Aufgaben die > 30 Min/Woche kosten", "Beschreibe jeden Workflow in max. 5 Schritten (Trigger → Aktion → Output → Bedingung → Fehlerfall)".
6. `skills/meta/elvis-skill-generator.md` schreiben — alle 9 Sektionen + alle 4 Safeguards. In `## Einschränkungen`: Max-Limit (max. 10 neue Skills pro Durchlauf), Approval-Gate (Operator bestätigt Skill-Liste vor Erstellung), Stop-Bedingung (Prozess endet wenn alle angeforderten Skills erstellt oder Operator abbricht), Rollback-Hinweis (bei fehlerhaftem Skill: Original-Anforderung nochmals senden, nicht weiter generieren). Ausführungsschritte: konkret für den Skill-Generierungsprozess.
7. `bash scripts/verify-s01.sh` ausführen — alle Checks müssen grün sein; Exit-Code 0

## Must-Haves

- [ ] Alle 6 Skill-Dateien existieren im richtigen Unterordner
- [ ] Jeder Skill hat alle 9 Sektions-Header (`## Name` bis `## Output`)
- [ ] `## Name` enthält `/elvis-*` Prefix (z.B. `/elvis-x-growth`)
- [ ] Kein Ausführungsschritt ist abstrakt ohne Menge/Format/Zeitangabe (R003)
- [ ] `skills/meta/elvis-skill-generator.md` enthält explizit: "Max-Limit", "Approval-Gate", "Stop-Bedingung", "Rollback" in `## Einschränkungen`
- [ ] Alle Inhalte auf Deutsch
- [ ] `bash scripts/verify-s01.sh` endet mit Exit-Code 0

## Verification

```bash
bash scripts/verify-s01.sh
# Erwartete Ausgabe: ✅ S01 Verifikation bestanden — alle Checks OK
# Exit-Code: 0
```

Zusatz-Check Meta-Skill Safeguards:
```bash
grep -E "Max-Limit|Approval-Gate|Stop-Bedingung|Rollback" skills/meta/elvis-skill-generator.md
# Muss mindestens 4 Treffer liefern
```

## Observability Impact

- Signals added/changed: `verify-s01.sh` läuft jetzt vollständig durch; alle 30+ Checks sind grün; Exit-Code 0 ist das Completion-Signal für S01
- How a future agent inspects this: `bash scripts/verify-s01.sh` — vollständiger Qualitäts-Check der S01-Artefakte in ~2 Sekunden
- Failure state exposed: Wenn ein späterer Slice einen Skill kaputtmacht, zeigt das Script genau welche Sektion fehlt

## Inputs

- `templates/skill-template.md` (T02) — verbindliches Format für alle 6 Skills
- `M001-CONTEXT.md` — Skill-Kategorien, Safeguard-Anforderungen
- `DECISIONS.md` D001 (/elvis-* Prefix), D006 (Execution Steps Granularität), D007 (Autonomous Safeguards)
- `scripts/verify-s01.sh` (T01) — definiert was "fertig" bedeutet

## Expected Output

- `skills/growth/elvis-x-growth.md` — vollständig ausgearbeiteter Growth-Skill
- `skills/content/elvis-x-content.md` — vollständig ausgearbeiteter Content-Skill
- `skills/research/elvis-ai-research.md` — vollständig ausgearbeiteter Research-Skill
- `skills/strategy/elvis-growth-strategy.md` — vollständig ausgearbeiteter Strategy-Skill
- `skills/automation/elvis-automation.md` — vollständig ausgearbeiteter Automation-Skill
- `skills/meta/elvis-skill-generator.md` — vollständig ausgearbeiteter Meta-Skill mit allen 4 Safeguards
- `bash scripts/verify-s01.sh` → Exit-Code 0, ✅-Meldung
