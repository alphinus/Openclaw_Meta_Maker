# S04: Growth + Content Skills (~30 Skills) — UAT

**Milestone:** M001
**Written:** 2026-03-11

## UAT Type

- UAT mode: artifact-driven
- Why this mode is sufficient: S04 liefert ausschließlich Markdown-Dateien ohne Runtime-Verhalten. Die Korrektheit ist vollständig durch strukturelle Checks (verify-s04.sh) und manuelle Stichproben (D06-Konformität) prüfbar — kein Server, kein Code, keine API erforderlich.

## Preconditions

- Repository ausgecheckt in `C:\Dev\Openclaw_Meta_Maker`
- `bash` verfügbar (Git Bash oder WSL)
- `scripts/verify-s04.sh` existiert und ist ausführbar
- Alle 28 Skill-Dateien in `skills/growth/` und `skills/content/` vorhanden

## Smoke Test

```bash
bash scripts/verify-s04.sh; echo "Exit: $?"
# Erwartetes Ergebnis: Exit: 0
```

Wenn Exit-Code 0, sind alle 4 strukturellen Check-Gruppen bestanden — Slice ist grundsätzlich vollständig.

## Test Cases

### 1. Strukturelle Vollständigkeit aller 28 Skills

```bash
bash scripts/verify-s04.sh
```

1. Skript ausführen
2. Alle 28 Dateien-Existenz-Checks prüfen → ✓ für jede Datei
3. Alle 252 Sektions-Checks prüfen → ✓ für jede Sektion
4. Alle 28 `/elvis-*` Prefix-Checks prüfen → ✓ für jede Datei
5. Alle 28 Phantom-Referenz-Checks prüfen → ✓ für jede Datei
6. **Erwartetes Ergebnis:** Exit-Code 0, Banner "✅ S04 Verifikation bestanden"

### 2. D006-Stichprobe: Growth Skills Ausführungsschritte

Skills: `skills/growth/elvis-viral-formula.md`, `skills/growth/elvis-growth-loop.md`, `skills/growth/elvis-niche-finder.md`

1. Datei öffnen und `## Ausführungsschritte`-Block finden
2. Nummerierte Schritte zählen → ≥4 erwartet
3. Pro Schritt: mindestens eine Mengenangabe (Zahl, Zeitraum, Zeichenlimit) identifizieren
4. **Erwartetes Ergebnis:** Alle 3 Skills haben ≥4 Schritte, jeder Schritt ≥1 Mengenangabe

Schnell-Checks:
```bash
grep -A 30 "## Ausführungsschritte" skills/growth/elvis-viral-formula.md | grep -E "^\d+\."
grep -A 30 "## Ausführungsschritte" skills/growth/elvis-growth-loop.md | grep -E "^\d+\."
grep -A 30 "## Ausführungsschritte" skills/growth/elvis-niche-finder.md | grep -E "^\d+\."
```

### 3. D006-Stichprobe: Content Skills Ausführungsschritte

Skills: `skills/content/elvis-x-thread-writer.md`, `skills/content/elvis-headline-writer.md`, `skills/content/elvis-content-brief.md`

1. Datei öffnen und `## Ausführungsschritte`-Block finden
2. Nummerierte Schritte zählen → ≥4 erwartet
3. Pro Schritt: mindestens eine Mengenangabe identifizieren
4. **Erwartetes Ergebnis:** Alle 3 Skills haben ≥4 Schritte, jeder Schritt ≥1 Mengenangabe

Schnell-Checks:
```bash
grep -A 30 "## Ausführungsschritte" skills/content/elvis-x-thread-writer.md | grep -E "^\d+\."
grep -A 30 "## Ausführungsschritte" skills/content/elvis-headline-writer.md | grep -E "^\d+\."
grep -A 30 "## Ausführungsschritte" skills/content/elvis-content-brief.md | grep -E "^\d+\."
```

### 4. Failure-Indikatoren vorhanden

```bash
grep -l "Failure-Indikator" skills/growth/*.md skills/content/*.md | wc -l
```

1. Grep-Befehl ausführen
2. **Erwartetes Ergebnis:** 28 (alle 28 Skills enthalten einen Failure-Indikator im Verifikations-Block)

### 5. /elvis-* Prefix im Name-Block

```bash
grep -A 3 "^## Name" skills/growth/elvis-viral-formula.md
grep -A 3 "^## Name" skills/content/elvis-content-brief.md
```

1. Name-Block auslesen
2. **Erwartetes Ergebnis:** `/elvis-viral-formula` bzw. `/elvis-content-brief` im Block vorhanden

### 6. Lesbarkeitstest: Ein vollständiger Skill in OpenClaw

