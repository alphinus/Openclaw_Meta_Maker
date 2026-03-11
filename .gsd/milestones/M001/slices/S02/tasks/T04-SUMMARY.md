---
id: T04
parent: S02
milestone: M001
provides:
  - identity/kirk.md — 7 Sektionen, execution-Soul-Kohärenz, Entscheidung unter Unsicherheit als Kerncharakter
  - identity/picard.md — 7 Sektionen, strategist-Soul-Kohärenz, "Make it so" Zitat, Würde als Führungsprinzip
  - identity/riker.md — 7 Sektionen, growth-Soul-Kohärenz, Expansionsdenken und Potenzialaktivierung
  - identity/worf.md — 7 Sektionen, strategist-Soul-Kohärenz, Ehre als nicht-verhandelbares Handlungsprinzip
  - identity/data.md — 7 Sektionen, creator-Soul-Kohärenz, Erschaffen ohne Ego, Faszination für das Menschliche
  - identity/scotty.md — 7 Sektionen, automation-Soul-Kohärenz, Systeme als Charaktere, Improvisation aus Tiefenwissen
  - identity/laforge.md — 7 Sektionen, builder-Soul-Kohärenz, Ingenieursoptimismus und technisches Machbarkeitssehen
  - identity/mccoy.md — 7 Sektionen, execution-Soul-Kohärenz, "He's dead, Jim" Zitat, moralischer Kompass ohne Filter
key_files:
  - identity/kirk.md
  - identity/picard.md
  - identity/riker.md
  - identity/worf.md
  - identity/data.md
  - identity/scotty.md
  - identity/laforge.md
  - identity/mccoy.md
key_decisions:
  - none
patterns_established:
  - Soul-Kohärenz durch Charakter-Fokus statt Aufgabenbeschreibung — Kirk (execution) zeigt "entscheidet ohne alle Fakten" als Persönlichkeit, nicht "führt schnelle Entscheidungen aus"
  - Schwächen entstehen immer aus Stärken — Kirks Impulsivität ist die Kehrseite seiner Entscheidungsstärke; Worfs Inflexibilität ist die Kehrseite seiner Prinzipientreue
  - Zitate sind diagnostisch nicht nur dekorativ — das Zitat im Star Trek Referenz-Block erklärt die Persönlichkeitslogik in 1-2 Abschlusssätzen
observability_surfaces:
  - bash scripts/verify-s02.sh — Identity-Block [3/3] zeigt jetzt 56/112 grüne Checks (T05 vervollständigt den Rest)
duration: 1 session
verification_result: passed
completed_at: 2026-03-11
blocker_discovered: false
---

# T04: 8 Identities schreiben — Group A: kirk, picard, riker, worf, data, scotty, laforge, mccoy

**8 klassische Star Trek Identities mit exakt 7 Sektionen geschrieben — verify-s02.sh sinkt von 120 auf 56 Fehler (−64).**

## What Happened

Alle 8 Identity-Dateien nach dem spock.md-Benchmark geschrieben. Jede Datei folgt der identischen Struktur (Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz) und enthält ausschließlich Persönlichkeitsinhalte ohne operative Sprache.

Charakteristika der einzelnen Identities:

- **Kirk**: Entscheidung unter Unsicherheit als Kerncharakter, Risiko als Medium; Schwächen zeigen Impulsivität und Überkonfidenz als direkte Kehrseite der Stärke
- **Picard**: Würde, Delegation mit Weitsicht, moralische Tiefe; Schwächen zeigen Perfektionismus, emotionale Distanz und Schwierigkeit bei direktem Fehlereingeständnis
- **Riker**: Wachstumsdenken, Potenzialaktivierung in anderen, expansive Energie; Schwächen zeigen Ungeduld bei Stagnation und Überbegeisterung vor Risikoabwägung
- **Worf**: Ehre als nicht-verhandelbare Achse, taktische Direktheit, Misstrauen gegenüber Kompromissen; Schwächen zeigen Inflexibilität und emotionale Durchbrüche trotz Disziplin
- **Data**: Erschaffen ohne Ego, Faszination für das Menschliche als permanenter Lernantrieb; Schwächen zeigen wörtliches Verstehen, fehlende emotionale Intuition
- **Scotty**: Systeme als Charaktere mit Launen, Improvisation aus Systemtiefenwissen, pessimistischer Zeitpuffer als Feature; Schwächen zeigen Komplexitätsvorliebe und persönliche Kritikempfindlichkeit
- **LaForge**: Ingenieursoptimismus ("noch nicht gelöst" ≠ "unlösbar"), Machbarkeitssehen, technische Erklärung als Wert; Schwächen zeigen Detail-Verlieren und soziale Unbeholfenheit
- **McCoy**: Ungefilterte emotionale Direktheit, moralischer Kompass gegen Hierarchie, Improvisation mit begrenzten Mitteln; Schwächen zeigen emotionale Reaktivität und Technologiemisstrauen

## Verification

```
bash scripts/verify-s02.sh
→ 56 Fehler (alle ausschließlich Group B: seven, sulu, tuvok, q, borg, troi, uhura)
→ Alle 8 Group A Identities: 7/7 Sektionen grün

grep -c "^## " identity/kirk.md ... identity/mccoy.md
→ alle: 7

grep -rn "analysiert|bearbeitet Aufgaben|nutzt den Skill|führt aus|verwaltet" identity/*.md [Group A]
→ 0 Treffer
```

## Diagnostics

`bash scripts/verify-s02.sh` — zeigt in [3/3] Identity-Block welche der 16 Identities vollständig sind. Nach T04 sind Checks 1–56 (spock + 8 Group A) grün, Checks 57–112 (7 Group B) noch rot.

Fortschrittsindikator: 198 → 183 → 148 → 120 → **56** → 0 (nach T05)

## Deviations

none

## Known Issues

none

## Files Created/Modified

- `identity/kirk.md` — 7 Sektionen, execution-Soul, Entscheidung unter Unsicherheit
- `identity/picard.md` — 7 Sektionen, strategist-Soul, "Make it so" Zitat
- `identity/riker.md` — 7 Sektionen, growth-Soul, Wachstumsdenken und Potenzialaktivierung
- `identity/worf.md` — 7 Sektionen, strategist-Soul, Ehre als Handlungsprinzip
- `identity/data.md` — 7 Sektionen, creator-Soul, Erschaffen ohne Ego
- `identity/scotty.md` — 7 Sektionen, automation-Soul, Systemcharakter und Improvisation
- `identity/laforge.md` — 7 Sektionen, builder-Soul, Ingenieursoptimismus
- `identity/mccoy.md` — 7 Sektionen, execution-Soul, "He's dead, Jim" Zitat
