# Skill

## Name

/elvis-source-validator

## Beschreibung

Prüft eine Sammlung von Informationsquellen systematisch nach einem 5-Kriterien-Scoring-System (Autorität, Aktualität, Methodik, Belege, Bias). Jede Quelle erhält einen Gesamtscore von max. 25 Punkten — Quellen mit Score ≥ 15 gelten als "verwendbar", Quellen darunter als "nicht verwendbar". Liefert eine priorisierte Auswahl der besten Quellen plus Hinweise auf Qualitätslücken.

## Ziele

- Vollständiges 5-Kriterien-Scoring für alle eingereichten Quellen (je 1–5 Punkte pro Kriterium)
- Einstufung jeder Quelle als "verwendbar" (≥ 15/25) oder "nicht verwendbar" (< 15/25)
- Mindestens 50 % der Quellen mit Score ≥ 15 — oder Failure-Abbruch
- Priorisierte Rangliste der "verwendbaren" Quellen nach Gesamtscore
- Qualitätslücken-Bericht: welche Kriterien sind systemisch schwach (häufig Score 1–2)?

## Strategie

Quellen-Qualität wird oft pauschal nach Bekanntheit bewertet ("Forbes" = gut, "Blog" = schlecht). Dieses 5-Kriterien-System erzwingt kriterienbasierte Bewertung unabhängig vom Publisher-Namen. Die Schwelle 15/25 entspricht einem Durchschnitt von 3/5 pro Kriterium — solide aber nicht perfekt. Ein Quellen-Set bei dem > 50 % die Schwelle verfehlen signalisiert grundlegende Recherche-Probleme und erfordert Neu-Recherche statt Weiterarbeit mit schlechten Quellen.

## Einschränkungen

- Mindestens 3, maximal 20 Quellen pro Durchlauf — bei > 20 Quellen vorab nach Relevanz auf 20 reduzieren
- Jedes der 5 Kriterien muss bewertet werden — kein Kriterium darf als "nicht anwendbar" übersprungen werden
- Score-Begründungen: pro Kriterium 1 Satz Erklärung (warum dieser Score?)
- Keine automatische Freigabe ohne vollständige Bewertung — Teilbewertungen sind ungültig
- Quellen-URLs oder eindeutige Identifikationen müssen im Output stehen

## Ausführungsschritte

