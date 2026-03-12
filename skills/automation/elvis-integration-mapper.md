# Skill

## Name

/elvis-integration-mapper

## Beschreibung

Kartiert die vollständige Tool-Integrations-Landschaft: alle verwendeten Tools, verfügbare Verbindungen, Integrations-Lücken und Handlungs-Empfehlungen. Erzeugt eine Übersichts-Matrix die zeigt welche Tools bereits miteinander verbunden sind, wo manuelle Brücken existieren (Copy-Paste, CSV-Export/Import) und welche fehlenden Verbindungen das größte Automatisierungs-Potenzial haben. Dieser Übersichts-Skill ist der Vorläufer für spezifische Automatisierungs-Projekte.

## Ziele

- Tool-Inventar: mindestens 10 verwendete Tools mit Kategorie (CRM/E-Mail/Projektmanagement/Analytics/etc.) dokumentiert
- Verbindungs-Matrix: N×N-Tabelle zeigt für jedes Tool-Paar ob Integration existiert (✓), manuell (⚠) oder fehlend (✗)
- Lücken-Analyse: mindestens 5 fehlende Integrationen mit Impact-Score (Häufigkeit × Zeitaufwand) identifiziert und priorisiert
- Handlungs-Empfehlungen: Top-3 fehlende Integrationen mit empfohlenem Integrations-Ansatz (Native/Zapier/API/Webhook) und geschätztem Implementierungs-Aufwand

## Strategie

Der Skill nutzt eine systematische Matrix-Sicht statt Ad-hoc-Integrations-Planung: Die N×N-Matrix zeigt alle möglichen Verbindungen zwischen den verwendeten Tools, nicht nur die offensichtlichen. Manuelle Brücken (⚠) sind Kandidaten für Automatisierung — sie zeigen dass der Datenfluss existiert aber ineffizient ist. Fehlende Integrationen (✗) werden mit Impact-Score bewertet: Häufigkeit (wie oft wird die Verbindung benötigt) × Zeitaufwand (wie viele Minuten kostet der manuelle Workaround) = Priorisierung. Im Gegensatz zu `elvis-workflow-builder` (baut einen konkreten Workflow) und `elvis-data-pipeline` (transferiert Daten) liefert dieser Skill die Übersicht bevor spezifische Automations gebaut werden.

## Einschränkungen

- Mindestens 10 Tools erfassen — weniger ergibt keine aussagekräftige Integrations-Landschaft
- Nur Tools aufnehmen die aktiv genutzt werden (mindestens wöchentlich) — keine vergessenen Legacy-Systeme die nur historische Daten halten
- Manuelle Brücken (⚠) nur markieren wenn der Datenfluss regelmäßig benötigt wird (mindestens monatlich) — seltene Einmal-Exports sind kein Integrations-Kandidat
- Native Integrationen (✓) nur markieren wenn sie tatsächlich konfiguriert sind — verfügbare aber nicht aktivierte Integrationen zählen als fehlend (✗)
- Keine Implementierung liefern — nur Übersicht und Empfehlungen, die eigentliche Integrations-Arbeit erfolgt in nachfolgenden Skills

## Ausführungsschritte

