# S02: Souls und Identities

**Goal:** 10 vollständige Soul-Dateien und 16 vollständige Identity-Dateien schreiben — die philosophische und persönliche Grundlage für alle 16 Star Trek Agenten.
**Demo:** `bash scripts/verify-s02.sh` läuft mit Exit-Code 0 (198 Checks grün: 26 Datei-Existenz + 60 Soul-Sektionen + 112 Identity-Sektionen).

## Must-Haves

- 10 `soul/*.md` — je mit exakt 6 Sektionen: `## Name`, `## Philosophie`, `## Core Values`, `## Operating Principles`, `## Success Metrics`, `## Geeignet für`
- 16 `identity/*.md` — je mit exakt 7 Sektionen: `## Name`, `## Charakter-Beschreibung`, `## Persönlichkeitsmerkmale`, `## Kommunikationsstil`, `## Stärken`, `## Schwächen`, `## Star Trek Referenz`
- `## Geeignet für` in jeder Soul-Datei enthält das explizite Agenten-Mapping aus S02-RESEARCH.md (bindendes Vorarbeits-Dokument für S03)
- Identities strikt auf Charakter/Persönlichkeit begrenzt — kein einziger operativer Satz (D012)
- Soul-Philosophien klar voneinander abgegrenzt (insbesondere researcher vs. analyst, builder vs. creator)
- Authentische Schwächen in jeder Identity — entstehen aus der Stärke (keine Pseudo-Schwächen)
- Alle Inhalte auf Deutsch; Star Trek Referenz-Zitate im englischen Original + deutsche Übersetzung
- `scripts/verify-s02.sh` mit 198 Checks, Exit-Code = Fehleranzahl (konsistent mit D014)

## Proof Level

- This slice proves: contract (Datei-Existenz + Sektions-Vollständigkeit durch verify-s02.sh)
- Real runtime required: no
- Human/UAT required: no — Verifikation vollständig durch Shell-Skript abgedeckt

## Verification

```bash
# Primäre Stopping-Condition:
bash scripts/verify-s02.sh
# Erwartetes Ergebnis: Exit-Code 0, alle 198 Checks ✓

# Sekundäre Checks:
grep -c "^## Geeignet für" soul/*.md
# Erwartung: 10 (jede Soul-Datei enthält diese Sektion)

grep -rn "analysiert\|bearbeitet\|nutzt den Skill\|führt aus" identity/
# Erwartung: 0 Treffer (kein operativer Inhalt in Identities)

ls soul/ | grep -v ".gitkeep" | wc -l
# Erwartung: 10

ls identity/ | grep -v ".gitkeep" | wc -l
# Erwartung: 16
```

## Observability / Diagnostics

- Runtime signals: none (reine Markdown-Generierung)
- Inspection surfaces: `bash scripts/verify-s02.sh` — strukturierter Check-Report mit ✓/✗ pro Datei und Sektion; Exit-Code = Fehleranzahl
- Failure visibility: Exit-Code N zeigt exakt N fehlgeschlagene Checks; fehlende Sektionen werden mit Dateiname + Sektion gemeldet
- Redaction constraints: none

## Integration Closure

- Upstream surfaces consumed: `templates/soul-template.md` (6-Sektionen-Format + strategist-Beispiel), `templates/identity-template.md` (7-Sektionen-Format + spock-Beispiel)
- New wiring introduced in this slice: Soul-zu-Agenten-Mapping in `## Geeignet für`-Sektionen — diese werden in S03 als Referenz für Agent-Datei-Erstellung genutzt
- What remains before the milestone is truly usable end-to-end: S03 (Agent-Dateien mit Soul-Referenzen und Capabilities), S04–S07 (Skills), S08 (Commands), S09 (README + Verifikation)

## Tasks

