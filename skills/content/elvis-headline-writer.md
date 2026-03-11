# Skill

## Name

/elvis-headline-writer

## Beschreibung

Schreibt 7 Headline-Varianten für denselben Inhalt — je eine pro Formel: Zahl, Frage, How-To, Secret, Warning, Result, Contrast. Jede Variante max. 100 Zeichen. Liefert Stärken-Ranking, Zielgruppen-Analyse und A/B-Test-Empfehlung für die 2 besten Varianten.

## Ziele

- 7 Headline-Varianten: je eine für alle 7 Formeln
- Jede Variante max. 100 Zeichen (explizit dokumentiert)
- Stärkste Variante empfohlen mit Begründung (Emotion + Zielgruppe)
- A/B-Test-Empfehlung: welche 2 Varianten testen

## Strategie

7 Formeln decken die wichtigsten psychologischen Trigger ab: Neugierde (Frage, Secret), Nutzen (Zahl, How-To), Dringlichkeit (Warning), Sozialem Beweis (Result) und Kontrast (Contrast). Die format-neutrale Ausrichtung unterscheidet sich von elvis-x-hook-writer: Headline-Writer erzeugt wiederverwendbare Überschriften für beliebige Plattformen und Formate — Hook-Writer erzeugt fertige Tweet-Varianten für X/Twitter.

## Einschränkungen

- Genau 7 Varianten — je eine pro Formel, nicht mehr, nicht weniger
- Jede Variante max. 100 Zeichen (zählen und dokumentieren)
- Formeln sind fest: (1) Zahl, (2) Frage, (3) How-To, (4) Secret, (5) Warning, (6) Result, (7) Contrast
- Templates je Formel einhalten (siehe Ausführungsschritte)
- Abgrenzung zu elvis-x-hook-writer: Headline-Writer ist format-neutral, Hook-Writer ist X-spezifisch
- Kein automatisches Posten — Output ist zur manuellen Freigabe bestimmt

## Ausführungsschritte

1. Formuliere die Kern-Aussage des Inhalts in 1 Satz (max. 20 Wörter): Was ist das zentrale Versprechen oder die zentrale Erkenntnis? Dokumentiere diesen Satz als "Kern-Aussage" vor den Varianten.
2. Schreibe Variante 1–4 nach Formel-Template: (1) Zahl: "7 Wege, um [Ergebnis]" oder "[Zahl] [Substantiv] die [Ergebnis] bringen"; (2) Frage: "Warum [Problem]?" oder "Wie [Ergebnis] in [Zeitraum]?"; (3) How-To: "So [Ergebnis] in [Zeitraum]" oder "So [Aktion] ohne [Hindernis]"; (4) Secret: "Das [Gruppe] nicht über [Thema] sagt" oder "Was [Gruppe] über [Thema] verschweigt". Je Variante: Zeichenzahl in Klammern dokumentieren.
3. Schreibe Variante 5–7 nach Formel-Template: (5) Warning: "Stopp: Bevor du [Aktion]..." oder "Nicht [Aktion] bis du [Bedingung] weißt"; (6) Result: "Ich habe [X] getan. Das ist passiert." oder "[Zeitraum] [Experiment]. Ergebnis: [Zahl/Ergebnis]"; (7) Contrast: "Die meisten [Aktion]. Ich nicht." oder "Alle sagen [These]. Hier ist warum sie falsch liegen." Je Variante: Zeichenzahl in Klammern dokumentieren.
4. Empfehle die stärkste Variante mit Begründung: (a) Welche Emotion spricht sie an (Neugierde, Dringlichkeit, Überraschung, Neid)? (b) Für welche Zielgruppe wirkt sie am stärksten? Begründung in max. 2 Sätzen.
5. Gib A/B-Test-Empfehlung: Wähle die 2 Varianten die sich psychologisch am stärksten unterscheiden (z.B. Zahl vs. Contrast). Begründe kurz warum dieser Vergleich aufschlussreich ist. Dokumentiere die 2 Test-Varianten als "A/B-Test: Variante X vs. Variante Y".

## Verifikation

- Kern-Aussage vorhanden: 1 Satz vor den Varianten
- Exakt 7 Varianten vorhanden, je mit Formel-Label (1–7)
- Alle Formeln benannt: Zahl, Frage, How-To, Secret, Warning, Result, Contrast
- Zeichenzahl je Variante ≤ 100 Zeichen, explizit dokumentiert
- Stärkste Variante empfohlen mit Emotion-Label und Zielgruppen-Nennung
- A/B-Test mit 2 Varianten empfohlen und begründet
- Failure-Indikator: Variante > 100 Zeichen → Meldung "Variante [N] zu lang ([X] Zeichen) — kürzen: [Vorschlag]"
- Akzeptanzkriterium: 7 Varianten in 7 Formeln, alle ≤ 100 Zeichen, Empfehlung + A/B-Test vorhanden

## Abhängigkeiten

- Input: Inhalt, Thema oder Kern-Aussage für die Headline-Varianten erstellt werden sollen
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

Kern-Aussage (1 Satz) + 7 Headline-Varianten (je mit Formel-Label, Text, Zeichenzahl) + Stärken-Empfehlung mit Begründung + A/B-Test-Empfehlung. Gesamtlänge: max. 350 Wörter, Markdown-Format.
