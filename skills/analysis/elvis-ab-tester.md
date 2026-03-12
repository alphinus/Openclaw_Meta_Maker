# Skill

## Name

/elvis-ab-tester

## Beschreibung

Entwirft A/B-Tests mit wissenschaftlicher Methodik als fortlaufendes Optimierungs-System: genau 2 Varianten, genau 1 getestete Variable, berechnete Stichprobengröße und 95 %-Signifikanz-Schwelle. Der Skill begleitet den gesamten Test-Zyklus von der Hypothese bis zur Entscheidung — und baut durch wöchentliche Test-Planung einen kontinuierlichen Verbesserungs-Rhythmus auf: ein abgeschlossener Test ergibt den nächsten Test.

## Ziele

- Formulierte Test-Hypothese im Format "Wenn [Variable X geändert wird], dann [Ergebnis Y], weil [Annahme Z]"
- Berechnete Mindeststichprobengröße pro Variante für 95 %-Signifikanz und 80 %-Power
- Klares Test-Design: 2 Varianten (Kontrolle vs. Variation), 1 primäre Erfolgsvariable, Laufzeit in Tagen
- Statistische Auswertung nach Testende: p-Wert-Einschätzung, Konfidenzintervall, Handlungsempfehlung
- Dokumentiertes Lerning: Was zeigt dieser Test unabhängig vom Ergebnis?

## Strategie

Der Skill verfolgt das "eine Variable"-Prinzip konsequent — jeder Test testet genau eine Änderung. Mehrere Variablen gleichzeitig zu testen macht es unmöglich den Effekt zuzuordnen. Die 95 %-Signifikanz-Schwelle ist der wissenschaftliche Standard: Sie akzeptiert eine 5 %-Wahrscheinlichkeit dass ein beobachteter Effekt zufällig ist. Die Stichprobengrößen-Berechnung kommt vor dem Test-Start — nicht danach ("optional stopping" ist einer der häufigsten Statistik-Fehler). Auch negative Test-Ergebnisse (keine signifikante Differenz) sind wertvolle Learnings.

## Einschränkungen

- Genau 2 Varianten (A = Kontrolle, B = Variation) — keine Multivariat-Tests (A/B/C)
- Genau 1 primäre Erfolgsvariable — sekundäre Metriken dürfen beobachtet, nicht entschieden werden
- Test läuft mindestens 7 Tage (Wochentag-Schwankungen ausgleichen), maximal 28 Tage
- Keine vorzeitigen Test-Abbrüche ("peeking") — festes End-Datum wird vor Test-Start festgelegt
- Stichprobengröße muss vor Teststart berechnet und bestätigt werden — kein nachträgliches Anpassen

## Ausführungsschritte

