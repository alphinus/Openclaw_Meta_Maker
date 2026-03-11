---
estimated_steps: 7
estimated_files: 7
---

# T02: Growth Skills 1–7 erstellen

**Slice:** S04 — Growth + Content Skills (~30 Skills)
**Milestone:** M001

## Description

Die erste Hälfte der Growth Skills erstellen — von Trend-Scanner bis Engagement-Booster. Qualitäts-Benchmark ist `skills/growth/elvis-growth-audit.md` aus S01: konkrete Mengen (Top-20, 14 Tage, 10 Hypothesen), explizite Formate (Markdown-Tabelle mit N Spalten), Failure-Indikator in Verifikation. Jeder Skill muss mindestens so konkret sein wie dieser Benchmark.

Die 7 Skills bilden den Beginn der Growth-Kette: niche-finder und audience-builder (Einstieg), competitor-analysis (externe Analyse), posting-schedule und profile-optimizer (Konto-Optimierung), viral-formula und engagement-booster (Wachstums-Mechanismen).

**Abhängigkeits-Regelwerk für diese 7 Skills (nur folgende Vorgänger erlaubt):**
- Andere Skills aus dieser Gruppe (falls bereits erstellt)
- S01-Skills: `elvis-growth-audit`, `elvis-x-hook-writer`, `elvis-market-scan`, `elvis-execution-plan`, `elvis-workflow-builder`, `elvis-skill-generator`
- `"keine (Einstiegs-Skill)"` wenn keine echte Abhängigkeit besteht

## Steps

1. **elvis-x-trend-scanner.md** — Scannt Nischen-Trends auf X der letzten 48 Stunden. Ausführungsschritte: (1) 10 Nischen-Keywords definieren, (2) Top-20 Posts pro Keyword abrufen (48h-Zeitfenster), (3) Trending-Topics aus Überschneidungen extrahieren, (4) Relevanz-Score 1–5 für jedes Topic vergeben, (5) Top-10 Trend-Report als Markdown-Tabelle ausgeben. Einschränkung: max. 10 Keywords, max. 48 Stunden. Failure: Weniger als 3 Topics mit Score ≥3 → Meldung.

2. **elvis-audience-builder.md** — Definiert Zielgruppe in 5 Dimensionen. Ausführungsschritte: (1) Demografische Dimension (Alter, Berufsfeld, Standort), (2) Psychografische Dimension (Werte, Ziele, Schmerzpunkte), (3) Content-Präferenzen (Formate, Themen, Posting-Zeiten), (4) Plattform-Verhalten (Like/Repost/Reply-Ratio, Account-Typen), (5) 10 Accounts identifizieren die diese Zielgruppe bereits erreichen. Output: 5-Dimensionen-Profil + Account-Liste. Abhängigkeiten: keine (Einstiegs-Skill).

3. **elvis-competitor-analysis.md** — Analysiert 5 Konkurrenz-Accounts. Pro Account: Follower-Anzahl, Posting-Frequenz/Woche, Content-Mix (% Text / % Bild / % Thread), Top-3-Posts (Engagement-Rate), geschätztes Follower-Wachstum/Woche. Ausführungsschritte: 5 nummerierte Schritte. Output: Vergleichstabelle 5 Accounts × 5 Metriken + 3 Handlungsempfehlungen. Abhängigkeiten: elvis-audience-builder.

4. **elvis-posting-schedule.md** — Erstellt 4-Wochen-Posting-Plan. Ausführungsschritte: (1) Beste Posting-Zeiten aus Analytics (3 Zeitfenster), (2) Content-Mix definieren (5 Kategorien, %-Anteile), (3) Themen-Rotation über 4 Wochen planen, (4) Kalender-Tabelle (7 Tage × 4 Wochen = 28 Zeilen), (5) Puffer-Posts für Breaking-Topics reservieren (2/Woche). Abhängigkeiten: elvis-growth-audit, elvis-competitor-analysis.

5. **elvis-profile-optimizer.md** — Optimiert alle 7 Profil-Elemente (Name, Bio, Profilbild-Beschreibung, Header-Beschreibung, Pinned Post, Location, Website) nach 20-Punkte-Scoring. Pro Element: Ist-Zustand, Score 0–4, Optimierungs-Empfehlung (max. 2 Sätze), Beispiel-Text. Ausführungsschritte: 5 Schritte. Failure: Score < 10/20 → kritischer Optimierungsbedarf markieren.

