#!/usr/bin/env bash
set -uo pipefail   # strict, but no -e to avoid early exits

# ==== Search for .env in ., .., ../.., ../../.., ../../../.. ====
ENVFILE=""
for D in . .. ../.. ../../.. ../../../..; do
  if [ -f "$D/.env" ]; then
    ENVFILE="$D/.env"
    break
  fi
done

if [ -z "$ENVFILE" ]; then
  echo "[WARN] No .env file found in current or up to 4 parent directories."
  echo "[INFO] Environment load complete (0 variables)."
  read -rp "Press Enter to continue . . ."
  exit 0
fi

echo "[INFO] Found .env at: $ENVFILE"

# ==== Copy .env to current folder ====
cp "$ENVFILE" .env
echo "[INFO] Copied .env to current folder: $(pwd)/.env"

# ==== Load environment variables from copied .env ====
count=0
while IFS= read -r line || [ -n "$line" ]; do
  # Trim whitespace
  line="${line#"${line%%[![:space:]]*}"}"
  line="${line%"${line##*[![:space:]]}"}"

  # Skip comments and empty lines
  if [ -z "$line" ] || [ "${line:0:1}" = "#" ]; then
    continue
  fi

  # Split into name=value
  name="${line%%=*}"
  value="${line#*=}"

  # Strip quotes if present
  value="${value%\"}"
  value="${value#\"}"

  export "$name=$value"
  echo "[OK] Set $name=$value"
  count=$((count+1))
done < <(tr -d '\r' < .env)   # handle CRLF endings

echo
echo "[INFO] Environment load complete. Loaded $count variables."

# ==== Pause (like Windows "pause") ====
read -rp "Press Enter to continue . . ."
