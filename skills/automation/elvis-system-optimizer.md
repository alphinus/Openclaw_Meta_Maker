# Skill

## Name

/elvis-system-optimizer

## Beschreibung

Optimiert ein bestehendes System nach 4 Effizienz-Dimensionen (Geschwindigkeit, Zuverlässigkeit, Wartbarkeit, Kosten-Effizienz) mit objektiver Score-Bewertung und priorisierten Verbesserungs-Maßnahmen. Analysiert jede Dimension unabhängig auf einer Skala von 1-10, berechnet einen Gesamt-Effizienz-Score und identifiziert die 3-5 Maßnahmen mit dem größten Impact. Im Gegensatz zu `elvis-automation-audit` (entdeckt Automatisierungs-Potenzial) verbessert dieser Skill bereits existierende Systeme systematisch.

## Ziele

- System-Profil: Vollständige Beschreibung des zu optimierenden Systems (Zweck, Komponenten, aktueller Zustand)
- 4-Dimensionen-Bewertung: Jede Dimension (Geschwindigkeit/Zuverlässigkeit/Wartbarkeit/Kosten) mit Score 1-10 bewertet und begründet
- Gesamt-Effizienz-Score: Durchschnitt der 4 Dimensionen als Baseline-Metrik
- Maßnahmen-Priorisierung: 3-5 konkrete Verbesserungs-Maßnahmen sortiert nach Impact × Umsetzbarkeit, jeweils mit erwartetem Score-Gewinn

## Strategie

Der Skill nutzt eine 4-Dimensionen-Zerlegung statt globaler "System läuft gut/schlecht"-Bewertung: Geschwindigkeit (Ausführungszeit, Latenz, Durchsatz), Zuverlässigkeit (Fehlerquote, Uptime, Wiederherstellungszeit), Wartbarkeit (Code-Qualität, Dokumentation, Testabdeckung), Kosten-Effizienz (Infrastruktur-Kosten, Betriebsaufwand, Skalierungs-Kosten). Jede Dimension wird unabhängig bewertet — ein System kann schnell aber teuer sein, oder zuverlässig aber schwer wartbar. Der Gesamt-Score zeigt ob Optimierung überhaupt lohnt: Score >7 bedeutet das System ist bereits gut optimiert, Maßnahmen sind Feintuning. Score <5 bedeutet grundlegende Probleme, größere Umbauten nötig.

## Einschränkungen

- Nur Systeme optimieren die bereits produktiv laufen — keine Optimierung von Prototypen oder geplanten Systemen
- Jede Dimension muss objektiv messbar sein (z.B. Geschwindigkeit in ms, Zuverlässigkeit in % Uptime) — keine rein subjektiven Bewertungen
- Maßnahmen müssen konkret sein (z.B. "Datenbank-Index auf Spalte X") — keine abstrakten Empfehlungen wie "Code-Qualität verbessern"
- Score-Gewinn pro Maßnahme ist Schätzung — tatsächliche Wirkung muss nach Umsetzung gemessen werden
- Keine Kosten-Nutzen-Analyse liefern — nur technische Optimierungs-Empfehlungen, Geschäfts-Entscheidung erfolgt separat

## Ausführungsschritte

