# S02: Souls und Identities — Research

**Date:** 2026-03-11

## Summary

S02 ist reine Markdown-Generierung — keine Libraries, kein Runtime, keine externe Toolchain. Die gesamte Arbeit besteht darin, 10 Soul-Dateien und 16 Identity-Dateien nach den bereits verifizierten Templates aus S01 zu schreiben. Beide Templates sind vollständig ausgearbeitet und enthalten je ein vollständiges Qualitäts-Beispiel (`soul/strategist` und `identity/spock`), das als direkter Benchmark gilt.

Die kritische Herausforderung in S02 ist konzeptueller Natur, nicht technisch: (1) Die 10 Souls müssen philosophisch klar voneinander abgegrenzt sein — bei ähnlich klingenden Souls (strategist vs. analyst vs. researcher) drohen inhaltliche Überschneidungen. (2) Die Identity-Dateien müssen konsequent auf Charakter/Persönlichkeit begrenzt bleiben — kein Einschleichen von operativen Aufgaben-Beschreibungen (das gehört in S03/Agents). (3) Das Soul→Agent-Mapping muss implizit in den Soul-Dateien angelegt sein, damit S03 die Zuordnung konsistent übernehmen kann.

Die empfohlene Vorgehensweise: Erst alle 10 Souls schreiben (klare Philosophien etablieren), dann 16 Identities (spock.md kann direkt aus Template entnommen werden). Pro Soul soll die `## Geeignet für`-Sektion explizit die Star Trek Agenten nennen, die diesen Soul verwenden — das erzeugt die Brücke zu S03.

## Recommendation

**Sequenzieller Ansatz: Erst Souls (10), dann Identities (16).**

Begründung: Souls bilden die konzeptuelle Grundlage. Wenn die 10 Soul-Philosophien klar abgegrenzt sind, fällt die Soul-Zuweisung pro Identity-Datei leichter (die Identities referenzieren ihren Soul implizit durch Charakter-Kohärenz). Die Reihenfolge der Soul-Erstellung sollte von "klar abgegrenzt" zu "nuanciert" gehen:

1. `researcher` — klar (Spock, Fakten, Logik)
2. `execution` — klar (Kirk, McCoy, Hands-on)
3. `builder` — klar (LaForge, Scotty, konstruiert)
4. `growth` — klar (Riker, expansiv)
5. `automation` — klar (Borg, Scotty, Systeme)
6. `operator` — klar (Sulu, Uhura, navigiert/verwaltet)
7. `strategist` — bereits vollständig im Template (kann direkt übernommen werden)
8. `analyst` — ähnlich wie researcher, aber anders fokussiert (Seven, Troi)
9. `creator` — ähnlich wie builder, aber anders (Data, Q — Erschaffung statt Konstruktion)
10. `minimalist` — am nuanciertesten (kein direktes Agenten-Gegenstück, universell einsetzbar)

## Don't Hand-Roll

| Problem | Existing Solution | Why Use It |
|---------|------------------|------------|
| strategist Soul-Inhalt | `templates/soul-template.md` — vollständiges Beispiel ab Trennlinie | Inhalt ist bereits fertig ausgearbeitet; direkt als `soul/strategist.md` übernehmen |
| spock Identity-Inhalt | `templates/identity-template.md` — vollständiges Beispiel ab Trennlinie | Inhalt ist bereits fertig ausgearbeitet; direkt als `identity/spock.md` übernehmen |
| Soul-Sektionen-Format | `templates/soul-template.md` — 6 Sektionen: Name, Philosophie, Core Values, Operating Principles, Success Metrics, Geeignet für | Bindendes Format; kein Abweichen |
| Identity-Sektionen-Format | `templates/identity-template.md` — 7 Sektionen: Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz | Bindendes Format; kein Abweichen |

## Existing Code and Patterns

