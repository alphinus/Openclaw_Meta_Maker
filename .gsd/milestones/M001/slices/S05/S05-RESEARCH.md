# S05: Research + Strategy Skills (~30 Skills) — Research

**Date:** 2026-03-11

## Summary

S05 erstellt ~28 neue Skill-Dateien in zwei Kategorien: ~14 Research Skills (`skills/research/`) und ~14 Strategy Skills (`skills/strategy/`). Zusammen mit den beiden S01-Benchmark-Skills (`elvis-market-scan`, `elvis-execution-plan`) ergibt das je ~15 Skills pro Kategorie — exakt wie in der S05-Spec vorgesehen.

Das Skill-Format ist durch S01/S04 vollständig etabliert: 9 Pflicht-Sektionen, D006-konforme Ausführungsschritte (≥1 Mengenangabe pro Schritt), Failure-Indikator im Verifikations-Block, keine Phantom-Referenzen auf nicht-existierende Skills. S05 folgt diesen Mustern ohne Ausnahme.

Der größte Risikofaktor ist **Abgrenzung**: Research Skills müssen sich von den S04-Growth-Skills (`elvis-competitor-analysis`, `elvis-x-trend-scanner`) unterscheiden — durch Tiefe statt Breite und durch analytischen Fokus statt taktischer Empfehlungen. Strategy Skills müssen sich von den S04-Growth-Skills (`elvis-monetization-planner`, `elvis-posting-schedule`) durch Meta-Ebene und Langfristigkeit unterscheiden.

## Recommendation

**Vorgehen: Batch-Generierung aller 28 Skills in 4 Tasks (7 Skills/Task), analog zu S04. Ein separater Task für `verify-s05.sh` und SUMMARY.**

Die Skill-Inhalte folgen den in S04 etablierten Mustern ohne Erfindung neuer Konventionen. Die einzige S05-spezifische Entscheidung ist die Abhängigkeits-Whitelist (D021-Erweiterung): S05-Skills dürfen S01-Benchmarks, alle 28 S04-Skills und andere S05-Skills aus dieser Liste referenzieren — aber keine S06/S07-Skills.

## Don't Hand-Roll

| Problem | Bestehende Lösung | Warum nutzen |
|---------|------------------|-------------|
| Skill-Format definieren | `templates/skill-template.md` (S01) | Verbindliches 9-Sektionen-Format mit Anweisungs-Block + Beispiel |
| Beispiel für Research-Skill | `skills/research/elvis-market-scan.md` (S01 Benchmark) | Konkretheitsgrad und Struktur als Qualitäts-Benchmark |
| Beispiel für Strategy-Skill | `skills/strategy/elvis-execution-plan.md` (S01 Benchmark) | SMART-Ziele, Impact/Aufwand-Matrix als bewährtes Muster |
| Verifikations-Skript | `scripts/verify-s04.sh` (S04) | Vorlage für `verify-s05.sh` — gleiche 4 Check-Gruppen |
| Failure-Indikator-Muster | Alle 28 S04-Skills | Weichmacher-Wortliste + konkrete Schwelle + Standard-Meldungstext |

## Existing Code and Patterns

- `skills/research/elvis-market-scan.md` — Benchmark für Research: 10 Quellen × 5-Felder-Struktur, 3 belegte Erkenntnisse, Relevanz-Score 1–5, Failure-Check bei <5 Quellen. Dieses Format ist der Qualitäts-Standard für alle Research Skills.
- `skills/strategy/elvis-execution-plan.md` — Benchmark für Strategy: 3 SMART-Ziele, 2×2 Impact/Aufwand-Matrix, 30-Tage-Aktionsplan mit 10 Maßnahmen. Strategy Skills müssen mindestens diesen Konkretisierungsgrad erreichen.
- `scripts/verify-s04.sh` — Vorlage für `verify-s05.sh`. Gleiche 4 Check-Gruppen: Datei-Existenz, Sektions-Vollständigkeit (9 Sektionen × N Skills), /elvis-Prefix, Phantom-Referenz-Check.
- `skills/growth/elvis-competitor-analysis.md` — Zeigt die Grenze zwischen Growth und Research: Surface-Scan (5 Accounts × 5 Metriken in 4 Wochen). Research-Pendant `elvis-competitor-deep-dive` geht tiefer: ein Account, qualitative Muster, Content-Strategie-Analyse.
- `skills/growth/elvis-monetization-planner.md` — Zeigt die Grenze zwischen Growth und Strategy: taktisch (3 Modelle, ROI-Berechnung). Strategy-Pendant `elvis-monetization-strategy` ist meta-strategisch: Angebots-Portfolio, Preis-Positionierung, Zielgruppen-Segmentierung.

## Constraints

