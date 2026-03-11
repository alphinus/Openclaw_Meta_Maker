# Skill

## Name

/elvis-niche-finder

## Beschreibung

Bewertet 5 potenzielle Nischen für einen X/Twitter-Account nach 4 Kriterien: Marktgröße, Wettbewerbs-Intensität, Monetarisierbarkeit und Expertise-Fit. Jede Nische erhält einen Gesamt-Score von 4–20 Punkten. Output: Scoring-Tabelle 5 × 5 plus Empfehlung der Top-Nische mit Begründung.

## Ziele

- 5 Nischen-Kandidaten definiert und vollständig nach 4 Kriterien bewertet
- Scoring-Tabelle 5 × 5 (5 Nischen × 4 Kriterien + Gesamt-Score) erstellt
- Gesamt-Score pro Nische berechnet (4–20 Punkte, je Kriterium 1–5)
- Top-Nische mit höchstem Gesamt-Score identifiziert und mit Begründung empfohlen
- Risiko-Hinweis für Nischen mit Score ≤ 10/20 formuliert

## Strategie

Nischen-Wahl ist die wichtigste Einzel-Entscheidung für Account-Wachstum — falsch gewählt kostet Monate. Die 4-Kriterien-Matrix zwingt zur Trennung zwischen attraktiven und erreichbaren Nischen: hohe Marktgröße allein reicht nicht, wenn der Wettbewerb undurchdringlich ist. Expertise-Fit verhindert den häufigen Fehler, eine lukrative Nische zu wählen, für die man keine glaubwürdige Stimme hat. Der Score-Range 4–20 (nicht 0–20) stellt sicher, dass jede Nische mindestens als "möglich" eingestuft wird — keine Nische wird pauschal ausgeschlossen.

## Einschränkungen

- Genau 5 Nischen bewerten — nicht mehr (Entscheidungsparalyse), nicht weniger (zu wenig Auswahl)
- Genau 4 Kriterien, Score je 1–5 (keine halben Punkte)
- Gesamt-Score = Summe der 4 Kriterien-Scores (4–20 Punkte)
- Empfehlung: genau 1 Top-Nische (auch bei Gleichstand: Tie-Breaker über Expertise-Fit)
- Begründung der Empfehlung: max. 100 Wörter

## Ausführungsschritte

1. Definiere 5 Nischen-Kandidaten: Leite sie aus der eigenen Expertise, bestehenden Interessen und ersten Marktbeobachtungen auf X ab. Pro Nische: Kurz-Label (2–4 Wörter), Zielgruppen-Beschreibung (1 Satz), 3 repräsentative Hashtags oder Schlüssel-Accounts. Dokumentiere die 5 Nischen als nummerierte Liste mit den genannten Feldern.
2. Bewerte jede Nische nach Kriterium 1 — Marktgröße: Schätze die Anzahl der Community-Accounts auf X, die explizit dieser Nische zuzuordnen sind (Suche per Hashtag + Bio-Keywords). Score-Skala: 1 = < 500 Accounts, 2 = 500–2.000, 3 = 2.000–10.000, 4 = 10.000–50.000, 5 = > 50.000. Dokumentiere Schätz-Grundlage pro Nische (1 Satz).
3. Bewerte jede Nische nach Kriterium 2 — Wettbewerbs-Intensität: Zähle die Top-10 Accounts dieser Nische mit > 10.000 Followern. Score-Skala (invertiert — weniger Wettbewerb = höherer Score): 1 = ≥ 8 solcher Accounts, 2 = 5–7, 3 = 3–4, 4 = 1–2, 5 = 0. Dokumentiere die gezählten Accounts pro Nische mit @Handle und Follower-Größenordnung.
4. Bewerte jede Nische nach Kriterium 3 — Monetarisierbarkeit (Produkt/Kurs/Consulting-Potenzial, Score 1–5): 1 = keine offensichtliche Zahlungsbereitschaft, 2 = Micro-Produkte möglich (< 50 €), 3 = Digitale Produkte etabliert (50–200 €), 4 = Kurse und Consulting marktfähig (200–1.000 €), 5 = High-Ticket-Angebote nachgefragt (> 1.000 €). Dann Kriterium 4 — Expertise-Fit (eigenes Wissen 1–5): 1 = kein Vorwissen, 3 = solides Fundament, 5 = ausgewiesener Experte. Dokumentiere Begründung je Kriterium pro Nische (max. 1 Satz).
5. Erstelle die Scoring-Tabelle (5 Zeilen × 6 Spalten): Nische | Marktgröße (1–5) | Wettbewerb (1–5) | Monetarisierung (1–5) | Expertise (1–5) | Gesamt (4–20). Berechne den Gesamt-Score als Summe der 4 Kriterien. Identifiziere die Top-Nische (höchster Score; Tie-Breaker: Expertise-Fit). Formuliere die Empfehlung: Name der Top-Nische, Gesamt-Score, 3 Stärken, 1 Risiko, 1 erster konkreter Schritt (max. 100 Wörter gesamt).

## Verifikation

- Scoring-Tabelle: Genau 5 Zeilen (Nischen) × 6 Spalten (4 Kriterien + Gesamt + Nischen-Label)
- Score-Range: Jeder Einzel-Score 1–5, jeder Gesamt-Score 4–20 (mathematisch korrekt)
- Empfehlung: Genau 1 Top-Nische benannt mit Gesamt-Score, 3 Stärken, 1 Risiko, 1 erster Schritt
- Failure-Indikator: Alle 5 Nischen erzielen Gesamt-Score ≤ 10/20 → Meldung: "Keine valide Nische identifiziert — alle 5 Kandidaten unter 50% des Maximal-Scores. 5 neue Nischen-Kandidaten definieren oder Expertise-Bereich erweitern."
- Akzeptanzkriterium: 5 × 5 Scoring-Tabelle vollständig, Top-Nische empfohlen mit Begründung ≤ 100 Wörter, alle Scores nachvollziehbar belegt

## Abhängigkeiten

- Input: Eigene Expertise-Felder, bestehende Interessen, grobe Marktbeobachtungen auf X
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

Scoring-Tabelle (5 Nischen × 4 Kriterien + Gesamt-Score) im Markdown-Tabellenformat plus Empfehlungs-Block (Top-Nische, Score, 3 Stärken, 1 Risiko, 1 erster Schritt). Gesamtlänge: max. 500 Wörter. Dient als Eingabe für elvis-monetization-planner.
