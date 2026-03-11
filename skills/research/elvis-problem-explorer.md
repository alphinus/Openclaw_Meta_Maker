# Skill

## Name

/elvis-problem-explorer

## Beschreibung

Kartiert einen Problemraum systematisch: 5-Warum-Analyse (5 Iterationen von "Warum?" ausgehend vom Symptom), 3 Problemebenen (Symptom / Ursache / Systemursache) und 10 Sub-Probleme als Untermenge des Haupt-Problems. Ergebnis: Problem-Map mit 3 Ebenen plus Priorisierungs-Empfehlung nach Auswirkung — eine strukturierte Grundlage für Lösungs-Entwicklung statt symptomatischer Schnell-Fixes.

## Ziele

- 5-Warum-Analyse mit 5 vollständigen Iterationen vom Symptom zur Systemursache
- 3-Ebenen-Klassifikation: Symptom, Ursache und Systemursache klar voneinander getrennt und beschrieben
- 10 Sub-Probleme: eigenständige Teilprobleme die zusammen das Haupt-Problem konstituieren
- Problem-Map: visuelle Darstellung der 3 Ebenen und Sub-Probleme-Zuordnung (Markdown-Struktur)
- Priorisierungs-Empfehlung: Top-3 Sub-Probleme nach Auswirkung mit Begründung

## Strategie

Die 5-Warum-Methode ist wirkungsvoll wenn sie diszipliniert angewendet wird — das häufigste Fehler-Muster ist Iteration 2–3 zu überspringen und direkt von Symptom zu Systemursache zu springen. Dieser Skill erzwingt alle 5 Iterationen mit expliziter Begründung pro Schritt. Die 3-Ebenen-Klassifikation (Symptom / Ursache / Systemursache) liefert Handlungs-Orientierung: Symptome können schnell adressiert werden (sofortige Wirkung, keine Nachhaltigkeit), Ursachen brauchen gezielte Interventionen, Systemursachen erfordern strukturelle Änderungen. Die 10 Sub-Probleme verhindern Tunnel-Fokus: ein komplexes Problem hat immer mehrere Aspekte die parallel adressiert werden müssen.

## Einschränkungen

- Genau 5 Warum-Iterationen — nicht weniger (dann Problem neu analysieren), nicht mehr (dann auf 5 komprimieren)
- Jede Iteration muss kausal aus der vorherigen folgen (kein Sprung über Ebenen)
- Sub-Probleme müssen eigenständig sein: kein Sub-Problem darf lediglich eine Umformulierung eines anderen sein
- Priorisierungs-Empfehlung nach Auswirkung — nicht nach Lösungs-Einfachheit oder persönlicher Präferenz
- Symptom, Ursache und Systemursache müssen operationell unterscheidbar beschrieben sein — nicht "alles ist eine Systemursache"

## Ausführungsschritte

