# S04: Growth + Content Skills (~30 Skills)

**Goal:** 28 neue Skill-Dateien erstellen (14 Growth + 14 Content), vollständig nach dem 9-Sektionen-Format, D006-konform, auf Deutsch — sodass `bash scripts/verify-s04.sh` mit Exit-Code 0 beendet.
**Demo:** `bash scripts/verify-s04.sh` → alle 4 Check-Gruppen grün (Datei-Existenz, Sektions-Vollständigkeit, /elvis-Prefix, Keine Phantomreferenzen). Stichproben-Prüfung: 3 Growth + 3 Content Skills enthalten pro Ausführungsschritt mindestens eine konkrete Mengenangabe.

## Must-Haves

- `scripts/verify-s04.sh` existiert und prüft alle 4 Check-Gruppen mit Fehlerzähler als Exit-Code (D014)
- 14 neue Growth Skills in `skills/growth/` — alle 9 Pflichtfelder befüllt
- 14 neue Content Skills in `skills/content/` — alle 9 Pflichtfelder befüllt
- Alle 28 Skills enthalten `/elvis-` im `## Name`-Block (R006)
- Alle `## Abhängigkeiten`-Sektionen referenzieren nur existierende Skills (keine Phantomreferenzen)
- Alle Inhalte auf Deutsch (R011)
- Jeder `## Ausführungsschritte`-Block hat mindestens 4 nummerierte Schritte, jeder mit mindestens einer Mengenangabe (D006, R003)
- `## Verifikation` jedes Skills benennt einen Failure-Indikator (Muster aus elvis-growth-audit.md)

## Proof Level

- This slice proves: contract (Datei-Existenz + Sektion-Vollständigkeit + Format-Konformität)
- Real runtime required: nein (reine Markdown-Dateien)
- Human/UAT required: ja — manuelle Stichproben-Prüfung auf D006-Konformität (3+3 Skills)

## Verification

```bash
bash scripts/verify-s04.sh
# Erwartetes Ergebnis: Exit-Code 0
# Check-Gruppen:
# [1/4] 28 neue Skill-Dateien vorhanden (14 Growth + 14 Content)
# [2/4] 252 Sektions-Checks (28 × 9 Pflichtfelder)
# [3/4] 28 /elvis-* Prefix-Checks
# [4/4] Abhängigkeits-Phantomreferenz-Check (alle genannten Skills existieren als Dateien)
```

**Manuelle Stichproben (T06):**
- Je 3 Growth + 3 Content Skills: jeden `## Ausführungsschritte`-Block auf ≥4 nummerierte Schritte mit ≥1 Mengenangabe prüfen
- Je 3 + 3 Skills: `## Verifikation`-Block auf expliziten Failure-Indikator prüfen

## Observability / Diagnostics

- Runtime signals: none (Markdown-Dateien, kein Code)
- Inspection surfaces: `bash scripts/verify-s04.sh` — strukturierter Check-Report mit ✓/✗ pro Datei/Sektion; Exit-Code = Fehleranzahl
- Failure visibility: Fehlerzähler im Skript-Output zeigt genau welche Datei/Sektion fehlt
- Redaction constraints: none

## Integration Closure

- Upstream surfaces consumed: `templates/skill-template.md` (S01), `skills/growth/elvis-growth-audit.md` (S01 Benchmark), `skills/content/elvis-x-hook-writer.md` (S01 Benchmark)
- New wiring introduced in this slice: Cross-Referenzen zwischen Growth und Content Skills via `## Abhängigkeiten`
- What remains before the milestone is truly usable end-to-end: S05 (Research/Strategy), S06 (Automation/Analysis), S07 (Meta-Agent Skills), S08 (Command System), S09 (Integration + README)

## Tasks

- [x] **T01: verify-s04.sh schreiben + Initial-Lauf** `est:20m`
  - Why: Objektive Stopping-Condition definieren bevor Skills erstellt werden; Fehlerzähler als Exit-Code (D014); setzt die erwartete Fehleranzahl ~284 für den Baseline-Lauf
  - Files: `scripts/verify-s04.sh`
  - Do: Skript mit 4 Check-Gruppen schreiben: (1) Existenz aller 28 neuen Dateien, (2) 9 Pflichtsektion-Header in jeder Datei, (3) `/elvis-`-Prefix im `## Name`-Block, (4) Phantomreferenz-Check. Initiales Ausführen → erwartete ~284 Fehler dokumentieren.
  - Verify: `bash scripts/verify-s04.sh; echo "Exit: $?"` → Exit-Code > 0 (erwartete Fehler), Skript läuft ohne Bash-Fehler durch
  - Done when: `scripts/verify-s04.sh` existiert, ist ausführbar, gibt strukturierten Output mit ✓/✗ pro Datei aus und endet mit Fehlerzähler als Exit-Code

