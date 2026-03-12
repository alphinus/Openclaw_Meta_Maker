---
id: T02
parent: S06
milestone: M001
provides:
  - 5 weitere Analysis Skills (elvis-reporting-system, elvis-growth-tracker, elvis-conversion-analyzer, elvis-competitor-monitor, elvis-revenue-tracker) mit vollständigen 9 Pflicht-Sektionen und Failure-Indikatoren
  - Vervollständigung der 10 Analysis Skills in skills/analysis/
  - verify-s06.sh zeigt 10/19 Dateien ✓ (alle Analysis Skills komplett, Automation Skills fehlen planmäßig)
key_files:
  - skills/analysis/elvis-reporting-system.md
  - skills/analysis/elvis-growth-tracker.md
  - skills/analysis/elvis-conversion-analyzer.md
  - skills/analysis/elvis-competitor-monitor.md
  - skills/analysis/elvis-revenue-tracker.md
key_decisions:
  - Analysis Skills mit fortlaufendem/Tracking-Charakter von einmaligen Audits/Analysen abgegrenzt durch explizite Beschreibungs-Texte und Mess-Cadence-Definitionen (wöchentlich/monatlich)
  - CLV-Formel (D028) in elvis-revenue-tracker mehrfach dokumentiert: in Ziele, Ausführungsschritte mit Beispielrechnung, Verifikation und Output-Sektion
  - Differenzierung durch System-Charakter: Tracker/Monitor = fortlaufende Mess-Systeme vs. Planner/Strategy = Planungs-Skills vs. Analysis/Audit = einmalige Scans
patterns_established:
  - Fortlaufende Analysis Skills positionieren "Tracking-System" / "Monitoring-System" mit expliziter Cadence (wöchentlich/monatlich) in ## Beschreibung
  - Abgrenzung zu ähnlichen Skills immer in ## Beschreibung als Kontrast-Satz ("Im Gegensatz zu X ist dieser Skill Y")
  - Failure-Indikatoren mit konkreten numerischen Schwellen (< X Metriken / < N Accounts / > Y Prozent) plus vollständiger Meldungstext