1. Nimm die Liste der zu prüfenden Quellen entgegen. Erstelle eine Quellen-Inventarliste mit fortlaufender Nummer, Quellen-Name, URL und Typ (Studie/Artikel/Video/Social-Post/Buch/Report). Zähle die Quellen — bei mehr als 20 Quellen: reduziere auf 20 durch Eliminierung offensichtlich irrelevanter Quellen (Begründung in 1 Satz pro eliminierten Eintrag).
2. Bewerte jede Quelle nach **Kriterium 1 Autorität** (1–5): Wer steht hinter dieser Quelle? 1 = Anonyme Person oder unbekannte Seite ohne nachweisbare Expertise, 2 = Branchenbekannter Blogger oder Journalist ohne Peer-Review, 3 = Anerkannte Fachpublikation oder nachgewiesener Experte, 4 = Peer-reviewte Publikation oder Institution mit klarem Mandat, 5 = Primärquelle (Original-Studie, offizieller Bericht, direkte Erhebung). Dokumentiere Score + 1-Satz-Begründung.
3. Bewerte jede Quelle nach **Kriterium 2 Aktualität** (1–5): Wie aktuell ist die Information? 1 = Älter als 36 Monate, 2 = 24–36 Monate alt, 3 = 12–24 Monate alt, 4 = 6–12 Monate alt, 5 = Weniger als 6 Monate alt (oder für das spezifische Thema zeitlos gültig — dann Score 4 + Vermerk "zeitlos"). Bewerte nach **Kriterium 3 Methodik** (1–5): Ist die Erhebungsmethode transparent? 1 = Keine Methodenbeschreibung, 2 = Vage Beschreibung ohne Nachvollziehbarkeit, 3 = Grundlegende Methodik beschrieben, 4 = Vollständige Methodik mit Stichprobengröße, 5 = Peer-reviewte oder replizierbare Methodik mit Rohdaten. Dokumentiere je Score + 1-Satz-Begründung.
4. Bewerte jede Quelle nach **Kriterium 4 Belege** (1–5): Werden Aussagen belegt? 1 = Keine Belege, reine Meinung, 2 = Einzelne Anekdoten ohne Repräsentativität, 3 = Einige Belege vorhanden aber lückenhaft, 4 = Solide Belegdichte mit Verweisen, 5 = Vollständige Quellenangaben, jede zentrale Aussage belegt. Bewerte nach **Kriterium 5 Bias** (1–5): Wie unparteiisch ist die Quelle? 1 = Offensichtlicher kommerzieller oder ideologischer Bias ohne Offenlegung, 2 = Erkennbarer Bias, der Schlussfolgerungen verzerrt, 3 = Leichter Bias erkennbar, Kernaussagen aber valide, 4 = Neutrale Darstellung, mögliche Bias-Quellen offengelegt, 5 = Strukturell neutral (z.B. staatliche Statistik, unabhängige Forschungseinrichtung). Dokumentiere je Score + 1-Satz-Begründung.
5. Summiere für jede Quelle den Gesamtscore (Summe aller 5 Kriterien, max. 25). Erstelle die Scoring-Tabelle (N Zeilen × 7 Spalten: Quelle-Nr., Name, Autorität, Aktualität, Methodik, Belege, Bias, Gesamtscore). Markiere jede Zeile als ✓ "verwendbar" (Score ≥ 15) oder ✗ "nicht verwendbar" (Score < 15). Prüfe: Sind mindestens 50 % der Quellen "verwendbar"? Falls nicht, löse Failure-Indikator aus. Erstelle die Qualitätslücken-Analyse: welches der 5 Kriterien hat den niedrigsten Durchschnittsscore über alle Quellen (systemisch schwaches Kriterium)?

## Verifikation

- Scoring-Vollständigkeit: Alle Quellen haben alle 5 Kriterien bewertet (N × 5 Felder vollständig), jedes Feld enthält Score + Begründung
- Schwellen-Einstufung: Jede Quelle ist als "verwendbar" oder "nicht verwendbar" markiert
- 50%-Regel: Anzahl "verwendbarer" Quellen ≥ 50 % der Gesamt-Quellenzahl (dokumentiert als Formel: X/N ≥ 0,5)
- Qualitätslücken-Bericht vorhanden: schwächstes Kriterium benannt mit Durchschnittsscore
- Failure-Indikator: Weniger als 50 % der Quellen erreichen Score ≥ 15 → Skill bricht ab mit "Quellen-Qualität unzureichend: Weniger als 50 % der geprüften Quellen (X/N) erreichen Score ≥ 15 — Recherche mit besseren Quellen wiederholen oder Thema neu eingrenzen"
- Akzeptanzkriterium: Vollständige Scoring-Tabelle, ≥ 50 % "verwendbar", Qualitätslücken-Bericht, priorisierte Rangliste der "verwendbaren" Quellen

## Abhängigkeiten

- Input: Liste von 3–20 Informationsquellen mit Name und URL (oder eindeutiger Identifikation) — z.B. aus /elvis-market-scan, /elvis-ai-research oder manuell zusammengestellt
- Empfohlene Vorgänger-Skills: /elvis-market-scan (liefert 10 Quellen als Bewertungs-Input), /elvis-ai-research (KI-generierte Quellen zur Qualitätsprüfung)

## Output

Quellen-Bewertungs-Report mit 3 Teilen: (1) Scoring-Tabelle (alle Quellen × 7 Spalten inkl. Gesamtscore und Verwendbarkeits-Markierung), (2) Priorisierte Rangliste der "verwendbaren" Quellen (absteigend nach Score), (3) Qualitätslücken-Bericht (systemisch schwaches Kriterium, empfohlene Recherche-Verbesserungen). Gesamtlänge: max. 1.000 Wörter (ohne Tabelle).
