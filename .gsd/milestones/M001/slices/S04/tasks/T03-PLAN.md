---
estimated_steps: 7
estimated_files: 7
---

# T03: Growth Skills 8–14 erstellen

**Slice:** S04 — Growth + Content Skills (~30 Skills)
**Milestone:** M001

## Description

Die zweite Hälfte der Growth Skills — von Follower-Analyse bis X-Analytics. Diese 7 Skills schließen die Growth-Kette ab: niche-finder ist der Einstiegs-Skill der Kette, follower-analysis liefert Zielgruppen-Tiefe, collab-strategy und monetization-planner bauen auf dem Wachstum auf, growth-sprint und growth-loop operationalisieren es, x-analytics misst es.

Nach T03 sind alle 14 Growth Skills vorhanden — der erste große Meilenstein für R001 und R003.

**Erlaubte Vorgänger in `## Abhängigkeiten`:**
- Alle 14 Growth Skills (T02 + T03)
- S01-Skills: `elvis-growth-audit`, `elvis-market-scan`, `elvis-execution-plan`, `elvis-workflow-builder`
- `"keine (Einstiegs-Skill)"` wenn zutreffend

## Steps

1. **elvis-follower-analysis.md** — Analysiert die 50 aktivsten Follower (definiert als: höchste Reply/Repost-Frequenz). Pro Follower: Berufsfeld-Kategorie, primäre Themen (max. 3), Account-Alter in Jahren, Engagement-Typ (Replyer, Reposter, Liker). Output: Follower-Segment-Report mit 3 Haupt-Segmenten, je Segment: Name, Größe (Anzahl von 50), Top-3-Themen, Empfehlung für Content-Ausrichtung (2 Sätze). Abhängigkeiten: elvis-audience-builder.

2. **elvis-niche-finder.md** — Bewertet 5 potenzielle Nischen nach 4 Kriterien. Kriterien: (1) Marktgröße (geschätzte Community-Accounts auf X), (2) Wettbewerbs-Intensität (Top-10 Accounts mit >10k Followern — Score 1=viele, 5=wenige), (3) Monetarisierbarkeit (Produkt/Kurs/Consulting-Potenzial — Score 1–5), (4) Expertise-Fit (eigenes Wissen 1–5). Gesamt-Score je Nische: 4–20 Punkte. Output: Scoring-Tabelle 5 × 5 + Empfehlung der Top-Nische mit Begründung. Abhängigkeiten: keine (Einstiegs-Skill).

3. **elvis-collab-strategy.md** — Identifiziert 10 Kollaborations-Partner + 3 Formate. Partner-Kriterien: Überschneidende Zielgruppe, Follower-Bereich 0,5× bis 2× der eigenen Follower-Zahl, komplementäres (nicht identisches) Thema. 3 Formate: (A) Co-Thread (je 4 Tweets), (B) Cross-Promotion (je 1 Post empfehlt den anderen), (C) gemeinsames AMA (je 5 Fragen/Antworten). Outreach-Skript für Format A: max. 3 Sätze, DM-Format. Abhängigkeiten: elvis-audience-builder, elvis-follower-analysis.

4. **elvis-monetization-planner.md** — Bewertet 5 Monetarisierungs-Wege nach Aufwand (1–5) und Ertragspotenzial (1–5). Wege: (1) Digitales Produkt (eBook/Template), (2) Online-Kurs, (3) Consulting/1:1, (4) Newsletter-Sponsoring, (5) Affiliate-Marketing. Output: 2×2-Matrix Aufwand/Ertrag + 90-Tage-Plan für den Top-Weg (Monat 1: Aufbau, Monat 2: Launch, Monat 3: Skalierung, je 3 Aktionen). Abhängigkeiten: elvis-audience-builder, elvis-niche-finder.

5. **elvis-growth-sprint.md** — 7-Tage-Intensivplan mit täglichen Aktionen, Zeitbudget und erwarteten Metriken. Pro Tag: (1) Content-Aktion (welcher Post-Typ, Zeitaufwand max. 30 Min), (2) Engagement-Aktion (welche Aktivität, max. 20 Min), (3) Analyse-Check (welche Metrik, max. 10 Min). Erwartete Metriken-Range für 7 Tage: +50–150 Impressionen/Tag, +2–10 Follower/Tag, ≥5% Engagement-Rate. Failure: Tag 3 Metriken unter 50% der Zielwerte → Strategie-Review empfehlen. Abhängigkeiten: elvis-posting-schedule, elvis-engagement-booster.

