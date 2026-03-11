---
estimated_steps: 7
estimated_files: 7
---

# T02: Research Skills R08–R14 erstellen

**Slice:** S05 — Research + Strategy Skills (~30 Skills)
**Milestone:** M001

## Description

Erstellt die zweiten 7 Research Skills (R08–R14): Pain Point Finder, Research Synthesizer, Expert Finder, Case Study Analyzer, Data Collector, Problem Explorer und Insight Extractor. Diese Skills bilden die "Analyse-Ebene" nach der Daten-Erhebung — sie verdichten, synthetisieren und strukturieren Research-Outputs.

`elvis-research-synthesizer` darf R01–R07-Skills aus T01 als Abhängigkeiten referenzieren (T01 muss zuerst abgeschlossen sein).

## Steps

1. Lies `skills/research/elvis-market-scan.md` und die 7 T01-Skills als Format-Referenz für Konkretheitsgrad und Failure-Indikator-Muster.
2. Erstelle `skills/research/elvis-pain-point-finder.md` — Schmerzen der Zielgruppe in 3 Ebenen kartieren: oberflächlich (bewusst, sofort genannt), tief (kontextabhängig, mit Nachfragen erkennbar), latent (unbewusst, durch Verhaltens-Analyse). Ergebnis: 10 Pain Points × 3 Ebenen-Einordnung + Häufigkeits-Score 1–5. Differenzierung von `elvis-audience-research`: spezifischer Fokus auf Problemtiefe, kein breites Zielgruppen-Profil. Failure-Indikator bei < 6 Pain Points mit allen 3 Ebenen ausgefüllt.
3. Erstelle `skills/research/elvis-research-synthesizer.md` — 3–5 bestehende Research-Outputs (z.B. aus `elvis-market-scan`, `elvis-audience-research`) zu einem Insight-Brief verdichten. Format: 5 übergreifende Erkenntnisse, 3 Widersprüche/Spannungen, 1 zentrale Handlungsempfehlung. Abhängigkeiten: `elvis-market-scan`, `elvis-audience-research` als empfohlene Vorgänger. Failure-Indikator bei < 3 Research-Inputs vorhanden.
4. Erstelle `skills/research/elvis-expert-finder.md` — Top-10 Experten/Thought Leaders in einer Nische identifizieren: Qualifikations-Score aus 4 Kriterien (Veröffentlichungen, Plattform-Reichweite, Praxis-Erfahrung, Nischen-Spezifität) je 1–5 Punkte. Pro Experte: Name, Plattform, Score, 1-Satz-Qualifikation, empfohlener Kontakt-Ansatz. Failure-Indikator bei < 5 Experten mit Score ≥ 12/20.
5. Erstelle `skills/research/elvis-case-study-analyzer.md` — 3 Erfolgs-Case-Studies analysieren: je Kontext (Ausgangssituation + Ziel), 5 eingesetzte Taktiken, 3 Metriken (vorher/nachher), 3 übertragbare Muster. Abschluss: Muster-Matrix (was ist kontextabhängig vs. universell anwendbar). Failure-Indikator bei < 2 Case Studies mit vollständigem vorher/nachher-Daten.
6. Erstelle `skills/research/elvis-data-collector.md` — Strukturierte Daten aus 5 Quelltypen erheben: (1) öffentliche Statistiken/Reports, (2) Plattform-Metriken, (3) Nutzer-Aussagen, (4) Konkurrenz-Beobachtungen, (5) Eigene Tests/Experimente. Format: Tabelle mit Spalten (Quelle, Typ, Datum, Datenpunkt, Relevanz 1–3). Vollständigkeits-Check: mindestens 3 Einträge pro Quelltyp. Failure-Indikator bei < 2 Quelltypen mit ausreichend Daten.
7. Erstelle `skills/research/elvis-problem-explorer.md` — Problemraum kartieren: 5-Warum-Analyse (5 Iterationen von "Warum?"), 3 Problemebenen (Symptom / Ursache / Systemursache), 10 Sub-Probleme als Untermenge des Haupt-Problems. Ergebnis: Problem-Map mit 3 Ebenen + Priorisierungs-Empfehlung nach Auswirkung. Failure-Indikator bei < 3 vollständigen Warum-Iterationen.
8. Erstelle `skills/research/elvis-insight-extractor.md` — Rohdaten in priorisierte Erkenntnisse umwandeln: Muster-Erkennung aus mindestens 3 Datenpunkten pro Muster, Priorisierungs-Matrix (2×2: Konfidenz × Auswirkung), Top-5 Erkenntnisse mit Handlungsrelevanz-Einschätzung. Abhängigkeit: `elvis-data-collector` als empfohlener Vorgänger. Failure-Indikator bei < 3 Datenpunkte pro behauptetes Muster.

