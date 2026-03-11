#!/usr/bin/env bash
# scripts/verify-s04.sh
# Objektive Stopping-Condition für Slice S04 — Growth + Content Skills (~30 Skills)
# Ausführen aus dem Projekt-Root: bash scripts/verify-s04.sh

set -euo pipefail

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " S04 Verifikation — Growth + Content Skills"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [1/4] — Datei-Existenz (28 neue Skills)
# ─────────────────────────────────────────────────────────
echo ""
echo "[1/4] Datei-Existenz — 28 neue Skill-Dateien (14 Growth + 14 Content)"

GROWTH_SKILLS=(
  "skills/growth/elvis-x-trend-scanner.md"
  "skills/growth/elvis-audience-builder.md"
  "skills/growth/elvis-competitor-analysis.md"
  "skills/growth/elvis-posting-schedule.md"
  "skills/growth/elvis-profile-optimizer.md"
  "skills/growth/elvis-viral-formula.md"
  "skills/growth/elvis-engagement-booster.md"
  "skills/growth/elvis-follower-analysis.md"
  "skills/growth/elvis-niche-finder.md"
  "skills/growth/elvis-collab-strategy.md"
  "skills/growth/elvis-monetization-planner.md"
  "skills/growth/elvis-growth-sprint.md"
  "skills/growth/elvis-growth-loop.md"
  "skills/growth/elvis-x-analytics.md"
)

CONTENT_SKILLS=(
  "skills/content/elvis-x-thread-writer.md"
  "skills/content/elvis-content-calendar.md"
  "skills/content/elvis-copywriting.md"
  "skills/content/elvis-content-repurpose.md"
  "skills/content/elvis-story-writer.md"
  "skills/content/elvis-bio-writer.md"
  "skills/content/elvis-cta-writer.md"
  "skills/content/elvis-opinion-post.md"
  "skills/content/elvis-how-to-writer.md"
  "skills/content/elvis-content-ideas.md"
  "skills/content/elvis-headline-writer.md"
  "skills/content/elvis-reply-writer.md"
  "skills/content/elvis-dm-writer.md"
  "skills/content/elvis-content-brief.md"
)

ALL_S04_SKILLS=("${GROWTH_SKILLS[@]}" "${CONTENT_SKILLS[@]}")

for skill in "${ALL_S04_SKILLS[@]}"; do
  if [ -f "$ROOT/$skill" ]; then
    pass "$skill"
  else
    fail "$skill — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [2/4] — Sektions-Vollständigkeit (28 × 9 = 252 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[2/4] Sektions-Vollständigkeit — 252 Checks (28 Dateien × 9 Pflichtfelder)"

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

for skill in "${ALL_S04_SKILLS[@]}"; do
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
# CHECK-GRUPPE [3/4] — /elvis-Prefix im ## Name Block (28 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[3/4] /elvis-* Prefix — 28 Checks (je 1 pro Datei)"

for skill in "${ALL_S04_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    if grep -A5 "^## Name" "$skill_path" | grep -q "/elvis-"; then
      pass "$skill_name: enthält /elvis-* im ## Name Block"
    else
      fail "$skill_name: kein /elvis-* Prefix im ## Name Block gefunden"
    fi
  else
    fail "$skill_name: Datei fehlt — /elvis-* Prüfung übersprungen"
  fi
done

# ─────────────────────────────────────────────────────────
# CHECK-GRUPPE [4/4] — Phantomreferenz-Check
# Alle in ## Abhängigkeiten genannten elvis-[a-z-]+ müssen als .md existieren
# ─────────────────────────────────────────────────────────
echo ""
echo "[4/4] Phantomreferenz-Check — alle referenzierten Skills müssen existieren"

for skill in "${ALL_S04_SKILLS[@]}"; do
  skill_path="$ROOT/$skill"
  skill_name=$(basename "$skill")
  if [ -f "$skill_path" ]; then
    # Abhängigkeiten-Block extrahieren und elvis-[a-z-]+ Referenzen herausfiltern
    deps_block=$(awk '/^## Abhängigkeiten/,/^## /' "$skill_path" | grep -oE 'elvis-[a-z-]+' || true)
    if [ -z "$deps_block" ]; then
      pass "$skill_name: Abhängigkeiten-Block — keine Referenzen (ok)"
    else
      while IFS= read -r dep; do
        # Suche die referenzierte Datei in allen skills/-Unterordnern
        found=0
        for subdir in growth content research strategy automation meta; do
          if [ -f "$ROOT/skills/$subdir/$dep.md" ]; then
            found=1
            break
          fi
        done
        if [ "$found" -eq 1 ]; then
          pass "$skill_name: Abhängigkeit '$dep' existiert als Datei"
        else
          fail "$skill_name: Abhängigkeit '$dep' — Phantomreferenz! Datei nicht gefunden"
        fi
      done <<< "$deps_block"
    fi
  fi
done

# ─────────────────────────────────────────────────────────
# ZUSAMMENFASSUNG
# ─────────────────────────────────────────────────────────
echo ""
echo "══════════════════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ]; then
  echo " ✅ S04 Verifikation bestanden — alle Checks grün"
  echo "    28 Skills × 9 Sektionen × Prefix + Phantom = vollständig"
else
  echo " ❌ S04 Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
  echo "    Erstelle fehlende Skill-Dateien und starte das Skript erneut."
fi
echo "══════════════════════════════════════════════════════"
echo ""

# D014: Fehlerzähler als Exit-Code
exit $ERRORS
