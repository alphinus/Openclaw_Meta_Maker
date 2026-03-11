# Skill

## Name

/elvis-profile-optimizer

## Beschreibung

Optimiert alle 7 Profil-Elemente eines X/Twitter-Accounts nach einem 20-Punkte-Scoring-System. Pro Element werden Ist-Zustand, Score (0–4), Optimierungs-Empfehlung (max. 2 Sätze) und ein Beispiel-Text geliefert — kritische Elemente mit Score < 10/20 Gesamt werden separat hervorgehoben.

## Ziele

- Alle 7 Profil-Elemente analysiert: Name, Bio, Profilbild-Beschreibung, Header-Beschreibung, Pinned Post, Location, Website
- 20-Punkte-Score ermittelt (7 Elemente × max. 4 Punkte pro Element, davon 4 Punkte für den wertvollsten Slot vergeben nach Gewichtung)
- Pro Element: Ist-Zustand dokumentiert, Optimierungs-Empfehlung formuliert, Beispiel-Text erstellt
- Kritischer Optimierungsbedarf markiert falls Gesamt-Score < 10/20
- Priorisierungs-Reihenfolge für Umsetzung (von höchstem Impact zu niedrigstem)

## Strategie

Das Scoring priorisiert Klarheit und Conversion: ein guter Profilname und eine starke Bio entscheiden über den Follow-Klick in Sekunden. Das 20-Punkte-System macht den Handlungsbedarf sofort sichtbar — Score < 10 bedeutet aktiver Wachstums-Bremse. Beispiel-Texte sind nicht optional: Empfehlungen ohne konkreten Alternativ-Text sind wertlos. Alle Optimierungen beachten den 160-Zeichen-Limit der Bio und plattformspezifische Best Practices.

## Einschränkungen

- Analyse genau 7 Elemente — keine Erweiterung auf zusätzliche Elemente
- Score pro Element: 0–4 Punkte (0 = nicht vorhanden/kontraproduktiv, 4 = optimal)
- Maximaler Gesamt-Score: 28 Punkte (7 × 4) — für die normierte 20-Punkte-Skala wird mit Faktor 20/28 = 0,714 umgerechnet
- Optimierungs-Empfehlung: max. 2 Sätze pro Element
- Profilbild und Header werden beschreibend analysiert (kein Bild-Upload oder -Generierung)

## Ausführungsschritte

1. Erhebe den Ist-Zustand aller 7 Profil-Elemente. Für jedes Element: dokumentiere den aktuellen Text/Inhalt wörtlich (bei Profilbild/Header: Beschreibung in 1–2 Sätzen). Elemente: (1) Display-Name, (2) Bio (max. 160 Zeichen), (3) Profilbild (Bildinhalt, Qualität, Professionalisierungsgrad), (4) Header-Bild (Bildinhalt, Botschaft, Nischen-Relevanz), (5) Pinned Post (Thema, Engagement-Stärke, Call-to-Action), (6) Location (gesetzt/leer, Nischen-Relevanz), (7) Website-Link (gesetzt/leer, Ziel-URL-Qualität).
2. Score jeden der 7 Punkte nach diesem Schema: 4 = optimal für Nische und Zielgruppe (klar, konkret, konversionsstark); 3 = gut, aber 1 Element optimierbar; 2 = vorhanden, aber schwach oder generisch; 1 = vorhanden, aber kontraproduktiv oder unklar; 0 = nicht ausgefüllt oder schädlich. Dokumentiere pro Element: Rohpunkte (0–4) und die Hauptbegründung in einem Halbsatz.
3. Berechne den normierten 20-Punkte-Score: Summe der 7 Rohpunkte × (20/28), auf ganze Zahlen gerundet. Erstelle eine Übersichts-Tabelle: Profil-Element | Rohpunkte (0–4) | Gewichteter Anteil | Begründung (Halbsatz).
4. Formuliere pro Element eine Optimierungs-Empfehlung (max. 2 Sätze: 1 Satz Problem-Diagnose, 1 Satz Lösung) und einen konkreten Beispiel-Text. Für textbasierte Elemente (Name, Bio, Pinned Post): Beispiel-Text muss das Zeichenlimit einhalten (Bio ≤160 Zeichen). Für Bild-Elemente (Profilbild, Header): Beschreibe das ideale Bild in 2–3 Sätzen.
5. Erstelle die Priorisierungs-Reihenfolge: Sortiere die 7 Elemente nach Impact-Potenzial (Differenz zwischen aktuellem Score und maximal möglichem Score × Wichtigkeit). Markiere die Top-3-Prioritäten explizit. Falls Gesamt-Score < 10/20: füge Warnblock ein mit Text "⚠️ KRITISCHER OPTIMIERUNGSBEDARF: Gesamt-Score [X]/20 — Profil wirkt als aktiver Wachstums-Bremser. Priorität: die 3 markierten Elemente innerhalb von 48 Stunden umsetzen."

## Verifikation

- Vollständigkeit: Alle 7 Profil-Elemente in der Tabelle mit Rohpunkt, gewichtetem Anteil und Begründung
- Beispiel-Texte: Alle 7 Elemente haben einen Optimierungs-Beispieltext (für Bilder: Bildkonzept-Beschreibung)
- Score-Berechnung: Normierter Score ist korrekt berechnet (Rohpunkte-Summe × 20/28, gerundet)
- Failure-Indikator: Gesamt-Score < 10/20 → Warnblock muss erscheinen; fehlt der Warnblock bei Score < 10 ist die Ausführung unvollständig
- Akzeptanzkriterium: 7 Elemente analysiert, 20-Punkte-Score berechnet, Priorisierungs-Liste mit Top-3 vorhanden, alle Empfehlungen ≤2 Sätze

## Abhängigkeiten

- Input: Zugang zum X/Twitter-Profil des zu optimierenden Accounts (öffentlich sichtbare Profil-Daten) sowie Zielgruppen-Profil aus elvis-audience-builder als Referenz
- Empfohlene Vorgänger-Skills: elvis-audience-builder (für Zielgruppen-Kontext der Optimierungen)

## Output

Profil-Analyse-Report im Markdown-Format: Übersichts-Tabelle (7 Zeilen × 4 Spalten), normierten 20-Punkte-Score, pro Element Empfehlung + Beispiel-Text, Priorisierungs-Liste Top-3, ggf. Warnblock. Gesamtlänge: max. 800 Wörter.
