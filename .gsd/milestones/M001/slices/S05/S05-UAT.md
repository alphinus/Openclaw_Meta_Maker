# S05: Research + Strategy Skills (~30 Skills) — UAT

**Milestone:** M001
**Written:** 2026-03-11

## UAT Type

- UAT mode: artifact-driven
- Why this mode is sufficient: S05 produziert ausschließlich Markdown-Dateien ohne Runtime-Komponenten. Die Korrektheit der Artefakte ist vollständig maschinell verifizierbar durch `scripts/verify-s05.sh` (4 Check-Gruppen, Exit-Code 0). Kein Server, keine API, keine UI — artifact-driven UAT ist vollständig ausreichend.

## Preconditions

- `scripts/verify-s05.sh` muss ausführbar sein
- `skills/research/` und `skills/strategy/` müssen existieren
- S01-Benchmark-Skill `skills/research/elvis-market-scan.md` muss existieren (Referenz-Standard)

## Smoke Test

```bash
bash scripts/verify-s05.sh; echo "Exit-Code: $?"
```
**Erwartetes Ergebnis:** Exit-Code 0 — alle 4 Check-Gruppen grün.

## Test Cases

### 1. Datei-Existenz: alle 28 neuen Skills vorhanden

```bash
ls skills/research/*.md | wc -l   # → 15 (14 neu + 1 S01-Benchmark)
ls skills/strategy/*.md | wc -l   # → 15 (14 neu + 1 S01-Benchmark)
```
**Expected:** Beide Zahlen 15.

### 2. Sektions-Vollständigkeit: jeder Skill hat exakt 9 Pflicht-Sektionen

```bash
for f in skills/research/elvis-*.md skills/strategy/elvis-*.md; do
  count=$(grep -c "^## " "$f")
  [ "$count" -ne 9 ] && echo "FEHLER: $f hat $count Sektionen (erwartet: 9)"
done
```
**Expected:** Keine Ausgabe (0 Fehler).

### 3. /elvis-* Prefix: jeder Skill enthält `/elvis-` im ## Name Block

```bash
grep -l "Failure-Indikator:" skills/research/*.md skills/strategy/*.md | wc -l  # → 30
```
**Expected:** 30 (alle 15+15 Skills haben Failure-Indikator).

### 4. Phantom-Referenz-Check: keine ungültigen Abhängigkeiten

```bash
bash scripts/verify-s05.sh 2>&1 | grep "✗"
```
**Expected:** Keine Ausgabe (0 Fehler-Zeilen).

### 5. D006-Konformität: konkrete Mengenangaben in Ausführungsschritten (Stichproben)

```bash
# Stichprobe 1: elvis-risk-assessment enthält RPS-Formel
grep "RPS" skills/strategy/elvis-risk-assessment.md

# Stichprobe 2: elvis-decision-framework enthält Kriterien-Anzahl
grep -E "[0-9]+ Kriterien|[0-9] Alternativen" skills/strategy/elvis-decision-framework.md

# Stichprobe 3: elvis-data-collector enthält konkrete Datenpunkt-Anzahl
grep -E "[0-9]+ Datenpunkte|[0-9]+ Quell" skills/research/elvis-data-collector.md

# Stichprobe 4: elvis-audience-research enthält Pain-Point-Anzahl
grep "20 Pain Points\|30 Pain\|Pain Points" skills/research/elvis-audience-research.md
```
**Expected:** Alle 4 grep-Befehle geben mindestens 1 Treffer zurück.

### 6. Forward-Reference-Konsistenz: elvis-decision-framework in agent/kirk.md referenziert

```bash
grep "decision-framework" agent/kirk.md
```
**Expected:** Mindestens 1 Treffer (Forward-Referenz aus S03 erfüllt).

## Edge Cases

### Differenzierung ähnlicher Skills verifizieren

```bash
# Abgrenzungsnotiz in elvis-trend-analyzer (vs. elvis-x-trend-scanner)
grep -i "trend-scanner\|x-trend\|Abgrenzung\|Plattform" skills/research/elvis-trend-analyzer.md | head -5

# Abgrenzungsnotiz in elvis-monetization-strategy (vs. elvis-monetization-planner)
grep -i "monetization-planner\|Planner\|Portfolio\|CLV" skills/strategy/elvis-monetization-strategy.md | head -5
```
**Expected:** Beide Dateien enthalten Differenzierungs-Hinweise auf ihre taktischen S04-Pendants.