1. Formuliere die Test-Hypothese im Drei-Teile-Format: "Wenn [konkrete Variable X geändert wird, z.B. 'der Call-to-Action-Button von Blau auf Orange geändert wird'], dann [erwartetes Ergebnis Y, z.B. 'steigt die Klick-Rate um min. 10 %'], weil [begründende Annahme Z, z.B. 'Orange eine höhere Kontrast-Aufmerksamkeit erzeugt']." Prüfe: Ist die Variable isolierbar? Ist das Ergebnis messbar?
2. Definiere das Test-Design exakt: Variante A (Kontrolle) = aktueller Zustand, beschrieben in 1–2 Sätzen. Variante B (Variation) = präzise Beschreibung der einen Änderung (keine anderen Unterschiede!). Primäre Erfolgsvariable: welche eine Metrik entscheidet ob B gewonnen hat? Akzeptanz-Schwelle: um wie viel Prozent muss B besser sein damit die Änderung übernommen wird (Min. 5 %)?
3. Berechne die Mindeststichprobengröße pro Variante. Verwende die Faustformel für zwei Proportionen bei 95 % Konfidenz und 80 % Power: n ≈ (16 × p × (1−p)) / d² wobei p = erwartete Baseline-Conversion-Rate (als Dezimalzahl), d = erwartete minimale Differenz (als Dezimalzahl). Gib das Ergebnis in ganzen Zahlen an. Berechne die Gesamt-Testdauer: Stichprobengröße / täglicher Traffic = benötigte Tage. Runde auf volle Wochen auf.
4. Erstelle die Test-Durchführungs-Checkliste mit 10 Punkten: Vor Test-Start (Baseline-Wert messen, Traffic-Aufteilung 50/50 sicherstellen, End-Datum festlegen, Tracking einrichten), Während Test (täglich prüfen dass Traffic-Aufteilung stimmt, kein vorzeitiges Auswerten), Nach Test (Rohdaten exportieren, Ergebnis-Tabelle befüllen, statistischen Test berechnen, Entscheidung dokumentieren).
5. Erstelle die Ergebnis-Auswertungs-Vorlage: Tabelle mit 6 Feldern die nach Testende befüllt werden: Variante A Ergebnis (Wert + Stichprobe), Variante B Ergebnis (Wert + Stichprobe), Differenz in Prozentpunkten, Differenz in %, p-Wert-Einschätzung (< 0.05 = signifikant / ≥ 0.05 = nicht signifikant), Entscheidung (B übernehmen / A behalten / Test wiederholen mit größerer Stichprobe).
6. Formuliere vorab 3 mögliche Szenarien und die jeweilige Handlungsempfehlung: Szenario 1 (B signifikant besser): Was wird getan? Szenario 2 (kein signifikanter Unterschied): Was bedeutet das? Was ist das Lernprinzip? Szenario 3 (A signifikant besser als B): Was zeigt das über die Ausgangshypothese?
7. Schreibe das Learnings-Template: Unabhängig vom Test-Ergebnis dokumentieren: Was hat dieser Test über das Nutzerverhalten gezeigt? Welche Folgefrage entsteht? Welcher Test sollte als nächstes durchgeführt werden?

## Verifikation

- Hypothesen-Format: Drei-Teile-Format (Wenn / dann / weil) vollständig ausgefüllt
- Eine Variable: Test-Design enthält exakt 1 Unterschied zwischen Variante A und B
- Stichprobe berechnet: Formel angewendet, Ergebnis in ganzen Zahlen, Testdauer in vollen Wochen
- Szenarien vorbereitet: Alle 3 Szenarien mit Handlungsempfehlung dokumentiert
- Failure-Indikator: Wenn die berechnete Stichprobengröße weniger als 100 pro Variante ergibt → Skill gibt aus: "Stichprobe zu klein (< 100 pro Variante) — Test nicht statistisch valide. Baseline-Conversion-Rate oder erwartete Differenz anpassen, oder Test auf einen Kanal mit höherem Traffic verschieben."
- Akzeptanzkriterium: Test-Design vollständig, Stichprobengröße berechnet, Durchführungs-Checkliste erstellt, Ergebnis-Auswertungsvorlage bereit

## Abhängigkeiten

- Input: Baseline-Conversion-Rate für die Erfolgsmetrik, aktueller täglicher Traffic auf dem Test-Element, genaue Beschreibung der einen Variable die getestet werden soll
- Empfohlene Vorgänger-Skills: /elvis-funnel-analyzer (identifiziert welche Funnel-Stufe am meisten Optimierungspotenzial hat), /elvis-performance-tracker (liefert Baseline-Metriken für Stichprobenberechnung)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) Test-Hypothese und Test-Design (Variante A/B, primäre Erfolgsvariable, Akzeptanz-Schwelle), (2) Stichprobengrößen-Berechnung mit Formel und Testdauer, (3) Durchführungs-Checkliste (10 Punkte), (4) Ergebnis-Auswertungs-Vorlage (nach Testende befüllbar), (5) Szenarien-Planung (3 Szenarien + Learnings-Template). Sofort einsatzbereit als vollständige Test-Dokumentation.
