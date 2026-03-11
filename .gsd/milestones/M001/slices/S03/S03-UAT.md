# S03: Agent Layer — 16 Star Trek Agenten — UAT

**Milestone:** M001
**Written:** 2026-03-11

## UAT Type

- UAT mode: artifact-driven
- Why this mode is sufficient: S03 produziert ausschließlich Markdown-Dateien — kein Runtime, kein ausführbarer Code. Die Korrektheit aller Outputs ist vollständig durch `scripts/verify-s03.sh` (148 maschinelle Checks) und ergänzende grep-Befehle prüfbar. Human/UAT-Interaktion ist für diesen Slice nicht erforderlich.

## Preconditions

- `bash` verfügbar
- Working directory: Root des Openclaw_Meta_Maker Projekts
- `scripts/verify-s03.sh` vorhanden und ausführbar
- `agent/` Verzeichnis existiert mit 16 `.md` Dateien

## Smoke Test

```bash
bash scripts/verify-s03.sh
# Erwartetes Ergebnis: Exit-Code 0, letzte Zeile: "✅ S03 Verifikation bestanden — alle 148 Checks grün"
```

## Test Cases

### 1. Alle 16 Agent-Dateien existieren

```bash
ls agent/*.md | wc -l
```
**Expected:** `16`

```bash
ls agent/kirk.md agent/spock.md agent/picard.md agent/data.md agent/worf.md agent/scotty.md agent/laforge.md agent/seven.md agent/sulu.md agent/tuvok.md agent/mccoy.md agent/riker.md agent/q.md agent/borg.md agent/troi.md agent/uhura.md
```
**Expected:** alle 16 Dateien aufgelistet, kein "No such file" Fehler

### 2. Alle 7 Pflichtfelder in jeder Agent-Datei

```bash
bash scripts/verify-s03.sh 2>&1 | grep "✗" | wc -l
```
**Expected:** `0` (keine fehlgeschlagenen Checks)

```bash
grep -c "^## Name\|^## Mission\|^## Capabilities\|^## Operating Loop\|^## Constraints\|^## Primärer Soul\|^## Primäre Skills" agent/picard.md
```
**Expected:** `7`

### 3. Safeguard-Marker in allen 5 autonomen Agenten

```bash
grep -rl "\*\*Max-Limit:\*\*" agent/ | wc -l
grep -rl "\*\*Approval-Gate:\*\*" agent/ | wc -l
grep -rl "\*\*Stop-Bedingung:\*\*" agent/ | wc -l
grep -rl "\*\*Rollback-Hinweis:\*\*" agent/ | wc -l
```
**Expected:** jeweils `5` (picard, q, borg, troi, uhura)

### 4. Kein Persönlichkeitsinhalt in Agent-Dateien (D012)

```bash
grep -ri "mutig\|intuitiv\|leidenschaft\|charakter\|persönlich\|temperament" agent/*.md | wc -l
```
**Expected:** `0`

### 5. Alle Skills nutzen /elvis-* Prefix (D001)

```bash
grep -h "^- /" agent/*.md | grep -v "^- /elvis-" | wc -l
```
**Expected:** `0` (kein Skill ohne /elvis- Prefix)

### 6. Tuvok: kein Delegations-Vokabular

```bash
grep -i "delegier\|orchestrier\|koordinier" agent/tuvok.md | wc -l
```
**Expected:** `0`

### 7. Kirk/McCoy Differenzierung

```bash
grep -i "entscheid\|kurskorrektur\|ressourcen" agent/kirk.md | wc -l
```
**Expected:** `>=1` (Kirk hat Entscheidungs-Fokus)

```bash
grep -i "ausführ\|lieferung\|ohne rückfragen" agent/mccoy.md | wc -l
```
**Expected:** `>=1` (McCoy hat Ausführungs-Fokus)

### 8. Scotty/LaForge Vocabulary-Grenzen

