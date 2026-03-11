---
id: S05
parent: M001
milestone: M001
provides:
  - skills/research/elvis-ai-research.md — KI-gestützte Recherche, 5 Prompt-Templates, Relevanz-Score 1–5
  - skills/research/elvis-opportunity-finder.md — 5 Opportunity-Typen × 4 Kriterien, Score 4–20
  - skills/research/elvis-trend-analyzer.md — 12-Wochen-Trend-Analyse, 3 Reifegrad-Stufen
  - skills/research/elvis-source-validator.md — 4-Dimensionen-Validierung (Autorität/Aktualität/Methodik/Bias), Score 1–5
  - skills/research/elvis-competitor-deep-dive.md — 1 Hauptkonkurrent × 8 Analysedimensionen, 90-Punkte-Bericht
  - skills/research/elvis-audience-research.md — 20 Pain Points, 5 demografische Segmente, 3 Buying-Trigger
  - skills/research/elvis-keyword-researcher.md — 30 Keywords in 3 Absichts-Kategorien (Awareness/Consideration/Decision)
  - skills/research/elvis-pain-point-finder.md — 30–40 Roh-Pain-Points → Cluster → Top-10 priorisiert
  - skills/research/elvis-research-synthesizer.md — 5 Quellen → Synthese-Matrix 4×N, 3 Schlussfolgerungen
  - skills/research/elvis-expert-finder.md — 10 Experten × 5 Vertrauenskriterien, Engagement-Plan
  - skills/research/elvis-case-study-analyzer.md — 3 Case Studies × 6 Analysedimensionen, Muster-Extraktion
  - skills/research/elvis-data-collector.md — 15 Datenpunkte × 3 Quellen-Typen, Vollständigkeits-Score
  - skills/research/elvis-problem-explorer.md — 5 Iterationen (5×Why), Problem-Karte 3 Ebenen, Haupt-Ursache
  - skills/research/elvis-insight-extractor.md — 5 Kerninsights mit Handlungsrelevanz-Score 1–10
  - skills/strategy/elvis-growth-strategy.md — 90-Tage-Wachstumsplan, 3 Wachstums-Hebel, OKR-Verknüpfung
  - skills/strategy/elvis-positioning-strategy.md — 4-Dimensionen-Positionierungs-Matrix, Differenzierungs-Statement
  - skills/strategy/elvis-content-strategy.md — 12-Wochen-Content-Rahmen, 5 Themen-Säulen, Kanal-Priorisierung
  - skills/strategy/elvis-go-to-market.md — 7-Wochen-GTM-Plan (Pre-Launch 2W / Launch-Woche / Post-Launch 4W)
  - skills/strategy/elvis-platform-strategy.md — Plattform-Scoring 5 Kriterien × N Plattformen, Primär/Sekundär-Matrix
  - skills/strategy/elvis-risk-assessment.md — RPS = Wahrscheinlichkeit × Auswirkung × (6−Erkennbarkeit), Top-5 Risiken
  - skills/strategy/elvis-competitive-strategy.md — 3 Wettbewerbs-Positionen, Angriff/Verteidigung/Koexistenz-Rahmen
  - skills/strategy/elvis-decision-framework.md — 5 Kriterien-Gewichtungs-Matrix, 3 Alternativen, Decision-Score
  - skills/strategy/elvis-prioritization-engine.md — ICE-Score (Impact/Confidence/Ease je 1–10), Top-10 Liste
  - skills/strategy/elvis-scenario-planner.md — 3 Szenarien (Best/Base/Worst), 5 Trigger pro Szenario
  - skills/strategy/elvis-okr-planner.md — 3 Objectives × 3–5 KRs, Quartal-Rahmen, Fortschritts-Check-Template
  - skills/strategy/elvis-pivot-advisor.md — 5 Pivot-Signale, 3 Pivot-Richtungen, 30-Tage-Pivot-Plan
  - skills/strategy/elvis-resource-allocator.md — Budget/Zeit/Energie auf 100% verteilt, 5 Allokations-Kategorien
  - skills/strategy/elvis-monetization-strategy.md — Portfolio-Logik, Preis-Positionierungs-Matrix, CLV = Kaufwert × Frequenz × Dauer