- [x] **T01: verify-s02.sh erstellen + strategist.md + spock.md aus Templates extrahieren** `est:30m`
  - Why: Stopping-Condition vor der Inhaltserstellung definieren (TDD-Äquivalent für Markdown); strategist und spock sind bereits fertig ausgearbeitet in den Templates — direkte Extraktion ohne Neuschreiben
  - Files: `scripts/verify-s02.sh`, `soul/strategist.md`, `identity/spock.md`
  - Do: (1) verify-s02.sh schreiben mit 3 Check-Gruppen: [1/3] Datei-Existenz (26 Dateien), [2/3] Soul-Sektionen (10×6=60), [3/3] Identity-Sektionen (16×7=112). Exit-Code = Fehleranzahl. (2) Initialen Lauf ausführen — erwartetes Ergebnis: ~182 Fehler (26 fehlen - 3 die gleich erstellt werden + alle Sektions-Checks schlagen fehl). (3) Soul `strategist.md` aus Template-Beispiel-Block extrahieren (unterhalb der Trennlinie in soul-template.md), HTML-Kommentare entfernen. (4) Identity `spock.md` analog aus identity-template.md extrahieren. (5) verify-s02.sh erneut ausführen — Fehleranzahl muss merklich gesunken sein (2 Dateien + ihre Sektionen korrekt erkannt).
  - Verify: `bash scripts/verify-s02.sh` läuft ohne Bash-Fehler durch; `grep -c "^##" soul/strategist.md` = 6; `grep -c "^##" identity/spock.md` = 7
  - Done when: verify-s02.sh existiert und ist ausführbar; soul/strategist.md und identity/spock.md existieren mit vollständigen Sektionen; Skript meldet genau 182 verbleibende Fehler (198 - 16 korrekte Checks für die 2 fertigen Dateien + ihre 13 Sektionen = 2 Existenz + 6 Soul + 7 Identity)

