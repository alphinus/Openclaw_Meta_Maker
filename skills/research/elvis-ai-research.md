# Skill

## Name

/elvis-ai-research

## Beschreibung

Nutzt KI-Systeme als strukturiertes Recherche-Werkzeug durch 5 parametrisierte Prompt-Templates. Erhebt zu einem vorgegebenen Thema Informationen aus verschiedenen Perspektiven, bewertet die KI-Outputs nach 3 Qualitätskriterien und verdichtet die verwertbaren Antworten zu einem abgesicherten Recherche-Ergebnis.

## Ziele

- 5 ausgefüllte Prompt-Templates mit je 3 Parametern — vollständig dokumentiert und wiederholbar
- KI-Output-Bewertung nach 3-Kriterien-Matrix (Belegt, Präzise, Widerspruchsfrei) für jeden der 5 Prompts
- Mindestens 3 verwertbare Antworten nach Qualitätsfilter — oder Failure-Abbruch
- Konsolidierte Recherche-Zusammenfassung mit Quellenangaben und Unsicherheits-Markierungen
- Liste von 3–5 KI-generierten Aussagen, die externer Verifikation bedürfen ("Verification-Queue")

## Strategie

KI als Recherche-Tool erfordert strukturierte Prompt-Architektur statt freier Abfragen. Jeder der 5 Prompts deckt einen anderen Erkenntniswinkel ab (Definitionen, Zahlen, Kontraste, Prognosen, Beispiele), um Einseitigkeit zu vermeiden. Die Qualitätsbewertung folgt dem Prinzip "vertraubar bis zum Gegenbeweis": nur Aussagen, die alle 3 Kriterien erfüllen, fließen in das Endergebnis ein. KI-typische Konfabulation wird durch den Widerspruchsfrei-Filter und die Verification-Queue aktiv adressiert.

## Einschränkungen

- Genau 5 Prompts pro Durchlauf — kein Überspringen, kein Hinzufügen weiterer Prompts ohne neue Dokumentation
- Jeder Prompt muss genau 3 Parameter enthalten (Thema, Fokus, Format) — undefinierte Parameter machen den Prompt ungültig
- Keine Aussagen ohne Qualitätsbewertung in den Output aufnehmen
- KI-Output gilt nicht als primäre Quelle — er ist Hypothesen-Generator, der externer Bestätigung bedarf
- Max. 1.500 Wörter im Gesamt-Output

## Ausführungsschritte