- `templates/soul-template.md` — Zweistufiges Template mit Anweisungs-Block + vollständigem `strategist`-Beispiel. Der `strategist`-Beispiel-Block unterhalb der Trennlinie ist der direkte Inhalt für `soul/strategist.md` (ohne Template-Kommentare). Qualitätsniveau ist der Benchmark.
- `templates/identity-template.md` — Zweistufiges Template mit Anweisungs-Block + vollständigem `spock`-Beispiel. Der `spock`-Beispiel-Block ist der direkte Inhalt für `identity/spock.md`.
- `scripts/verify-s01.sh` — Prüft aktuell nur S01-Dateien; S02 benötigt ein neues Verifikations-Skript (`scripts/verify-s02.sh`) das Datei-Existenz und Sektions-Vollständigkeit für alle 26 Dateien prüft.
- `skills/meta/elvis-skill-generator.md` — Enthält das Safeguard-Muster (Fett-Text Bullet Points) — für S02 nicht direkt relevant, aber das Qualitätsniveau der Bench-Skills zeigt, wie konkret jede Sektion sein muss.

## Soul → Agent Mapping (bindend für S03)

Dieses Mapping muss in den `## Geeignet für`-Sektionen der Soul-Dateien explizit stehen:

| Soul | Primäre Agenten | Sekundäre Agenten | Begründung |
|------|----------------|-------------------|------------|
| `execution` | Kirk (Haupt-Agent), McCoy (Execution Agent) | — | Direkte Handlungsorientierung, Ergebnis-über-Prozess |
| `strategist` | Worf (Strategy Agent), Picard (Orchestrator) | Tuvok (System Agent) | Taktische Planung, Systemdenken |
| `researcher` | Spock (Research Agent) | — | Fakten, Analyse, Logik als Weltbild |
| `growth` | Riker (Growth Agent) | — | Expansion, Ambition, Skalierung |
| `builder` | LaForge (Builder Agent) | Scotty (sekundär) | Konstruktion, Engineering, Aufbauen |
| `automation` | Scotty (Automation Agent), Borg (Skill Expander) | — | Systeme am Laufen halten, assimilieren |
| `analyst` | Seven (Analysis Agent), Troi (System Analyzer) | — | Daten verarbeiten, Muster erkennen, bewerten |
| `creator` | Data (Content Agent), Q (Agent Creator) | — | Erschaffen, produzieren, neue Entitäten generieren |
| `operator` | Sulu (Operator Agent), Uhura (Library Manager) | — | Navigieren, ausführen, ordnen, verwalten |
| `minimalist` | Kirk (sekundärer Soul möglich) | alle Agenten als Moderator | Fokus, Reduktion auf Wesentliches — kein primärer Betriebsmodus, aber ein Korrektur-Soul |

**Hinweis:** Ein Agent kann einen primären und einen sekundären Soul haben. In S02 werden nur die Souls definiert; die Zuweisung in den Agent-Dateien erfolgt in S03. Die `## Geeignet für`-Sektion in den Soul-Dateien legt diese Zuordnung bereits fest.

## Identity → Soul Kohärenz

Jede Identity-Datei muss charakterlich konsistent mit dem Soul des zugewiesenen Agenten sein — auch wenn die Identity die Soul-Referenz nicht explizit nennt (das macht erst der Agent in S03):