```bash
grep -i "konzipiert\|baut\|architektur\|neu.*system" agent/scotty.md | wc -l
```
**Expected:** `0` (Scotty hat kein Aufbau-Vokabular)

```bash
grep -i "repariert\|wartet\|betreib\|laufend" agent/laforge.md | wc -l
```
**Expected:** `0` (LaForge hat kein reines Betriebs-Vokabular)

## Edge Cases

### Safeguards enthalten konkrete Zahlen (keine vagen Formulierungen)

```bash
grep "\*\*Max-Limit:\*\*" agent/picard.md agent/q.md agent/borg.md agent/troi.md agent/uhura.md
```
**Expected:** Jede Zeile enthält eine konkrete Zahl (3, 5, 10, 1) — keine Formulierungen wie "möglichst wenig" oder "nach Bedarf"

### Alle Agent-Dateien referenzieren existierende Souls

```bash
grep -h "## Primärer Soul" agent/*.md -A1 | grep "soul/" | sed 's/.*soul\///' | sed 's/\.md.*//' | sort | uniq
```
**Expected:** Alle genannten Souls existieren als `soul/*.md` Dateien

### Keine englischen Begriffe im Fließtext (D002 — Deutsch)

```bash
grep -c "^## Name\|^## Mission" agent/kirk.md
```
**Expected:** `2` — Sektionsheader sind deutsch

## Failure Signals

- `bash scripts/verify-s03.sh` Exit-Code > 0: mindestens eine Datei fehlt oder eine Sektion ist unvollständig
- `grep -rl "**Max-Limit:**" agent/ | wc -l` < 5: nicht alle autonomen Agenten haben Safeguards
- `ls agent/*.md | wc -l` < 16: nicht alle Agenten existieren
- `grep "^- /" agent/*.md | grep -v "/elvis-"` gibt Treffer: Skill ohne /elvis- Prefix

## Requirements Proved By This UAT

- **R005** (Star Trek Agenten-Namen) — 16/16 Agenten mit korrekten Star Trek Namen, vollständigen 7 Sektionen und verify-s03.sh Exit-Code 0; R005 ist damit vollständig validiert
- **R004** (Safeguards für Autonome Agenten) auf Agent-Ebene — alle 5 autonomen Agenten (Picard, Q, Borg, Troi, Uhura) haben alle 4 Safeguard-Marker mit konkreten Zahlen; Skill-Ebene wird in S07 bewiesen
- **R012** (D012 — Kein Persönlichkeitsinhalt) — agent/*.md enthalten keinen Charakter-Inhalt, ausschließlich operative Felder

## Not Proven By This UAT

- Tatsächliche Ausführbarkeit der Skills in OpenClaw — S03 definiert nur den Agent-Layer, keine Skills
- `/elvis-*` Skill-Handles zeigen auf existierende Dateien — Skills entstehen erst in S04–S06; Dependency-Verifikation in S09
- Vollständige R004-Validierung auf Skill-Ebene (Meta-Skills mit Safeguards) — folgt in S07
- R001 (vollständiges Skill-Ökosystem) — S03 enthält nur Forward-References auf Skills, keine Skill-Inhalte
- Integration des Agent-Layers mit dem Command System (R009) — folgt in S08

## Notes for Tester

- `scripts/verify-s03.sh` ist die einzige notwendige Verifikation für Contract-Level-Checks — alle 148 Checks grün = S03 bestanden
- Safeguard-Grep mit `grep -rl "**Max-Limit:**"` funktioniert nur mit exakter Schreibweise inkl. ** — Sternchen-Verdopplung ist das grep-Pattern
- Tuvok teilt den strategist-Soul mit Worf und Picard — Differenzierung ist ausschließlich durch Capabilities und Constraints erkennbar, nicht durch den Soul-Header
- Scotty/LaForge Abgrenzung ist subtil (Verb-Auswahl) — beim Lesen auf Betriebs- vs. Aufbau-Vokabular achten