6. **elvis-viral-formula.md** — Identifiziert Viral-Muster aus Top-5-Posts der letzten 30 Tage. Ausführungsschritte: (1) Top-5-Posts nach absoluten Impressionen abrufen, (2) Strukturelle Merkmale extrahieren (Hook-Typ, Länge, Format), (3) Emotionale Trigger identifizieren (max. 5 Kategorien), (4) 3 häufigste Viral-Muster mit Häufigkeit dokumentieren, (5) Replikations-Vorlage für jedes Muster erstellen (Template mit Platzhaltern). Abhängigkeiten: elvis-growth-audit.

7. **elvis-engagement-booster.md** — Definiert 5 tägliche Engagement-Aktionen mit Zeitbudget max. 20 Min/Tag. Aktionen: (1) Kommentieren von 3 viralen Posts in der Nische (5 Min, min. 2 Sätze je Kommentar), (2) 2 Reposts mit eigenem Kommentar (3 Min), (3) Replies auf alle eigenen Post-Kommentare (5 Min), (4) 1 strategisches Follow + Welcome-Reply (2 Min), (5) 1 Nischen-Hashtag durchsuchen + engagieren (5 Min). Output: Tages-Checkliste + Fortschritts-Tracker (Tabelle 7 Tage × 5 Aktionen). Abhängigkeiten: elvis-audience-builder.

## Must-Haves

- [ ] Alle 7 Dateien enthalten alle 9 Pflichtsektion-Header
- [ ] Jeder `## Ausführungsschritte`-Block hat ≥4 nummerierte Schritte
- [ ] Jeder Schritt enthält ≥1 konkrete Mengenangabe (Zahl, Zeitraum oder Zeichenlimit)
- [ ] Jede `## Verifikation`-Sektion benennt einen Failure-Indikator
- [ ] `## Abhängigkeiten` referenziert nur existierende Skills aus S01 oder dieser Gruppe
- [ ] Alle Inhalte auf Deutsch
- [ ] `/elvis-`-Prefix im `## Name`-Block jeder Datei

## Verification

- `bash scripts/verify-s04.sh 2>&1 | grep "✗" | grep -E "trend-scanner|audience-builder|competitor-analysis|posting-schedule|profile-optimizer|viral-formula|engagement-booster"` → keine ✗-Zeilen für diese 7 Skills
- `grep -l "Failure" skills/growth/elvis-x-trend-scanner.md skills/growth/elvis-audience-builder.md skills/growth/elvis-competitor-analysis.md skills/growth/elvis-posting-schedule.md skills/growth/elvis-profile-optimizer.md skills/growth/elvis-viral-formula.md skills/growth/elvis-engagement-booster.md | wc -l` → 7

## Observability Impact

- Signals added/changed: 7 neue Skill-Dateien — `bash scripts/verify-s04.sh` zeigt jetzt 7 × 9 = 63 zusätzliche ✓-Zeilen
- How a future agent inspects this: `bash scripts/verify-s04.sh` — Exit-Code sinkt von ~284 auf ~221 Fehler nach T02
- Failure state exposed: Jede fehlende Sektion pro Datei explizit in Skript-Output sichtbar

## Inputs

- `skills/growth/elvis-growth-audit.md` — Qualitäts-Benchmark: Mengenformat, Failure-Indikator-Muster, Hypothesen-Format
- `templates/skill-template.md` — Verbindliche 9-Sektionen-Struktur
- S04-RESEARCH.md Abschnitt 5.1 — Skill-Beschreibungen und Mengen-Spezifikationen
- S04-RESEARCH.md Abschnitt 6 — Abhängigkeits-Kette

## Expected Output

- `skills/growth/elvis-x-trend-scanner.md` — Top-10 Trend-Themen / 48h, Relevanz-Score 1–5
- `skills/growth/elvis-audience-builder.md` — 5-Dimensionen-Profil + 10 Referenz-Accounts
- `skills/growth/elvis-competitor-analysis.md` — 5 Accounts × 5 Metriken
- `skills/growth/elvis-posting-schedule.md` — 4-Wochen-Kalender (28 Tage)
- `skills/growth/elvis-profile-optimizer.md` — 7 Elemente × 20-Punkte-Scoring
- `skills/growth/elvis-viral-formula.md` — 3 Viral-Muster + Replikations-Vorlage
- `skills/growth/elvis-engagement-booster.md` — 5 tägliche Aktionen + Tages-Checkliste