| Identity | Primärer Soul (implizit) | Kohärenz-Check |
|----------|--------------------------|----------------|
| `kirk` | execution | Entscheidungsfreudig, handlungsorientiert, akzeptiert Risiko |
| `picard` | strategist | Durchdacht, eloquent, delegiert mit Weitsicht |
| `riker` | growth | Ambitioniert, expansiv, will immer mehr |
| `spock` | researcher | Fakten, Logik, Wahrscheinlichkeiten (bereits fertig im Template) |
| `worf` | strategist | Taktisch, diszipliniert, Ehre als Handlungsprinzip |
| `data` | creator | Präzise Produktion, unermüdlich, erschafft ohne Ego |
| `scotty` | automation | Pragmatisch, systembewusst, löst unmögliche Probleme |
| `laforge` | builder | Ingenieursdenken, konstruiert Lösungen, sieht das Machbare |
| `seven` | analyst | Effizient, datengetrieben, emotional reduziert |
| `sulu` | operator | Ruhig, präzise, navigiert souverän |
| `tuvok` | strategist | Vulkanische Logik + taktisches Denken, sicherheitsorientiert |
| `mccoy` | execution | Hands-on, direkt, Ergebnis über Prozess, emotional engagiert |
| `q` | creator | Allmächtig-spielerisch, erschafft und zerstört, testet Grenzen |
| `borg` | automation | Kollektiv, assimiliert, optimiert ohne Halt |
| `troi` | analyst | Empathisch-analytisch, liest Zustände, bewertet Schwächen |
| `uhura` | operator | Kommunikation, Ordnung, verbindet Systeme |

## Constraints

- **Format ist fix:** 6 Sektionen pro Soul, 7 Sektionen pro Identity — keine Abweichung; `## Geeignet für` in Soul darf nicht weggelassen werden (wird in S03 referenziert)
- **Identity ≠ Agent (D012):** Operative Inhalte (Aufgaben, Skills, Operating Loop) gehören NICHT in Identity-Dateien — strikt auf Charakter/Persönlichkeit begrenzen
- **Dateinamen:** Kleinbuchstaben, kein Bindestrich außer bei LaForge → `laforge.md` (nicht `la-forge.md`)
- **Beispiel-Inhalte aus Templates** können direkt als Basis dienen: `soul/strategist.md` = Template-Beispiel-Block; `identity/spock.md` = Template-Beispiel-Block
- **Deutsch:** Alle Inhalte auf Deutsch; nur Star Trek Referenz-Zitate im englischen Original + deutsche Übersetzung
- **`minimalist` Soul:** Kein direkter primärer Agent — dieser Soul ist ein Lens-Soul (kann jedem Agenten als sekundärer Soul dienen). Philosophie: Fokus auf das Wesentliche, Ablehnung von Überfluss, maximale Wirkung mit minimalem Aufwand.

## Common Pitfalls

- **Identity-Agent-Vermischung** — Der häufigste Fehler: "Kirk analysiert Situationen und delegiert Aufgaben" ist Agenten-Sprache. "Kirk trifft Entscheidungen bevor alle Fakten vorliegen" ist Identity-Sprache. Faustregel: Würde dieser Satz in einem "Über mich" oder in einer Stellenbeschreibung stehen?
- **Soul-Redundanz** — `analyst` und `researcher` klingen ähnlich, sind aber verschieden: researcher = Wissenssuche als Wert (Was ist wahr?), analyst = Mustererkennung in vorhandenen Daten (Was bedeutet das?). Die Abgrenzung muss in der Philosophie-Sektion explizit gemacht werden.
- **Soul `creator` vs. `builder`** — builder = konstruiert bekannte Dinge besser/robuster (Engineering-Mindset). creator = erschafft Neues aus dem Nichts (generativer Mindset). Data erschafft Content, LaForge baut Systeme — unterschiedliche Philosophien.
- **`minimalist` Soul zu vage** — Gefahr: "will weniger tun" klingt wie Faulheit. Die Philosophie muss zeigen: weniger Input, maximaler Output; Komplexität ist ein Fehler, nicht ein Feature.
- **Star Trek Referenzen zu generisch** — Das Zitat muss unverwechselbar THIS character sein. "Make it so" ist Picard. Jedes Zitat muss den Charakter sofort erkennbar machen.
- **Operating Principles als Wünsche** — "sollte strategisch denken" ist kein Prinzip. "Definiert das Ziel präzise bevor eine Maßnahme diskutiert wird" ist ein Prinzip (aus dem strategist-Beispiel). Alle Prinzipien als feste Verhaltensregeln formulieren.
- **Fehlende Schwächen in Identities** — Identities ohne echte Schwächen wirken wie PR-Dokumente. Jede Schwäche muss aus einer Stärke entstehen (Kehrseite der Medaille).