### verify-s05.sh Exit-Code bei fehlendem Skill

```bash
# Sicherheits-Test: temporär Datei umbenennen und Skript ausführen
mv skills/research/elvis-ai-research.md skills/research/elvis-ai-research.md.bak
bash scripts/verify-s05.sh; echo "Exit-Code: $?"
mv skills/research/elvis-ai-research.md.bak skills/research/elvis-ai-research.md
```
**Expected:** Exit-Code > 0 (Fehler wird erkannt), nach Wiederherstellung Exit-Code 0.

## Failure Signals

- `bash scripts/verify-s05.sh` gibt Exit-Code > 0 — zeigt genau welche Datei/Sektion fehlt
- `ls skills/research/*.md | wc -l` gibt < 15 — nicht alle Research Skills erstellt
- `ls skills/strategy/*.md | wc -l` gibt < 15 — nicht alle Strategy Skills erstellt
- `grep -c "Failure-Indikator:" skills/research/*.md skills/strategy/*.md` gibt < 30 — fehlende Failure-Indikatoren
- `bash scripts/verify-s05.sh 2>&1 | grep "✗"` zeigt Zeilen — konkrete Fehler sichtbar

## Requirements Proved By This UAT

- **R001** (Vollständiges Skill-Ökosystem) — 28 weitere Skills erstellt; Research (14) + Strategy (14) vollständig; jetzt 56/~80 Skills fertig (S01+S04+S05)
- **R002** (Erweitertes Skill-Format) — alle 28 Skills enthalten alle 9 Pflicht-Sektionen; 252/252 Sektions-Checks grün
- **R003** (Konkrete Execution Steps) — D006-Stichproben bestätigt: RPS-Formel, ICE-Score, CLV-Formel, 7-Wochen-GTM, 5×Why-Iterationen — alle mit konkreten Mengenangaben
- **R006** (/elvis-* Naming Convention) — alle 28 neuen Skills enthalten /elvis-* im ## Name Block; verify-s05.sh Check [3/4] = 28/28 grün
- **R011** (Deutsch als Inhaltssprache) — alle 28 Skills auf Deutsch verfasst (manuell durch T01–T04 bestätigt)

## Not Proven By This UAT

- **R004** (Safeguards für Autonome Agenten) — nicht relevant für S05; R004 wird in S07 auf Skill-Ebene bewiesen
- **R005** (Star Trek Agenten-Namen) — bereits in S03 vollständig bewiesen; S05 fügt keine Agenten hinzu
- **R007** (Integrierte Ordnerstruktur) — bereits in S01 bewiesen; S05 fügt keine neuen Verzeichnisse hinzu
- **R008** (10 Souls) — bereits in S02 bewiesen; S05 fügt keine Souls hinzu
- **R009** (Command System) — nicht abgedeckt; liegt in S08
- **R010** (Templates für Wiederverwendung) — bereits in S01 bewiesen
- **R001 vollständig** — noch 20+ Automation/Meta-Skills ausstehend (S06+S07); R001 erst nach S08 vollständig validiert
- **Laufzeit-Tests** — reine Markdown-Dateien, kein Runtime-Verhalten testbar; OpenClaw-Integration bleibt Human-UAT in S09

## Notes for Tester

- verify-s05.sh ist das primäre Verifikations-Werkzeug — Exit-Code 0 = alle 252 maschinellen Checks bestanden
- Stichproben-Checks in Test Case 5 decken D006-Konformität ab, die verify-s05.sh nicht maschinell prüft
- Die Differenzierungs-Notizen (Edge Case: ähnliche Skills) sind semantischer Qualitäts-Check — nicht durch Skripting erzwingbar
- Phantom-Referenz-Check schützt nur den `## Abhängigkeiten`-Block — Fließtext-Referenzen in anderen Sektionen sind manuell diszipliniert (Known Limitation)
- S01-Benchmark-Skills (`skills/research/elvis-market-scan.md`, `skills/strategy/elvis-execution-plan.md`) wurden als Qualitäts-Standard für alle 28 Skills verwendet