6. **elvis-growth-loop.md** — Definiert einen wiederkehrenden 7-Tage-Wachstumszyklus in 4 Phasen. Phase 1 (Tag 1–2): Analyse (elvis-growth-audit Kurzversion — Top-5 Posts, 1 Muster). Phase 2 (Tag 2–4): Produktion (3 Posts auf Basis des Musters). Phase 3 (Tag 4–6): Distribution (Engagement-Booster-Aktionen × 3 Tage). Phase 4 (Tag 7): Optimierung (Metriken-Vergleich, 1 Hypothese testen). Eintrittsvoraussetzung: Cycle beginnt erst wenn ≥2 Wochen Posting-History vorliegen. Abhängigkeiten: elvis-growth-sprint, elvis-engagement-booster, elvis-growth-audit.

7. **elvis-x-analytics.md** — Wertet 90-Tage-Analytics aus. Ausführungsschritte: (1) Follower-Wachstumskurve (wöchentliche Delta-Werte, 13 Datenpunkte), (2) Beste 3 Wochen nach Impressionen identifizieren + Ursachen benennen, (3) Engagement-Rate-Entwicklung (wöchentlicher Durchschnitt, Trend up/down/stabil), (4) Top-5 Content-Kategorien nach Engagement-Rate (Kategorien aus Posting-Schedule), (5) Wachstums-Score berechnen: (Follower-Delta 90 Tage / Ausgangs-Follower) × 100 = % Wachstum. Output: Analytics-Report mit 5 Abschnitten, max. 800 Wörter. Abhängigkeiten: elvis-growth-audit, elvis-posting-schedule.

## Must-Haves

- [ ] Alle 7 Dateien enthalten alle 9 Pflichtsektion-Header
- [ ] Jeder `## Ausführungsschritte`-Block hat ≥4 nummerierte Schritte mit ≥1 Mengenangabe
- [ ] elvis-niche-finder.md enthält 4×5 Scoring-Matrix (4 Kriterien × 5 Nischen)
- [ ] elvis-growth-loop.md enthält die 4-Phasen-Struktur mit Tages-Zuordnung
- [ ] elvis-growth-sprint.md enthält Failure-Indikator (Tag-3-Check)
- [ ] elvis-x-analytics.md enthält Wachstums-Score-Formel
- [ ] Alle `## Abhängigkeiten` referenzieren nur existierende Skills

## Verification

- `bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep -E "follower-analysis|niche-finder|collab-strategy|monetization|growth-sprint|growth-loop|x-analytics"` → keine ✗-Zeilen
- `bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep "skills/growth"` → keine ✗-Zeilen (alle 14 Growth Skills grün)

## Observability Impact

- Signals added/changed: Nach T03 zeigt `bash scripts/verify-s04.sh` alle 14 Growth Skills × 9 Sektionen = 126 ✓-Zeilen
- How a future agent inspects this: `bash scripts/verify-s04.sh` — nach T03 sollten nur noch Content-Skills-Fehler übrig sein
- Failure state exposed: Fehlende Sektionen pro Datei explizit in Output

## Inputs

- `skills/growth/elvis-growth-audit.md` — Qualitäts-Benchmark
- `skills/growth/elvis-audience-builder.md` (aus T02) — Abhängigkeit für follower-analysis, collab-strategy, monetization-planner
- `skills/growth/elvis-posting-schedule.md` (aus T02) — Abhängigkeit für growth-sprint, x-analytics
- `skills/growth/elvis-engagement-booster.md` (aus T02) — Abhängigkeit für growth-sprint, growth-loop
- S04-RESEARCH.md Abschnitt 5.1 + 6

## Expected Output

- `skills/growth/elvis-follower-analysis.md` — 50-Follower-Analyse, 3 Segmente
- `skills/growth/elvis-niche-finder.md` — 5 Nischen × 4 Kriterien, Score 4–20
- `skills/growth/elvis-collab-strategy.md` — 10 Partner + 3 Formate + Outreach-Skript
- `skills/growth/elvis-monetization-planner.md` — 5 Wege × 2 Dimensionen + 90-Tage-Plan
- `skills/growth/elvis-growth-sprint.md` — 7-Tage-Plan mit täglichen Aktionen
- `skills/growth/elvis-growth-loop.md` — 4-Phasen-Wochenzyklus
- `skills/growth/elvis-x-analytics.md` — 90-Tage-Analytics-Report (5 Abschnitte)
