# Skill

## Name

/elvis-opinion-post

## Beschreibung

Erstellt einen klaren Meinungsbeitrag für X/Twitter nach der Struktur: Stance → Begründung → Konsequenz → Gegenargumente → Widerlegung. Liefert einen positionierten Single-Post (max. 500 Zeichen) oder einen 5-Tweet-Thread — ohne Weichmacher, mit Haltung.

## Ziele

- Stance in 1 Satz formuliert: klar positioniert, max. 100 Zeichen, kein Weichspülen
- Begründung mit 2–3 Sätzen, je mit Datenpunkt oder Erfahrung belegt
- Konsequenz in 1 Satz: was folgt aus der Position
- 2 Gegenargumente benannt und je mit 1 Satz widerlegt
- Output als Single-Post (max. 500 Zeichen) oder Thread (5 Tweets à max. 280 Zeichen)

## Strategie

Meinungsbeiträge erzeugen mehr Engagement als neutrale Inhalte — weil sie Leser zur Zustimmung oder zum Widerspruch provozieren. Die Stance-first-Struktur verhindert das häufigste Problem: zu lange Einleitung vor der eigentlichen Position. Gegenargumente + Widerlegung zeigen intellektuelle Redlichkeit und erhöhen Glaubwürdigkeit. Das Zeichenlimit erzwingt Präzision — jede Aussage muss das Gewicht tragen.

## Einschränkungen

- Stance enthält keine Weichmacher: kein "vielleicht", "könnte", "es kommt drauf an", "in manchen Fällen"
- Begründung: mindestens 1 konkreter Datenpunkt oder persönliche Erfahrung pro Satz
- Single-Post: Gesamt max. 500 Zeichen
- Thread: genau 5 Tweets, je max. 280 Zeichen; Tweet 1 = Stance, Tweets 2–4 = Begründung/Konsequenz/Gegenargumente, Tweet 5 = Widerlegung + CTA
- Kein automatisches Posten — Output ist zur manuellen Freigabe bestimmt
- Format-Wahl: Single-Post wenn Stance + Begründung in 500 Zeichen passt, sonst Thread

## Ausführungsschritte

1. Formuliere die Stance: 1 klarer Satz, max. 100 Zeichen, aktive Sprache, Präsens. Prüfe: Enthält der Satz ein Verb das eine klare Position einnimmt? Enthält er keinen der Weichmacher-Begriffe ("vielleicht", "könnte", "kommt drauf an")? Wenn nein → umformulieren bis die Antwort auf beide Fragen "Ja" lautet.
2. Sammle 3 Begründungspunkte: je 1 Satz mit (a) konkretem Datenpunkt (Zahl, Studie, Beobachtung) oder (b) eigener Erfahrung ("Ich habe X getan und Y erlebt"). Wähle die 2 stärksten für Single-Post, alle 3 für Thread.
3. Leite die Konsequenz ab: 1 Satz, der beschreibt was sich verändert wenn die Stance stimmt. Format: "Das bedeutet: [Konsequenz]." oder "Wer das ignoriert, [Folge]."
4. Benenne die 2 stärksten Gegenargumente: je 1 Satz, die die Stance am überzeugendsten angreift. Dann formuliere je 1 Satz Widerlegung pro Gegenargument — nicht ausweichen, direkt widerlegen.
5. Wähle Format (Single-Post oder Thread) und füge die Elemente zusammen. Prüfe Zeichenzahl: Single-Post ≤ 500 Zeichen (zählen), Thread: je Tweet ≤ 280 Zeichen (zählen). Empfehle den stärksten Tweet des Threads für Solo-Posting.

## Verifikation

- Stance vorhanden: 1 Satz, ≤ 100 Zeichen, kein Weichmacher
- Begründung vorhanden: mindestens 2 Sätze mit je 1 Datenpunkt oder Erfahrung
- Konsequenz vorhanden: 1 Satz mit "Das bedeutet" oder "Wer das ignoriert"
- 2 Gegenargumente + 2 Widerlegungen vorhanden (je 1 Satz)
- Zeichenzahl geprüft: Single-Post ≤ 500 Zeichen oder Thread 5 Tweets à ≤ 280 Zeichen
- Failure-Indikator: Stance enthält "vielleicht", "könnte" oder "es kommt drauf an" → Meldung "Weichmacher gefunden — Stance neu formulieren: Position klar benennen ohne Einschränkung"
- Akzeptanzkriterium: Stance + Begründung + Konsequenz + 2×(Gegenargument + Widerlegung) im festgelegten Format, alle Zeichenlimits eingehalten

## Abhängigkeiten

- Input: Thema oder These, zu der eine Meinung formuliert werden soll
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

Stance (1 Satz) + Begründung (2–3 Sätze) + Konsequenz (1 Satz) + 2 Gegenargumente mit Widerlegungen + fertiger Post oder Thread. Format-Empfehlung (Single/Thread) mit Begründung. Gesamtlänge des Outputs: max. 300 Wörter, Markdown-Format.
