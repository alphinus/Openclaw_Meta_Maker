---
estimated_steps: 5
estimated_files: 8
---

# T04: 8 Identities schreiben — Group A: kirk, picard, riker, worf, data, scotty, laforge, mccoy

**Slice:** S02 — Souls und Identities
**Milestone:** M001

## Description

Die erste Hälfte der 16 Identity-Dateien schreiben. Diese 8 Charaktere sind klassische Star Trek Figuren mit klar erkennbaren Persönlichkeiten — weniger Sonderfälle als Group B (Q, Borg, Seven). `identity/spock.md` aus T01 ist der Qualitäts-Benchmark: 7 Sektionen, Charakter-Fokus ohne operative Inhalte, authentische Schwächen, unverwechselbares Zitat. D012 ist die kritische Regel: Kein Satz darf in einer Stellenbeschreibung stehen.

## Steps

1. `identity/kirk.md`, `identity/picard.md`, `identity/riker.md`, `identity/worf.md` schreiben:
   - **Kirk** (execution-Soul): Entscheidet bevor alle Fakten vorliegen, akzeptiert Risiko als Führungsprinzip, unerschütterlich optimistisch. Zitat: unverwechselbar Kirk (z.B. zu Spock: "Dammit, Spock..."). Schwächen: Impulsivität, Überkonfidenz, Schwierigkeit mit Autorität.
   - **Picard** (strategist-Soul): Eloquent, delegiert mit Weitsicht, intellectuell fundiert, trägt Verantwortung mit Würde. Zitat: "Make it so." oder "Engage." Schwächen: Perfektionismus, emotionale Distanz, Schwierigkeit Fehler zuzugeben.
   - **Riker** (growth-Soul): Ambitioniert, sucht immer die nächste Gelegenheit, charismatisch, expansives Denken. Zitat: charakteristisch Riker. Schwächen: Ungeduld wenn er stagniert, gelegentlich zu selbstsicher.
   - **Worf** (strategist-Soul): Taktisch, diszipliniert, Ehre als nicht-verhandelbares Handlungsprinzip, direkt bis zur Härte. Zitat: "Today is a good day to die." oder "Qapla'." Schwächen: Inflexibel bei Regeln, emotionale Reaktionen trotz Disziplin, Misstrauen gegenüber Kompromissen.
2. `identity/data.md`, `identity/scotty.md` schreiben:
   - **Data** (creator-Soul): Produziert unermüdlich und präzise, erschafft ohne Ego, strebt nach dem Menschlichen ohne es je ganz zu verstehen. Zitat: charakteristisch über seine Andersartigkeit. Schwächen: Keine emotionale Intuition, wörtliches Verstehen von Metaphern, kann soziale Situationen falsch lesen.
   - **Scotty** (automation-Soul): Pragmatisch, sieht Systeme als Charakter mit eigenen Launen, löst das Unlösbare durch Improvisation und tiefes Systemwissen. Zitat: "I'm giving it all she's got, Captain!" oder "I cannot change the laws of physics." Schwächen: Pessimismus bei Zeitschätzungen (Feature?), Vorliebe für Komplexität.
3. `identity/laforge.md`, `identity/mccoy.md` schreiben:
   - **LaForge** (builder-Soul): Sieht das technisch Machbare wo andere Grenzen sehen, Ingenieursdenken als Weltanschauung, ausdauernd bei Problemen, optimistisch-pragmatisch. Zitat: charakteristisch LaForge. Schwächen: Verliert sich in technischen Details, soziale Unbeholfenheit.
   - **McCoy** (execution-Soul): Hands-on, emotional engagiert, direkt bis zur Unhöflichkeit, Ergebnis über Prozess, starkes moralisches Kompass. Zitat: "He's dead, Jim." oder "Dammit Jim, I'm a doctor not a [X]!" Schwächen: Emotionale Reaktivität, Sturheit, Vorurteile gegenüber Technologie.
4. Jede Datei intern prüfen: Enthält sie einen Satz der in einer Stellenbeschreibung stehen würde? → Löschen oder umformulieren auf Charakterebene.
5. `bash scripts/verify-s02.sh` ausführen — Fehleranzahl muss auf ≤56 gesunken sein (8 neue Dateien × 7 Checks = 56 neue korrekte Checks)

## Must-Haves

- [ ] Alle 8 identity/*.md existieren mit exakt 7 Sektionen
- [ ] Keine operative Sprache in keiner Identity (kein "analysiert", "bearbeitet", "nutzt den Skill X", "führt aus")
- [ ] Jede `## Schwächen`-Sektion enthält ≥3 authentische Schwächen die aus Stärken entstehen
- [ ] Jedes Zitat in `## Star Trek Referenz` ist unverwechselbar DIESER Charakter
- [ ] Implizite Soul-Kohärenz (D012-konformer Charakter-Fokus): Kirk = execution, Picard = strategist, etc.

## Verification

- `bash scripts/verify-s02.sh` — Fehleranzahl ≤56
- `grep -c "^## " identity/kirk.md identity/picard.md identity/riker.md identity/worf.md identity/data.md identity/scotty.md identity/laforge.md identity/mccoy.md` — alle geben 7 zurück
- `grep -rn "analysiert\|bearbeitet Aufgaben\|nutzt den Skill\|führt aus\|verwaltet" identity/kirk.md identity/picard.md identity/riker.md identity/worf.md identity/data.md identity/scotty.md identity/laforge.md identity/mccoy.md` — 0 Treffer
- `grep -c "Schwächen" identity/mccoy.md` ≥ 1 (Sektion existiert)

## Observability Impact

- Signals added/changed: `bash scripts/verify-s02.sh` — Identity-Block ([3/3]) zeigt zunehmend grüne Checks
- How a future agent inspects this: Skript-Gruppe [3/3] zeigt welche der 16 Identities vollständig sind
- Failure state exposed: Fehlende Sektionen werden einzeln mit Dateiname gemeldet

## Inputs

- `identity/spock.md` (T01) — Qualitäts-Benchmark: 7 Sektionen, keine operative Sprache, authentische Schwächen
- `templates/identity-template.md` — verbindliches Format und D012-Faustregel
- S02-RESEARCH.md — Identity → Soul Kohärenz-Tabelle und Common Pitfalls (Identity-Agent-Vermischung)

## Expected Output

- `identity/kirk.md` — 7 Sektionen, execution-Soul-Kohärenz, "decide before all facts" als Kerncharakter
- `identity/picard.md` — 7 Sektionen, strategist-Soul-Kohärenz, "Make it so" Zitat
- `identity/riker.md` — 7 Sektionen, growth-Soul-Kohärenz, ambitionierter Charakter
- `identity/worf.md` — 7 Sektionen, strategist-Soul-Kohärenz, Ehre als Handlungsprinzip
- `identity/data.md` — 7 Sektionen, creator-Soul-Kohärenz, Produktion ohne Ego
- `identity/scotty.md` — 7 Sektionen, automation-Soul-Kohärenz, Systemwissen als Charakter
- `identity/laforge.md` — 7 Sektionen, builder-Soul-Kohärenz, Ingenieursoptimismus
- `identity/mccoy.md` — 7 Sektionen, execution-Soul-Kohärenz, "He's dead, Jim" Zitat
