# Skill

## Name

/elvis-content-scheduler

## Beschreibung

Richtet einen automatisierten Content-Veröffentlichungsplan für die nächsten 4 Wochen ein: Definition von min. 3 Zeitslots pro Tag oder Woche, Plattform-Konfiguration für min. 2 Plattformen, Fallback-Regeln für min. 1 Szenario. Liefert eine Tool-Konfigurations-Spezifikation — keine Code-Implementierung, sondern präzise Anweisungen für Scheduling-Tools.

## Ziele

- Vollständiger 4-Wochen-Zeitplan: min. 28 geplante Veröffentlichungs-Slots (bei 1 Post/Tag) oder min. 12 Slots (bei 3 Posts/Woche)
- Konfigurierte min. 2 Plattformen (z.B. X/Twitter + LinkedIn) mit jeweils plattform-spezifischen Formatierungs-Regeln
- Definierte min. 1 Fallback-Regel für Szenarien ohne verfügbaren Content (z.B. "Evergreen-Content aus Pool wiederverwenden" oder "Zeitslot überspringen und im Monitoring markieren")
- Tool-Konfigurations-Anweisungen für Scheduling-Tool (z.B. Buffer, Later, Hootsuite) — konkrete Settings pro Plattform

## Strategie

Der Skill kombiniert Content-Planung (elvis-content-calendar liefert Ideen) mit Automatisierungs-Logik (wann wird was wo gepostet?). Der Fokus liegt auf **Systemdesign statt Taktik**: Nicht "welche Posts?", sondern "welche Zeitslots, welche Plattformen, welche Regeln?". Die Fallback-Regel ist kritisch: Ohne sie stoppt das System bei fehlendem Content. Der 4-Wochen-Zeitraum ist bewusst kurz — längere Zeiträume erfordern Content-Vorrat der oft nicht existiert. Output ist keine Code-Implementierung, sondern Tool-Konfigurations-Spezifikation in natürlicher Sprache.

## Einschränkungen

- Zeitplan: min. 4 Wochen (28 Tage), max. 8 Wochen — längere Zeiträume sind unrealistisch ohne dediziertes Content-Team
- Min. 2 Plattformen — Single-Platform-Scheduling ist trivial und braucht keinen Skill
- Min. 3 Zeitslots pro Tag (bei Daily-Posting) ODER min. 3 Posts pro Woche (bei Weekly-Posting) — weniger ist ineffizient
- Keine automatische Content-Erstellung — dieser Skill plant die Veröffentlichung, nicht die Produktion (dafür sind Content-Skills zuständig)
- Fallback-Regel darf nicht "gar nichts posten" sein — ein stiller Account ist schlechter als Evergreen-Content

## Ausführungsschritte

