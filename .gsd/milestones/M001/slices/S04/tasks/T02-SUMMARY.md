---
id: T02
parent: S04
milestone: M001
provides:
  - skills/growth/elvis-x-trend-scanner.md — Top-10 Trend-Themen / 48h, Relevanz-Score 1–5
  - skills/growth/elvis-audience-builder.md — 5-Dimensionen-Profil + 10 Referenz-Accounts
  - skills/growth/elvis-competitor-analysis.md — 5 Accounts × 5 Metriken Vergleichstabelle
  - skills/growth/elvis-posting-schedule.md — 4-Wochen-Kalender (28 Tage)
  - skills/growth/elvis-profile-optimizer.md — 7 Elemente × 20-Punkte-Scoring
  - skills/growth/elvis-viral-formula.md — 3 Viral-Muster + Replikations-Vorlagen
  - skills/growth/elvis-engagement-booster.md — 5 tägliche Aktionen + 7-Tage-Tracker
key_files:
  - skills/growth/elvis-x-trend-scanner.md
  - skills/growth/elvis-audience-builder.md
  - skills/growth/elvis-competitor-analysis.md
  - skills/growth/elvis-posting-schedule.md
  - skills/growth/elvis-profile-optimizer.md
  - skills/growth/elvis-viral-formula.md
  - skills/growth/elvis-engagement-booster.md
key_decisions:
  - elvis-profile-optimizer verwendet 7-Element × 4-Punkte Raw-Score (max 28), normiert auf 20 via Faktor 20/28 — ermöglicht ganzzahligen 20-Punkte-Score bei 7 Elementen
  - elvis-posting-schedule definiert genau 2 Puffer-Slots/Woche (fest), nicht "bis zu 2" — erzwingt explizite Kalender-Lücken
patterns_established:
  - Alle Skills enthalten Failure-Indikator mit konkreter Schwelle (z.B. "weniger als 3 Topics mit Score ≥3", "Score < 10/20", "< 70% Tracker-Felder")
  - Abhängigkeiten ausschließlich auf bestehende S01-Skills oder Skills dieser Gruppe begrenzt
  - Quantitative Constraints in Einschränkungen-Sektion (max. 10 Keywords, max. 48h, genau 5 Accounts, max. 20 Min/Tag)
observability_surfaces:
  - bash scripts/verify-s04.sh — zeigt ✓/✗ pro Datei/Sektion; Fehleranzahl als Exit-Code
duration: ~30 Minuten
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T02: Growth Skills 1–7 erstellen

**7 Growth-Skill-Dateien erstellt (elvis-x-trend-scanner bis elvis-engagement-booster) — alle 9 Pflichtsektion-Header vorhanden, alle Failure-Indikatoren gesetzt, verify-s04.sh zeigt 0 ✗-Zeilen für diese 7 Skills.**

## What Happened

Alle 7 Skill-Dateien im 9-Sektionen-Format nach Benchmark `elvis-growth-audit.md` erstellt:

1. **elvis-x-trend-scanner.md** — 10 Keywords × 20 Posts / 48h, Relevanz-Score 1–5, Top-10-Tabelle (4 Spalten). Failure: < 3 Topics mit Score ≥3.
2. **elvis-audience-builder.md** — 5 Dimensionen (Demografie, Psychografie, Content, Verhalten, Referenzen), 10 Referenz-Accounts-Tabelle (4 Spalten). Failure: < 5 Referenz-Accounts.
3. **elvis-competitor-analysis.md** — 5 Accounts × 5 Metriken (Follower, Frequenz, Content-Mix, Spitzen-Engagement, Wachstum), 3 Handlungsempfehlungen. Failure: < 3 analysierbare Konkurrenten.
4. **elvis-posting-schedule.md** — 3 Zeitfenster, 5 Content-Kategorien, 28-Tage-Kalender, 8 Puffer-Slots (2/Woche). Failure: < 20 Posts / 28 Tage.
5. **elvis-profile-optimizer.md** — 7 Profil-Elemente, 20-Punkte-Score (normiert via 7×4→20), Warnblock bei Score < 10. Failure: Score < 10 ohne Warnblock = unvollständig.
6. **elvis-viral-formula.md** — Top-5 Posts / 30 Tage, 5×5 Merkmal-Tabelle, 5 Trigger-Kategorien, 3 Muster + Replikations-Vorlagen ≤280 Zeichen. Failure: < 2 Posts teilen Muster.
7. **elvis-engagement-booster.md** — 5 Aktionen (5+3+5+2+5 Min = 20 Min exakt), Tages-Checkliste, 7×5 Fortschritts-Tracker. Failure: < 70% Tracker-Felder nach 7 Tagen.

## Verification

```
bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep -E "trend-scanner|audience-builder|competitor-analysis|posting-schedule|profile-optimizer|viral-formula|engagement-booster"
# → (keine Ausgabe) ✓

grep -l "Failure" skills/growth/elvis-x-trend-scanner.md \
  skills/growth/elvis-audience-builder.md \
  skills/growth/elvis-competitor-analysis.md \
  skills/growth/elvis-posting-schedule.md \
  skills/growth/elvis-profile-optimizer.md \
  skills/growth/elvis-viral-formula.md \
  skills/growth/elvis-engagement-booster.md | wc -l
# → 7 ✓
```

Fehleranzahl: 308 (Baseline T01) → 231 nach T02 (Reduktion 77 = 7 Dateien × 11 Checks).

## Diagnostics

- `bash scripts/verify-s04.sh` — zeigt ✓/✗ pro Datei/Sektion, 231 Restfehler (21 fehlende Dateien × 11 Checks)
- Alle 7 neuen Dateien in `skills/growth/` — alle ≥4 nummerierte Ausführungsschritte, alle mit ≥1 Mengenangabe pro Schritt

## Deviations

- elvis-profile-optimizer: Normierungs-Faktor 20/28 eingeführt (7 Elemente × 4 Punkte = 28 Roh-Maximum), weil das 20-Punkte-Scoring aus dem Plan mit 7 Elementen mathematisch nicht ohne Normierung realisierbar ist. Ergebnis trotzdem 20-Punkte-kompatibel.

## Known Issues

none

## Files Created/Modified

- `skills/growth/elvis-x-trend-scanner.md` — Top-10 Trend-Report / 48h, Relevanz-Score 1–5, 4-Spalten-Tabelle
- `skills/growth/elvis-audience-builder.md` — 5-Dimensionen-Profil, 10 Referenz-Accounts-Tabelle
- `skills/growth/elvis-competitor-analysis.md` — 5×5 Vergleichstabelle, 3 Handlungsempfehlungen
- `skills/growth/elvis-posting-schedule.md` — 28-Tage-Kalender, 5 Content-Kategorien, 8 Puffer-Slots
- `skills/growth/elvis-profile-optimizer.md` — 7 Elemente, 20-Punkte-Score, Warnblock bei < 10
- `skills/growth/elvis-viral-formula.md` — 3 Viral-Muster, 3 Replikations-Vorlagen ≤280 Zeichen
- `skills/growth/elvis-engagement-booster.md` — 20-Min-Tagesplan, 5 Aktionen, 7×5 Tracker
