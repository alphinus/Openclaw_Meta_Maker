# Skill

## Name

/elvis-dm-writer

## Beschreibung

Schreibt eine Cold-DM-Sequenz aus 3 Nachrichten: Opener (max. 150 Zeichen), Mehrwert (max. 200 Zeichen), Follow-Up (max. 100 Zeichen). Mit Timing-Plan: Nachricht 2 frühestens 24h nach Opener, Nachricht 3 frühestens 48h nach Nachricht 2. Kein Verkaufsangebot im Opener.

## Ziele

- 3 fertige Nachrichten: Opener, Mehrwert, Follow-Up — alle innerhalb ihrer Zeichenlimits
- Opener: spezifisch auf Empfänger, keine Template-Floskeln ("Ich habe Ihre Arbeit verfolgt")
- Mehrwert ohne Gegenleistung: konkrete Ressource, Insight oder Idee die der Empfänger sofort nutzen kann
- Follow-Up: weiche CTA ("Falls relevant — [Angebot in 1 Satz]"), kein Druck
- Timing-Plan dokumentiert: Tag 0 / Tag 1+ / Tag 3+

## Strategie

Cold-DMs haben eine Öffnungsrate nahe 0 wenn sie wie Spam aussehen. Die 3-Nachrichten-Struktur simuliert eine organische Beziehung: Opener zeigt echtes Interesse (nicht Copy-Paste), Mehrwert gibt ohne sofortige Gegenleistung (baut Vertrauen), Follow-Up macht das Angebot nach 2 Wärme-Signalen (höhere Konversionsrate). Das Timing verhindert Spam-Wirkung durch Staffelung über mindestens 3 Tage.

## Einschränkungen

- Nachricht 1 Opener: max. 150 Zeichen, kein "Ich habe Ihre Arbeit verfolgt", kein Preis, kein Verkaufsangebot
- Nachricht 2 Mehrwert: max. 200 Zeichen, konkreter Mehrwert ohne implizite oder explizite Gegenleistung
- Nachricht 3 Follow-Up: max. 100 Zeichen, weiche Einladung nicht Druck
- Timing: Nachricht 2 frühestens 24h nach Opener; Nachricht 3 frühestens 48h nach Nachricht 2
- Kein Preis oder Verkaufsangebot in Nachricht 1 oder 2 — nur in Nachricht 3 erlaubt (als 1 Satz)
- Kein automatisches Versenden — Output ist zur manuellen Freigabe und Anpassung bestimmt

## Ausführungsschritte

1. Studiere das Empfänger-Profil: (a) letzter Post (Thema, Ton), (b) Bio (Tätigkeit, Ziel), (c) Übergreifendes Thema (wofür steht diese Person?). Dokumentiere 3 spezifische Beobachtungen als "Empfänger-Profil" vor den Nachrichten. Mindestens 1 Beobachtung muss aus dem letzten Post stammen.
2. Schreibe Nachricht 1 — Opener (max. 150 Zeichen): Beziehe dich auf 1 spezifische Beobachtung aus dem Empfänger-Profil + nenne 1 konkrete Gemeinsamkeit (gleiche Nische, gleiches Problem, gleiches Ziel). Kein "Ich habe Ihre Arbeit verfolgt". Kein Angebot. Zeichenzahl dokumentieren.
3. Schreibe Nachricht 2 — Mehrwert (max. 200 Zeichen): Biete konkrete Ressource, Insight oder Idee die der Empfänger sofort nutzen kann — ohne Gegenleistung zu nennen oder zu implizieren. Format: "[Ressource/Insight] könnte für [spezifisches Ziel des Empfängers] nützlich sein." Zeichenzahl dokumentieren.
4. Schreibe Nachricht 3 — Follow-Up (max. 100 Zeichen): Weiche CTA als Einladung nicht als Aufforderung. Format: "Falls relevant — [Angebot in max. 1 Satz]." Kein Druck, keine Dringlichkeit. Zeichenzahl dokumentieren.
5. Dokumentiere den Timing-Plan: Tag 0 = Nachricht 1 senden. Tag 1 (frühestens 24h später) = Nachricht 2 senden wenn keine Antwort. Tag 3 (frühestens 48h nach Tag 1) = Nachricht 3 senden wenn keine Antwort. Hinweis: Bei Antwort auf Nachricht 1 oder 2 → Sequenz verlassen und organisch fortführen.

## Verifikation

- Empfänger-Profil vorhanden: 3 spezifische Beobachtungen, mindestens 1 aus letztem Post
- Nachricht 1 Opener: ≤ 150 Zeichen, keine Floskel "Ich habe Ihre Arbeit verfolgt", kein Angebot
- Nachricht 2 Mehrwert: ≤ 200 Zeichen, konkreter Mehrwert ohne Gegenleistungs-Nennung
- Nachricht 3 Follow-Up: ≤ 100 Zeichen, weiche CTA
- Timing-Plan vorhanden: Tag 0, Tag 1+ (≥24h), Tag 3+ (≥48h nach Tag 1)
- Failure-Indikator: Nachricht enthält Preis oder Verkaufsangebot in Opener → Meldung "Verkaufsangebot in Opener gefunden — in Nachricht 3 verschieben: [Zitat des problematischen Satzes]"
- Akzeptanzkriterium: 3 Nachrichten in Zeichenlimits, kein Angebot in Nachrichten 1–2, Timing-Plan dokumentiert

## Abhängigkeiten

- Input: Empfänger-Profil (Name/Handle, letzter Post, Bio) + eigenes Angebot (1 Satz)
- Empfohlene Vorgänger-Skills: keine (Einstiegs-Skill)

## Output

Empfänger-Profil (3 Beobachtungen) + 3 Nachrichten (je mit Label, Text, Zeichenzahl) + Timing-Plan (Tag 0 / Tag 1+ / Tag 3+). Gesamtlänge: max. 300 Wörter, Markdown-Format.
