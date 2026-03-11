---
estimated_steps: 5
estimated_files: 7
---

# T01: Research Skills R01–R07 erstellen

**Slice:** S05 — Research + Strategy Skills (~30 Skills)
**Milestone:** M001

## Description

Erstellt die ersten 7 Research Skills (R01–R07): KI-gestützte Recherche, Opportunity Finder, Trend Analyzer, Source Validator, Competitor Deep Dive, Audience Research und Keyword Researcher. Alle 7 Dateien folgen strikt dem 9-Sektionen-Format aus `templates/skill-template.md` und dem Qualitäts-Standard von `skills/research/elvis-market-scan.md`.

Diese 7 Skills decken die grundlegenden Recherche-Methoden ab: KI als Tool, Lücken finden, Trends tief analysieren, Quellen bewerten, Einzelkonkurrenten analysieren, Zielgruppe qualitativ verstehen, Keywords kartieren.

## Steps

1. Lies `skills/research/elvis-market-scan.md` als Qualitäts-Benchmark — merke Format: konkrete Zahlen in jedem Schritt, Failure-Indikator mit Schwelle + Meldungstext, D021-konforme Abhängigkeiten.
2. Erstelle `skills/research/elvis-ai-research.md` — KI-gestützte Recherche: Prompt-Templates für strukturierte Datenerhebung. Mindestens 5 Prompt-Templates mit je 3 Parametern, Bewertungs-Matrix für KI-Outputs (3 Qualitätskriterien), Failure-Indikator bei < 3 verwertbaren Antworten.
3. Erstelle `skills/research/elvis-opportunity-finder.md` — Marktlücken-Analyse: 5 Gaps aus 3 Quellentypen (Konkurrenz-Lücken, Zielgruppen-Wünsche, unbesetzte Nischen). Gap-Scoring mit 3 Kriterien (Nachfrage, Wettbewerb, Erreichbarkeit). Failure-Indikator bei < 3 validierten Gaps.
4. Erstelle `skills/research/elvis-trend-analyzer.md` — Tiefgehende Trend-Analyse: 3 Trends mit je 5 Analyse-Dimensionen (Ursache, Reifegrad, Plattformverteilung, Zielgruppen-Relevanz, 6-Monate-Prognose). Differenzierung von `elvis-x-trend-scanner` (nur X, surface) durch multi-platform, kausal, prädiktiv. Failure-Indikator bei < 2 belegten Datenquellen pro Trend.
5. Erstelle `skills/research/elvis-source-validator.md` — Quellen-Qualitätsprüfung: 5-Kriterien-Scoring (Autorität, Aktualität, Methodik, Belege, Bias) je 1–5 Punkte. Gesamtscore ≥ 15/25 für "verwendbar". Failure-Indikator bei < 50% der Quellen mit Score ≥ 15.
6. Erstelle `skills/research/elvis-competitor-deep-dive.md` — Einzel-Konkurrenten-Tiefenanalyse über 12 Wochen: Content-Strategie (Formate, Frequenz, Top-5 Posts), Positioning, Funnel-Struktur, 3 Stärken + 3 Schwächen. Differenzierung von `elvis-competitor-analysis` (5 Accounts × 5 Metriken, surface) durch Einzel-Fokus + Tiefe. Abhängigkeit: `elvis-competitor-analysis` als empfohlener Vorgänger.
7. Erstelle `skills/research/elvis-audience-research.md` — Qualitative Zielgruppen-Recherche: 5 Quellen (Foren, Kommentare, Reviews, Communities, Direktgespräche), 20 Pain Points kategorisiert nach Häufigkeit, 5 Job-to-be-done im Format "Wenn [Situation], möchte ich [Motivation], damit [Erwartetes Ergebnis]". Failure-Indikator bei < 3 Quellen analysiert.
8. Erstelle `skills/research/elvis-keyword-researcher.md` — Keyword-Recherche: 30 relevante Keywords/Themen in 3 Kategorien (Kern-Keywords 10, Long-Tail 15, Frage-Keywords 5), Volumen-Einschätzung (hoch/mittel/niedrig), Content-Prioritäten-Matrix (3×3 Volumen × Relevanz). Failure-Indikator bei < 20 Keywords mit Volumen-Einschätzung.

## Must-Haves

