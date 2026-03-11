# Skill

## Name

/elvis-decision-framework

## Beschreibung

Strukturierter Entscheidungsrahmen für komplexe, folgenreiche Entscheidungen: bewertet bis zu 3 Alternativen anhand einer 5-Kriterien-Matrix (Gewichtung 1–3 × Score 1–5), führt einen Sensitivitäts-Check durch und liefert eine dokumentierte Entscheidungsempfehlung. Verhindert Bauchentscheidungen bei hoher Unsicherheit oder hohem Einsatz.

## Ziele

- 5 Entscheidungskriterien mit Gewichtung (1–3) und individueller Begründung definiert
- 3 Alternativen vollständig bewertet (5 Kriterien × Score 1–5 = gewichteter Gesamt-Score)
- Sensitivitäts-Check abgeschlossen: identifiziert welche Kriterien die Entscheidung kippen
- Dokumentierte Entscheidungsempfehlung mit Begründung (3 Sätze) und nächstem Schritt
- Entscheidungs-Log (1 Seite) als Referenz für Rückblick und Lerneffekte erstellt

## Strategie

Die Bewertungsmatrix erzwingt explizite Priorisierung: Kriterien-Gewichtungen müssen vor der Bewertung festgelegt werden, um Confirmation Bias zu vermeiden. Der Sensitivitäts-Check ist kein optionaler Schritt — er deckt auf, ob die Entscheidung robust ist oder von einem einzigen Kriterium abhängt. Entscheidungen die den Sensitivitäts-Check nicht bestehen (Ergebnis kippt bei Entfernung eines Kriteriums) erfordern zusätzliche Informationsbeschaffung vor dem Abschluss.

## Einschränkungen

- Genau 5 Kriterien bewerten (nicht weniger, nicht mehr — Fokus erzwingen)
- Mindestens 2, maximal 3 Alternativen (weniger = keine echte Wahl, mehr = Entscheidungslähmung)
- Gewichtungen: 1 = niedrig, 2 = mittel, 3 = hoch (keine anderen Werte)
- Scores: 1–5 ganzzahlig (keine halben Punkte)
- Keine Empfehlung ohne abgeschlossenen Sensitivitäts-Check
- Keine externen Datenabfragen oder API-Aufrufe ohne explizite Operator-Freigabe

## Ausführungsschritte

1. Kläre die Entscheidungssituation: Formuliere die Entscheidungsfrage in 1 Satz ("Soll ich X oder Y tun?"), benenne die 3 Alternativen (A1, A2, A3) und setze einen Entscheidungs-Deadline (Datum). Dokumentiere in einem 3-Felder-Block.
2. Definiere 5 Entscheidungskriterien: Jedes Kriterium bekommt (a) einen Namen (1–3 Wörter), (b) eine Gewichtung 1–3 (1=nice-to-have, 2=wichtig, 3=kritisch) und (c) eine Begründung in 1 Satz warum dieses Kriterium für diese Entscheidung relevant ist. Erstelle eine Kriterien-Tabelle mit 3 Spalten: Kriterium | Gewichtung | Begründung.
3. Bewerte jede der 3 Alternativen für alle 5 Kriterien: Score 1–5 (1=sehr schlecht bis 5=sehr gut). Berechne den gewichteten Score pro Kriterium: Gewichtung × Score. Summiere alle 5 gewichteten Scores zur Gesamtpunktzahl pro Alternative. Erstelle eine Bewertungsmatrix als Markdown-Tabelle: 4 Spalten (Kriterium/Gewichtung | A1 Score×G | A2 Score×G | A3 Score×G) + Gesamt-Zeile.
4. Führe den Sensitivitäts-Check durch: Entferne nacheinander jedes der 5 Kriterien und berechne die neue Rangliste. Dokumentiere in 5 Zeilen: "Ohne [Kriterium X]: Reihenfolge A? > A? > A?" — prüfe ob die führende Alternative in allen 5 Varianten dieselbe bleibt. Falls ja: Entscheidung ist robust. Falls nein: benenne welche Kriterien die Entscheidung kippen und warum das relevant ist.
5. Formuliere die Entscheidungsempfehlung in 3 Sätzen: (1) Empfohlene Alternative mit Gesamt-Score, (2) wichtigste Begründung (2–3 ausschlaggebende Kriterien), (3) Hauptrisiko der empfohlenen Alternative und Gegenmaßnahme. Ergänze den konkreten nächsten Schritt (1 Aktion mit Zeitrahmen).
6. Erstelle den Entscheidungs-Log als Markdown-Block mit 6 Feldern: Entscheidungsfrage | Datum | Alternativen (3) | Gewinner + Score | Sensitivitäts-Check-Ergebnis (robust/anfällig + Kriterium) | Nächster Schritt. Dieser Log dient als Referenz für den Rückblick nach 30–90 Tagen.

## Verifikation

- Matrix-Vollständigkeit: Alle 3 Alternativen × 5 Kriterien = 15 Bewertungs-Felder ausgefüllt, alle mit Gewichtung multipliziert
- Sensitivitäts-Check: Genau 5 Szenarien ("Ohne Kriterium X") dokumentiert, Robustheit explizit bewertet
- Empfehlung: Enthält Gesamt-Score, Begründung und Gegenmaßnahme für Hauptrisiko
- Entscheidungs-Log: Alle 6 Felder befüllt
- Failure-Indikator: Wenn weniger als 2 vollständig bewertete Alternativen vorliegen (weniger als 10 ausgefüllte Score-Felder) → Skill gibt aus: "Entscheidungsmatrix unvollständig: Mindestens 2 Alternativen mit je 5 Kriterien erforderlich. Fehlende Bewertungen bitte ergänzen."

## Abhängigkeiten

- Input: Entscheidungsfrage (1 Satz), 2–3 konkrete Alternativen, grobe Kriterien-Vorstellung (kann vom Skill verfeinert werden)
- Empfohlene Vorgänger-Skills: /elvis-risk-assessment (Risiko-Profil der Alternativen), /elvis-scenario-planner (Zukunfts-Szenarien als Bewertungskontext)

## Output

Bewertungsmatrix (5×3 Felder mit gewichteten Scores + Gesamt-Zeile), Sensitivitäts-Check (5 Szenarien + Robustheitsbewertung), Entscheidungsempfehlung (3 Sätze + nächster Schritt), Entscheidungs-Log (6 Felder). Gesamtlänge: max. 600 Wörter.
