#!/usr/bin/env bash
# scripts/verify-s01.sh
# Objektive Stopping-Condition für Slice S01 — Foundation
# Ausführen aus dem Projekt-Root: bash scripts/verify-s01.sh

set -euo pipefail

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " S01 Verifikation — OpenClaw Meta Maker"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# CHECK 1: Alle 11 Verzeichnisse existieren
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 1/7 ] Verzeichnisse (11 erwartet)"

DIRS=(
  "soul"
  "identity"
  "agent"
  "skills/growth"
  "skills/content"
  "skills/research"
  "skills/strategy"
  "skills/automation"
  "skills/meta"
  "commands"
  "templates"
)

for dir in "${DIRS[@]}"; do
  if [ -d "$ROOT/$dir" ]; then
    pass "$dir/"
  else
    fail "$dir/ — Verzeichnis fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK 2: 4 Template-Dateien existieren
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 2/7 ] Template-Dateien (4 erwartet)"

TEMPLATES=(
  "templates/skill-template.md"
  "templates/soul-template.md"
  "templates/identity-template.md"
  "templates/agent-template.md"
)

for tmpl in "${TEMPLATES[@]}"; do
  if [ -f "$ROOT/$tmpl" ]; then
    pass "$tmpl"
  else
    fail "$tmpl — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK 3: skill-template.md hat alle 9 Sektions-Header
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 3/7 ] skill-template.md — 9 Sektions-Header"

SKILL_TMPL="$ROOT/templates/skill-template.md"
REQUIRED_SECTIONS=(
  "## Name"
  "## Beschreibung"
  "## Ziele"
  "## Strategie"
  "## Einschränkungen"
  "## Ausführungsschritte"
  "## Verifikation"
  "## Abhängigkeiten"
  "## Output"
)

if [ -f "$SKILL_TMPL" ]; then
  for section in "${REQUIRED_SECTIONS[@]}"; do
    if grep -qF "$section" "$SKILL_TMPL"; then
      pass "skill-template.md: $section"
    else
      fail "skill-template.md: $section — Sektion fehlt"
    fi
  done
else
  for section in "${REQUIRED_SECTIONS[@]}"; do
    fail "skill-template.md: $section — Datei fehlt"
  done
fi

# ─────────────────────────────────────────────────────────
# CHECK 4: 6 Beispiel-Skill-Dateien existieren
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 4/7 ] Beispiel-Skills (6 erwartet, einer pro Kategorie)"

EXAMPLE_SKILLS=(
  "skills/growth/elvis-growth-audit.md"
  "skills/content/elvis-x-hook-writer.md"
  "skills/research/elvis-market-scan.md"
  "skills/strategy/elvis-execution-plan.md"
  "skills/automation/elvis-workflow-builder.md"
  "skills/meta/elvis-skill-generator.md"
)

for skill in "${EXAMPLE_SKILLS[@]}"; do
  if [ -f "$ROOT/$skill" ]; then
    pass "$skill"
  else
    fail "$skill — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK 5: Jeder Beispiel-Skill hat alle 9 Sektions-Header
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 5/7 ] Beispiel-Skills — 9 Sektionen pro Skill"

for skill in "${EXAMPLE_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    for section in "${REQUIRED_SECTIONS[@]}"; do
      if grep -qF "$section" "$skill_path"; then
        pass "$skill_name: $section"
      else
        fail "$skill_name: $section — Sektion fehlt"
      fi
    done
  else
    for section in "${REQUIRED_SECTIONS[@]}"; do
      fail "$skill_name: $section — Datei fehlt"
    done
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK 6: Jeder Skill enthält /elvis-* in ## Name
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 6/7 ] Beispiel-Skills — /elvis-* Prefix im ## Name Block"

for skill in "${EXAMPLE_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    # Prüft ob nach "## Name" eine Zeile mit /elvis- kommt (innerhalb der nächsten 5 Zeilen)
    if grep -A5 "^## Name" "$skill_path" | grep -q "/elvis-"; then
      pass "$skill_name: enthält /elvis-* im Name-Block"
    else
      fail "$skill_name: kein /elvis-* Prefix im ## Name Block gefunden"
    fi
  else
    fail "$skill_name: Datei fehlt — /elvis-* Prüfung übersprungen"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK 7: skills/meta/elvis-skill-generator.md enthält Safeguard-Keywords
# ─────────────────────────────────────────────────────────
echo ""
echo "[ 7/7 ] elvis-skill-generator.md — Safeguard-Keywords"

GENERATOR="$ROOT/skills/meta/elvis-skill-generator.md"
SAFEGUARDS=(
  "Max-Limit"
  "Approval-Gate"
  "Stop-Bedingung"
  "Rollback"
)

if [ -f "$GENERATOR" ]; then
  for keyword in "${SAFEGUARDS[@]}"; do
    if grep -qF "$keyword" "$GENERATOR"; then
      pass "elvis-skill-generator.md: enthält '$keyword'"
    else
      fail "elvis-skill-generator.md: '$keyword' — Safeguard-Keyword fehlt"
    fi
  done
else
  for keyword in "${SAFEGUARDS[@]}"; do
    fail "elvis-skill-generator.md: '$keyword' — Datei fehlt"
  done
fi

# ─────────────────────────────────────────────────────────
# ZUSAMMENFASSUNG
# ─────────────────────────────────────────────────────────
echo ""
echo "══════════════════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ]; then
  echo " ✅ S01 Verifikation bestanden — alle Checks grün"
else
  echo " ❌ S01 Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
  echo "    Führe die fehlenden Tasks aus und starte das Skript erneut."
fi
echo "══════════════════════════════════════════════════════"
echo ""

exit $ERRORS
