# Skill

## Name

/elvis-scenario-planner

## Beschreibung

Entwickelt 3 strukturierte Zukunftsszenarien (Best Case / Base Case / Worst Case) mit je 5 Annahmen, 3 Konsequenzen und 1 Strategie-Anpassung. Definiert messbare Entscheidungs-Trigger die anzeigen ab welchem Metrik-Wert ein Szenario-Wechsel eintritt. Schützt vor Single-Point-of-Failure-Planung und reaktivem statt proaktivem Handeln.

## Ziele

- 3 vollständige Szenarien (Best / Base / Worst) mit je 5 Annahmen dokumentiert
- 3 Konsequenzen pro Szenario identifiziert (je 1 für Wachstum, Ressourcen, Risiko)
- 1 Strategie-Anpassung pro Szenario formuliert (Was ändert sich am Vorgehen?)
- Entscheidungs-Trigger für alle 3 Szenarien definiert (Metrik + Schwellenwert + Zeitfenster)
- Szenario-Monitoring-Plan: 3 KPIs die wöchentlich zu beobachten sind um Szenario-Drift früh zu erkennen

## Strategie

Szenario-Planung ist kein Pessimismus — sie ist strukturierte Vorbereitung. Base Case ist das realistischste Szenario, nicht das erwünschte. Best Case und Worst Case sind keine Extremwerte um "Safe" und "Panic" zu markieren, sondern plausible Szenarien mit konkreten Annahmen-Sets. Die Entscheidungs-Trigger sind der Kern: sie verwandeln Szenarien von abstrakten Narrativen in operative Handlungsanweisungen — wann genau wird das Vorgehen geändert?

## Einschränkungen

- Genau 3 Szenarien (Best Case / Base Case / Worst Case — keine anderen Labels)
- Genau 5 Annahmen pro Szenario (mehr führt zu Überlappung und Verwässerung)
- Entscheidungs-Trigger: müssen eine messbare Metrik, einen konkreten Schwellenwert und ein Zeitfenster enthalten — keine vagen Trigger wie "wenn es schlecht läuft"
- Annahmen müssen szenario-spezifisch sein (nicht alle 3 Szenarien dieselben Annahmen mit anderem Vorzeichen)
- Keine Prognosen als Fakten darstellen — alle Aussagen als Annahmen kennzeichnen

## Ausführungsschritte

1. Definiere den Planungs-Horizont und das Thema: In welchem Bereich wird geplant (Wachstum, Produkteinführung, Monetarisierung, etc.)? Welcher Zeitraum wird abgedeckt (3 / 6 / 12 Monate)? Was ist der kritischste Unsicherheitsfaktor? Dokumentiere in 3 Feldern (je 1 Satz).
2. Entwickle 5 Annahmen für den Base Case (realistischstes Szenario): Was ist zu erwarten wenn alles nach Plan läuft? Annahmen betreffen: (1) Markt-/Umfeld-Entwicklung, (2) eigene Ressourcen und Kapazitäten, (3) Zielgruppen-Verhalten, (4) Wettbewerb, (5) externe Faktoren (Regulierung, Technologie). Je Annahme: 1 Satz mit konkreten Zahlen wo möglich.
3. Entwickle 5 Annahmen für den Best Case (optimistisches aber plausibles Szenario): Mindestens 3 der 5 Annahmen müssen sich konkret vom Base Case unterscheiden (kein "wie Base Case aber besser"). Selbe 5 Kategorien wie in Schritt 2.
4. Entwickle 5 Annahmen für den Worst Case (pessimistisches aber plausibles Szenario): Mindestens 3 der 5 Annahmen müssen sich konkret vom Base Case unterscheiden. Selbe 5 Kategorien. Worst Case = realistisches Negativszenario, nicht Katastrophen-Fantasie.
5. Leite pro Szenario 3 Konsequenzen ab und formuliere 1 Strategie-Anpassung: Konsequenz 1: Auswirkung auf Wachstumsrate oder Reichweite. Konsequenz 2: Auswirkung auf Ressourcen (Zeit, Budget, Team). Konsequenz 3: Wichtigstes Risiko das entsteht oder wegfällt. Strategie-Anpassung (1–2 Sätze): Was ändert sich konkret am Vorgehen in diesem Szenario?
6. Definiere den Entscheidungs-Trigger für jedes Szenario: Format — "Wenn [Metrik] [Schwellenwert] innerhalb von [Zeitfenster] erreicht → wechsle zu [Szenario] und aktiviere [Strategie-Anpassung]". Beispiel: "Wenn Follower-Wachstum < 3 % pro Woche über 4 Wochen → Worst Case aktiv → Content-Frequenz auf 14x/Woche erhöhen." Je Szenario 1 primärer Trigger.
7. Erstelle den Szenario-Monitoring-Plan: Benenne 3 KPIs die wöchentlich zu beobachten sind um Szenario-Drift früh zu erkennen. Für jeden KPI: Name, Mess-Methode, Frequenz (wöchentlich), aktueller Ist-Wert (falls bekannt) und Zielbereich für Base Case.

## Verifikation

- Szenarien-Vollständigkeit: Alle 3 Szenarien × 5 Annahmen + 3 Konsequenzen + 1 Strategie-Anpassung = 27 Felder befüllt
- Annahmen-Differenzierung: Best und Worst Case unterscheiden sich in mindestens 3 von 5 Annahmen vom Base Case
- Entscheidungs-Trigger: Alle 3 Trigger enthalten Metrik + Schwellenwert + Zeitfenster (kein einziger vager Trigger)
- Monitoring-Plan: 3 KPIs mit Mess-Methode und Ist-Wert (oder Hinweis "unbekannt") dokumentiert
- Failure-Indikator: Wenn für eines der 3 Szenarien kein Entscheidungs-Trigger definiert ist → Skill gibt aus: "Entscheidungs-Trigger unvollständig: Alle 3 Szenarien (Best/Base/Worst Case) benötigen je 1 messbaren Trigger. Fehlende Trigger jetzt definieren."

## Abhängigkeiten

- Input: Planungs-Thema (1–3 Sätze), Zeitraum, aktueller Ist-Stand in 2–3 relevanten Metriken
- Empfohlene Vorgänger-Skills: /elvis-risk-assessment (Risiko-Profil für Worst-Case-Annahmen), /elvis-growth-strategy (Wachstumsziele für Best-Case-Kalibrierung)

## Output

3 Szenario-Blöcke (je 5 Annahmen + 3 Konsequenzen + 1 Strategie-Anpassung + 1 Entscheidungs-Trigger), Szenario-Monitoring-Plan (3 KPIs). Gesamtlänge: max. 900 Wörter.