- [x] **T02: 5 Souls schreiben — researcher, execution, builder, growth, automation** `est:45m`
  - Why: Die 5 klar abgegrenzten Archetypes (aus RESEARCH.md Reihenfolge 1-5) zuerst schreiben — diese haben das geringste Verwechslungsrisiko und etablieren die Qualitätsbasis für die nuancierteren Souls in T03
  - Files: `soul/researcher.md`, `soul/execution.md`, `soul/builder.md`, `soul/growth.md`, `soul/automation.md`
  - Do: Für jeden Soul: exakt 6 Sektionen nach soul-template.md-Format. Qualitätsniveau: strategist.md als Benchmark. Kernunterscheidungen einhalten: (A) `researcher` = Wissenssuche als Wert (Was ist wahr? → Spock), konkrete Suche nach Fakten und Beweisen; (B) `execution` = Ergebnis über Prozess, Risiko akzeptieren, handeln bevor alle Fakten vorliegen (→ Kirk, McCoy); (C) `builder` = konstruiert Bekanntes besser/robuster, Engineering-Mindset, inkrementelle Verbesserung (→ LaForge, Scotty); (D) `growth` = Expansion und Skalierung als Weltbild, Ambitionen nach oben kalibrieren (→ Riker); (E) `automation` = Systeme > Einzellösungen, Wiederholbarkeit als Wert, assimiliert Best-Practices (→ Scotty, Borg). `## Geeignet für` in jedem Soul: explizit die primären/sekundären Agenten aus RESEARCH.md nennen.
  - Verify: `bash scripts/verify-s02.sh` — Fehleranzahl sinkt von ~182 auf ~127 (5 Dateien × 7 Checks = 35 weniger Fehler); `grep -c "^## Geeignet für" soul/*.md` = 7 (strategist + 5 neue + spock hat diese Sektion nicht — ist Identity-Datei)
  - Done when: Alle 5 soul/*.md existieren mit 6 vollständigen Sektionen; Operating Principles als feste Regeln formuliert (nicht als Wünsche); Philosophien klar voneinander abgegrenzt; verify-s02.sh meldet 127 oder weniger verbleibende Fehler

- [x] **T03: 4 Souls schreiben — operator, analyst, creator, minimalist** `est:45m`
  - Why: Die 4 nuanciertesten Souls — analyst vs. researcher, creator vs. builder, minimalist ohne primären Agenten — erfordern besondere konzeptuelle Sorgfalt und werden nach der etablierten Qualitätsbasis aus T02 geschrieben
  - Files: `soul/operator.md`, `soul/analyst.md`, `soul/creator.md`, `soul/minimalist.md`
  - Do: (A) `operator` = navigiert und verwaltet laufende Systeme, Ordnung und Zuverlässigkeit, kein Erschaffen sondern Erhalten (→ Sulu, Uhura); (B) `analyst` = Muster in vorhandenen Daten erkennen und bewerten (Was bedeutet das? — im Gegensatz zu researcher: Was ist wahr?), empathisch-datengetrieben (→ Seven, Troi); (C) `creator` = erschafft Neues aus dem Nichts, generativer Mindset, Erschaffen ohne Ego oder mit spielerischer Leichtigkeit (→ Data, Q; unterscheidet sich von builder: builder = Engineering, creator = Generierung); (D) `minimalist` — besondere Sorgfalt: Fokus auf maximale Wirkung mit minimalem Aufwand, Komplexität als Fehler formulieren, kein primärer Agent → `## Geeignet für` erklärt ihn als Lens-Soul (sekundärer Soul für alle Agenten). Success Metrics für minimalist müssen konkret sein (z.B. "Lösung braucht keine Dokumentation weil sie sich selbst erklärt"). Nach den 4 Dateien: `bash scripts/verify-s02.sh` ausführen.
  - Verify: `bash scripts/verify-s02.sh` — Fehleranzahl sinkt auf ~91 (nur noch Identity-Fehler: 16×7=112 - 21 korrekte Identity-Checks für spock); `grep -c "^##" soul/minimalist.md` = 6; Philosophie-Abgrenzungen: `grep "Was bedeutet das" soul/analyst.md` und `grep "Was ist wahr" soul/researcher.md` sollten charakteristische Formulierungen zeigen
  - Done when: Alle 4 soul/*.md existieren mit 6 vollständigen Sektionen; analyst≠researcher und creator≠builder klar in Philosophie-Sektionen differenziert; minimalist enthält konkrete Success Metrics (keine abstrakten Wünsche); verify-s02.sh meldet ≤91 verbleibende Fehler

- [x] **T04: 8 Identities schreiben — Group A: kirk, picard, riker, worf, data, scotty, laforge, mccoy** `est:50m`
  - Why: Die 8 "klassischeren" Star Trek Charaktere ohne die Sonderfall-Persönlichkeiten (Q, Borg, Seven) — etabliert den Qualitätsstandard für Identity-Dateien mit klaren Charakter-Profilen
  - Files: `identity/kirk.md`, `identity/picard.md`, `identity/riker.md`, `identity/worf.md`, `identity/data.md`, `identity/scotty.md`, `identity/laforge.md`, `identity/mccoy.md`
  - Do: Für jeden Charakter: exakt 7 Sektionen nach identity-template.md. Spock ist Benchmark. Kernregel D012 einhalten: KEIN Satz der in einer Stellenbeschreibung stehen würde. Charakter-Kohärenz mit implizitem Soul (aus RESEARCH.md): Kirk (execution: entscheidet vor alle Fakten vorliegen), Picard (strategist: eloquent, delegiert mit Weitsicht, "Make it so"), Riker (growth: ambitioniert, will immer mehr), Worf (strategist: taktisch, Ehre als Handlungsprinzip), Data (creator: präzise Produktion, erschafft ohne Ego), Scotty (automation: pragmatisch, löst unmögliche Probleme), LaForge (builder: Ingenieursdenken, sieht das Machbare), McCoy (execution: hands-on, emotional engagiert, Ergebnis über Prozess). Jede Schwäche muss Kehrseite einer Stärke sein. Zitat: unverwechselbar THIS character — "Beam me up" (Kirk), "Make it so" (Picard), "He's dead, Jim" (McCoy) etc.
  - Verify: `bash scripts/verify-s02.sh` — Fehleranzahl sinkt auf ≤35 (verbleibend: 8 Identity-Dateien × 7 Checks = 56 offene Checks); `grep -rn "analysiert\|nutzt den Skill\|bearbeitet Aufgaben" identity/kirk.md identity/picard.md` = 0 Treffer
  - Done when: Alle 8 identity/*.md existieren mit 7 vollständigen Sektionen; kein operativer Satz in keiner Identity-Datei; authentische (nicht PR-artige) Schwächen-Sektionen; verify-s02.sh meldet ≤35 verbleibende Fehler

- [x] **T05: 8 Identities schreiben — Group B: seven, sulu, tuvok, q, borg, troi, uhura — und finale Verifikation** `est:50m`
  - Why: Die 8 verbleibenden Identities — darunter die Sonderfälle Q (omnipotent, Schwächen verborgen), Borg (Kollektiv-Entität), Seven (post-Borg) — abschließen und den Slice mit Exit-Code 0 verifizieren
  - Files: `identity/seven.md`, `identity/sulu.md`, `identity/tuvok.md`, `identity/q.md`, `identity/borg.md`, `identity/troi.md`, `identity/uhura.md`, `scripts/verify-s02.sh` (ggf. Bugfix)
  - Do: Seven (analyst: effizient, datengetrieben, emotional reduziert — ex-Borg-Perspektive), Sulu (operator: ruhig, präzise, navigiert souverän), Tuvok (strategist: vulkanische Logik + taktisches Denken, sicherheitsorientiert), Q (creator: spielerisch-omnipotent; Schwächen: Langeweile-Anfälligkeit, Empathiemangel, Unzuverlässigkeit bei Verpflichtungen — mindestens 3 echte Schwächen), Borg (automation: Singular-Sprecher mit Kollektiv-Weltbild — "ich" = das Kollektiv; Schwäche: keine Individualität als Grenze), Troi (analyst: empathisch-analytisch, liest Zustände, bewertet Schwächen), Uhura (operator: Kommunikation, Ordnung, verbindet Systeme). Nach allen 8 Dateien: `bash scripts/verify-s02.sh` ausführen. Falls Exit-Code > 0: fehlende Sektionen identifizieren und korrigieren. Repeat bis Exit-Code 0.
  - Verify: `bash scripts/verify-s02.sh` → Exit-Code 0 und alle 198 Checks ✓; `grep -c "^## Geeignet für" soul/*.md` = 10; `ls soul/ | grep -v ".gitkeep" | wc -l` = 10; `ls identity/ | grep -v ".gitkeep" | wc -l` = 16; `grep -rn "analysiert\|nutzt den Skill\|bearbeitet Aufgaben" identity/` = 0 Treffer
  - Done when: Alle 26 Dateien existieren mit vollständigen Sektionen; verify-s02.sh Exit-Code = 0; keine operativen Inhalte in Identities; R005 und R008 nachweislich erfüllt

## Files Likely Touched

- `scripts/verify-s02.sh`
- `soul/strategist.md`
- `soul/researcher.md`
- `soul/execution.md`
- `soul/builder.md`
- `soul/growth.md`
- `soul/automation.md`
- `soul/operator.md`
- `soul/analyst.md`
- `soul/creator.md`
- `soul/minimalist.md`
- `identity/spock.md`
- `identity/kirk.md`
- `identity/picard.md`
- `identity/riker.md`
- `identity/worf.md`
- `identity/data.md`
- `identity/scotty.md`
- `identity/laforge.md`
- `identity/mccoy.md`
- `identity/seven.md`
- `identity/sulu.md`
- `identity/tuvok.md`
- `identity/q.md`
- `identity/borg.md`
- `identity/troi.md`
- `identity/uhura.md`
