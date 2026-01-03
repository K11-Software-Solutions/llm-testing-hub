#!/usr/bin/env bash
set -euo pipefail

YAML="promptfooconfig.yaml"
BACKUP="promptfooconfig.yaml.bak"

# === Revert mode ===
if [[ "${1:-}" == "revert" ]]; then
  if [[ -f "$BACKUP" ]]; then
    echo "[INFO] Restoring $YAML from $BACKUP..."
    mv -f "$BACKUP" "$YAML"
    echo "[OK] Reverted $YAML to placeholder (\${WEOPTIMIZE_API_KEY})"
  else
    echo "[WARN] No backup file found. Replacing any hardcoded key with placeholder..."
    if [[ -z "${WEOPTIMIZE_API_KEY:-}" ]]; then
      echo "[ERROR] WEOPTIMIZE_API_KEY not set. Cannot know what to revert."
      exit 1
    fi
    # Replace the actual key string with placeholder
    sed -i.bak "s|$WEOPTIMIZE_API_KEY|\${WEOPTIMIZE_API_KEY}|g" "$YAML"
    echo "[OK] Reverted by replacing key with placeholder."
  fi
  exit 0
fi

# === Inject mode ===
if [[ -z "${WEOPTIMIZE_API_KEY:-}" ]]; then
  echo "[ERROR] WEOPTIMIZE_API_KEY is not set in environment."
  echo "Use: export WEOPTIMIZE_API_KEY=your_key_here"
  exit 1
fi

if [[ ! -f "$YAML" ]]; then
  echo "[ERROR] $YAML not found."
  exit 1
fi

# Make a backup only if it doesn't exist yet
if [[ ! -f "$BACKUP" ]]; then
  echo "[INFO] Backing up $YAML to $BACKUP..."
  cp "$YAML" "$BACKUP"
fi

echo "[INFO] Injecting API key into $YAML..."
sed "s|\${WEOPTIMIZE_API_KEY}|$WEOPTIMIZE_API_KEY|g" "$BACKUP" > "$YAML"

echo "[OK] Key injected. Use './toggle-key.sh revert' to undo."