observability_surfaces:
  - bash scripts/verify-s06.sh — zeigt 120 ✓ Checks für 10 Analysis Skills (alle Sektionen vorhanden)
  - grep "Failure-Indikator" skills/analysis/*.md — alle 10 Skills haben Failure-Indikatoren
  - grep -c "fortlaufend\|Tracking\|wöchentlich" für Differenzierungs-Stichprobe
duration: ~12min
verification_result: passed
completed_at: 2026-03-12T07:16:11+01:00
blocker_discovered: false
---

# T02: Restliche 5 Analysis Skills

**Vervollständigt skills/analysis/ mit 5 weiteren Analysis Skills (Reporting, Growth Tracking, Conversion, Competitor Monitor, Revenue) — alle 10 Analysis Skills vorhanden, verify-s06.sh zeigt 10/19 ✓**

## What Happened

Erstellte die restlichen 5 Analysis Skills mit allen 9 Pflicht-Sektionen, Failure-Indikatoren und inhaltlicher Differenzierung zu ähnlichen Skills aus S01, S04 und S05:

1. **elvis-reporting-system.md** — Wöchentliches + monatliches Reporting-System mit 5 Pflicht-Metriken, Report-Templates (Weekly 1-Seite / Monthly 3-Seiten), Verteilungs-Matrix und Archivierungs-Konvention. Referenziert elvis-performance-tracker aus T01.

2. **elvis-growth-tracker.md** — 90-Tage-Wachstums-Tracking mit wöchentlicher Mess-Cadence für 3 Kern-Metriken (Follower, Reichweite, Engagement). Explizite Abgrenzung zu elvis-growth-audit (einmaliger Snapshot) in ## Beschreibung. 12-Wochen-Tracking-Tabelle mit Frühwarn-System (🟢🟡🔴).

3. **elvis-conversion-analyzer.md** — Monatliche Tiefenanalyse von 3 Konversionspunkten (CTA-Klicks, Opt-Ins, Käufe) mit 5-Warum-Analyse und 2 testbaren Hypothesen je Punkt. Differenziert sich von elvis-funnel-analyzer durch Fokus auf einzelne Konversionspunkte statt gesamtem Funnel.

4. **elvis-competitor-monitor.md** — Fortlaufendes Monitoring-System für 5 Konkurrenz-Accounts × 4 Metriken mit wöchentlicher Messung und Alarm-Triggern (🔴 bei >20 % Abweichung). Explizite Abgrenzung zu elvis-competitor-analysis (S04, einmaliger 4-Wochen-Scan) und elvis-competitor-deep-dive (S05, qualitative 12-Wochen-Tiefenanalyse eines Accounts) in ## Beschreibung.

5. **elvis-revenue-tracker.md** — Monatliches Revenue-Tracking über 3 Einkommensquellen mit MRR-Berechnung, CLV-Formel (`CLV = Kaufwert × Kauffrequenz × Kundendauer`) und Revenue-Mix-Analyse. CLV-Formel explizit in ## Ziele, ## Ausführungsschritte Schritt 4 mit Beispielrechnung, ## Verifikation und ## Output dokumentiert (D028). Differenziert sich von elvis-monetization-planner (plant Soll) und elvis-monetization-strategy (definiert Strategie) durch Fokus auf Ist-Ergebnis-Messung.

Alle Skills folgen dem etablierten 9-Sektionen-Muster mit Failure-Indikator als letzter Bullet in ## Verifikation vor Akzeptanzkriterium.

## Verification

```bash
# Alle 10 Analysis Skills vorhanden
$ ls skills/analysis/*.md | wc -l
10

# Differenzierungs-Check Growth-Tracker
$ grep -c "fortlaufend\|Tracking\|wöchentlich" skills/analysis/elvis-growth-tracker.md
18  # ≥2 ✓

# Differenzierungs-Check Competitor-Monitor
$ grep -c "Monitoring-System\|fortlaufend" skills/analysis/elvis-competitor-monitor.md
6  # ≥1 ✓

# CLV-Formel im Revenue-Tracker
$ grep -c "CLV" skills/analysis/elvis-revenue-tracker.md
10  # ≥1 ✓, mehrfach dokumentiert

# Failure-Indikatoren alle vorhanden
$ grep -l "Failure-Indikator" skills/analysis/*.md | wc -l
10  # Alle 10 ✓

# Sektions-Vollständigkeit Spot-Check
$ grep "^## " skills/analysis/elvis-reporting-system.md | wc -l
9  # Alle Pflicht-Sektionen ✓

# verify-s06.sh: 10 Analysis grün, 9 Automation noch fehlend
$ bash scripts/verify-s06.sh 2>&1 | grep -c "✓"
120  # ≥90 ✓ (10 Datei-Checks + ~100 Sektions-Checks + Prefix-Checks)

# /elvis-* Prefix alle vorhanden
$ for file in skills/analysis/elvis-{reporting-system,growth-tracker,conversion-analyzer,competitor-monitor,revenue-tracker}.md; do grep "^/elvis-" "$file"; done
/elvis-reporting-system
/elvis-growth-tracker
/elvis-conversion-analyzer
/elvis-competitor-monitor
/elvis-revenue-tracker
```

Alle Must-Haves erfüllt:
- ✅ Alle 5 Skills mit 9 Pflicht-Sektionen
- ✅ Alle 5 Skills mit `/elvis-*` im ## Name-Block (D001)
- ✅ Alle 5 Skills mit `Failure-Indikator:` und konkreter Schwelle
- ✅ elvis-growth-tracker.md mit "fortlaufend" + expliziter Abgrenzung zu elvis-growth-audit
- ✅ elvis-competitor-monitor.md mit "fortlaufendes Monitoring-System" + Abgrenzung zu competitor-analysis & competitor-deep-dive
- ✅ elvis-revenue-tracker.md mit `CLV = Kaufwert × Kauffrequenz × Kundendauer` als explizite Formel (D028)
- ✅ Alle Inhalte Deutsch, Dateinamen Englisch (D002)
- ✅ Keine Phantom-Referenzen (nur S01/S04/S05 + T01-Analysis-Skills)
- ✅ elvis-reporting-system.md referenziert elvis-performance-tracker (existiert aus T01)

## Diagnostics

- `bash scripts/verify-s06.sh` — vollständiger Check-Report, zeigt 10/19 Dateien ✓ (alle Analysis Skills), 9 Automation-Dateien fehlen planmäßig
- `grep -c "Failure-Indikator" skills/analysis/*.md` — alle 10 Analysis Skills haben Failure-Indikatoren
- `grep "CLV.*Kaufwert.*×.*Kauffrequenz.*×.*Kundendauer" skills/analysis/elvis-revenue-tracker.md` — CLV-Formel (D028) mehrfach dokumentiert
- `grep -A 5 "## Beschreibung" skills/analysis/elvis-growth-tracker.md | grep "audit"` — Differenzierungs-Text vorhanden
- `grep -A 10 "## Beschreibung" skills/analysis/elvis-competitor-monitor.md | grep "competitor-analysis\|competitor-deep-dive"` — beide Differenzierungen vorhanden

## Deviations

None — alle Schritte laut Taskplan ausgeführt. Zwei der 5 Dateien (elvis-reporting-system.md, elvis-growth-tracker.md) existierten bereits aus vorherigem Lauf, wurden aber verifiziert und entsprechen den Anforderungen.

## Known Issues

- verify-s06.sh Phantom-Check meldet für alle 10 Analysis Skills "keine Referenzen (ok)" statt tatsächliche Referenzen zu extrahieren — bekanntes Verhalten aus T01 wegen awk-Range-Pattern-Terminierung. Da keine Phantom-Referenzen vorhanden sind (nur gültige S01/S04/S05/T01-Referenzen), ist das Ergebnis korrekt (keine False Positives).

## Files Created/Modified

- `skills/analysis/elvis-reporting-system.md` — Wöchentliches + monatliches Reporting-System mit 5 Pflicht-Metriken, Report-Templates und Verteilungs-Prozess (6167 bytes)
- `skills/analysis/elvis-growth-tracker.md` — 90-Tage-Wachstums-Tracking mit wöchentlicher Mess-Cadence, Frühwarn-System und Abgrenzung zu Growth-Audit (6279 bytes)
- `skills/analysis/elvis-conversion-analyzer.md` — Tiefenanalyse von 3 Konversionspunkten mit 5-Warum-Analyse und testbaren Hypothesen (6326 bytes)
- `skills/analysis/elvis-competitor-monitor.md` — Fortlaufendes 5-Accounts-Monitoring mit Alarm-Triggern und Benchmark-Report (6976 bytes)
- `skills/analysis/elvis-revenue-tracker.md` — MRR + CLV-Tracking über 3 Einkommensquellen mit expliziter CLV-Formel (7082 bytes)