1. Erfasse das Tool-Inventar: Bitte den Operator alle Tools zu nennen die regelmäßig (mindestens wöchentlich) verwendet werden. Für jedes Tool dokumentiere: Tool-Name, Kategorie (CRM/E-Mail/Projektmanagement/Analytics/Datenbank/etc.), primärer Zweck (1-2 Sätze). Erstelle eine Tabelle mit 3 Spalten: Tool-Name, Kategorie, Primärer Zweck. Mindestens 10 Tools erfassen.
2. Erstelle die Verbindungs-Matrix: N×N-Tabelle mit allen Tools als Zeilen und Spalten. Für jedes Tool-Paar frage den Operator: Existiert eine konfigurierte Integration (✓ = direkte Verbindung/Plugin/Native-Integration), manuelle Brücke (⚠ = regelmäßiger CSV-Export/Copy-Paste/E-Mail-Weiterleitung) oder keine Verbindung (✗ = Datenfluss existiert nicht oder nur sehr selten). Diagonale bleibt leer (Tool mit sich selbst). Matrix ist symmetrisch — nur obere Dreiecks-Hälfte ausfüllen.
3. Identifiziere Integrations-Lücken: Extrahiere alle Tool-Paare mit manueller Brücke (⚠) oder fehlender Verbindung (✗) die regelmäßig benötigt werden. Für jede Lücke bewerte: Häufigkeit (1=monatlich, 3=wöchentlich, 5=täglich), Zeitaufwand pro manuellem Transfer (Minuten), Impact-Score = Häufigkeit × Zeitaufwand. Erstelle eine Lücken-Tabelle mit 5 Spalten: Tool A, Tool B, Status (⚠/✗), Häufigkeit, Zeitaufwand, Impact-Score. Sortiere absteigend nach Impact-Score. Mindestens 5 Lücken dokumentieren.
4. Priorisiere nach Impact-Score: Die Top-3 Lücken mit höchstem Score sind Automatisierungs-Kandidaten. Für jede der Top-3 recherchiere: Gibt es eine Native-Integration (Tool A hat offizielles Plugin für Tool B), Zapier/Make-Connector verfügbar, API-Zugang auf beiden Seiten vorhanden, Webhook-Support. Dokumentiere verfügbare Integrations-Ansätze pro Lücke.
5. Empfehle Handlungs-Schritte für Top-3 Lücken: Für jede Lücke gib an: empfohlener Integrations-Ansatz (Native/Zapier/API/Webhook), geschätzter Implementierungs-Aufwand (Einfach <2h / Mittel 2-8h / Komplex >8h), erwartete Zeitersparnis pro Woche (Häufigkeit × Zeitaufwand × 0.9 — 90% Automatisierung realistisch), ROI-Zeitraum (Implementierungs-Aufwand / wöchentliche Zeitersparnis in Wochen). Priorisiere Empfehlungen mit ROI <4 Wochen.

## Verifikation

- Tool-Inventar: mindestens 10 Tools dokumentiert mit Kategorie und Zweck
- Verbindungs-Matrix: N×N-Tabelle vollständig ausgefüllt (obere Dreiecks-Hälfte), jedes Paar hat Status ✓/⚠/✗
- Lücken-Tabelle: mindestens 5 Tool-Paare mit Impact-Score dokumentiert, sortiert nach Score absteigend
- Handlungs-Empfehlungen: Top-3 Lücken haben Integrations-Ansatz, Aufwand-Schätzung und ROI-Zeitraum
- Failure-Indikator: Wenn weniger als 5 verwendete Tools mit regelmäßigem Datenfluss identifizierbar → Meldung "Tool-Landschaft zu klein für Integrations-Mapping — nur [N] Tools erfasst. Empfehle mindestens 10 aktiv genutzte Tools zu dokumentieren oder manuelles Integrations-Management beizubehalten."
- Akzeptanzkriterium: Tool-Inventar mit ≥10 Tools, vollständige Verbindungs-Matrix, Lücken-Tabelle mit ≥5 Einträgen sortiert nach Impact-Score, Top-3 mit Handlungs-Empfehlungen und ROI-Zeiträumen

## Abhängigkeiten

- Input: Liste verwendeter Tools (Name und ungefährer Zweck) — kann unstrukturiert sein, der Skill organisiert sie in Kategorien
- Empfohlene Nachfolger-Skills: `elvis-workflow-builder` (baut konkrete Workflows für identifizierte Integrations-Lücken), `elvis-data-pipeline` (implementiert Daten-Transfer für Top-Lücken)

## Output

Markdown-Dokument mit 4 Abschnitten: (1) Tool-Inventar (≥10 Tools, Kategorien, Zwecke), (2) Verbindungs-Matrix (N×N-Tabelle mit ✓/⚠/✗-Status für jedes Tool-Paar), (3) Lücken-Analyse (≥5 Tool-Paare sortiert nach Impact-Score), (4) Handlungs-Empfehlungen (Top-3 Lücken mit Integrations-Ansatz, Aufwand-Schätzung, ROI-Zeitraum). Einsatzbereit als strategische Grundlage für Integrations-Roadmap.
