# Decisions Register

<!-- Append-only. Never edit or remove existing rows.
     To reverse a decision, add a new row that supersedes it.
     Read this file at the start of any planning or research phase. -->

| # | When | Scope | Decision | Choice | Rationale | Revisable? |
|---|------|-------|----------|--------|-----------|------------|
| D001 | M001 | convention | Skill Naming Prefix | /elvis-* für alle Skills im gesamten Ökosystem | Konsistenz, direkte OpenClaw-Nutzbarkeit, einheitliche Wiedererkennbarkeit | Nein |
| D002 | M001 | convention | Inhaltssprache | Deutsch | Explizite Nutzeranforderung | Nein |
| D003 | M001 | arch | Ordnerstruktur | Eine integrierte Struktur (soul/, identity/, agent/, skills/, commands/, templates/) statt separate Pakete | Übersichtlich, direkt importierbar, kein Chaos durch mehrere Top-Level-Ordner | Ja — wenn separate Pakete für Verteilung benötigt |
| D004 | M001 | convention | Agenten-Namen | Ausschließlich Star Trek Charaktere: Kirk, Spock, Picard, Data, Worf, Scotty, LaForge, Seven, Sulu, Tuvok, McCoy, Riker, Q, Borg, Troi, Uhura | Identität, Erkennbarkeit, Charakter-Persönlichkeit reflektiert Agenten-Funktion | Nein |
| D005 | M001 | arch | Skill-Format | Erweitertes 9-Sektionen-Format: Name, Beschreibung, Ziele, Strategie, Einschränkungen, Ausführungsschritte, Verifikation, Abhängigkeiten, Output | Verhindert Endlosschleifen, Agent-Improvisation und unkontrollierte Ausführung | Ja — wenn weiterer Bedarf |
| D006 | M001 | arch | Execution Steps Granularität | Konkret und ausführbar: spezifische Mengen, Zeitangaben, Formate (z.B. "Top 20 Posts der letzten 7 Tage") statt abstrakter Anweisungen | Vage Steps führen zu unvorhersehbaren Ergebnissen | Nein |
| D007 | M001 | constraint | Autonomous System Safeguards | Alle autonomen Agenten (Borg, Q, Picard, Troi, Uhura) erhalten: Max-Limit pro Durchlauf, Operator-Approval-Gate, Stop-Bedingung, Rollback-Hinweis | Verhindert endlose Generierung und Systeminstabilität | Nein |
| D008 | M001 | scope | Skill-Deduplizierung | ~100 einzigartige deduplizierte Skills statt exakte Kopie der Spec-Listen | Spec enthält Duplikate (elvis-hook-writer / elvis-x-hook-writer etc.) — ein einziger vollständiger Skill ist besser als zwei halbfertige | Ja — wenn spezifische Varianten gewünscht |
| D009 | M001 | scope | Pixel Agents | Komplett weggelassen | Technisch inkompatibel mit OpenClaw Markdown-System; separates VS Code Extension-Projekt | Ja — separates zukünftiges Projekt |
| D010 | M001 | scope | Gesamtscope | Alle 6 Layer in einem Milestone (Starter Kit, 50-Skill Library, Operator Pack, Meta-Agent System, Autonomous System, Command System) | Reine Datei-Generierung — kein Code, kein Runtime. Alles in einem Durchgang umsetzbar. | Nein |