## Must-Haves

- [ ] 7 Dateien existieren in `skills/research/`
- [ ] Jede Datei enthält genau 9 Sektionen (Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output)
- [ ] Jeder `## Name` Block enthält `/elvis-*` Prefix
- [ ] Jeder Ausführungsschritt enthält mindestens 1 konkrete Zahl, Zeitangabe oder Tabellenformat (D006)
- [ ] Jeder `## Verifikation` Block enthält `Failure-Indikator:` mit Schwelle + Standard-Meldungstext
- [ ] `elvis-research-synthesizer` referenziert nur D021-konforme Skills (`elvis-market-scan`, `elvis-audience-research` aus T01) — keine Phantom-Referenzen
- [ ] `elvis-insight-extractor` referenziert nur `elvis-data-collector` (aus diesem Task) — keine S06/S07-Referenzen

## Verification

```bash
# Datei-Existenz (7 neue Checks)
for f in elvis-pain-point-finder elvis-research-synthesizer elvis-expert-finder \
          elvis-case-study-analyzer elvis-data-collector \
          elvis-problem-explorer elvis-insight-extractor; do
  [ -f "skills/research/$f.md" ] && echo "✓ $f" || echo "✗ $f FEHLT"
done

# Gesamtzahl Research Skills
ls skills/research/*.md | wc -l  # erwartet: 15

# Sektions-Check (Stichprobe)
grep -c "^## " skills/research/elvis-research-synthesizer.md  # erwartet: 9
grep -c "^## " skills/research/elvis-insight-extractor.md  # erwartet: 9

# Phantom-Referenz-Check für research-synthesizer
awk '/^## Abhängigkeiten/,/^## /' skills/research/elvis-research-synthesizer.md | grep "elvis-"
# Darf nur: elvis-market-scan, elvis-audience-research (beide existieren)

# Failure-Indikator Vollständigkeit
grep -rl "Failure-Indikator:" skills/research/ | wc -l  # erwartet: 15
```

## Observability Impact

- Signals added/changed: None
- How a future agent inspects this: `bash scripts/verify-s05.sh` (nach T05) prüft alle 14 Research Skills; Phantom-Referenz-Check in Check-Gruppe [4/4]
- Failure state exposed: Wenn `elvis-research-synthesizer` auf nicht-existierende Skills referenziert, schlägt Check [4/4] in verify-s05.sh fehl — lokalisierbar bis auf Skill + Referenz

## Inputs

- T01-Output: 7 Research Skills (R01–R07) für Abhängigkeits-Referenzen
- `templates/skill-template.md` — verbindliches 9-Sektionen-Format
- `skills/research/elvis-market-scan.md` — Qualitäts-Benchmark
- `skills/research/elvis-audience-research.md` (aus T01) — referenzierbar in research-synthesizer

## Expected Output

- `skills/research/elvis-pain-point-finder.md` — 10 Pain Points × 3 Ebenen + Häufigkeits-Score
- `skills/research/elvis-research-synthesizer.md` — Insight-Brief aus 3–5 Research-Outputs
- `skills/research/elvis-expert-finder.md` — Top-10 Experten mit 4-Kriterien-Scoring
- `skills/research/elvis-case-study-analyzer.md` — 3 Case Studies × Kontext + Taktiken + Metriken + Muster
- `skills/research/elvis-data-collector.md` — Daten aus 5 Quelltypen in Tabellen-Format
- `skills/research/elvis-problem-explorer.md` — 5-Warum + 3 Ebenen + 10 Sub-Probleme
- `skills/research/elvis-insight-extractor.md` — Muster aus ≥3 Datenpunkten, 2×2 Priorisierungs-Matrix