1. Definiere die 3 Pflicht-Parameter für alle 5 Prompts: (a) **Thema** — präzise Beschreibung des Recherche-Gegenstands in 1–2 Sätzen, (b) **Fokus** — welchen Aspekt soll dieser Prompt beleuchten (Definition / Daten / Kontrast / Prognose / Beispiele), (c) **Format** — gewünschtes Ausgabe-Format (Liste mit N Punkten / Tabelle mit K Spalten / 3-Absatz-Text). Dokumentiere die Parameter als 3-Zeilen-Header über jedem Prompt.
2. Formuliere und stelle die 5 Prompt-Templates in dieser Reihenfolge: **P1 Definitions-Prompt** ("Was bedeutet [Thema] konkret? Nenne 5 präzise Definitionen aus verschiedenen Perspektiven im Format: Definition | Perspektive | Schlüsselbegriff"), **P2 Daten-Prompt** ("Welche messbaren Kennzahlen und Statistiken beschreiben [Thema]? Liste 7 konkrete Zahlen mit Zeitraum und Quelle"), **P3 Kontrast-Prompt** ("Welche gegensätzlichen Standpunkte existieren zu [Thema]? Stelle 3 Pro- und 3 Contra-Argumente gegenüber"), **P4 Prognose-Prompt** ("Wie wird sich [Thema] in den nächsten 12 Monaten entwickeln? Nenne 4 begründete Szenarien mit Eintrittsbedingungen"), **P5 Beispiel-Prompt** ("Nenne 5 konkrete Praxisbeispiele für [Thema] — je mit Kontext, Ergebnis und Übertragbarkeits-Einschätzung"). Notiere jeden KI-Output vollständig im Protokoll.
3. Bewerte jeden der 5 KI-Outputs nach der 3-Kriterien-Matrix — vergib je Kriterium 1 (nicht erfüllt) oder 2 (erfüllt): **Kriterium 1 Belegt** (enthält die Antwort überprüfbare Fakten, Zahlen oder Verweise?), **Kriterium 2 Präzise** (ist die Antwort themenspezifisch und nicht generisch-vage?), **Kriterium 3 Widerspruchsfrei** (widerspricht die Antwort nicht früheren Prompts oder bekannten Fakten?). Erstelle eine Bewertungstabelle (5 Zeilen × 3 Spalten + Gesamtscore 2–6).
4. Filtere: Outputs mit Gesamtscore ≥ 4/6 gelten als "verwertbar". Outputs mit Score < 4 werden als "unzuverlässig" markiert und fließen nicht in das Endergebnis ein. Prüfe ob mindestens 3 verwertbare Outputs vorliegen — falls nicht, löse den Failure-Indikator aus.
5. Extrahiere aus den verwertbaren Outputs alle Aussagen, die externer Verifikation bedürfen: (a) Zahlen ohne Quellenangabe, (b) Prognosen ohne benannte Grundlage, (c) Beispiele die nicht als allgemein bekannt gelten. Dokumentiere diese als "Verification-Queue" in einer numerierten Liste (max. 5 Einträge) mit dem Hinweis "Zu prüfen via: [empfohlene Quelle-Typ]".
6. Schreibe die Recherche-Zusammenfassung in 3 Abschnitten: (1) **Gesichertes Wissen** — Kernaussagen aus verwertbaren Outputs, die alle 3 Kriterien erfüllen (max. 5 Punkte), (2) **Unsicheres Terrain** — Aussagen mit Score 3/6 die als Hypothesen gelten, klar markiert mit "Hypothese:", (3) **Lücken und nächste Schritte** — was konnte die KI-Recherche nicht klären, welche Quellen-Typen sollten als nächstes konsultiert werden?

## Verifikation

- Prompt-Vollständigkeit: Alle 5 Prompts wurden ausgefüllt, jeder hat genau 3 Parameter-Header dokumentiert
- Bewertungs-Matrix: 5-Zeilen-Tabelle mit 3 Kriterien + Gesamtscore vorhanden, keine leeren Felder
- Verwertbarkeits-Schwelle: Mindestens 3 Outputs mit Score ≥ 4/6 wurden in die Zusammenfassung aufgenommen
- Verification-Queue: 3–5 prüfbedürftige Aussagen benannt (nicht 0 — bei 0 ist der Filter nicht aktiv gewesen)
- Failure-Indikator: Weniger als 3 verwertbare Antworten nach Qualitätsfilter (Score ≥ 4/6) → Skill bricht ab mit "KI-Qualitätsfilter: Weniger als 3 verwertbare Outputs (< 3 mit Score ≥ 4) — Prompts überarbeiten oder anderes Thema wählen"
- Akzeptanzkriterium: Bewertungs-Tabelle vollständig, ≥ 3 verwertbare Outputs, Verification-Queue mit 3–5 Einträgen, Zusammenfassung in 3 Abschnitten

## Abhängigkeiten

- Input: Ein klar definiertes Recherche-Thema (1–2 Sätze) und optional: gewünschte KI-Perspektive (technisch / strategisch / nutzerfokussiert) sowie Sprache des Outputs (DE / EN)
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill für KI-gestützte Recherche)

## Output

Strukturiertes Protokoll mit 4 Teilen: (1) Prompt-Tabelle (5 Prompts × 3 Parameter), (2) Bewertungs-Matrix (5 × 3 Kriterien + Score), (3) Verification-Queue (3–5 Einträge), (4) Recherche-Zusammenfassung (3 Abschnitte: Gesichertes Wissen, Unsicheres Terrain, Lücken). Gesamtlänge: max. 1.500 Wörter.
