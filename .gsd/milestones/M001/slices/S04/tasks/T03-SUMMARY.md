---
id: T03
parent: S04
milestone: M001
provides:
  - skills/growth/elvis-follower-analysis.md — 50-Follower-Analyse, 3 Segmente mit Content-Empfehlung
  - skills/growth/elvis-niche-finder.md — 5 Nischen × 4 Kriterien, Score 4–20, Empfehlung + Begründung
  - skills/growth/elvis-collab-strategy.md — 10 Partner + 3 Formate + Outreach-DM-Skript (2 Varianten)
  - skills/growth/elvis-monetization-planner.md — 5 Wege × 2 Dimensionen + 2×2-Matrix + 90-Tage-Plan
  - skills/growth/elvis-growth-sprint.md — 7-Tage-Intensivplan mit Tag-3-Midpoint-Check
  - skills/growth/elvis-growth-loop.md — 4-Phasen-Wochenzyklus mit Loop-Tracker-Tabelle
  - skills/growth/elvis-x-analytics.md — 90-Tage-Analytics-Report (5 Abschnitte) + Wachstums-Score-Formel
key_files:
  - skills/growth/elvis-follower-analysis.md
  - skills/growth/elvis-niche-finder.md
  - skills/growth/elvis-collab-strategy.md
  - skills/growth/elvis-monetization-planner.md
  - skills/growth/elvis-growth-sprint.md
  - skills/growth/elvis-growth-loop.md
  - skills/growth/elvis-x-analytics.md
key_decisions:
  - elvis-niche-finder verwendet Score-Range 4–20 (nicht 0–20), damit jede Nische mindestens als "möglich" gilt — kein pauschal-Ausschluss
  - elvis-collab-strategy definiert Follower-Bereich 0,5× bis 2× als harte Grenze (nicht "ca.") — erzwingt Augenhöhe-Partnerschaften
  - elvis-growth-loop verwendet Eintrittsvoraussetzung ≥14 Posts aus 14 Tagen als explizite Gate-Bedingung mit Meldung bei Nicht-Erfüllung
  - elvis-x-analytics Wachstums-Score normiert auf Prozent (nicht absolute Zahl) — ermöglicht Vergleich über Account-Größen hinweg
patterns_established:
  - Alle 7 Skills enthalten Failure-Indikator mit konkreter Schwelle und Standard-Meldungstext
  - Abhängigkeiten verweisen ausschließlich auf bestehende S01-Skills oder T02-Growth-Skills
  - Alle Ausführungsschritte enthalten mindestens 1 Mengenangabe (50 Follower, 13 Datenpunkte, 3 Segmente, etc.)
  - 4-Phasen-Struktur (Analyse/Produktion/Distribution/Optimierung) als Zyklus-Muster etabliert
observability_surfaces:
  - bash scripts/verify-s04.sh — zeigt ✓/✗ pro Datei und Sektion; alle 14 Growth Skills zeigen ✓ (154 ✓-Zeilen für Growth)
duration: 1 session
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T03: Growth Skills 8–14 erstellen

**7 Growth-Skill-Dateien erstellt (elvis-follower-analysis bis elvis-x-analytics) — alle 9 Pflichtsektion-Header vorhanden, verify-s04.sh zeigt 0 ✗-Zeilen für alle 14 Growth Skills.**

## What Happened

Alle 7 Growth Skills der zweiten Hälfte erstellt:

