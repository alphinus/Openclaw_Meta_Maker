# Skill

## Name

/elvis-revenue-tracker

## Beschreibung

Trackt monatlich Umsatz und Monetarisierungs-Metriken über 3 definierte Einkommensquellen: Monatliche Trends, CLV-Entwicklung und MRR-Berechnung (Monthly Recurring Revenue). Differenzierung zu bestehenden Skills: `elvis-monetization-planner` (S04) plant Soll-Zustände (welche Monetarisierungs-Wege bewerten wir? Wie bauen wir sie in 90 Tagen auf?). `elvis-monetization-strategy` (S05) definiert Portfolio-Strategie und Preis-Positionierung auf Meta-Ebene. Dieser Skill dagegen misst Ist-Ergebnisse: Wie viel wurde tatsächlich verdient? Welche Einkommensquelle wächst? Wie entwickelt sich der Customer Lifetime Value? Das Ergebnis ist ein monatlich aktualisierbares Revenue-Tracking-System.

## Ziele

- Definiertes Tracking-System für 3 Haupt-Einkommensquellen mit monatlicher Mess-Cadence
- MRR-Berechnung: Monthly Recurring Revenue für wiederkehrende Einnahmen (Abos, Memberships)
- CLV-Tracking: Customer Lifetime Value nach Formel `CLV = Kaufwert × Kauffrequenz × Kundendauer`
- Monatlicher Revenue-Trend: 6-Monats-Verlauf aller 3 Einkommensquellen als Vergleichstabelle
- Revenue-Mix-Analyse: Welcher Prozentsatz des Gesamtumsatzes kommt aus welcher Quelle?

## Strategie

Das Tracking-System folgt dem "Was gemessen wird, wird verbessert"-Prinzip: Ohne konsistente Messung bleiben Umsätze Bauchgefühl statt datenbasierte Entscheidungsgrundlage. Die monatliche Cadence ist bewusst gewählt — wöchentlich ist zu granular für strategische Revenue-Entscheidungen, quartalsweise zu träge für Kursanpassungen. Die CLV-Formel übersetzt Einzeltransaktionen in langfristigen Kundenwert. Die Revenue-Mix-Analyse identifiziert Abhängigkeiten: Wenn 80 % des Umsatzes aus einer Quelle kommen, ist das ein Diversifikations-Risiko.

## Einschränkungen

- Exakt 3 Haupt-Einkommensquellen im fortlaufenden Tracking — mehr verwässern den Fokus
- Nur Einkommensquellen tracken die monatlich messbare Umsätze generieren (keine Hobby-Projekte mit 0 € Revenue)
- CLV-Berechnung nur für Quellen mit wiederkehrenden Kunden (nicht sinnvoll für einmalige Freelance-Projekte)
- MRR-Tracking nur für tatsächlich wiederkehrende Einnahmen (Abos, Memberships, Retainer) — keine Hochrechnungen aus einmaligen Verkäufen
- Mindestens 3 Monate Daten erforderlich für aussagekräftige Trend-Aussagen (Tracking-System wird ab Monat 4 aussagekräftig)

## Ausführungsschritte

