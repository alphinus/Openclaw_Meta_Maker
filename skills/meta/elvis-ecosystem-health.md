# Skill

## Name

/elvis-ecosystem-health

## Beschreibung

Führt einen schnellen quantitativen Gesundheitscheck des OpenClaw-Ökosystems durch und gibt einen Score von 0–100 aus. Der Score setzt sich aus 4 Kategorien zu je 25 Punkten zusammen: Template-Konformität, Querverweis-Integrität, Safeguard-Vollständigkeit und Kategorie-Balance. Read-only, keine Dateiänderungen. Kein Kontext, keine Empfehlungen (das ist Aufgabe von /elvis-system-analyzer) — nur Score, Breakdown und benannte Issues mit Zähler.

## Ziele

- Gesamtscore 0–100 mit Breakdown nach 4 Kategorien (je 0–25 Punkte)
- Benannte Issues pro Kategorie mit explizitem Zähler (z.B. "3 Agents mit gebrochenem Soul-Verweis")
- Schneller Überblick in einem Durchlauf — kein Deep-Dive, keine qualitative Analyse
- Klare Abgrenzung: Score zeigt WO Probleme sind; /elvis-system-analyzer erklärt WARUM und gibt Empfehlungen

## Strategie

Ecosystem-Health ist der quantitative Quick-Check — nicht zu verwechseln mit /elvis-system-analyzer, der qualitative Tiefenanalyse mit Kontext und Handlungsempfehlungen liefert. Dieser Skill misst und zählt: Wie viele Entities entsprechen dem Template? Wie viele Querverweise sind intakt? Wie vollständig sind die Safeguards? Wie ausgeglichen ist die Kategorie-Verteilung? Das Ergebnis ist ein einziger Score der sofort zeigt ob das Ökosystem gesund ist. Keine Empfehlungen, keine Priorisierung, kein Kontext zu den Issues — wer Tiefe braucht, ruft /elvis-system-analyzer auf.

## Einschränkungen

- **Max-Limit:** Max. 1 Health-Check pro Durchlauf. Ein Check = vollständiger Scan aller 4 Kategorien des gesamten Ökosystems.
- **Approval-Gate:** Kein Approval-Gate notwendig — read-only Score-Output ohne Änderungen. ABER als nummerierter Schritt (Schritt 7) vorhanden: "Präsentiere Score-Ergebnis — warte auf Bestätigung oder Rückfragen bevor abgeschlossen wird."
- **Stop-Bedingung:** Regulär wenn vollständiger Score-Report (Gesamtscore + alle 4 Teilscores + Issues) ausgegeben wurde. Vorzeitig wenn Ökosystem-Dateien nicht zugänglich sind — fehlende Inputs dokumentieren und Health-Check stoppen.
- **Rollback-Hinweis:** Score ist read-only — keine direkten Systemänderungen durch diesen Skill. Rollback nicht anwendbar. Bei fehlerhafter Score-Berechnung: Health-Check vollständig neu starten.
- Kein Schreiben von Dateien — alle Ergebnisse werden im Chat ausgegeben
- Keine Handlungsempfehlungen — nur Score und benannte Issues. Empfehlungen sind ausschließlich Aufgabe von /elvis-system-analyzer
- Max. 1 Check pro Durchlauf — bei erneutem Aufruf: "Bereits ein Health-Check in diesem Durchlauf abgeschlossen — neuen Durchlauf starten"

## Ausführungsschritte

1. Max-Limit prüfen: Sicherstellen dass dies der erste Health-Check in diesem Durchlauf ist. Ökosystem-Scan starten: Alle Dateien in `soul/`, `identity/`, `agent/`, `skills/` zählen und kategorisieren. Ergebnis als Inventar-Zählung: [N] Souls, [N] Identities, [N] Agents, [N] Skills (aufgeteilt nach Kategorie). Wenn keine Dateien zugänglich: "Ökosystem-Dateien nicht zugänglich — Health-Check gestoppt. Fehlende Inputs: [Liste]."

