#!/usr/bin/env bash
set -euo pipefail

# ==== Search for .env.weoptimize.ai in ., .., ../.., ../../.., ../../../.. (up to 4 parents) ====
ENVFILE=""
for D in . .. ../.. ../../.. ../../../..; do
  if [[ -f "$D/.env.weoptimize.ai" ]]; then
    ENVFILE="$D/.env.weoptimize.ai"
    break
  fi
done

if [[ -z "$ENVFILE" ]]; then
  echo "[WARN] No .env.weoptimize.ai file found in current or up to 4 parent directories."
  exit 0
fi

echo "[INFO] Found .env.weoptimize.ai at: $ENVFILE"

# ==== Load environment variables from .env.weoptimize.ai ====
while IFS='=' read -r key value; do
  # Skip empty lines or comments
  [[ -z "$key" || "$key" =~ ^# ]] && continue

  export "$key=$value"
  echo "[OK] Set $key=$value"

  # ==== Sync with .env (update if exists, else append) ====
  TARGET_ENV=".env"
  if [[ -f "$TARGET_ENV" ]]; then
    # Remove any existing line for key=
    grep -v "^$key=" "$TARGET_ENV" > "$TARGET_ENV.tmp" || true
    mv "$TARGET_ENV.tmp" "$TARGET_ENV"
  fi
  echo "$key=$value" >> "$TARGET_ENV"
  echo "[SYNC] $key set in $TARGET_ENV as $value"
done < "$ENVFILE"

# ==== Confirm ====
echo "Inside shell: WEOPTIMIZE_API_KEY=${WEOPTIMIZE_API_KEY:-<not set>}"

# ==== Curl test ====
curl -X POST "https://api.weoptimize.ai/chats/promptfoo/session" \
  -H "Content-Type: application/json" \
  -H "x-api-key: ${WEOPTIMIZE_API_KEY:-}" \
  -d "{\"email\":\"kavita.jadhav1109@gmail.com\",\"messages\":[{\"role\":\"user\",\"content\":\"Test message\"}]}"

echo
echo "Finished. In a NEW shell, you can run:"
echo "   echo \$WEOPTIMIZE_API_KEY"