1. Definiere die 3 Haupt-Einkommensquellen gemeinsam mit dem Operator: Was sind die wichtigsten Revenue-Streams? Typische Kategorien: (A) Digitale Produkte (E-Books, Kurse, Templates), (B) Services (Coaching, Consulting, Freelancing), (C) Wiederkehrende Einnahmen (Memberships, Sponsorships, Affiliate). Dokumentiere für jede Quelle: Bezeichnung, Typ (einmalig / wiederkehrend), Datenquelle für Umsatz-Zahlen (z.B. Stripe Dashboard / PayPal / Rechnung-Excel).
2. Erhebe für jede der 3 Einkommensquellen die Umsatzzahlen der letzten 3 Monate: Monat 1, Monat 2, Monat 3 (rückwirkend). Erstelle eine Baseline-Tabelle mit 5 Spalten: Einkommensquelle | Monat 1 (€) | Monat 2 (€) | Monat 3 (€) | Trend (↗ ↘ →). Berechne den 3-Monats-Durchschnitt je Quelle als Baseline-Referenz.
3. Berechne den MRR (Monthly Recurring Revenue) für alle wiederkehrenden Einkommensquellen: Summiere alle Abos, Memberships, Retainer-Verträge die monatlich Umsatz generieren. Formel: `MRR = Anzahl Abos × durchschnittlicher Abo-Preis`. Beispiel: 20 Mitglieder × 15 €/Monat = 300 € MRR. Dokumentiere zusätzlich die Churn-Rate: `Churn (%) = Gekündigte Abos / Gesamt-Abos zu Monatsbeginn × 100`.
4. Berechne den CLV (Customer Lifetime Value) für mindestens eine der 3 Einkommensquellen mit wiederkehrenden Kunden: Verwende die Formel `CLV = Kaufwert × Kauffrequenz × Kundendauer`. Beispiel: Ein Kurs-Kunde kauft durchschnittlich 2 Kurse (Kauffrequenz), je 100 € (Kaufwert), über 12 Monate Kundenbeziehung (Kundendauer) = CLV von 200 €. Dokumentiere alle 3 Komponenten der Formel mit ihren aktuellen Durchschnittswerten.
5. Erstelle die monatliche Revenue-Tracking-Tabelle mit 10 Spalten: Monat | Einkommensquelle 1 (€) | Einkommensquelle 2 (€) | Einkommensquelle 3 (€) | Gesamt-Revenue (€) | MRR (€) | Churn (%) | CLV (€) | Trend ↗↘→ | Notizen. Befülle die ersten 3 Monate (Baseline) und lege 9 weitere Monats-Zeilen als Platzhalter an (für 12-Monats-Zyklus).
6. Berechne die Revenue-Mix-Analyse für den aktuellen Monat: Welcher Prozentsatz des Gesamtumsatzes kommt aus welcher Quelle? Formel: `Anteil (%) = Umsatz Quelle X / Gesamt-Revenue × 100`. Visualisiere das Ergebnis als Prozent-Verteilung: Quelle 1: 45 %, Quelle 2: 35 %, Quelle 3: 20 %. Identifiziere Konzentrationsrisiken: Wenn >60 % aus einer Quelle kommt → Notiz "Diversifikation prüfen".
7. Schreibe die monatliche Tracking-Anleitung (max. 10 Schritte): Wann messen (erster Tag des Folgemonats für abgelaufenen Monat), wo die Umsatzdaten abrufen (Klickpfad in Stripe / PayPal / Rechnungs-Tool), wie MRR und CLV berechnen (Formeln als Copy-Paste-Vorlage), wie Revenue-Mix aktualisieren, wie Trends interpretieren (↗ = >10 % Wachstum / → = ±10 % / ↘ = >10 % Rückgang). Füge Kalender-Erinnerungs-Template bei.

## Verifikation

- Alle 3 Einkommensquellen definiert: Bezeichnung, Typ (einmalig/wiederkehrend), Datenquelle dokumentiert
- Baseline vorhanden: Alle 3 Quellen mit 3-Monats-Umsatzzahlen rückwirkend befüllt
- MRR berechnet: Für alle wiederkehrenden Quellen MRR-Wert mit Abo-Anzahl × Preis dokumentiert
- CLV-Formel vorhanden: `CLV = Kaufwert × Kauffrequenz × Kundendauer` explizit mit Beispielrechnung dokumentiert
- Tracking-Tabelle: 12 Monats-Zeilen angelegt (3 Monate Baseline befüllt, 9 als Platzhalter)
- Failure-Indikator: Wenn weniger als 2 der 3 Einkommensquellen mit konkreten Umsatzzahlen (nicht Schätzungen) trackbar sind → Skill gibt aus: "Weniger als 2 der 3 Einkommensquellen mit echten Zahlen trackbar — Revenue-Tracking nicht valide. Bitte Datenquellen-Zugang prüfen oder Tracking-Setup (z.B. Stripe-Integration, Rechnungs-Export) einrichten."
- Akzeptanzkriterium: Befüllte Revenue-Tracking-Tabelle (3 Monate Baseline), MRR-Berechnung, CLV-Formel mit Beispielrechnung, Revenue-Mix-Analyse und monatliche Tracking-Anleitung

## Abhängigkeiten

- Input: Zugang zu Umsatzdaten für alle 3 Einkommensquellen über mindestens 3 Monate (z.B. Stripe Dashboard, PayPal, Rechnungs-Tool, Freelance-Projekt-Excel)
- Empfohlene Vorgänger-Skills: /elvis-monetization-planner (identifiziert die wichtigsten Einkommensquellen die getrackt werden sollten), /elvis-performance-tracker (liefert Tracking-Framework-Muster)

## Output

Markdown-Dokument mit 5 Abschnitten: (1) 3 Einkommensquellen-Steckbriefe (Bezeichnung, Typ, Datenquelle, 3-Monats-Baseline), (2) Revenue-Tracking-Tabelle (10 Spalten × 12 Monate, 3 Monate Baseline befüllt), (3) MRR-Berechnung mit Churn-Rate für wiederkehrende Einnahmen, (4) CLV-Formel mit Beispielrechnung (`CLV = Kaufwert × Kauffrequenz × Kundendauer`), (5) Revenue-Mix-Analyse mit Konzentrations-Risiko-Bewertung und monatliche Tracking-Anleitung. Sofort einsatzbereit als monatliches Revenue-Mess-System.
