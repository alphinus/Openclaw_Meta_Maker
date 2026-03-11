# Skill

## Name

/elvis-story-writer

## Beschreibung

Schreibt eine Personal-Story nach dem 3-Akt-Prinzip für X/Twitter. Liefert 3 Akte — Problem, Wendepunkt, Erkenntnis — je als eigenständigen Tweet mit max. 280 Zeichen, bereit zur Veröffentlichung als 3-Tweet-Mini-Story oder als Basis für einen längeren Thread.

## Ziele

- 3 fertige Akte als eigenständige Tweets: Akt 1 Problem (max. 280 Zeichen), Akt 2 Wendepunkt (max. 280 Zeichen), Akt 3 Erkenntnis (max. 280 Zeichen)
- Akt 2 enthält eine spezifische Szene — kein Allgemeinplatz
- Akt 3 transportiert die Botschaft implizit — keine explizite Moral-Aussage
- Zeichenanzahl für jeden Akt explizit dokumentiert

## Strategie

Story-Telling auf X funktioniert weil persönliche Erfahrungen Identifikation erzeugen. Der 3-Akt-Aufbau (Problem → Wendepunkt → Erkenntnis) ist das Minimum einer vollständigen Geschichte. Akt 2 ist der entscheidende Unterschied zwischen einer guten und einer generischen Story: er enthält eine einzige, konkrete Szene statt einer abstrakten Beschreibung. Akt 3 zeigt — er erklärt nicht. Die Moral entsteht beim Leser, nicht im Text.

## Einschränkungen

- Jeder Akt: max. 280 Zeichen — kein Akt darf das Limit überschreiten
- Akt 2 muss eine spezifische Szene enthalten (wer, wo, was — konkret)
- Akt 3 enthält keine direkte Moral-Aussage wie "Die Moral daraus:" oder "Was ich gelernt habe:"
- Keine Hashtags außer explizit angefordert
- Kein automatisches Posten — Output ist zur manuellen Freigabe bestimmt

## Ausführungsschritte

1. Lies die vorgegebene Kern-Erfahrung und fasse sie in genau 1 Satz zusammen: Was ist passiert? Was hat sich verändert? Dieser Satz ist das Fundament aller 3 Akte und wird als "Story-Kern" vor den Akten dokumentiert.
2. Schreibe Akt 1 — Problem (max. 280 Zeichen): Beschreibe die Ausgangssituation konkret und benenne den Schmerzpunkt direkt. Kein Jammern, kein Selbstmitleid — nur die klare Beschreibung des Zustands vor der Veränderung. Zeichenanzahl in Klammern dokumentieren.
3. Schreibe Akt 2 — Wendepunkt (max. 280 Zeichen): Beschreibe den Moment der Veränderung als spezifische Szene mit konkretem Erlebnis. Nenne wer dabei war, was genau gesagt oder getan wurde, oder was konkret gesehen/gehört wurde. Kein Allgemeinplatz wie "Dann änderte sich alles" — eine Szene. Zeichenanzahl dokumentieren.
4. Schreibe Akt 3 — Erkenntnis (max. 280 Zeichen): Beschreibe was sich seit dem Wendepunkt verändert hat. Transportiere die Botschaft implizit durch das Ergebnis, nicht durch eine direkte Moral-Aussage. Endet mit einem Satz der den Leser in Bezug zu seiner eigenen Situation bringt. Zeichenanzahl dokumentieren.
5. Prüfe alle 3 Akte auf Zeichenlimits: Falls ein Akt > 280 Zeichen → Meldung "Akt [N] überschreitet 280 Zeichen — kürzen" und konkrete Kürzungs-Vorschläge (welche Satzteile können entfernt werden ohne den Kern zu beschädigen).

## Verifikation

- Alle 3 Akte vorhanden und als eigene Blöcke formatiert: Akt 1 Problem, Akt 2 Wendepunkt, Akt 3 Erkenntnis
- Zeichenanzahl für jeden Akt dokumentiert und ≤ 280 Zeichen
- Akt 2 enthält eine konkrete Szene mit mindestens 1 spezifischem Detail
- Akt 3 enthält keine direkte Moral-Formulierung ("Die Moral:", "Was ich gelernt habe:", "Der Takeaway:")
- Failure-Indikator: Ein Akt > 280 Zeichen → Meldung "Akt [N] überschreitet 280 Zeichen — kürzen"
- Failure-Indikator: Kern-Erfahrung zu vage (weniger als 3 Wörter, kein konkretes Ereignis) → Meldung "Erfahrung zu abstrakt — bitte ein konkretes Ereignis beschreiben"
- Akzeptanzkriterium: 3 Akte, alle ≤ 280 Zeichen, Akt 2 mit konkreter Szene, Akt 3 ohne explizite Moral

## Abhängigkeiten

- Input: Eine konkrete Kern-Erfahrung (2–5 Sätze Beschreibung des Erlebnisses)
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

Story-Kern (1 Satz) + 3 Akte (je mit Akt-Label, Text und Zeichenanzahl in Klammern) + optionale Kürzungs-Hinweise falls ein Akt das Limit überschreitet. Gesamtlänge: max. 400 Wörter, Markdown-Format.