1. Erstelle das System-Profil: Bitte den Operator das zu optimierende System zu beschreiben: Zweck (was macht das System), Haupt-Komponenten (z.B. Frontend/Backend/Datenbank/Integrations), Nutzungs-Frequenz (Anfragen pro Tag/Woche), aktuell bekannte Probleme oder Engpässe. Dokumentiere diese Informationen strukturiert in 4 Absätzen: Zweck, Komponenten, Nutzung, Bekannte Probleme.
2. Bewerte die 4 Effizienz-Dimensionen: Geschwindigkeit (1=sehr langsam/unbenutzbar, 5=akzeptabel, 10=optimal schnell — messbarer Indikator z.B. durchschnittliche Antwortzeit in ms oder Durchlaufzeit in Minuten), Zuverlässigkeit (1=häufige Fehler/Ausfälle, 5=gelegentliche Fehler, 10=hochverfügbar/fehlerfrei — messbarer Indikator z.B. Uptime in % oder Fehlerquote in %), Wartbarkeit (1=unverständlicher Code/keine Doku, 5=wartbar mit Aufwand, 10=sauberer Code/vollständige Doku — Indikator z.B. Zeit für typische Änderung in Stunden), Kosten-Effizienz (1=sehr teuer/unwirtschaftlich, 5=angemessen, 10=sehr günstig — Indikator z.B. Kosten pro 1000 Anfragen in Euro). Dokumentiere für jede Dimension: Score (1-10), messbarer Indikator mit Wert, Begründung (1-2 Sätze).
3. Berechne Gesamt-Effizienz-Score: Effizienz-Score = (Geschwindigkeit + Zuverlässigkeit + Wartbarkeit + Kosten-Effizienz) / 4. Dokumentiere die Formel und das Ergebnis. Interpretiere das Ergebnis: Score >7 = bereits gut optimiert (Feintuning), Score 5-7 = Optimierungs-Potenzial vorhanden (selektive Maßnahmen), Score <5 = grundlegende Probleme (größere Umbauten nötig).
4. Identifiziere Optimierungs-Maßnahmen: Für jede Dimension mit Score <8 sammle konkrete Verbesserungs-Ideen. Jede Maßnahme dokumentiere mit: Titel (max. 50 Zeichen), betroffene Dimension(en), erwarteter Score-Gewinn (z.B. +2 Punkte in Geschwindigkeit), Umsetzbarkeit (Einfach/Mittel/Komplex), geschätzter Aufwand (Stunden oder Tage). Sammle mindestens 5 Maßnahmen über alle Dimensionen.
5. Priorisiere nach Impact × Umsetzbarkeit: Berechne für jede Maßnahme einen Priorisierungs-Score = erwarteter Score-Gewinn × Umsetzbarkeits-Faktor (Einfach=3, Mittel=2, Komplex=1). Sortiere alle Maßnahmen absteigend nach Priorisierungs-Score. Die Top-3 bis Top-5 Maßnahmen sind die empfohlene Optimierungs-Roadmap. Dokumentiere für jede Top-Maßnahme: Titel, betroffene Dimensionen, erwarteter Score-Gewinn, Aufwand-Schätzung, Umsetzbarkeits-Einstufung, Priorisierungs-Score.

## Verifikation

- System-Profil: Zweck, Komponenten, Nutzung und bekannte Probleme vollständig dokumentiert
- 4-Dimensionen-Bewertung: Alle 4 Dimensionen haben Score (1-10), messbaren Indikator und Begründung
- Gesamt-Effizienz-Score: Formel korrekt angewendet (Durchschnitt der 4 Einzel-Scores), Ergebnis interpretiert
- Maßnahmen-Liste: mindestens 5 Maßnahmen gesammelt, jede mit Score-Gewinn, Umsetzbarkeit und Aufwand
- Priorisierung: Top-3 bis Top-5 Maßnahmen sortiert nach Priorisierungs-Score (Score-Gewinn × Umsetzbarkeits-Faktor)
- Failure-Indikator: Wenn Gesamt-Effizienz-Score >7 → Meldung "System bereits gut optimiert — Score [X]/10. Nur Feintuning-Maßnahmen sinnvoll, keine grundlegenden Optimierungen nötig. Empfehle Fokus auf neue Features statt Effizienz-Steigerung."
- Akzeptanzkriterium: Vollständiges System-Profil, alle 4 Dimensionen bewertet mit Begründung, Gesamt-Score berechnet, ≥5 Maßnahmen gesammelt, Top-3 bis Top-5 priorisiert mit Priorisierungs-Score

## Abhängigkeiten

- Input: Beschreibung des zu optimierenden Systems (Zweck, Komponenten, aktuelle Metriken falls vorhanden) — kann unstrukturiert sein, der Skill strukturiert sie
- Empfohlene Vorgänger-Skills: `elvis-automation-audit` (identifiziert Automatisierungs-Kandidaten, die dann mit diesem Skill optimiert werden können)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) System-Profil (Zweck, Komponenten, Nutzung, Probleme), (2) 4-Dimensionen-Bewertung (je Score, Indikator, Begründung), (3) Gesamt-Effizienz-Score (Formel und Interpretation), (4) Maßnahmen-Liste (≥5 Maßnahmen mit Score-Gewinn und Umsetzbarkeit), (5) Priorisierte Roadmap (Top-3 bis Top-5 Maßnahmen sortiert nach Priorisierungs-Score). Einsatzbereit als Optimierungs-Plan für Entwicklungs-Team.
