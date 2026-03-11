# Skill

## Name

/elvis-resource-allocator

## Beschreibung

Optimiert die Aufteilung von Zeit, Geld und Energie auf 5 strategische Aktivitäten: führt eine 80/20-Analyse durch, erstellt ein Ressourcen-Budget in Prozent (muss zusammen 100 % ergeben) und definiert monatliche Überprüfungs-Trigger für die Reallokation. Verhindert verteilte Aufmerksamkeit und erzwingt explizite Priorisierung statt intuitiver Ressourcen-Drift.

## Ziele

- 5 strategische Aktivitäten identifiziert und mit aktuellem Ressourcen-Einsatz dokumentiert
- 80/20-Analyse abgeschlossen: welche 20 % der Aktivitäten bringen 80 % der Ergebnisse?
- Ressourcen-Budget erstellt: Zeit (%), Geld (%), Energie (%) je Aktivität — je Dimension 100 %
- Monatliche Überprüfungs-Trigger definiert: 3 Bedingungen bei denen reallociert wird
- Delta-Analyse: Ist-Verteilung vs. Soll-Verteilung — wo ist die größte Lücke?

## Strategie

Ressourcen-Allokation ohne explizite 80/20-Analyse führt zum "Busy ≠ Productive"-Fehler: viel Aktivität, wenig Output. Die 80/20-Analyse erzwingt die unbequeme Frage welche Aktivitäten trotz hohem Aufwand wenig bringen. Das Ressourcen-Budget in Prozent ist absichtlich in drei Dimensionen aufgeteilt (Zeit, Geld, Energie) — sie sind nicht austauschbar und werden oft unterschiedlich falsch verteilt. Die Summen-Constraint (je 100 %) macht Umverteilungs-Kosten sofort sichtbar: mehr für A bedeutet zwingend weniger für B.

## Einschränkungen

- Genau 5 strategische Aktivitäten (nicht mehr — Fokus erzwingen; nicht weniger — zu wenig Differenzierung)
- Ressourcen-Budget: Zeit-%, Geld-% und Energie-% je Aktivität müssen je Dimension exakt 100 % ergeben
- Budget-Angaben: ganzzahlig in %, Minimum 5 % je befüllter Kategorie (keine 0 %-Einträge für aktive Aktivitäten)
- 80/20-Analyse: konkrete Metrik benennen die "Ergebnis" definiert (nicht abstrakt "Mehrwert")
- Überprüfungs-Trigger: messbar formuliert mit Zeitrahmen (kein "wenn nötig")

## Ausführungsschritte

1. Identifiziere 5 strategische Aktivitäten: Was sind die 5 Aktivitäten auf die aktuell Zeit, Geld oder Energie verwendet wird? Je Aktivität: Name (1–3 Wörter), kurze Beschreibung (1 Satz) und strategisches Ziel (welchem übergeordneten Ziel dient diese Aktivität?). Falls mehr als 5 Aktivitäten existieren: die 5 ressourcenintensivsten auswählen.
2. Erfasse die Ist-Verteilung: Schätze den aktuellen Ressourcen-Einsatz pro Aktivität in den 3 Dimensionen: Zeit (Stunden/Woche oder %), Geld (€/Monat oder %), Energie (subjektiv 1–10 oder %). Dokumentiere als Tabelle: Aktivität | Zeit-Ist | Geld-Ist | Energie-Ist. Falls genaue Zahlen unbekannt: grobe Schätzung mit "(Schätzung)" markiert.
3. Führe die 80/20-Analyse durch: Definiere zuerst die Ergebnis-Metrik (z.B. "Follower-Wachstum pro Woche", "Umsatz €/Monat", "qualifizierte Leads"). Bewerte dann jede der 5 Aktivitäten: Welchen Anteil am Gesamt-Ergebnis (%) liefert sie? Ranke alle 5 nach Ergebnis-Beitrag. Identifiziere die "80/20-Gewinner" (typisch 1–2 Aktivitäten die ≥60 % des Ergebnisses liefern) und die "80/20-Verlierer" (Aktivitäten mit <10 % Ergebnis-Beitrag trotz nennenswertem Einsatz).
4. Erstelle das Soll-Ressourcen-Budget: Weise jeder Aktivität einen Soll-Wert zu für: Zeit (%), Geld (%), Energie (%). Soll = optimale Verteilung auf Basis der 80/20-Analyse (80/20-Gewinner bekommen mehr, Verlierer weniger). Jede der 3 Dimensionen muss exakt 100 % ergeben. Erstelle Budget-Tabelle mit Ist vs. Soll für alle 3 Dimensionen.
5. Führe die Delta-Analyse durch: Berechne die Differenz (Soll minus Ist) für jede Aktivität × Dimension. Identifiziere die 2 größten positiven Deltas (Aktivitäten die mehr Ressourcen bekommen sollen) und die 2 größten negativen Deltas (Aktivitäten die entlasten werden). Formuliere 2–3 konkrete Umverteilungs-Maßnahmen die sofort umgesetzt werden können.
6. Definiere 3 monatliche Überprüfungs-Trigger: Bedingungen bei denen das Budget automatisch re-evaluiert wird. Format: "Trigger [N]: Wenn [Bedingung] → Budget-Review innerhalb von [Zeitraum]." Beispiel: "Trigger 1: Wenn eine Aktivität den Ergebnis-Beitrag um >20 % gegenüber Vormonat ändert → Budget-Review innerhalb von 7 Tagen." Alle 3 Trigger müssen messbar sein.

## Verifikation

- Ist-Tabelle: 5 Aktivitäten × 3 Dimensionen (Zeit/Geld/Energie) = 15 Felder ausgefüllt
- Soll-Budget: Zeit-Summe = 100 %, Geld-Summe = 100 %, Energie-Summe = 100 % (je exakt)
- 80/20-Analyse: Ergebnis-Metrik definiert, 80/20-Gewinner und -Verlierer benannt
- Delta-Analyse: 2 positive und 2 negative Deltas identifiziert, Umverteilungs-Maßnahmen formuliert
- Failure-Indikator: Wenn die Zeit-%, Geld-% oder Energie-%-Spalten des Ressourcen-Budgets nicht exakt 100 % ergeben → Skill gibt aus: "Ressourcen-Budget ungültig: [Dimension] ergibt [X]% statt 100%. Aktivitäts-Werte korrigieren bis Summe 100% erreicht."

## Abhängigkeiten

- Input: Liste der 5 wichtigsten Aktivitäten, grobe aktuelle Ressourcen-Verteilung, übergeordnetes Hauptziel (1 Satz)
- Empfohlene Vorgänger-Skills: /elvis-prioritization-engine (priorisierte Aktivitäten als Input), /elvis-growth-strategy (Wachstumsziele als Referenz für Ergebnis-Metrik)

## Output

Ist-Ressourcen-Tabelle (5×3), 80/20-Analyse-Ergebnis (Gewinner + Verlierer), Soll-Budget-Tabelle (5×3, je Dimension 100 %), Delta-Tabelle (Ist vs. Soll), 2–3 Umverteilungs-Maßnahmen, 3 Überprüfungs-Trigger. Gesamtlänge: max. 700 Wörter.
