# Skill

## Name

/elvis-identity-generator

## Beschreibung

Generiert eine neue Identity-Definition auf Basis einer Anforderungs-Beschreibung des Operators. Max. 1 Identity pro Durchlauf. Output im bindenden 7-Sektionen-Format (Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz) gemäß `templates/identity-template.md`. Identities beschreiben WER (Persönlichkeit) — niemals WAS (Aufgaben). Sichert Qualität durch Safeguards gegen unkontrollierte Generierung und Identity-Agent-Verwechslung.

## Ziele

- 1 vollständige Identity-Datei pro Durchlauf, im verbindlichen 7-Sektionen-Format nach `templates/identity-template.md`
- Operator hat vor der Generierung explizit freigegeben — kein stiller Auto-Commit
- Identity erfüllt die Identity-Agent-Trennung: Charakter-Beschreibung und Persönlichkeitsmerkmale enthalten ausschließlich Persönlichkeitseigenschaften, keine Aufgaben-Verben
- Star Trek Referenz ist unverwechselbar dem genannten Charakter zuzuordnen — kein austauschbares Allgemein-Zitat

## Strategie

Der Identity-Generator arbeitet nach dem Plan-Approve-Execute-Pattern: Erst eine kompakte Identity-Vorschau erstellen und vom Operator bestätigen lassen, dann die vollständige Identity Section-by-Section generieren. Die Trennung ist der zentrale Safeguard — der Operator sieht Name, 1-Satz-Charakter-Skizze und 3 Persönlichkeitsmerkmale bevor eine einzige Zeile Identity-Text geschrieben wird. Das Template (`templates/identity-template.md`) ist die verbindliche Vorlage — der Generator darf keine Sektionen erfinden oder weglassen. Alle 7 Sektionen müssen befüllt sein. Kritisch: Identities beschreiben Persönlichkeit, niemals Aufgaben. "Lässt sich von Emotionen anderer nicht beirren" ist Identity. "Analysiert Daten" ist Agent-Beschreibung und ein sofortiger Fehler.

## Einschränkungen

- **Max-Limit:** Max. 1 Identity pro Durchlauf. Identities sind zu nuancenreich für Batching — Charakter, Kommunikationsstil, authentische Schwächen erfordern Einzelbehandlung. Anforderungen für mehrere Identities werden sequentiell in separaten Durchläufen bearbeitet.
- **Approval-Gate:** Vor der Erstellung zeigt der Generator die geplante Identity-Übersicht (Name, 1-Satz-Charakter-Skizze, 3 Persönlichkeitsmerkmale als Stichworte) und wartet auf explizite Operator-Bestätigung ("bestätigt" oder "ok"). Keine Identity wird ohne Bestätigung erstellt.
- **Stop-Bedingung:** Der Prozess endet regulär wenn die Identity erstellt und vom Operator freigegeben wurde. Der Prozess endet vorzeitig wenn der Operator explizit abbricht ("stop", "abbrechen") oder wenn nach 3 Iterationen keine valide Anforderung formulierbar ist.
- **Rollback-Hinweis:** Wenn die generierte Identity nicht dem Template entspricht oder Aufgaben-Verben in der Charakter-Beschreibung enthält (Identity-Agent-Verwechslung), die Original-Anforderung erneut senden und komplett neu generieren — nicht iterativ korrigieren. Präzisierte Neu-Generierung ist schneller als schrittweise Reparatur.
- Kein automatisches Speichern oder Commiten — der Operator führt das manuelle Speichern durch

## Ausführungsschritte

