# Skill

<!-- ════════════════════════════════════════════════════════════════
     SKILL-TEMPLATE — OpenClaw Meta Maker
     Dieses Template ist bindend für alle ~100 Skills in S04–S07.
     
     ANLEITUNG:
     1. Lösche alle HTML-Kommentare (<!-- ... -->) nach dem Ausfüllen
     2. Ersetze alle [PFLICHTFELD]-Marker durch echten Inhalt
     3. Behalte die exakten Header-Namen (## Name, ## Beschreibung, usw.)
     4. Das vollständige Beispiel beginnt unterhalb der Trennlinie
     ════════════════════════════════════════════════════════════════ -->

## Name
<!-- [PFLICHTFELD]
     Format: /elvis-[kebab-case-name]
     Konvention: immer Kleinbuchstaben, Bindestriche statt Leerzeichen
     Beispiel: /elvis-x-growth-audit
     Häufiger Fehler: Name mit Leerzeichen oder Großbuchstaben -->

/elvis-[skill-name]

## Beschreibung
<!-- [PFLICHTFELD]
     Format: 1–3 prägnante Sätze
     Inhalt: Was tut dieser Skill? Welches Problem löst er?
     Zielgruppe: Operator oder Endnutzer, der den Skill aufruft
     Häufiger Fehler: Zu vage ("Analysiert Dinge") oder zu technisch ("Führt NLP-Pipeline aus") -->

Kurze, präzise Beschreibung des Skills und des gelösten Problems.

## Ziele
<!-- Format: 3–5 Bullet Points, messbar formuliert
     Inhalt: Was soll am Ende erreicht sein? Erfolg aus Nutzersicht.
     Häufiger Fehler: Ziele als Schritte formulieren ("Analysiere Posts") statt als Ergebnisse ("Identifizierte Top-10 Posts nach Engagement") -->

- Ziel 1 (messbar und ergebnisorientiert)
- Ziel 2
- Ziel 3

## Strategie
<!-- Format: Fließtext, 2–4 Sätze oder strukturierte Bullet Points
     Inhalt: Wie geht der Skill vor? Welcher Ansatz / welche Methode?
     Häufiger Fehler: Strategie = Wiederholung der Schritte. Strategie erklärt das WARUM und den ANSATZ, nicht das WIE im Detail. -->

Beschreibung des konzeptionellen Ansatzes: warum dieser Weg, welche Priorisierung, welches Prinzip liegt den Schritten zugrunde.

## Einschränkungen
<!-- Format: Bullet Points mit konkreten Limits und Verboten
     Inhalt: Hard Limits (Max-Mengen), Verbote (keine externen Calls ohne Freigabe), Scope-Grenzen
     Häufiger Fehler: Zu weiche Formulierungen ("möglichst wenig") statt harter Zahlen ("max. 20 Einträge") -->

- Max. [N] [Einheiten] pro Durchlauf
- Keine externen API-Aufrufe ohne explizite Operator-Freigabe
- [Weitere Scope-Grenzen und Verbote]

## Ausführungsschritte
<!-- [PFLICHTFELD]
     Format: Nummerierte Liste — jeder Schritt ist eine einzelne, ausführbare Aktion
     Pflicht-Elemente pro Schritt (D006): 
       - Konkrete Menge (z.B. "Top-20", "die letzten 7 Tage", "3 Varianten")
       - Konkretes Format (z.B. "Markdown-Tabelle mit 4 Spalten", "JSON-Array")
       - Zeitangabe wo sinnvoll (z.B. "innerhalb von 2 Stunden", "täglich")
     Häufiger Fehler: Abstrakte Schritte wie "Analysiere den Content" statt
     "Extrahiere die Top-20 Posts der letzten 7 Tage, sortiert nach Engagement-Rate (Likes + Reposts / Impressionen)" -->

1. [Konkreter Schritt mit Menge, Format und Zeitangabe wo zutreffend]
2. [Konkreter Schritt]
3. [Konkreter Schritt]

## Verifikation
<!-- [PFLICHTFELD]
     Format: Bullet Points mit prüfbaren Akzeptanzkriterien
     Inhalt: 
       - Was MUSS im Output vorhanden sein?
       - Was ist ein sicheres Zeichen für schlechten Output?
       - Wann gilt der Skill als erfolgreich abgeschlossen?
     Häufiger Fehler: Nur positive Kriterien — gute Verifikation benennt auch Failure-Indikatoren -->

- Prüfkriterium 1: [Was muss im Output vorhanden sein?]
- Prüfkriterium 2: [Was ist ein Zeichen für schlechten Output?]
- Akzeptanzkriterium: [Wann gilt der Skill als erfolgreich?]

## Abhängigkeiten
<!-- Format: Zwei Zeilen — Input und Vorgänger
     Inhalt: Welche Daten / welcher vorheriger Skill-Output wird benötigt?
     Häufiger Fehler: "keine" wenn tatsächlich Account-Zugang oder vorheriger Skill benötigt wird -->

- Input: [Welche Daten oder Zugänge werden benötigt?]
- Empfohlene Vorgänger-Skills: [/elvis-skill-name oder "keine"]

## Output
<!-- [PFLICHTFELD]
     Format: Kurze Beschreibung des konkreten Lieferobjekts
     Inhalt: Was bekommt der Nutzer am Ende? Format, Umfang, Verwendung.
     Häufiger Fehler: Zu abstrakt ("Ergebnis der Analyse") statt konkret ("Markdown-Bericht mit 3 Abschnitten: Übersicht, Top-Posts-Tabelle, Handlungsempfehlungen") -->

Beschreibung des konkreten Outputs: Format, Struktur, erwarteter Umfang.

---
<!-- BEISPIEL BEGINS BELOW — KEIN TEMPLATE-INHALT -->
<!-- Das folgende Beispiel demonstriert das angestrebte Qualitätsniveau.
     Es zeigt einen vollständig ausgearbeiteten Skill mit konkreten
     Mengen, Zeitangaben und Formaten in den Ausführungsschritten (D006). -->

# Skill

## Name

/elvis-x-growth

## Beschreibung

Analysiert die Wachstums-Performance eines X/Twitter-Accounts über die letzten 30 Tage. Identifiziert die Top-Posts nach Engagement-Rate, erkennt Content-Muster die überdurchschnittlich performen, und liefert konkrete Handlungsempfehlungen für die nächsten 7 Tage.

## Ziele

- Identifizierte Top-10 Posts der letzten 30 Tage nach Engagement-Rate (Likes + Reposts + Replies / Impressionen)
- Erkannte 3–5 Content-Muster, die überdurchschnittlich performen (Format, Thema, Posting-Zeit)
- Konkrete Posting-Empfehlung: beste Uhrzeit, beste Wochentage, Top-3 Content-Typen
- Vergleich Ist-Wachstum vs. Benchmark (Accounts ähnlicher Größe in derselben Nische)

## Strategie

Der Skill priorisiert Engagement-Rate über absolute Zahlen — ein kleiner Account mit 8 % Engagement-Rate liefert wertvolle Muster, absolute Like-Zahlen sind irreführend. Die Analyse geht vom Datensatz aus (was ist passiert?), dann zu Mustern (warum hat es funktioniert?), dann zu Empfehlungen (was als nächstes?). Alle Empfehlungen basieren ausschließlich auf beobachteten Daten — keine Spekulation.

## Einschränkungen

- Max. 30 Posts pro Analyse-Durchlauf (die neuesten 30 der letzten 30 Tage)
- Keine automatischen Posts oder Account-Aktionen — reine Lese- und Analyse-Operation
- Nur öffentlich zugängliche Metriken auswerten (keine API-Calls ohne Operator-Freigabe)
- Keine Analyse von Accounts Dritter ohne explizite Freigabe durch den Operator
- Ergebnis wird nur ausgegeben, nicht gespeichert oder weitergeleitet

## Ausführungsschritte

1. Rufe die letzten 30 Posts des Accounts ab (Zeitraum: die zurückliegenden 30 Kalendertage). Für jeden Post erfasse: Post-Text, Datum/Uhrzeit, Impressionen, Likes, Reposts, Replies, Link-Klicks (falls verfügbar).
2. Berechne für jeden Post die Engagement-Rate: (Likes + Reposts + Replies) / Impressionen × 100. Erstelle eine Rangliste der Top-10 Posts nach Engagement-Rate absteigend.
3. Analysiere die Top-10 Posts auf gemeinsame Muster innerhalb von 5 Minuten: Content-Format (Text, Bild, Video, Thread), Themenbereich (Nischen-Keywords), Posting-Uhrzeit (Uhrzeit + Wochentag), Post-Länge (Zeichenanzahl), Verwendung von Hashtags (0 / 1–3 / 4+).
4. Identifiziere die 3 stärksten Muster (höchste Konsistenz unter den Top-10). Formuliere für jedes Muster eine präzise Beobachtung: z.B. "Posts zwischen 08:00–09:00 Uhr haben eine durchschnittliche Engagement-Rate von 6,2 % vs. 2,1 % für alle anderen Uhrzeiten."
5. Erstelle eine Handlungsempfehlung für die nächsten 7 Tage: 3 empfohlene Content-Ideen (je 1–2 Sätze Briefing), 2 optimale Posting-Uhrzeiten mit Wochentag, 1 Format-Empfehlung basierend auf Muster-Befund.
6. Schreibe den vollständigen Analyse-Bericht im Markdown-Format mit 4 Abschnitten: (1) Metriken-Übersicht, (2) Top-10-Tabelle mit 5 Spalten (Rang, Post-Vorschau 50 Zeichen, Datum, Engagement-Rate, Muster-Tags), (3) Muster-Befunde, (4) Handlungsempfehlungen. Gesamtlänge: max. 800 Wörter.

## Verifikation

- Vollständigkeitsprüfung: Report enthält alle 4 Abschnitte (Metriken-Übersicht, Top-10-Tabelle, Muster-Befunde, Handlungsempfehlungen)
- Datenintegrität: Jede Engagement-Rate in der Tabelle ist berechenbar aus den angegebenen Rohdaten (keine Zahlen die nicht aus den Posts stammen)
- Konkretheit: Handlungsempfehlungen enthalten mindestens eine Uhrzeitangabe, einen Wochentag und einen Content-Typ
- Failure-Indikator: Wenn weniger als 5 Posts im Zeitraum existieren, bricht der Skill ab und gibt "Datenbasis zu klein (< 5 Posts) — Analyse nicht aussagekräftig" aus
- Akzeptanzkriterium: Report ist innerhalb von 10 Minuten nach Aufruf vollständig, alle 4 Abschnitte befüllt, mindestens 3 Muster identifiziert

## Abhängigkeiten

- Input: Zugang zu X/Twitter-Account-Metriken (Analytics-Ansicht oder exportierter Datensatz der letzten 30 Tage)
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für Growth-Kategorie)

## Output

Markdown-Bericht (max. 800 Wörter) mit 4 Abschnitten: (1) Metriken-Übersicht (Gesamt-Impressionen, Durchschnitts-Engagement-Rate, Posting-Frequenz), (2) Top-10-Tabelle mit Engagement-Rates, (3) 3–5 identifizierte Content-Muster mit Belegen, (4) konkrete Handlungsempfehlungen für die nächsten 7 Tage.