- **D021-Abhängigkeits-Whitelist (S05-Erweiterung):** Erlaubte Referenzen in `## Abhängigkeiten`: (a) S05-Skills aus dieser Liste, (b) S01-Benchmarks (`elvis-growth-audit`, `elvis-x-hook-writer`, `elvis-market-scan`, `elvis-execution-plan`, `elvis-workflow-builder`, `elvis-skill-generator`), (c) alle 28 S04-Skills, (d) `"keine (Einstiegs-Skill)"`. S06/S07-Skills existieren noch nicht und dürfen nicht referenziert werden.
- **D006-Konformität:** Jeder Ausführungsschritt enthält mindestens 1 Mengenangabe (Zahl, Zeitraum, Zeichenlimit oder Tabellenformat). Kein abstrakt-vager Step wie "analysiere den Markt".
- **D002 (Deutsch):** Alle Inhalte auf Deutsch; Dateinamen und technische Begriffe englisch.
- **Phantom-Referenz-Schutz:** Der Phantom-Check in `verify-s05.sh` prüft nur den `## Abhängigkeiten`-Block. Referenzen im Fließtext werden nicht validiert — manuelle Disziplin: Nur existierende Skills im Fließtext nennen.
- **Failure-Indikator Pflicht:** Jeder Skill enthält im `## Verifikation`-Block einen `Failure-Indikator:` mit konkreter Schwelle und Standard-Meldungstext.
- **9 Sektionen strikt:** Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output — alle 9 Pflicht-Header exakt wie im verify-Skript erwartet.

## Skill-Inventar (28 neue Dateien)

### Research Skills (14 neue + 1 bestehend = ~15 total)

| # | Dateiname | Kurzbeschreibung | Differenzierung |
|---|-----------|-----------------|-----------------|
| R01 | `elvis-ai-research.md` | KI-gestützte Recherche: Prompt-Templates für strukturierte Datenerhebung | Neu: Methodologie für KI als Recherche-Tool |
| R02 | `elvis-opportunity-finder.md` | Unbesetzte Marktlücken finden: 5 Gaps aus 3 Quellentypen | Neu: Gap-Analyse statt bestehenden Markt beschreiben |
| R03 | `elvis-trend-analyzer.md` | Tiefgehende Trend-Analyse: Ursachen, Reife, 6-Monate-Prognose für 3 Trends | Tiefer als `elvis-x-trend-scanner` (nur X/Twitter, Surface); multi-platform, kausal |
| R04 | `elvis-source-validator.md` | Quellen-Qualitätsprüfung: 5-Kriterien-Scoring (Autorität, Aktualität, Methodik, Belege, Bias) | Neu: Qualitätskontrolle für Research-Outputs |
| R05 | `elvis-competitor-deep-dive.md` | Einzel-Konkurrenten-Tiefenanalyse: Content-Strategie, Positioning, Funnel, 12-Wochen-Analyse | Tiefer als `elvis-competitor-analysis` (5 Accounts × 5 Metriken, Surface) |
| R06 | `elvis-audience-research.md` | Qualitative Zielgruppen-Recherche: Forum-/Kommentar-Analyse, 20 Pain Points, 5 Job-to-be-done | Tiefer als `elvis-audience-builder` (quantitative Profile + Referenz-Accounts) |
| R07 | `elvis-keyword-researcher.md` | Keyword-Recherche: 30 relevante Keywords/Themen, Volumen-Schätzung, Content-Prioritäten | Neu: SEO/Content-Discovery-Fokus |
| R08 | `elvis-pain-point-finder.md` | Schmerzen der Zielgruppe kartieren: 10 Pain Points × 3 Ebenen (oberflächlich/tief/latent) | Tiefer als `elvis-audience-research`; spezifischer Fokus auf Problemtiefe |
| R09 | `elvis-research-synthesizer.md` | 3–5 Reports/Recherchen zu einem Insight-Brief verdichten | Neu: Meta-Recherche, kombiniert Outputs anderer Research-Skills |
| R10 | `elvis-expert-finder.md` | Top-10 Experten/Thought Leaders in einer Nische: Qualifikations-Score + Kontakt-Ansatz | Neu: Netzwerk- und Referenz-Recherche |
| R11 | `elvis-case-study-analyzer.md` | 3 Erfolgs-Case-Studies analysieren: Kontext, Taktiken, Metriken, übertragbare Muster | Neu: Lern-aus-anderen-Fokus |
| R12 | `elvis-data-collector.md` | Strukturierte Daten aus 5 Quelltypen erheben: Tabellen-Format, Vollständigkeits-Check | Neu: Rohdaten-Erhebungs-Skill vor Analyse |
| R13 | `elvis-problem-explorer.md` | Problemraum kartieren: 5-Warum-Analyse, 3 Problemebenen, 10 Sub-Probleme | Neu: Problem-Definition vor Lösungssuche |
| R14 | `elvis-insight-extractor.md` | Rohdaten in Erkenntnisse umwandeln: Muster-Erkennung aus mindestens 3 Datenpunkten, Priorisierungs-Matrix | Neu: Analyse-Skill nach Daten-Sammlung |

### Strategy Skills (14 neue + 1 bestehend = ~15 total)

| # | Dateiname | Kurzbeschreibung | Differenzierung |
|---|-----------|-----------------|-----------------|
| S01 | `elvis-growth-strategy.md` | Meta-Wachstumsstrategie: 3 Horizonte (30/90/365 Tage), Haupt-Kanal, Neben-Kanäle | Meta-Ebene über Taktiken; `elvis-growth-audit` ist Ist-Analyse, dies ist Soll-Strategie |
| S02 | `elvis-positioning-strategy.md` | Differenzierung in der Nische: 5-Dimensionen-Map, USP, Positionierungs-Statement | Neu: W