- [ ] 7 Dateien existieren in `skills/research/`
- [ ] Jede Datei enthält genau 9 Sektionen: `## Name`, `## Beschreibung`, `## Ziele`, `## Strategie`, `## Einschränkungen`, `## Ausführungsschritte`, `## Verifikation`, `## Abhängigkeiten`, `## Output`
- [ ] Jeder `## Name` Block enthält `/elvis-*` Prefix
- [ ] Jeder Ausführungsschritt enthält mindestens 1 konkrete Zahl, Zeitangabe oder Tabellenformat (D006)
- [ ] Jeder `## Verifikation` Block enthält einen `Failure-Indikator:` mit konkreter Schwelle und Standard-Meldungstext
- [ ] Keine Phantom-Referenzen in `## Abhängigkeiten` — nur D021-Whitelist (S04-Skills, S01-Benchmarks, "keine (Einstiegs-Skill)")

## Verification

```bash
# Datei-Existenz (7 Checks)
for f in elvis-ai-research elvis-opportunity-finder elvis-trend-analyzer \
          elvis-source-validator elvis-competitor-deep-dive \
          elvis-audience-research elvis-keyword-researcher; do
  [ -f "skills/research/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done

# Sektions-Vollständigkeit (Stichprobe)
grep -c "^## " skills/research/elvis-ai-research.md  # erwartet: 9
grep -c "^## " skills/research/elvis-trend-analyzer.md  # erwartet: 9

# /elvis-* Prefix (alle 7)
grep -l "/elvis-" skills/research/elvis-ai-research.md \
     skills/research/elvis-opportunity-finder.md \
     skills/research/elvis-trend-analyzer.md \
     skills/research/elvis-source-validator.md \
     skills/research/elvis-competitor-deep-dive.md \
     skills/research/elvis-audience-research.md \
     skills/research/elvis-keyword-researcher.md | wc -l  # erwartet: 7

# Failure-Indikator Vollständigkeit
grep -l "Failure-Indikator:" skills/research/elvis-ai-research.md \
     skills/research/elvis-opportunity-finder.md \
     skills/research/elvis-trend-analyzer.md \
     skills/research/elvis-source-validator.md \
     skills/research/elvis-competitor-deep-dive.md \
     skills/research/elvis-audience-research.md \
     skills/research/elvis-keyword-researcher.md | wc -l  # erwartet: 7
```

## Observability Impact

- Signals added/changed: None (reine Markdown-Dateien, kein Runtime)
- How a future agent inspects this: `bash scripts/verify-s05.sh` (nach T05 erstellt) prüft alle 7 Dateien; `grep -c "^## " skills/research/DATEI.md` für Einzel-Check
- Failure state exposed: Fehlendes `Failure-Indikator:` oder Sektion wird in verify-s05.sh als ✗ angezeigt mit Dateiname + Sektionsname

## Inputs

- `templates/skill-template.md` — verbindliches 9-Sektionen-Format (Pflichtfeld-Marker, Beispiel-Struktur)
- `skills/research/elvis-market-scan.md` — Qualitäts-Benchmark für Research Skills (Mengenangaben, Failure-Indikator-Format)
- `skills/growth/elvis-competitor-analysis.md` — Grenzziehung Research vs. Growth für R05 (Competitor Deep Dive)
- `skills/growth/elvis-audience-builder.md` — Grenzziehung für R06 (Audience Research)
- `scripts/verify-s04.sh` — Referenz für Failure-Indikator-Muster und Constraint-Formulierungen

## Expected Output

- `skills/research/elvis-ai-research.md` — KI als Recherche-Methode, 5 Prompt-Templates
- `skills/research/elvis-opportunity-finder.md` — Gap-Analyse, 5 Lücken aus 3 Quellentypen
- `skills/research/elvis-trend-analyzer.md` — Tiefenanalyse 3 Trends × 5 Dimensionen, Kausalität + Prognose
- `skills/research/elvis-source-validator.md` — 5-Kriterien-Scoring, Schwelle 15/25
- `skills/research/elvis-competitor-deep-dive.md` — 12-Wochen-Tiefenanalyse eines Konkurrenten
- `skills/research/elvis-audience-research.md` — 20 Pain Points + 5 Job-to-be-done aus 5 Quellen
- `skills/research/elvis-keyword-researcher.md` — 30 Keywords in 3 Kategorien, Content-Matrix
