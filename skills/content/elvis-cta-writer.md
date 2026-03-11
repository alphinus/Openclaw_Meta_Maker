# Skill

## Name

/elvis-cta-writer

## Beschreibung

Schreibt 5 CTA-Varianten für einen X/Twitter-Post — Follow, Repost, Kommentar, Link-Klick und DM. Jede Variante nutzt eine eigene Formel und hält ein spezifisches Zeichenlimit ein. Liefert einsatzbereite CTAs mit Beispielen — passend zu jedem Content-Format.

## Ziele

- 5 fertige CTA-Varianten: Follow, Repost, Kommentar, Link-Klick, DM
- Jede Variante mit eigener Formel, eigenem Zeichenlimit und konkretem Beispiel
- Zeichenanzahl für jede Variante explizit dokumentiert
- Warnmeldung wenn mehr als 1 CTA für denselben Post vorgesehen ist

## Strategie

Ein CTA funktioniert wenn er genau eine Handlung fordert und den konkreten Nutzen für den Leser benennt. Fünf Varianten decken alle relevanten X/Twitter-Interaktions-Typen ab: Reichweite (Follow, Repost), Engagement (Kommentar), Traffic (Link-Klick) und Direktgeschäft (DM). Die Zeichenlimits sind je Typ unterschiedlich weil der Platz am Ende eines Posts begrenzt ist und jeder CTA-Typ unterschiedlich viel Kontext benötigt.

## Einschränkungen

- Genau 5 CTA-Varianten pro Aufruf — nicht mehr, nicht weniger
- Variante 1 Follow-CTA: max. 60 Zeichen
- Variante 2 Repost-CTA: max. 80 Zeichen
- Variante 3 Kommentar-CTA: max. 100 Zeichen
- Variante 4 Link-Klick-CTA: max. 100 Zeichen
- Variante 5 DM-CTA: max. 80 Zeichen
- Maximal 1 CTA pro Post — bei mehreren CTAs im gleichen Post sofort warnen
- Kein automatisches Posten — Output ist zur manuellen Freigabe bestimmt

## Ausführungsschritte

1. Lies den vorgegebenen Post-Inhalt und identifiziere: (a) das primäre Ziel des Posts (Reichweite, Engagement, Traffic, Konversion), (b) die Zielgruppe, (c) das stärkste Nutzen-Versprechen des Posts. Dokumentiere diese 3 Punkte als "CTA-Briefing" vor den Varianten.
2. Schreibe Variante 1 — Follow-CTA (max. 60 Zeichen): Formel: "Folge [mir/Kanal] für [1 konkreter Nutzen]." Beispiel: "Folge mir für tägliche Growth-Tipps." Kein "Folge mir einfach" ohne Nutzen. Zeichenanzahl in Klammern dokumentieren.
3. Schreibe Variante 2 — Repost-CTA (max. 80 Zeichen): Formel: "Reposte das für [konkrete Zielgruppe] die [Nutzen] braucht." Beispiel: "Reposte das für jeden Gründer der Reichweite aufbauen will." Zeichenanzahl dokumentieren.
4. Schreibe Variante 3 — Kommentar-CTA (max. 100 Zeichen): Formel: Offene Frage die zum Antworten einlädt, keine Ja/Nein-Frage. Beispiel: "Was ist dein größter Hebel beim Content? Schreib es in die Kommentare." Zeichenanzahl dokumentieren.
5. Schreibe Variante 4 — Link-Klick-CTA (max. 100 Zeichen): Formel: "[Nutzen] + [Dringlichkeit oder Einzigartigkeit]. Link in Bio." Beispiel: "Volle Anleitung mit Templates — heute noch anwendbar. Link in Bio." Zeichenanzahl dokumentieren. Schreibe dann Variante 5 — DM-CTA (max. 80 Zeichen): Formel: "[Trigger-Wort] + [klare Handlung]." Beispiel: "Schreib mir 'WACHSTUM' und ich schicke dir das Framework." Zeichenanzahl dokumentieren.

## Verifikation

- Alle 5 Varianten vorhanden: Follow, Repost, Kommentar, Link-Klick, DM — je als eigener Block mit Typ-Label
- Zeichenanzahl dokumentiert: V1 ≤ 60, V2 ≤ 80, V3 ≤ 100, V4 ≤ 100, V5 ≤ 80 Zeichen
- Jede Variante enthält Formel-Label und konkretes Beispiel
- Failure-Indikator: Mehr als 1 CTA für denselben Post vorgesehen → Warnmeldung "Zu viele CTAs — max. 1 pro Post. Empfehlung: [Varianten-Nummer] für dieses Post-Ziel."
- Failure-Indikator: CTA ohne konkreten Nutzen (z.B. "Folge mir.") → Meldung "CTA zu generisch — Nutzen ergänzen"
- Akzeptanzkriterium: 5 Varianten mit Formeln und Beispielen, alle innerhalb Zeichenlimits, Warnmeldung bei Mehrfach-CTA

## Abhängigkeiten

- Input: Post-Inhalt (oder Post-Thema) und Ziel-Interaktion (optional)
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill, passt zu jedem Content-Skill)

## Output

CTA-Briefing (3 Punkte) + 5 CTA-Varianten (je mit Typ-Label, Formel, Text und Zeichenanzahl) + Empfehlung welche Variante zum Post-Ziel passt. Gesamtlänge: max. 400 Wörter, Markdown-Format.