- **elvis-follower-analysis.md**: Analysiert 50 aktivste Follower (Reply/Repost-Frequenz), 4-Attribut-Rohdaten-Tabelle, 3-Segment-Report mit Content-Empfehlung (je 2 Sätze). Failure-Trigger bei < 20 aktiven Followern.
- **elvis-niche-finder.md**: 5 Nischen × 4 Kriterien (Marktgröße, Wettbewerb, Monetarisierung, Expertise), Score-Range 4–20, Scoring-Tabelle 5×6, Empfehlung der Top-Nische. Einstiegs-Skill (keine Abhängigkeiten).
- **elvis-collab-strategy.md**: 20-Kandidaten-Recherche → Top-10-Partner-Tabelle (Follower-Bereich 0,5× bis 2×), 3 Formate (Co-Thread/Cross-Promotion/AMA) vollständig spezifiziert, Outreach-DM-Skript 2 Varianten (spezifisch + Vorlage, max. 3 Sätze je).
- **elvis-monetization-planner.md**: 5 Wege (Digitales Produkt, Kurs, Consulting, Newsletter-Sponsoring, Affiliate) × Aufwand/Ertrag 1–5, 2×2-Matrix (4 Quadranten), 90-Tage-Plan (3 Monate × 3 Aktionen = 9 Schritte), Break-Even-Satz.
- **elvis-growth-sprint.md**: 7-Tage-Plan mit 3-Aktionen-Tagesblöcken (Content ≤30 Min, Engagement ≤20 Min, Analyse ≤10 Min), expliziter Tag-3-Midpoint-Check mit Failure-Trigger (< 50% Zielwerte → Strategie-Review), Sprint-Abschluss-Tabelle 7×4.
- **elvis-growth-loop.md**: 4-Phasen-Zyklus (Analyse T1–2, Produktion T2–4, Distribution T4–6, Optimierung T7), je 3 Aktionen mit Zeitbudget, Eintrittsvoraussetzung ≥14 Posts/14 Tage als Gate, Loop-Tracker-Tabelle 4×5 für 4 Zyklen.
- **elvis-x-analytics.md**: 5-Abschnitte-Report (Follower-Wachstumskurve 13 Datenpunkte, beste 3 Wochen + Ursachen, Engagement-Trend, Top-5-Kategorien, Wachstums-Score), Formel explizit: (Delta/Ausgangs-Follower) × 100.

## Verification

```
bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep -E "follower-analysis|niche-finder|collab-strategy|monetization|growth-sprint|growth-loop|x-analytics"
# → keine Ausgabe (alle 7 neuen Skills: 0 ✗-Zeilen)

bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep "skills/growth"
# → keine Ausgabe (alle 14 Growth Skills grün)

bash scripts/verify-s04.sh 2>&1 | grep -c "✓"
# → 168 (14 Growth × 11 Checks + 14 Content-Platzhalter-Checks aus T02-Dateien)
```

Restfehler: 154 (14 Content Skills fehlen noch — T04+ Aufgaben).

## Diagnostics

`bash scripts/verify-s04.sh` — zeigt ✓/✗ pro Datei/Sektion. Nach T03 zeigen alle 14 Growth Skills ✓ in allen 4 Check-Gruppen. Verbleibende ✗-Zeilen betreffen ausschließlich Content Skills (`skills/content/`).

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `skills/growth/elvis-follower-analysis.md` — 50-Follower-Analyse, 3 Segmente mit Name/Größe/Top-3-Themen/Content-Empfehlung
- `skills/growth/elvis-niche-finder.md` — 5 Nischen × 4 Kriterien, Score-Tabelle 5×6, Top-Nische-Empfehlung ≤100 Wörter
- `skills/growth/elvis-collab-strategy.md` — 10 Partner-Tabelle, 3 Formate-Definitionen, Outreach-DM-Skript (2 Varianten)
- `skills/growth/elvis-monetization-planner.md` — 5 Wege × Aufwand/Ertrag, 2×2-Matrix, 90-Tage-Plan (9 Aktionen), Break-Even-Satz
- `skills/growth/elvis-growth-sprint.md` — 7-Tage-Plan, Tag-3-Midpoint-Check, Sprint-Abschluss-Tabelle 7×4
- `skills/growth/elvis-growth-loop.md` — 4-Phasen-Zyklus, Gate-Bedingung ≥14 Posts, Loop-Tracker 4×5
- `skills/growth/elvis-x-analytics.md` — 5-Abschnitte-Analytics-Report, Wachstums-Score-Formel, Follower-Kurve 13 Datenpunkte