1. Lies die Anforderung des Operators: Beschreibung der gewünschten Persönlichkeit (Star Trek Charakter-Zuordnung oder Charakterskizze). Prüfe zwei Dinge: (a) Anzahl — bei mehr als 1 Identity informiere den Operator: "Anforderung enthält [N] Identities — max. 1 pro Durchlauf. Ich bearbeite die erste jetzt." (b) Typ — prüfe ob die Anforderung eine Persönlichkeit beschreibt (Identity) oder Aufgaben (Agent). Bei Verwechslung: "Die Anforderung beschreibt Aufgaben — das gehört in eine Agent-Definition. Eine Identity beschreibt WER jemand ist, nicht WAS er tut. Bitte die Persönlichkeit, den Charakter, die Kommunikationsart beschreiben."
2. **[APPROVAL-GATE]** Erstelle die Identity-Vorschau mit 3 Elementen: Name (Star Trek Charakter-Name, Kleinbuchstaben), 1-Satz-Charakter-Skizze (Persönlichkeit, keine Aufgaben-Verben), 3 Persönlichkeitsmerkmale als Stichworte. Präsentiere die Vorschau an den Operator und warte auf explizite Bestätigung ("bestätigt" oder "ok"). Schritt endet hier — keine weiteren Aktionen ohne Bestätigung.
3. Nach Bestätigung: Generiere die Identity vollständig Section-by-Section nach `templates/identity-template.md`. Alle 7 Sektionen müssen befüllt sein: Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz. KRITISCH: Charakter-Beschreibung (3–5 Sätze) und Persönlichkeitsmerkmale (5–8 Bullet Points) dürfen KEINE Aufgaben-Verben enthalten ("analysiert", "erstellt", "plant", "bearbeitet" = sofortiger Fehler). Schwächen müssen authentisch sein — Pseudo-Schwächen ("arbeitet zu hart") sind ungültig. Star Trek Referenz: 1 unverwechselbares Zitat (Original-Englisch + deutsche Übersetzung) das ausschließlich diesem Charakter zuzuordnen ist. D006-Konformität in allen Ausführungsdetails.
4. Präsentiere den generierten Identity-Volltext an den Operator. Warte auf Freigabe ("ok", "weiter") oder Korrektur-Anforderung. Bei Korrektur: max. 3 Versuche, dann Identity als "Offen" markieren und Ursprungs-Anforderung für den nächsten Durchlauf notieren.
5. Abschluss-Zusammenfassung: Identity-Name, Status (Erstellt / Offen / Abgebrochen), Dateipfad (`identity/[name].md`). Hinweis zum manuellen Speichern: "Identity wurde noch nicht gespeichert. Bitte kopiere den Inhalt in `identity/[name].md` und führe `git add identity/[name].md && git commit -m 'feat: identity [name]'` aus."

## Verifikation

- Approval-Gate eingehalten: Identity wurde erst nach expliziter Bestätigung in Schritt 2 generiert
- Format-Konformität: Identity hat genau 7 Sektionen mit den exakten Header-Namen aus `templates/identity-template.md` (Name, Charakter-Beschreibung, Persönlichkeitsmerkmale, Kommunikationsstil, Stärken, Schwächen, Star Trek Referenz)
- Identity-Agent-Trennung: Charakter-Beschreibung und Persönlichkeitsmerkmale enthalten keine Aufgaben-Verben ("analysiert", "erstellt", "plant") — ausschließlich Persönlichkeitseigenschaften und Verhaltensweisen
- Star Trek Referenz ist unverwechselbar: Das Zitat könnte nur von diesem Charakter stammen
- Abschluss-Zusammenfassung vorhanden mit Status und Dateipfad
- Failure-Indikator: Wenn Charakter-Beschreibung oder Persönlichkeitsmerkmale Aufgaben-Verben enthalten (Identity-Agent-Verwechslung) — Output ist ungültig; Identity neu generieren
- Akzeptanzkriterium: 1 Identity generiert oder mit Status "Offen" dokumentiert, Charakter-Beschreibung enthält ausschließlich Persönlichkeitsmerkmale, Operator über jeden Schritt informiert

## Abhängigkeiten

- Input: Beschreibung der gewünschten Persönlichkeit (Star Trek Charakter-Zuordnung, Charaktereigenschaften, Kommunikationsstil-Hinweise)
- Empfohlene Vorgänger-Skills: keine (eigenständig einsetzbar — kein Vorgänger-Skill erforderlich)
- Hinweis: Output (`identity/[name].md`) wird von `/elvis-agent-creator` (Phase 2) konsumiert — Identity und Agent-Definition werden dort zusammengeführt. Die klare Identity-Agent-Trennung im Output ist Voraussetzung für eine fehlerfreie Zusammenführung.

## Output

Identity-Vorschau (vor Bestätigung: Name + 1-Satz-Charakter-Skizze + 3 Persönlichkeitsmerkmale) + vollständige Identity-Definition im 7-Sektionen-Format nach `templates/identity-template.md` (nach Bestätigung) + Abschluss-Zusammenfassung mit Status und Dateipfad. Alle Inhalte im Chat ausgegeben — kein automatisches Speichern.