1. `skills/growth/elvis-growth-loop.md` in einem Markdown-Viewer oder OpenClaw öffnen
2. Alle 9 Sektionen prüfen: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output
3. Ausführungsschritte lesen: Ist jeder Schritt ohne Interpretation ausführbar?
4. Verifikations-Block lesen: Ist der Failure-Indikator klar und prüfbar?
5. **Erwartetes Ergebnis:** Jede Sektion ist vollständig und auf Deutsch; Schritte sind ohne Ambiguität ausführbar; Failure-Indikator nennt eine konkrete Bedingung

## Edge Cases

### Abhängigkeiten-Block mit Phantom-Referenzen

```bash
grep -A 5 "## Abhängigkeiten" skills/growth/elvis-growth-loop.md
```

1. Abhängigkeiten-Block des komplexesten Skills (elvis-growth-loop) prüfen
2. Alle genannten `/elvis-*`-Referenzen manuell gegen existierende Dateien prüfen
3. **Erwartetes Ergebnis:** Alle Referenzen sind existierende Dateien in `skills/` — keine Phantom-Referenzen

### Zeichenlimit-Konsistenz in Content Skills

```bash
grep -n "280 Zeichen\|160 Zeichen\|100 Zeichen" skills/content/elvis-bio-writer.md
grep -n "max\. 280\|max\. 100\|max\. 150" skills/content/elvis-dm-writer.md
```

1. Content-Skill mit expliziten Zeichenlimits öffnen
2. Konsistenz zwischen `## Einschränkungen` und `## Ausführungsschritte` prüfen
3. **Erwartetes Ergebnis:** Zeichenlimits in beiden Sektionen konsistent

## Failure Signals

- `bash scripts/verify-s04.sh` gibt Exit-Code > 0 → Strukturproblem in einer oder mehreren Dateien
- `grep -l "## Verifikation" skills/growth/*.md | wc -l` ergibt < 14 → fehlende Sektionen
- Failure-Indikator-Count < 28 → Skill(s) ohne prüfbaren Failure-Indikator
- Zeichenlimits inkonsistent zwischen Sektionen → D006-Verletzung
- Skill enthält englische Sätze → R011-Verletzung

## Requirements Proved By This UAT

- **R001 (Vollständiges Skill-Ökosystem) — teilweise:** 28 von ~80 Skills vollständig vorhanden (Growth + Content); die Domänen Growth und Content sind vollständig abgedeckt
- **R002 (Erweitertes Skill-Format):** verify-s04.sh Check [2/4] beweist 252/252 Sektions-Checks — alle 28 Skills enthalten alle 9 Pflichtfelder
- **R003 (Konkrete, ausführbare Execution Steps):** 6 D006-Stichproben (Test Cases 2+3) beweisen ≥4 Schritte mit ≥1 Mengenangabe pro Schritt
- **R006 (/elvis-* Naming Convention):** verify-s04.sh Check [3/4] + Test Case 5 beweisen 28/28 Prefix-Checks
- **R011 (Deutsch als Inhaltssprache):** Lesbarkeitstest (Test Case 6) + manueller Inhalt bestätigt Deutsch

## Not Proven By This UAT

- **R001 vollständig:** Research (S05), Strategy (S05), Automation (S06), Meta (S07) Skills fehlen noch — wird in S05–S08 bewiesen
- **R004 (Safeguards für Autonome Agenten):** S04 enthält keine autonomen Agenten-Skills — wird in S07 bewiesen
- **R009 (Command System):** S04 enthält keine Command-Definitionen — wird in S08 bewiesen
- **Operationale Korrektheit:** UAT prüft Struktur und Format, nicht ob die Skills in OpenClaw tatsächlich nützliche Outputs produzieren — das erfordert echte OpenClaw-Tests durch den Nutzer
- **Phantom-Referenzen in Fließtext:** verify-s04.sh prüft nur `## Abhängigkeiten`-Block; Fließtext-Referenzen in "Empfohlene Vorgänger-Skills" werden nicht validiert — manuelle Disziplin erforderlich

## Notes for Tester

- Die Stichproben in Test Cases 2 und 3 sind die wichtigsten manuellen Checks — sie beweisen R003 (D06-Konformität) als einzige nicht-automatisierbare Kriterien
- **Bekannte Einschränkung:** Der Phantom-Check deckt nur `## Abhängigkeiten`-Block ab, nicht Fließtext. Wenn ein Skill im Fließtext einen nicht-existierenden Skill erwähnt, wird das nicht erkannt.
- Alle Skill-Inhalte sind auf Deutsch — Dateinamen und Kommandos bleiben englisch (R011-Konvention)
- Bei Zweifeln an D06-Konformität: `grep -n "^\d\+\." skills/growth/elvis-viral-formula.md` zeigt alle nummerierten Schritte
