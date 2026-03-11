#!/usr/bin/env bash
# scripts/verify-s03.sh
# Objektive Stopping-Condition für Slice S03 — Agent Layer — 16 Star Trek Agenten
# Ausführen aus dem Projekt-Root: bash scripts/verify-s03.sh

ERRORS=0
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pass() { echo "  ✓ $1"; }
fail() { echo "  ✗ $1"; ERRORS=$((ERRORS + 1)); }

echo ""
echo "══════════════════════════════════════════════════════"
echo " S03 Verifikation — OpenClaw Meta Maker"
echo "══════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────────
# [1/3] Datei-Existenz (16 Dateien)
# ─────────────────────────────────────────────────────────
echo ""
echo "[1/3] Datei-Existenz (16 Dateien)"

AGENT_FILES=(
  "agent/kirk.md"
  "agent/spock.md"
  "agent/picard.md"
  "agent/data.md"
  "agent/worf.md"
  "agent/scotty.md"
  "agent/laforge.md"
  "agent/seven.md"
  "agent/sulu.md"
  "agent/tuvok.md"
  "agent/mccoy.md"
  "agent/riker.md"
  "agent/q.md"
  "agent/borg.md"
  "agent/troi.md"
  "agent/uhura.md"
)

for f in "${AGENT_FILES[@]}"; do
  if [ -f "$ROOT/$f" ]; then
    pass "$f"
  else
    fail "$f — Datei fehlt"
  fi
done

# ─────────────────────────────────────────────────────────
# [2/3] Agent-Sektionen (16 × 7 = 112 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[2/3] Agent-Sektionen (16 × 7 = 112 Checks)"

AGENT_SECTIONS=(
  "## Name"
  "## Mission"
  "## Capabilities"
  "## Operating Loop"
  "## Constraints"
  "## Primärer Soul"
  "## Primäre Skills"
)

for f in "${AGENT_FILES[@]}"; do
  agent_path="$ROOT/$f"
  agent_name=$(basename "$f")
  if [ -f "$agent_path" ]; then
    for section in "${AGENT_SECTIONS[@]}"; do
      if grep -qF "$section" "$agent_path"; then
        pass "$agent_name: $section"
      else
        fail "$agent_name: $section — Sektion fehlt"
      fi
    done
  else
    for section in "${AGENT_SECTIONS[@]}"; do
      fail "$agent_name: $section — Datei fehlt"
    done
  fi
done

# ─────────────────────────────────────────────────────────
# [3/3] Safeguard-Marker für autonome Agenten (5 × 4 = 20 Checks)
# ─────────────────────────────────────────────────────────
echo ""
echo "[3/3] Safeguard-Marker (5 autonome Agenten × 4 Marker = 20 Checks)"

AUTONOMOUS_AGENTS=(
  "agent/picard.md"
  "agent/q.md"
  "agent/borg.md"
  "agent/troi.md"
  "agent/uhura.md"
)

SAFEGUARD_MARKERS=(
  "**Max-Limit:**"
  "**Approval-Gate:**"
  "**Stop-Bedingung:**"
  "**Rollback-Hinweis:**"
)

for f in "${AUTONOMOUS_AGENTS[@]}"; do
  agent_path="$ROOT/$f"
  agent_name=$(basename "$f")
  if [ -f "$agent_path" ]; then
    for marker in "${SAFEGUARD_MARKERS[@]}"; do
      if grep -qF "$marker" "$agent_path"; then
        pass "$agent_name: $marker"
      else
        fail "$agent_name: $marker — Safeguard fehlt"
      fi
    done
  else
    for marker in "${SAFEGUARD_MARKERS[@]}"; do
      fail "$agent_name: $marker — Datei fehlt"
    done
  fi
done

# ─────────────────────────────────────────────────────────
# ZUSAMMENFASSUNG
# ─────────────────────────────────────────────────────────
echo ""
echo "══════════════════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ]; then
  echo " ✅ S03 Verifikation bestanden — alle 148 Checks grün"
else
  echo " ❌ S03 Verifikation fehlgeschlagen — $ERRORS Fehler gefunden"
  echo "    Führe die fehlenden Tasks aus und starte das Skript erneut."
fi
echo "══════════════════════════════════════════════════════"
echo ""

exit $ERRORS