- [x] **T02: Growth Skills 1–7 erstellen** `est:60m`
  - Why: Die erste Hälfte der Growth Skills — Trend-Scanner bis Engagement-Booster; aufbauend auf elvis-growth-audit.md als Qualitäts-Benchmark; Abhängigkeits-Kette beginnt hier (niche-finder → audience-builder → competitor-analysis)
  - Files: `skills/growth/elvis-x-trend-scanner.md`, `skills/growth/elvis-audience-builder.md`, `skills/growth/elvis-competitor-analysis.md`, `skills/growth/elvis-posting-schedule.md`, `skills/growth/elvis-profile-optimizer.md`, `skills/growth/elvis-viral-formula.md`, `skills/growth/elvis-engagement-booster.md`
  - Do: Jeden Skill mit allen 9 Sektionen erstellen. Jeder `## Ausführungsschritte`-Block: ≥4 nummerierte Schritte, je ≥1 Mengenangabe (Zahlen, Zeiträume, Zeichenlimits). `## Verifikation` mit Failure-Indikator. `## Abhängigkeiten` nur auf existierende S01/S04-Skills verweisen. Alle Inhalte Deutsch.
  - Verify: `bash scripts/verify-s04.sh 2>&1 | grep -E "✗|✓" | grep -E "trend-scanner|audience-builder|competitor-analysis|posting-schedule|profile-optimizer|viral-formula|engagement-booster"` → alle 7 × 9 = 63 Sektions-Checks ✓
  - Done when: Alle 7 Dateien existieren, `bash scripts/verify-s04.sh` zeigt für diese 7 Skills nur ✓

- [x] **T03: Growth Skills 8–14 erstellen** `est:60m`
  - Why: Die zweite Hälfte der Growth Skills — Follower-Analyse bis X-Analytics; schließt die Growth-Kette (growth-sprint → growth-loop → x-analytics); follower-analysis und niche-finder stehen am Anfang der Kette
  - Files: `skills/growth/elvis-follower-analysis.md`, `skills/growth/elvis-niche-finder.md`, `skills/growth/elvis-collab-strategy.md`, `skills/growth/elvis-monetization-planner.md`, `skills/growth/elvis-growth-sprint.md`, `skills/growth/elvis-growth-loop.md`, `skills/growth/elvis-x-analytics.md`
  - Do: Jeden Skill mit allen 9 Sektionen erstellen. Abhängigkeits-Kette abbilden: elvis-growth-sprint referenziert elvis-posting-schedule + elvis-engagement-booster; elvis-growth-loop referenziert elvis-growth-sprint; elvis-x-analytics referenziert elvis-growth-audit. Mengenangaben: niche-finder = 5 Nischen × 4 Kriterien, collab-strategy = 10 Partner + 3 Formate, monetization-planner = 5 Wege + 90-Tage-Plan.
  - Verify: `bash scripts/verify-s04.sh 2>&1 | grep -E "✗|✓" | grep -E "follower-analysis|niche-finder|collab-strategy|monetization|growth-sprint|growth-loop|x-analytics"` → alle 7 × 9 = 63 Sektions-Checks ✓
  - Done when: Alle 7 Dateien existieren, `bash scripts/verify-s04.sh` zeigt für alle 14 Growth Skills nur ✓

- [x] **T04: Content Skills 1–7 erstellen** `est:60m`
  - Why: Die erste Hälfte der Content Skills — Thread-Writer bis CTA-Writer; aufbauend auf elvis-x-hook-writer.md als Qualitäts-Benchmark; Abhängigkeits-Kette: content-ideas → content-brief → thread/hook/story/how-to/opinion
  - Files: `skills/content/elvis-x-thread-writer.md`, `skills/content/elvis-content-calendar.md`, `skills/content/elvis-copywriting.md`, `skills/content/elvis-content-repurpose.md`, `skills/content/elvis-story-writer.md`, `skills/content/elvis-bio-writer.md`, `skills/content/elvis-cta-writer.md`
  - Do: Jeden Skill mit allen 9 Sektionen erstellen. Zeichenlimits explizit: x-thread-writer = 8–12 Tweets × max. 280 Zeichen; story-writer = 3-Akt × max. 280 Zeichen; bio-writer = 3 Varianten × max. 160 Zeichen; cta-writer = 5 Varianten. content-calendar = 30 Ideen in 5 Kategorien; content-repurpose = 5 Posts + 1 Thread. PAS-Prinzip für copywriting explizit als Struktur nennen.
  - Verify: `bash scripts/verify-s04.sh 2>&1 | grep -E "✗|✓" | grep -E "thread-writer|content-calendar|copywriting|content-repurpose|story-writer|bio-writer|cta-writer"` → alle 7 × 9 = 63 Sektions-Checks ✓
  - Done when: Alle 7 Dateien existieren, `bash scripts/verify-s04.sh` zeigt für diese 7 Content Skills nur ✓