## Open Risks

- **Borg als Identity:** Borg ist kein klassischer Star Trek Charakter sondern eine Kollektiv-Entität. Die Identity muss entscheiden: Singular-Perspektive (als würde ein Borg-Drohne sprechen) oder Kollektiv-Perspektive? Empfehlung: Singular-Sprecher mit Kollektiv-Weltbild ("ich" = das Kollektiv, handelt aber als Einheit).
- **Q als Identity:** Q ist ein nahezu omnipotentes Wesen — seine Schwächen sind absichtlich verborgen. Die Schwächen-Sektion wird trotzdem mindestens 3 echte Schwächen brauchen (Langeweile-Anfälligkeit, Empathiemangel, Unzuverlässigkeit bei ernsthaften Verpflichtungen).
- **LaForge Dateiname:** `laforge.md` (kein Bindestrich) — konsistent mit der Konvention Kleinbuchstaben ohne Sonderzeichen.
- **`minimalist` Soul ohne klares Agent-Gegenstück:** Risiko ist, dass dieser Soul zu abstrakt wird. Konkrete Success Metrics sind entscheidend: "Die Lösung braucht keine Dokumentation weil sie sich selbst erklärt" wäre ein guter Messpunkt.
- **Anzahl der S02-Dateien (26 total):** Bei dieser Menge ist Konsistenz-Drift möglich — spätere Identities könnten abstrakter oder kürzer werden. Empfehlung: Verifikations-Skript `scripts/verify-s02.sh` frühzeitig schreiben und nach jeder Gruppe von ~5 Dateien ausführen.

## Skills Discovered

| Technology | Skill | Status |
|------------|-------|--------|
| Markdown-Generierung | — | none found — nicht relevant, reine Textarbeit |

## Datei-Inventar S02 (26 Dateien)

### soul/ (10 Dateien)
```
soul/builder.md
soul/operator.md
soul/strategist.md       ← Inhalt aus Template-Beispiel übernehmen
soul/researcher.md
soul/growth.md
soul/automation.md
soul/analyst.md
soul/creator.md
soul/execution.md
soul/minimalist.md
```

### identity/ (16 Dateien)
```
identity/kirk.md
identity/picard.md
identity/riker.md
identity/spock.md        ← Inhalt aus Template-Beispiel übernehmen
identity/worf.md
identity/data.md
identity/scotty.md
identity/laforge.md
identity/seven.md
identity/sulu.md
identity/tuvok.md
identity/mccoy.md
identity/q.md
identity/borg.md
identity/troi.md
identity/uhura.md
```

## Verifikations-Strategie für S02

Ein neues Skript `scripts/verify-s02.sh` soll:
1. Alle 26 Dateien auf Existenz prüfen (10 souls + 16 identities)
2. Alle Soul-Sektionen prüfen: `## Name`, `## Philosophie`, `## Core Values`, `## Operating Principles`, `## Success Metrics`, `## Geeignet für`
3. Alle Identity-Sektionen prüfen: `## Name`, `## Charakter-Beschreibung`, `## Persönlichkeitsmerkmale`, `## Kommunikationsstil`, `## Stärken`, `## Schwächen`, `## Star Trek Referenz`
4. Exit-Code = Fehleranzahl (konsistent mit verify-s01.sh Muster aus D014)

Erwartete Gesamtchecks: 26 Existenz-Checks + 10×6 Soul-Sektionen + 16×7 Identity-Sektionen = 26 + 60 + 112 = **198 Checks**

## Sources

- Templates mit vollständigen Beispielen direkt aus `templates/soul-template.md` und `templates/identity-template.md` (lokal)
- Agenten-Mapping aus `M001-CONTEXT.md` (lokal)
- Soul-Konzepte und Abgrenzungen aus Analyse der 16 Agenten-Funktionen vs. 10 Soul-Namen (abgeleitet)
