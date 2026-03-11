# S05: Research + Strategy Skills (~30 Skills)

**Goal:** 28 neue Skill-Dateien in zwei Kategorien erstellen (14 Research + 14 Strategy), sodass zusammen mit den S01-Benchmarks je ~15 Skills pro Kategorie vollständig und D006-konform existieren — verifiziert durch `bash scripts/verify-s05.sh` mit Exit-Code 0.

**Demo:** `bash scripts/verify-s05.sh` läuft aus dem Projekt-Root mit Exit-Code 0. Alle 4 Check-Gruppen grün: 28 Dateien existieren, 252 Sektions-Header vorhanden (28 × 9), 28 /elvis-* Prefix-Checks, 0 Phantom-Referenzen.

## Must-Haves

- 14 neue Research Skills in `skills/research/` (R01–R14, vollständig ausgearbeitet)
- 14 neue Strategy Skills in `skills/strategy/` (S01–S14, vollständig ausgearbeitet)
- Jeder der 28 Skills enthält alle 9 Pflicht-Sektionen (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- Jeder Ausführungsschritt enthält mindestens 1 Mengenangabe (D006-Konformität)
- Jeder Verifikations-Block enthält einen `Failure-Indikator:` mit konkreter Schwelle und Standard-Meldungstext
- Jeder `## Name` Block enthält `/elvis-*` Prefix
- Keine Phantom-Referenzen in `## Abhängigkeiten` (nur D021-Whitelist: S04-Skills, S01-Benchmarks, andere S05-Skills, oder "keine (Einstiegs-Skill)")
- `scripts/verify-s05.sh` — ausführbares 4-Gruppen-Skript analog zu verify-s04.sh, Exit-Code = Fehleranzahl
- `S05-SUMMARY.md` — vollständig ausgefüllte Slice-Summary mit Forward Intelligence

## Proof Level

- This slice proves: contract — alle 28 Skill-Dateien erfüllen das verbindliche 9-Sektionen-Format + D006-Konformität + Phantom-frei
- Real runtime required: nein (reine Markdown-Dateien)
- Human/UAT required: nein (vollständige maschinelle Verifikation via verify-s05.sh)

## Verification

```bash
# Haupt-Verifikation — muss Exit-Code 0 zurückgeben
bash scripts/verify-s05.sh

# Erwartete Ausgabe:
# [1/4] 28/28 Datei-Existenz-Checks ✓
# [2/4] 252/252 Sektions-Checks ✓
# [3/4] 28/28 /elvis-* Prefix-Checks ✓
# [4/4] 0 Phantom-Referenzen ✓
# Exit-Code: 0

# Schnell-Checks Research
ls skills/research/*.md | wc -l  # erwartet: 15 (14 neu + 1 S01-Benchmark)
ls skills/strategy/*.md | wc -l  # erwartet: 15 (14 neu + 1 S01-Benchmark)

# Failure-Indikator Vollständigkeit
grep -l "Failure-Indikator:" skills/research/*.md | wc -l  # erwartet: 15
grep -l "Failure-Indikator:" skills/strategy/*.md | wc -l  # erwartet: 15
```

## Observability / Diagnostics

- Runtime signals: keine (reine Markdown-Generierung)
- Inspection surfaces:
  - `bash scripts/verify-s05.sh` — strukturierter Check-Report mit ✓/✗ pro Datei/Sektion; Exit-Code = Fehleranzahl
  - `grep -E "^## " skills/research/elvis-ai-research.md` — schneller Sektions-Vollständigkeits-Check für einzelnen Skill
  - `grep "Failure-Indikator:" skills/research/*.md skills/strategy/*.md` — Vollständigkeits-Check für alle Failure-Indikatoren
  - `grep -rE "elvis-[a-z-]+" skills/research/*.md skills/strategy/*.md | grep "Abhängigkeiten" -A5` — Phantom-Referenz-Inspektion
- Failure visibility: verify-s05.sh zeigt genau welche Datei und welche Sektion fehlt — lokalisierbar bis auf Zeilen-Ebene
- Redaction constraints: keine (reine Markdown-Inhalte, keine Secrets)

## Integration Closure

- Upstream surfaces consumed:
  - `templates/skill-template.md` (S01) — verbindliches 9-Sektionen-Format
  - `skills/research/elvis-market-scan.md` (S01 Benchmark) — Qualitäts-Standard für Research
  - `skills/strategy/elvis-execution-plan.md` (S01 Benchmark) — Qualitäts-Standard für Strategy
  - `scripts/verify-s04.sh` (S04) — Vorlage für verify-s05.sh
  - Alle 28 S04-Skills in `skills/growth/` und `skills/content/` — referenzierbar in Abhängigkeiten
- New wiring introduced in this slice:
  - `scripts/verify-s05.sh` — neues Verifikations-Skript für S05
  - 28 neue Skill-Dateien die von S06/S07/S09 referenziert werden können
- What remains before the milestone is truly usable end-to-end:
  - S06: Automation + Analysis Skills (~20 Skills)
  - S07: Meta-Agent System Skills (~15 Skills)
  - S08: Command System (Router + 10 Commands)
  - S09: Integration und Verifikation + README

---

## Tasks

- [x] **T01: Research Skills R01–R07 erstellen** `est:45m`
  - Why: Erste Hälfte der Research Skills — Basis-Recherche-Tools (KI-Research, Opportunity, Trends, Quellen-Validierung, Konkurrenz-Tiefenanalyse, Zielgruppen, Keywords)
  - Files: `skills/research/elvis-ai-research.md`, `skills/research/elvis-opportunity-finder.md`, `skills/research/elvis-trend-analyzer.md`, `skills/research/elvis-source-validator.md`, `skills/research/elvis-competitor-deep-dive.md`, `skills/research/elvis-audience-research.md`, `skills/research/elvis-keyword-researcher.md`
  - Do: Erstelle 7 vollständige Skill-Dateien nach `templates/skill-template.md`, je mit D006-konformen Schritten, Failure-Indikator, erlaubten Abhängigkeiten (D021-Whitelist). Qualitäts-Benchmark: `elvis-market-scan.md`.
  - Verify: `grep -c "^## " skills/research/elvis-ai-research.md` → 9; alle 7 Dateien vorhanden; kein Schritt ohne Mengenangabe
  - Done when: 7 Dateien existieren, je 9 Sektionen, je /elvis-* Prefix, je Failure-Indikator, keine Phantom-Referenzen

- [x] **T02: Research Skills R08–R14 erstellen** `est:45m`
  - Why: Zweite Hälfte der Research Skills — tiefere Analyse-Tools (Pain Points, Synthese, Experten-Finder, Case Studies, Daten-Erhebung, Problem-Exploration, Insight-Extraktion)
  - Files: `skills/research/elvis-pain-point-finder.md`, `skills/research/elvis-research-synthesizer.md`, `skills/research/elvis-expert-finder.md`, `skills/research/elvis-case-study-analyzer.md`, `skills/research/elvis-data-collector.md`, `skills/research/elvis-problem-explorer.md`, `skills/research/elvis-insight-extractor.md`
  - Do: Erstelle 7 vollständige Skill-Dateien. `elvis-research-synthesizer` darf R01–R07-Skills als Abhängigkeiten referenzieren (T01 muss zuerst abgeschlossen sein). Alle anderen Skills können "keine (Einstiegs-Skill)" oder zulässige S04-Skills als Abhängigkeiten haben.
  - Verify: `ls skills/research/*.md | wc -l` → 15 (14 neu + S01-Benchmark); alle 7 neuen Dateien mit 9 Sektionen
  - Done when: 7 Dateien existieren, je 9 Sektionen, je Failure-Indikator, Phantom-Check sauber

- [x] **T03: Strategy Skills S01–S07 erstellen** `est:45m`
  - Why: Erste Hälfte der Strategy Skills — Meta-Strategien (Wachstum, Positioning, Content-Strategie, Go-to-Market, Plattform-Strategie, Risiko-Assessment, Competitive Strategy)
  - Files: `skills/strategy/elvis-growth-strategy.md`, `skills/strategy/elvis-positioning-strategy.md`, `skills/strategy/elvis-content-strategy.md`, `skills/strategy/elvis-go-to-market.md`, `skills/strategy/elvis-platform-strategy.md`, `skills/strategy/elvis-risk-assessment.md`, `skills/strategy/elvis-competitive-strategy.md`
  - Do: Erstelle 7 vollständige Skill-Dateien nach `elvis-execution-plan.md` als Qualitäts-Benchmark. Strategy Skills sind meta-strategisch (Langfristigkeit, Frameworks), nicht taktisch. Differenzierung von S04-Growth-Skills explizit in Beschreibung benennen.
  - Verify: `grep -c "^## " skills/strategy/elvis-growth-strategy.md` → 9; alle 7 Dateien vorhanden; Failure-Indikator in jedem Verifikations-Block
  - Done when: 7 Dateien existieren, je 9 Sektionen, je /elvis-* Prefix, je Failure-Indikator, keine Phantom-Referenzen

- [x] **T04: Strategy Skills S08–S14 erstellen** `est:45m`
  - Why: Zweite Hälfte der Strategy Skills — Entscheidungs- und Planungs-Tools (Decision Framework, Priorisierung, Szenario-Planung, OKR, Pivot-Bewertung, Ressourcen-Allokation, Monetarisierungs-Strategie)
  - Files: `skills/strategy/elvis-decision-framework.md`, `skills/strategy/elvis-prioritization-engine.md`, `skills/strategy/elvis-scenario-planner.md`, `skills/strategy/elvis-okr-planner.md`, `skills/strategy/elvis-pivot-advisor.md`, `skills/strategy/elvis-resource-allocator.md`, `skills/strategy/elvis-monetization-strategy.md`
  - Do: Erstelle 7 vollständige Skill-Dateien. `elvis-decision-framework` ist in `agent/*.md` vorwärts-referenziert (STATE.md) — Beschreibung muss den Entscheidungsrahmen-Zweck klar machen. `elvis-monetization-strategy` differenziert sich von `elvis-monetization-planner` (S04) durch meta-strategischen Fokus.
  - Verify: `ls skills/strategy/*.md | wc -l` → 15 (14 neu + S01-Benchmark); alle 7 neuen Dateien mit 9 Sektionen
  - Done when: 7 Dateien existieren, je 9 Sektionen, je Failure-Indikator, Phantom-Check sauber

- [x] **T05: verify-s05.sh schreiben + S05-SUMMARY.md erstellen** `est:20m`
  - Why: Objektive Stopping-Condition für S05 — Verifikations-Skript prüft alle 28 neuen Skills maschinell; SUMMARY dokumentiert Forward Intelligence für S06+
  - Files: `scripts/verify-s05.sh`, `.gsd/milestones/M001/slices/S05/S05-SUMMARY.md`
  - Do: Erstelle `verify-s05.sh` analog zu `verify-s04.sh` — 4 Check-Gruppen: (1) Datei-Existenz 28 Skills, (2) 9 Sektionen × 28 Skills (252 Checks), (3) /elvis-* Prefix × 28, (4) Phantom-Referenz-Check. Führe das Skript aus und behebe alle Fehler bis Exit-Code 0. Dann schreibe S05-SUMMARY.md mit vollständiger Forward Intelligence für S06.
  - Verify: `bash scripts/verify-s05.sh` → Exit-Code 0; alle 4 Check-Gruppen grün
  - Done when: `bash scripts/verify-s05.sh` gibt Exit-Code 0 zurück; S05-SUMMARY.md existiert mit allen Pflicht-Sektionen
