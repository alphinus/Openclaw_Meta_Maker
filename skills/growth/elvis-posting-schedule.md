# Skill

## Name

/elvis-posting-schedule

## Beschreibung

Erstellt einen vollständigen 4-Wochen-Posting-Plan für einen X/Twitter-Account. Basierend auf Analytics-Daten werden die besten Posting-Zeiten und ein ausgewogener Content-Mix (5 Kategorien) definiert, ergänzt durch einen 28-Tage-Kalender und 2 Puffer-Slots pro Woche für Breaking-Topics.

## Ziele

- 3 optimale Posting-Zeitfenster aus Analytics-Daten identifiziert und begründet
- Content-Mix mit 5 Kategorien und %-Anteilen definiert (Summe = 100 %)
- Themen-Rotation über 4 Wochen geplant (kein Thema wiederholt sich öfter als 2× pro Woche)
- Kalender-Tabelle mit 28 Zeilen (7 Tage × 4 Wochen) vollständig befüllt
- 8 Puffer-Slots reserviert (2 pro Woche für Breaking-Topics)

## Strategie

Der Plan balanciert Konsistenz mit Flexibilität: feste Zeitfenster und Kategorien geben dem Algorithmus stabile Signale, die 2 Puffer-Slots pro Woche erlauben Reaktion auf aktuelle Ereignisse. Content-Mix-Prozente werden aus den besten Mustern der Konkurrenz-Analyse abgeleitet — nicht erfunden. Der 4-Wochen-Horizont ist lang genug für Muster, kurz genug für Anpassungen.

## Einschränkungen

- Exakt 4 Wochen Planungshorizont (28 Tage) — kein längerer Zeitraum
- Max. 5 Content-Kategorien im Mix — mehr erzeugt Inkohärenz
- Puffer-Slots: genau 2 pro Woche, nicht mehr (Spontanität vs. Plan-Integrität)
- Posting-Zeitfenster: max. 3 Optionen — mehr überfordert die Ausführung
- Kalender-Tabelle: ein Post-Slot pro Zeile (manche Tage können mehrere Zeilen haben)

## Ausführungsschritte

1. Identifiziere die 3 besten Posting-Zeitfenster aus den Analytics der letzten 30 Tage (oder aus der Konkurrenz-Analyse als Proxy). Bewertungskriterium: höchste Durchschnitts-Engagement-Rate im jeweiligen Zeitblock (3-Stunden-Blöcke: 06–09, 09–12, 12–15, 15–18, 18–21, 21–00). Dokumentiere pro Zeitfenster: Uhrzeit, Wochentage (Mo–Fr / Sa–So), Durchschnitts-Engagement-Rate, Stichproben-Größe.
2. Definiere den Content-Mix mit genau 5 Kategorien und %-Anteilen (Summe = 100 %). Kategorien-Vorschlag als Ausgangspunkt: Bildung/Tipps (30 %), persönliche Erfahrungen (20 %), Nischen-Meinungen/Hot Takes (20 %), Engagement-Fragen/Polls (15 %), Kuratierter Content mit Kommentar (15 %). Passe die Kategorien an die Nische an und begründe jede Kategorie in 1 Satz.
3. Plane die Themen-Rotation über 4 Wochen: Weise jeder Woche 1–2 Schwerpunkt-Themen zu (aus der Nische). Stelle sicher, dass kein Schwerpunkt-Thema mehr als 2× pro Woche auftaucht. Dokumentiere die Themen-Rotation als 4-zeilige Liste (Woche 1–4, je Schwerpunkt + 1-Satz-Begründung für die Auswahl).
4. Erstelle die Kalender-Tabelle mit 28 Zeilen (mindestens 1 Post-Slot pro Tag, manche Tage 2 Slots). Spalten: Datum (KW + Wochentag), Uhrzeit-Slot, Content-Kategorie, Thema/Stichwort (5–10 Wörter), Puffer-Flag (Ja/Nein). Markiere 2 Puffer-Slots pro Woche mit "Puffer" in der Kategorie-Spalte und "Ja" im Puffer-Flag.
5. Prüfe den fertigen Plan auf Ausgewogenheit: Zähle tatsächliche %-Anteile der 5 Kategorien über alle 28 Tage. Vergleiche mit Soll-Mix. Weicht eine Kategorie um mehr als 10 Prozentpunkte ab, korrigiere 1–3 Slots und dokumentiere die Anpassung in einem kurzen Prüf-Protokoll (max. 3 Sätze).

## Verifikation

- Kalender-Vollständigkeit: Tabelle enthält genau 28 Tage, kein Tag ohne Post-Slot
- Puffer-Slots: Genau 8 Puffer-Slots im Gesamtplan (2 × 4 Wochen)
- Content-Mix-Abweichung: Keine Kategorie weicht mehr als 10 Prozentpunkte vom Soll ab
- Failure-Indikator: Weniger als 20 Posts über 28 Tage geplant (< 5 Posts/Woche) → Meldung: "Posting-Frequenz zu niedrig — mindestens 5 Posts/Woche für algorithmische Sichtbarkeit empfohlen. Plan anpassen."
- Akzeptanzkriterium: 28-Tage-Tabelle vollständig, 3 Zeitfenster definiert, 5 Kategorien mit %-Anteilen, 8 Puffer-Slots gesetzt, Prüf-Protokoll vorhanden

## Abhängigkeiten

- Input: Analytics-Daten der letzten 30 Tage (Engagement-Rate nach Uhrzeit) oder Konkurrenz-Analyse als Proxy; Nischen-Themen-Liste
- Empfohlene Vorgänger-Skills: elvis-growth-audit (für eigene Analytics-Basis), elvis-competitor-analysis (für Timing-Proxy falls Analytics fehlen)

## Output

4-Wochen-Posting-Kalender als Markdown-Tabelle (28 Zeilen, 5 Spalten) plus Dokumentations-Block: 3 Zeitfenster, 5 Content-Kategorien mit %-Anteilen, Themen-Rotation-Übersicht, Prüf-Protokoll. Gesamtlänge: max. 700 Wörter.