1. Definiere die Posting-Frequenz und Zeitslots: Erfrage vom Operator: Posting-Frequenz (täglich 1-3 Posts / 3-5 Posts pro Woche / wöchentlich 1 Post), Plattformen (min. 2 aus: X/Twitter, LinkedIn, Instagram, Facebook, TikTok), bevorzugte Posting-Zeiten (falls bekannt, sonst Default-Empfehlungen nutzen). Erstelle Zeitslot-Tabelle mit 4 Spalten: Tag/Wochentag, Uhrzeit, Plattform, Format (Text/Bild/Video/Link). Für 4 Wochen ergeben sich bei täglichem Posting: 28 Tage × 1 Post = 28 Zeitslots (oder bei 3/Woche: 4 Wochen × 3 = 12 Slots).
2. Konfiguriere plattform-spezifische Formatierungs-Regeln: Für jede der min. 2 Plattformen dokumentiere: Max. Zeichenlänge (z.B. X: 280, LinkedIn: 3000 empfohlen <1300), Hashtag-Strategie (z.B. X: 2-3 Hashtags, LinkedIn: 3-5), Bild-Format (z.B. X: 16:9 1200×675px, LinkedIn: 1200×627px), Link-Handling (z.B. X: Kurz-URL mit Preview, LinkedIn: nativer Link-Post). Erstelle Formatierungs-Checkliste pro Plattform (4-6 Regeln je Plattform).
3. Definiere Content-Zuordnung zu Zeitslots: Für jeden der geplanten Zeitslots (28 bei Daily, 12 bei 3/Woche) weise eine Content-Kategorie zu (z.B. "Bildung", "Unterhaltung", "Konversion" — aus elvis-content-calendar übernehmen falls vorhanden). Erstelle erweiterte Zeitslot-Tabelle mit 5 Spalten: Tag/Datum, Uhrzeit, Plattform, Content-Kategorie, Status (Geplant/Bereit/Veröffentlicht). Markiere Zeitslots ohne verfügbaren Content mit "⚠️ Content fehlt".
4. Spezifiziere min. 1 Fallback-Regel für fehlenden Content: Definiere was passiert wenn zum geplanten Zeitslot kein Content bereit ist. Fallback-Optionen: "Evergreen-Content aus Pool wiederverwenden (Pool = min. 10 zeitlose Posts die jederzeit passen)", "Zeitslot überspringen und im Monitoring markieren (max. 2 Überspringungen pro Woche erlaubt)", "Benachrichtigung an Operator + 2h Verzögerung für manuelle Content-Erstellung". Wähle 1 Haupt-Fallback + 1 Notfall-Fallback (wenn Haupt-Fallback nicht möglich, z.B. Evergreen-Pool leer).
5. Erstelle Tool-Konfigurations-Anweisungen: Wähle ein Scheduling-Tool (Buffer / Later / Hootsuite / Meta Business Suite — nach Plattform-Kompatibilität). Dokumentiere für das gewählte Tool: Plattform-Anbindung (welche Accounts verbinden?), Zeitslot-Einrichtung (wie Zeitplan im Tool eintragen? Screenshot-Beschreibung oder Schritt-für-Schritt), Content-Queue-Setup (wo wird Content vor Veröffentlichung gespeichert?), Fallback-Konfiguration (wie wird Fallback-Regel im Tool umgesetzt? Oft manuell), Monitoring-Dashboard (welche Metriken täglich prüfen?). Format: 5-8 konkrete Setup-Schritte für das Tool.

## Verifikation

- Zeitslot-Tabelle: min. 28 Zeitslots (Daily) oder 12 Slots (3/Woche) für 4 Wochen, alle mit Datum/Uhrzeit/Plattform
- Plattform-Konfiguration: Min. 2 Plattformen mit jeweils 4-6 Formatierungs-Regeln dokumentiert
- Content-Zuordnung: Jeder Zeitslot hat eine Content-Kategorie, fehlende Inhalte markiert
- Fallback-Regeln: Min. 1 Haupt-Fallback + 1 Notfall-Fallback definiert mit klarer Aktivierungs-Bedingung
- Tool-Konfigurations-Anweisungen: 5-8 konkrete Setup-Schritte für das gewählte Scheduling-Tool
- Failure-Indikator: Wenn Content-Vorrat für <2 Wochen verfügbar (basierend auf Zeitslot-Zuordnung und verfügbarem Content-Pool) → Meldung "Content-Vorrat zu gering — nur [N] von [M] Zeitslots befüllt. Empfehle Content-Produktion mit /elvis-content-calendar vor Scheduling-Setup."
- Akzeptanzkriterium: Vollständige Zeitslot-Tabelle für 4 Wochen, min. 2 Plattformen konfiguriert, min. 1 Fallback-Regel, Tool-Setup-Anweisungen einsatzbereit

## Abhängigkeiten

- Input: Posting-Frequenz (täglich/wöchentlich), Plattformen (min. 2), optional: verfügbarer Content-Pool oder elvis-content-calendar-Output
- Empfohlene Vorgänger-Skills: /elvis-content-calendar — liefert 30-Tage-Ideen-Pool als Content-Basis für die Zeitslots; /elvis-content-ideas — liefert erweiterten Themen-Pool

## Output

Markdown-Dokument mit 5 Abschnitten: (1) Zeitslot-Tabelle (4 Wochen, alle geplanten Veröffentlichungs-Zeitpunkte mit Plattform und Content-Kategorie), (2) Plattform-Konfigurations-Checklisten (min. 2 Plattformen mit Formatierungs-Regeln), (3) Fallback-Regeln (Haupt + Notfall mit Aktivierungs-Bedingungen), (4) Tool-Konfigurations-Anweisungen (5-8 Setup-Schritte für gewähltes Scheduling-Tool), (5) Monitoring-Checkliste (welche Metriken täglich prüfen? z.B. "veröffentlichte Posts heute", "Fallback-Aktivierungen diese Woche", "Content-Vorrat verbleibende Tage"). Einsatzbereit als Setup-Briefing für Scheduling-System.