2. Template-Konformität prüfen (Kategorie 1 — max. 25 Punkte): Für jeden Entity-Typ die vorgeschriebene Sektionen-Anzahl gegen jede Datei prüfen: Souls müssen 6 Sektionen haben (## Name, ## Philosophie, ## Core Values, ## Operating Principles, ## Success Metrics, ## Geeignet für), Identities müssen 7 Sektionen haben, Agents müssen 7 Sektionen haben, Skills müssen 9 Sektionen haben. Für jeden Entity-Typ: Anzahl konformer Dateien / Gesamt-Dateien = Konformitätsrate. Teilpunktzahl = Durchschnitt aller 4 Konformitätsraten × 25. Nicht-konforme Dateien als Issues dokumentieren: "[Dateiname] hat [N] Sektionen statt [Soll]."

3. Querverweis-Integrität prüfen (Kategorie 2 — max. 25 Punkte): Alle Agent-Dateien (agent/*.md) auf 2 Arten von Referenzen prüfen: (a) Soul-Referenz: Feld "Primärer Soul" zeigt auf eine existierende Datei in soul/. (b) Skill-Referenzen: Alle Skills in "Primäre Skills" (/elvis-*) haben eine entsprechende Datei in skills/**/*.md. Gebrochene Referenzen zählen. Teilpunktzahl = (Intakte Referenzen / Gesamt-Referenzen) × 25. Gebrochene Referenzen als Issues dokumentieren: "[Agent] → [Referenz] — Datei nicht gefunden."

4. Safeguard-Vollständigkeit prüfen (Kategorie 3 — max. 25 Punkte): Alle Meta-Skills (skills/meta/*.md) auf Vorhandensein aller 4 Safeguard-Elemente prüfen: (a) Max-Limit (Formulierung "Max-Limit:" in Einschränkungen), (b) Approval-Gate (nummerierter Schritt mit "[APPROVAL-GATE]" oder "Approval-Gate:"), (c) Stop-Bedingung mit zwei Varianten (regulär + vorzeitig), (d) Rollback-Hinweis (Formulierung "Rollback-Hinweis:" in Einschränkungen). Für jeden Meta-Skill: Anzahl vorhandener Safeguards / 4 = Safeguard-Rate. Teilpunktzahl = Durchschnitt aller Meta-Skill-Safeguard-Raten × 25. Fehlende Safeguards als Issues dokumentieren: "[Skill] fehlt [Safeguard-Element]."

5. Kategorie-Balance prüfen (Kategorie 4 — max. 25 Punkte): Anzahl Skills pro Kategorie zählen: growth, content, research, strategy, automation, meta. Durchschnitt berechnen (Gesamt-Skills / 6). Standardabweichung berechnen. Teilpunktzahl = 25 × (1 − (Standardabweichung / Durchschnitt)), Minimum 0. Stark über- oder unterbesetzte Kategorien als Issues dokumentieren: "Kategorie [X]: [N] Skills (Durchschnitt: [M])" — nur bei Abweichung > 50% vom Durchschnitt.

6. Gesamtscore berechnen: Summe der 4 Teilpunktzahlen (Kategorie 1 + 2 + 3 + 4), gerundet auf ganze Zahlen. Score-Report zusammenstellen: Gesamtscore (0–100), Breakdown-Tabelle (4 Zeilen: Kategorie, Teilpunktzahl, Issues-Zähler), Liste aller benannten Issues mit Kategorien-Tag.

7. [APPROVAL-GATE] Score-Report präsentieren:

   **Ecosystem Health Score: [N]/100**

   | Kategorie | Punkte (max. 25) | Issues |
   |-----------|-----------------|--------|
   | Template-Konformität | [N] | [N] |
   | Querverweis-Integrität | [N] | [N] |
   | Safeguard-Vollständigkeit | [N] | [N] |
   | Kategorie-Balance | [N] | [N] |

   **Issues ([Gesamt-Zähler]):**
   - [Kategorie-Tag] [Issue-Beschreibung]
   - ...

   "Für qualitative Tiefenanalyse mit Kontext und Handlungsempfehlungen: /elvis-system-analyzer aufrufen."
   Präsentiere Score-Ergebnis — warte auf Bestätigung oder Rückfragen bevor abgeschlossen wird.

## Verifikation

- Score 0–100 vorhanden mit Breakdown nach exakt 4 Kategorien (je max. 25 Punkte) — fehlender Breakdown ist ein Fehler
- Issues sind benannt und gezählt (z.B. "3 Agents mit gebrochenem Soul-Verweis") — Issues ohne Zähler sind ein Fehler
- Kein Empfehlungs-Text im Output — Formulierungen wie "Du solltest..." oder "Empfehlung: ..." sind eine Überschneidung mit /elvis-system-analyzer
- Read-only bestätigt: Kein Schreiben von Dateien während des Health-Checks
- Approval-Gate als nummerierter Schritt 7 vorhanden — Safeguard-Quartet vollständig
- Failure-Indikator: Wenn kein Verzeichnis zugänglich ist → "Ökosystem-Dateien nicht zugänglich — fehlende Inputs: [Liste]. Health-Check gestoppt."
- Akzeptanzkriterium: Gesamtscore ausgegeben, alle 4 Kategorien mit Teilpunkten und Issues-Zähler dokumentiert, Score-Report vollständig im Chat

## Abhängigkeiten

- Input: Lesezugang zu den Verzeichnissen `soul/`, `identity/`, `agent/`, `skills/` im OpenClaw-Ökosystem
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Check, unabhängig einsetzbar)
- Ergänzender Skill: /elvis-system-analyzer (qualitative Tiefenanalyse mit Kontext und Handlungsempfehlungen — bei Score < 80 empfohlen)

## Output

Score-Report im Chat mit 3 Teilen: (1) Gesamtscore 0–100 als hervorgehobene Zahl, (2) Breakdown-Tabelle mit 4 Kategorien (Teilpunktzahl + Issues-Zähler pro Kategorie), (3) Liste aller benannten Issues mit Kategorien-Tag. Kein automatisches Speichern, keine Empfehlungen, keine qualitative Analyse — nur Score, Zahlen und Issues.