requires:
  - S01 (templates/skill-template.md, 9-Sektionen-Format)
  - S04 (skills/growth/*, skills/content/* — alle 28 Dateien referenzierbar)
affects:
  - S06 — Automation Skills (darf Research+Strategy-Skills referenzieren, aber nur existierende)
  - S09 — Integrations-Verifikation (alle 28 S05-Skills werden hier inspiziert)
key_files:
  - scripts/verify-s05.sh
  - skills/research/ (14 Dateien)
  - skills/strategy/ (14 Dateien)
key_decisions:
  - Risiko-Priorisierungs-Score (RPS) = Wahrscheinlichkeit × Auswirkung × (6−Erkennbarkeit) — messbare 3-Faktoren-Formel etabliert, konsistent mit FMEA-Ansatz
  - GTM-Plan verwendet 7-Wochen-Rahmen (Pre-Launch 2W / Launch-Woche / Post-Launch 4W) — konkrete Phasenstruktur statt generischem Modell
  - elvis-decision-framework Beschreibung nennt explizit "Entscheidungsrahmen für komplexe, folgenreiche Entscheidungen" — konsistent mit Forward-Referenz in agent/kirk.md
  - elvis-monetization-strategy differenziert sich von elvis-monetization-planner (Planner = 5 Modelle + ROI + 90-Tage-Plan; Strategy = Portfolio-Logik + Preis-Positionierung + CLV)
  - CLV-Formel = Kaufwert × Frequenz × Dauer — quantitative Basis für Monetisierungs-Entscheidungen
  - Alle Dependency-Blöcke ohne Phantom-Referenzen (bewusste Entscheidung: Abhängigkeiten als "Empfohlene Vorgänger" im Fließtext, keine maschinenlesbaren Listen)
patterns_established:
  - Failure-Indikator mit konkretem Schwellenwert + Standard-Meldungstext in jeder ## Verifikation-Sektion (konsistent mit S04-Pattern)
  - Jeder Ausführungsschritt enthält ≥1 Mengenangabe (D006): Prozent-Werte, Matrizen, Zeiträume, Anzahlen, Formeln
  - Differenzierungs-Notizen in ## Beschreibung für Skills mit ähnlichen S04-Pendants (z.B. trend-analyzer vs. x-trend-scanner, competitor-deep-dive vs. competitor-analysis)
  - Scoring-Formeln als explizite Gleichungen dokumentiert (RPS, ICE, CLV) — reproduzierbar und prüfbar
observability_surfaces:
  - bash scripts/verify-s05.sh — 4 Check-Gruppen: Datei-Existenz (28 Checks), Sektions-Vollständigkeit (252 Checks), /elvis-Prefix (28 Checks), Phantom-Referenz (28 Checks); Exit-Code = Fehleranzahl
  - grep "Failure-Indikator" skills/research/*.md skills/strategy/*.md — verifiziert Failure-Indikator in allen Skills
  - ls skills/research/ skills/strategy/ | wc -l — ergibt 30 (15 + 15, inkl. S01-Benchmark-Skills)
drill_down_paths:
  - .gsd/milestones/M001/slices/S05/tasks/T01-SUMMARY.md
  - .gsd/milestones/M001/slices/S05/tasks/T02-SUMMARY.md
  - .gsd/milestones/M001/slices/S05/tasks/T03-SUMMARY.md
  - .gsd/milestones/M001/slices/S05/tasks/T04-SUMMARY.md
  - .gsd/milestones/M001/slices/S05/tasks/T05-SUMMARY.md
duration: ~5 Tasks × ~60–90 Min = ~6 Stunden gesamt (T01: ~60min, T02: ~75min, T03: ~75min, T04: ~75min, T05: ~20min)
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# S05: Research + Strategy Skills (~30 Skills)

**28 neue Skill-Dateien erstellt (14 Research + 14 Strategy), vollständig nach 9-Sektionen-Format, D006-konform, auf Deutsch — `bash scripts/verify-s05.sh` Exit-Code 0, alle 4 Check-Gruppen grün (28/252/28/28), 0 Phantom-Referenzen.**

## What Happened

**T01 — Research Skills R01–R07:** `elvis-ai-research`, `elvis-opportunity-finder`, `elvis-trend-analyzer`, `elvis-source-validator`, `elvis-competitor-deep-dive`, `elvis-audience-research`, `elvis-keyword-researcher` erstellt. Je 9 Pflichtsektion-Header, D006-konforme Mengenangaben. Differenzierungs-Notizen für elvis-trend-analyzer (vs. elvis-x-trend-scanner) und elvis-competitor-deep-dive (vs. elvis-competitor-analysis) eingebaut.

**T02 — Research Skills R08–R14:** `elvis-pain-point-finder`, `elvis-research-synthesizer`, `elvis-expert-finder`, `elvis-case-study-analyzer`, `elvis-data-collector`, `elvis-problem-explorer`, `elvis-insight-extractor` erstellt. Alle Abhängigkeits-Blöcke ohne Phantom-Referenzen — elvis-insight-extractor referenziert nur elvis-data-collector (gleicher Task), elvis-research-synthesizer nur elvis-market-scan und elvis-audience-research (beide S01/T01).

**T03 — Strategy Skills S01–S07:** `elvis-growth-strategy`, `elvis-positioning-strategy`, `elvis-content-strategy`, `elvis-go-to-market`, `elvis-platform-strategy`, `elvis-risk-assessment`, `elvis-competitive-strategy` erstellt. RPS-Formel (Wahrscheinlichkeit × Auswirkung × (6−Erkennbarkeit)) und 7-Wochen-GTM-Rahmen als Key Decisions etabliert.

**T04 — Strategy Skills S08–S14:** `elvis-decision-framework`, `elvis-prioritization-engine`, `elvis-scenario-planner`, `elvis-okr-planner`, `elvis-pivot-advisor`, `elvis-resource-allocator`, `elvis-monetization-strategy` erstellt. elvis-decision-framework Beschreibung konsistent mit Forward-Referenz in agent/kirk.md. Differenzierung elvis-monetization-strategy vs. elvis-monetization-planner explizit in ## Beschreibung dokumentiert.

**T05 — verify-s05.sh + S05-SUMMARY.md:** `scripts/verify-s05.sh` analog zu `verify-s04.sh` geschrieben (4 Check-Gruppen, Fehlerzähler als Exit-Code). Erster Lauf: Exit-Code 0 — alle 28 Skills aus T01–T04 waren sofort vollständig. S05-SUMMARY.md geschrieben. STATE.md aktualisiert.

## Verification

```bash
bash scripts/verify-s05.sh; echo "Exit-Code: $?"
# ══════════════════════════════════════════════════════
#  S05 Verifikation — Research + Strategy Skills
# ══════════════════════════════════════════════════════
# [1/4] Datei-Existenz — 28/28 ✓
# [2/4] Sektions-Vollständigkeit — 252/252 ✓
# [3/4] /elvis-* Prefix — 28/28 ✓
# [4/4] Phantomreferenz-Check — 28/28 ✓ (alle ohne Referenzen oder validiert)
# ✅ S05 Verifikation bestanden — alle Checks grün
# Exit-Code: 0

ls skills/research/*.md | wc -l   # 15 (14 neu + 1 S01-Benchmark)
ls skills/strategy/*.md | wc -l   # 15 (14 neu + 1 S01-Benchmark)
grep -rl "Failure-Indikator:" skills/research/ skills/strategy/ | wc -l  # 30
```

**Alle Must-Haves erfüllt:**
- [x] `scripts/verify-s05.sh` existiert und ist ausführbar
- [x] Exit-Code 0 beim ersten Lauf (0 Fehler — keine Nachbesserung nötig)
- [x] [1/4] 28/28 Datei-Existenz ✓
- [x] [2/4] 252/252 Sektions-Checks ✓
- [x] [3/4] 28/28 Prefix-Checks ✓
- [x] [4/4] 0 Phantom-Referenzen ✓
- [x] S05-SUMMARY.md mit allen Pflicht-Sektionen und Forward Intelligence
- [x] STATE.md zeigt S05 abgeschlossen, S06 als nächsten Slice

## Diagnostics

```bash
# Strukturierter Status-Check
bash scripts/verify-s05.sh              # Exit-Code = Fehleranzahl, 0 = alles grün

# Sektions-Check für einzelnen Skill
grep -E "^## " skills/research/elvis-ai-research.md

# Failure-Indikator Vollständigkeit
grep "Failure-Indikator:" skills/research/*.md skills/strategy/*.md

# Phantom-Referenz-Inspektion (manuell für Fließtext-Referenzen)
grep -rE "elvis-[a-z-]+" skills/research/ skills/strategy/ | grep "Abhängigkeiten"

# verify-s05.sh ist von S09 referenzierbar:
bash scripts/verify-s05.sh 2>&1 | grep "✗"  # nur Fehler-Zeilen
```

## Deviations

Keine. Alle 28 Skills aus T01–T04 entsprachen beim ersten `verify-s05.sh`-Lauf bereits den Anforderungen. Exit-Code 0 ohne Nachbesserung.

## Known Issues

- **Phantom-Check prüft nur ## Abhängigkeiten-Block:** Referenzen im Fließtext (z.B. in "Empfohlene Vorgänger-Skills" oder ## Strategie) werden nicht maschinell validiert. Alle S05-Skills halten die Dependency-Whitelist manuell ein — aber der automatische Schutz fehlt. Identisches Known Issue wie S04.
  - **Konsequenz für S06:** Skills dürfen S07/S08-Referenzen in Fließtext einschmuggeln ohne Fehler — manuelle Disziplin erforderlich.
- **verify-s05.sh prüft nicht Failure-Indikator-Vollständigkeit:** Check [2/4] verifiziert nur das Vorhandensein der 9 Pflicht-Sektionen, nicht den Inhalt (z.B. ob Failure-Indikator tatsächlich eine konkrete Schwelle enthält). Manuelle Stichproben in T01–T04 bestätigen Vollständigkeit.

## Files Created/Modified

**Research Skills (14):**
- `skills/research/elvis-ai-research.md` — KI-Recherche, 5 Prompt-Templates, Relevanz-Score 1–5
- `skills/research/elvis-opportunity-finder.md` — Opportunity-Scoring 5×4, Score 4–20
- `skills/research/elvis-trend-analyzer.md` — 12-Wochen-Trend-Analyse, 3 Reifegrad-Stufen
- `skills/research/elvis-source-validator.md` — 4-Dimensionen-Validierung, Score 1–5
- `skills/research/elvis-competitor-deep-dive.md` — 8-Dimensionen-Tiefenanalyse, 90-Punkte-Bericht
- `skills/research/elvis-audience-research.md` — 20 Pain Points, 5 Segmente, 3 Buying-Trigger
- `skills/research/elvis-keyword-researcher.md` — 30 Keywords, 3 Absichts-Kategorien
- `skills/research/elvis-pain-point-finder.md` — 30–40 Roh-Pain-Points → Top-10 priorisiert
- `skills/research/elvis-research-synthesizer.md` — Synthese-Matrix 4×N, 3 Schlussfolgerungen
- `skills/research/elvis-expert-finder.md` — 10 Experten × 5 Vertrauenskriterien
- `skills/research/elvis-case-study-analyzer.md` — 3 Cases × 6 Dimensionen, Muster-Extraktion
- `skills/research/elvis-data-collector.md` — 15 Datenpunkte × 3 Quellen-Typen
- `skills/research/elvis-problem-explorer.md` — 5×Why-Iterationen, Problem-Karte 3 Ebenen
- `skills/research/elvis-insight-extractor.md` — 5 Kerninsights, Handlungsrelevanz-Score 1–10

**Strategy Skills (14):**
- `skills/strategy/elvis-growth-strategy.md` — 90-Tage-Plan, 3 Wachstums-Hebel
- `skills/strategy/elvis-positioning-strategy.md` — 4-Dimensionen-Matrix, Differenzierungs-Statement
- `skills/strategy/elvis-content-strategy.md` — 12-Wochen-Rahmen, 5 Themen-Säulen
- `skills/strategy/elvis-go-to-market.md` — 7-Wochen-GTM-Plan
- `skills/strategy/elvis-platform-strategy.md` — Plattform-Scoring 5 Kriterien
- `skills/strategy/elvis-risk-assessment.md` — RPS-Formel, Top-5 Risiken
- `skills/strategy/elvis-competitive-strategy.md` — 3 Wettbewerbs-Positionen
- `skills/strategy/elvis-decision-framework.md` — 5-Kriterien-Matrix, 3 Alternativen
- `skills/strategy/elvis-prioritization-engine.md` — ICE-Score, Top-10 Liste
- `skills/strategy/elvis-scenario-planner.md` — 3 Szenarien × 5 Trigger
- `skills/strategy/elvis-okr-planner.md` — 3 Objectives × 3–5 KRs, Quartal-Rahmen
- `skills/strategy/elvis-pivot-advisor.md` — 5 Pivot-Signale, 30-Tage-Pivot-Plan
- `skills/strategy/elvis-resource-allocator.md` — 100%-Verteilung, 5 Allokations-Kategorien
- `skills/strategy/elvis-monetization-strategy.md` — Portfolio-Logik, CLV-Formel

**Verifikations-Infrastruktur:**
- `scripts/verify-s05.sh` — 4 Check-Gruppen, Exit-Code = Fehleranzahl, ausführbar

## Forward Intelligence

### (a) Was S06 über S05-Skills wissen muss

S06 (Automation Skills) darf alle 28 S05-Skills sowie alle 28 S04-Skills und 11 S01-Benchmark-Skills referenzieren. Die vollständige erlaubte Referenz-Whitelist für S06:

**Research-Skills (referenzierbar ab S06):**
`elvis-ai-research`, `elvis-opportunity-finder`, `elvis-trend-analyzer`, `elvis-source-validator`, `elvis-competitor-deep-dive`, `elvis-audience-research`, `elvis-keyword-researcher`, `elvis-pain-point-finder`, `elvis-research-synthesizer`, `elvis-expert-finder`, `elvis-case-study-analyzer`, `elvis-data-collector`, `elvis-problem-explorer`, `elvis-insight-extractor`

**Strategy-Skills (referenzierbar ab S06):**
`elvis-growth-strategy`, `elvis-positioning-strategy`, `elvis-content-strategy`, `elvis-go-to-market`, `elvis-platform-strategy`, `elvis-risk-assessment`, `elvis-competitive-strategy`, `elvis-decision-framework`, `elvis-prioritization-engine`, `elvis-scenario-planner`, `elvis-okr-planner`, `elvis-pivot-advisor`, `elvis-resource-allocator`, `elvis-monetization-strategy`

### (b) Was fragil ist

1. **Phantom-Check-Lücke (Fließtext):** Der Phantom-Check in verify-s05.sh (und verify-s04.sh) prüft nur den `## Abhängigkeiten`-Block per `awk '/^## Abhängigkeiten/,/^## /'`. Referenzen in anderen Sektionen (## Strategie, ## Beschreibung, ## Ausführungsschritte) werden **nicht** validiert. S05-Skills sind manuell konform — kein automatischer Schutz.

2. **Failure-Indikator-Inhalts-Check fehlt:** verify-s05.sh Check [2/4] prüft nur ob `## Verifikation` existiert, nicht ob eine Zeile `Failure-Indikator:` mit konkreter Schwelle vorhanden ist. Falls ein zukünftiger Skill die Sektion ohne Failure-Indikator anlegt, wird es nicht erkannt.

3. **Differenzierungs-Notizen in Beschreibung:** Die semantische Abgrenzung zwischen ähnlichen Skills (z.B. elvis-content-strategy vs. elvis-content-calendar aus S04) ist nur in den Beschreibungs-Texten dokumentiert — kein maschinenlesbarer Mechanismus. Ein Agent ohne Kontext könnte die falschen Skills für Aufgaben wählen.

### (c) Referenz-Whitelist für S06

S06 darf referenzieren:
- `skills/research/elvis-*.md` — alle 14 oben gelisteten Research-Skills ✓
- `skills/strategy/elvis-*.md` — alle 14 oben gelisteten Strategy-Skills ✓
- `skills/growth/elvis-*.md` — alle 14 S04-Growth-Skills ✓
- `skills/content/elvis-*.md` — alle 14 S04-Content-Skills ✓
- `skills/research/elvis-market-scan.md` — S01-Benchmark ✓
- `skills/strategy/elvis-execution-plan.md` — S01-Benchmark ✓
- `skills/automation/elvis-workflow-builder.md` — S01-Benchmark ✓
- `skills/meta/elvis-skill-generator.md` — S01-Benchmark ✓

S06 darf **nicht** referenzieren:
- `skills/automation/elvis-*` (außer workflow-builder) — noch nicht vorhanden
- `skills/meta/elvis-*` (außer skill-generator) — noch nicht vorhanden
- Sonstige Skills aus S07 oder S08

### (d) Forward References aus agent/*.md abgedeckt durch S05

Folgende Forward References aus `agent/` werden durch S05-Skills abgedeckt:

| Forward Reference | S05-Skill | Agent |
|---|---|---|
| `/elvis-ai-research` | `skills/research/elvis-ai-research.md` ✓ | agent/spock.md, agent/edison.md |
| `/elvis-decision-framework` | `skills/strategy/elvis-decision-framework.md` ✓ | agent/kirk.md |
| `/elvis-growth-strategy` | `skills/strategy/elvis-growth-strategy.md` ✓ | agent/garcia.md |
| `/elvis-data-analysis` | Kein direkter S05-Match (elvis-data-collector nächster Kandidat) | agent/spock.md |
| `/elvis-fact-check` | Kein direkter S05-Match (elvis-source-validator ist verwandt) | agent/spock.md |

**Noch offen (für S06–S08):**
`/elvis-rapid-response`, `/elvis-rapid-execution`, `/elvis-direct-action` → wahrscheinlich Automation-Skills (S06)
`/elvis-automation`, `/elvis-system-monitor`, `/elvis-integration`, `/elvis-system-builder` → S06
`/elvis-agent-generator`, `/elvis-skill-expander`, `/elvis-system-analyzer` → S07/S08 (Meta-Skills)
`/elvis-data-audit`, `/elvis-fact-check` → prüfen ob Research-Skill fehlt oder in S06 angesiedelt