- [x] **T05: Content Skills 8–14 erstellen** `est:60m`
  - Why: Die zweite Hälfte der Content Skills — Opinion-Post bis Content-Brief; schließt die Content-Kette (content-ideas → content-brief); cross-kategorie Abhängigkeiten von Growth-Skills (x-trend-scanner → content-ideas, audience-builder → content-brief)
  - Files: `skills/content/elvis-opinion-post.md`, `skills/content/elvis-how-to-writer.md`, `skills/content/elvis-content-ideas.md`, `skills/content/elvis-headline-writer.md`, `skills/content/elvis-reply-writer.md`, `skills/content/elvis-dm-writer.md`, `skills/content/elvis-content-brief.md`
  - Do: Jeden Skill mit allen 9 Sektionen erstellen. Mengenangaben: content-ideas = 20 Ideen in 4 Kategorien; headline-writer = 7 Varianten × 7 Formeln; reply-writer = 5 strategische Antworten × 5 Ziele; dm-writer = max. 3 Nachrichten × max. 150 Zeichen; opinion-post = Stance + Begründung + 2 Gegenargumente + Widerlegung. Abhängigkeiten: content-ideas referenziert elvis-x-trend-scanner (existiert nach T02); content-brief referenziert elvis-audience-builder (existiert nach T02).
  - Verify: `bash scripts/verify-s04.sh 2>&1 | grep -E "✗|✓" | grep -E "opinion-post|how-to-writer|content-ideas|headline-writer|reply-writer|dm-writer|content-brief"` → alle 7 × 9 = 63 Sektions-Checks ✓
  - Done when: Alle 7 Dateien existieren, `bash scripts/verify-s04.sh` endet mit Exit-Code 0

- [x] **T06: Verifikation + S04-SUMMARY.md** `est:20m`
  - Why: Objektiven Nachweis erbringen dass alle 4 Check-Gruppen grün sind; R003-Proof durch manuelle D006-Stichproben; S04-SUMMARY.md als Forward Intelligence für S09
  - Files: `scripts/verify-s04.sh` (final run), `.gsd/milestones/M001/slices/S04/S04-SUMMARY.md`
  - Do: `bash scripts/verify-s04.sh` → Exit-Code 0 bestätigen. Manuelle Stichproben: 3 Growth (elvis-viral-formula, elvis-growth-loop, elvis-niche-finder) + 3 Content (elvis-x-thread-writer, elvis-headline-writer, elvis-content-brief) auf D006-Konformität prüfen (≥4 Schritte, ≥1 Mengenangabe pro Schritt, Failure-Indikator). S04-SUMMARY.md nach Standard-Format schreiben mit Forward Intelligence für S05/S09.
  - Verify: `bash scripts/verify-s04.sh; echo "Exit: $?"` → "Exit: 0"; S04-SUMMARY.md existiert mit Sektionen provides/requires/key_decisions/forward_intelligence
  - Done when: Exit-Code 0, Stichproben-Check dokumentiert in S04-SUMMARY.md, STATE.md aktualisiert

## Files Likely Touched

- `scripts/verify-s04.sh`
- `skills/growth/elvis-x-trend-scanner.md`
- `skills/growth/elvis-audience-builder.md`
- `skills/growth/elvis-competitor-analysis.md`
- `skills/growth/elvis-posting-schedule.md`
- `skills/growth/elvis-profile-optimizer.md`
- `skills/growth/elvis-viral-formula.md`
- `skills/growth/elvis-engagement-booster.md`
- `skills/growth/elvis-follower-analysis.md`
- `skills/growth/elvis-niche-finder.md`
- `skills/growth/elvis-collab-strategy.md`
- `skills/growth/elvis-monetization-planner.md`
- `skills/growth/elvis-growth-sprint.md`
- `skills/growth/elvis-growth-loop.md`
- `skills/growth/elvis-x-analytics.md`
- `skills/content/elvis-x-thread-writer.md`
- `skills/content/elvis-content-calendar.md`
- `skills/content/elvis-copywriting.md`
- `skills/content/elvis-content-repurpose.md`
- `skills/content/elvis-story-writer.md`
- `skills/content/elvis-bio-writer.md`
- `skills/content/elvis-cta-writer.md`
- `skills/content/elvis-opinion-post.md`
- `skills/content/elvis-how-to-writer.md`
- `skills/content/elvis-content-ideas.md`
- `skills/content/elvis-headline-writer.md`
- `skills/content/elvis-reply-writer.md`
- `skills/content/elvis-dm-writer.md`
- `skills/content/elvis-content-brief.md`
- `.gsd/milestones/M001/slices/S04/S04-SUMMARY.md`
- `.gsd/STATE.md`