1. Definiere das Haupt-Problem: Beschreibe das Problem in 2–3 Sätzen aus der Perspektive des Betroffenen (nicht des Lösungsanbieters). Identifiziere das erste Symptom: die sichtbarste, unmittelbarste Manifestation des Problems (was bemerkt jemand zuerst?). Notiere: "Symptom (Ausgangspunkt der 5-Warum-Analyse): [Konkrete Beschreibung]."
2. Führe die 5-Warum-Analyse durch — 5 Iterationen, jede folgt kausal aus der vorherigen: **Iteration 1**: Warum tritt [Symptom] auf? → [Antwort 1]. **Iteration 2**: Warum [Antwort 1]? → [Antwort 2]. **Iteration 3**: Warum [Antwort 2]? → [Antwort 3]. **Iteration 4**: Warum [Antwort 3]? → [Antwort 4]. **Iteration 5**: Warum [Antwort 4]? → [Antwort 5 = Systemursache]. Format: Nummerierte Liste mit Warum-Frage + Antwort pro Iteration. Prüfe nach jeder Iteration: Ist die Antwort wirklich eine Ursache der vorherigen Antwort oder eine unabhängige Beobachtung?
3. Klassifiziere die Iterationsergebnisse in 3 Problemebenen: **Ebene 1 — Symptom**: Iteration 1 Antwort (sichtbares Phänomen, direkt beobachtbar). **Ebene 2 — Ursache**: Iterationen 2–3 Antworten (zugrundeliegende Mechanismen, durch Analyse erkennbar). **Ebene 3 — Systemursache**: Iterationen 4–5 Antworten (strukturelle, systemische Faktoren die die Ursachen ermöglichen). Beschreibe jede Ebene in 2–3 Sätzen: Was charakterisiert Probleme auf dieser Ebene und welche Art von Intervention ist hier sinnvoll?
4. Identifiziere 10 Sub-Probleme: Durchsuche alle 5 Iterationen und die 3 Ebenen nach Teilproblemen die eigenständig adressierbar sind. Füge Sub-Probleme aus Randbeobachtungen hinzu (was wurde in der 5-Warum-Kette erwähnt aber nicht vertieft?). Format pro Sub-Problem: | Nr. | Sub-Problem | Ebene (1/2/3) | Eigenständig adressierbar (Ja/Nein) | Auswirkung auf Haupt-Problem (Hoch/Mittel/Niedrig) |. Alle 10 Einträge müssen vollständig ausgefüllt sein.
5. Erstelle die Problem-Map als Markdown-Struktur: Haupt-Problem oben, darunter 3 Ebenen-Abschnitte mit zugeordneten Sub-Problemen, 5-Warum-Kette als seitliche Referenz. Format: Eingerückte Markdown-Liste die die Hierarchie und Zuordnungen zeigt. Ziel: Auf einen Blick erkennbar welche Sub-Probleme auf welcher Ebene liegen.
6. Entwickle die Priorisierungs-Empfehlung: Wähle die Top-3 Sub-Probleme nach "Auswirkung auf Haupt-Problem" (Hoch > Mittel > Niedrig). Bei Gleichstand: Priorisiere Sub-Probleme auf Ebene 2 und 3 gegenüber Ebene 1. Format pro Empfehlung: "Priorität [Nr.]: Sub-Problem [X]. Auswirkung: [Hoch/Mittel/Niedrig]. Begründung: [Warum hat die Adressierung dieses Sub-Problems die größte Hebelwirkung auf das Haupt-Problem — 2 Sätze]. Interventions-Typ: [Symptom-Fix / Ursachen-Intervention / Systemische Änderung]."
7. Schreibe die Problem-Synthesese in 3 Sätzen: Kern-Einsicht aus der 5-Warum-Analyse (was war überraschend oder nicht-intuitiv), kritischste Systemursache und ihre Implikation, wichtigste Einschränkung für die Lösungs-Entwicklung (was macht dieses Problem schwerer zu lösen als es zunächst scheint?).

## Verifikation

- 5-Warum-Vollständigkeit: Genau 5 Iterationen mit Warum-Frage und Antwort, jede kausal mit der vorherigen verbunden
- 3-Ebenen-Klassifikation: Alle Iterationen einer Ebene zugeordnet, Ebenen operationell unterscheidbar beschrieben
- Sub-Probleme: Genau 10 Einträge in der Tabelle, alle mit Ebenen-Zuordnung und Auswirkungs-Einschätzung
- Problem-Map: Markdown-Struktur vorhanden mit Haupt-Problem, 3 Ebenen und Sub-Problem-Zuordnung
- Priorisierungs-Empfehlung: Top-3 mit Begründung und Interventions-Typ vorhanden
- Failure-Indikator: Weniger als 3 vollständige Warum-Iterationen (mit Kausal-Verbindung zur vorherigen) → Skill bricht ab mit "5-Warum-Analyse unvollständig: Weniger als 3 kausale Iterationen nachweisbar — Systemursachen-Analyse nicht möglich"
- Akzeptanzkriterium: 5 kausale Iterationen, 3 Ebenen beschrieben, 10 Sub-Probleme in Tabelle, Problem-Map, Priorisierungs-Empfehlung Top-3, Problem-Synthese

## Abhängigkeiten

- Input: Haupt-Problem in 2–3 Sätzen beschrieben (aus der Perspektive des Betroffenen) und optional: erste bekannte Symptome oder bisherige Lösungsversuche
- Empfohlene Vorgänger-Skills: /elvis-pain-point-finder (liefert Pain Points die als Ausgangsprobleme für die 5-Warum-Analyse dienen können)

## Output

Problem-Analyse mit 5 Teilen: (1) Haupt-Problem-Definition + Symptom-Ausgangspunkt, (2) 5-Warum-Kette (5 Iterationen), (3) 3-Ebenen-Klassifikation mit Charakterisierung, (4) Sub-Problem-Tabelle (10 Einträge × 5 Spalten) + Problem-Map, (5) Priorisierungs-Empfehlung Top-3 + Problem-Synthese. Gesamtlänge: max. 1.300 Wörter (ohne Tabellen und Map).
