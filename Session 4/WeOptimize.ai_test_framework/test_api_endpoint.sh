#!/usr/bin/env bash
# ping_weoptimize_session.sh
# Usage:
#   ./ping_weoptimize_session.sh <API_KEY> <EMAIL> [MESSAGE] [ENDPOINT]
# Example:
#   ./ping_weoptimize_session.sh sk-xxx you@example.com 'Return {"assignee":"Unassigned"} only.'
#   ./ping_weoptimize_session.sh sk-xxx you@example.com 'Hello' https://api.weoptimize.ai/chats/promptfoo/session

set -euo pipefail

API_KEY="${1:-}"
EMAIL="${2:-}"
MESSAGE="${3:-Return {\"assignee\":\"Unassigned\"} only.}"
ENDPOINT="${4:-https://api.weoptimize.ai/chats/promptfoo/session}"

if [[ -z "$API_KEY" || -z "$EMAIL" ]]; then
  echo "Usage: $0 <API_KEY> <EMAIL> [MESSAGE] [ENDPOINT]"
  exit 1
fi

ts="$(date +%Y%m%d-%H%M%S)"
HDRS="headers-$ts.txt"
BODY="response-$ts.json"

echo "[INFO] POST $ENDPOINT"
echo "[INFO] Email: $EMAIL"
echo "[INFO] Saving headers -> $HDRS"
echo "[INFO] Saving body    -> $BODY"

# Build minimal messages array payload
payload=$(cat <<JSON
{
  "email": "$EMAIL",
  "messages": [
    { "role": "user", "content": "$MESSAGE" }
  ]
}
JSON
)

# Perform request
code=$(curl -sS -D "$HDRS" -o "$BODY" -w "%{http_code}" \
  -X POST "$ENDPOINT" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $API_KEY" \
  --data "$payload" || true)

echo "[HTTP] $code"
if command -v jq >/dev/null 2>&1; then
  echo "[BODY pretty]"
  jq . "$BODY" || cat "$BODY"
else
  echo "[BODY raw]"
  sed -e 's/^/  /' "$BODY"
fi

# Exit non-zero on non-2xx to make this CI-friendly
case "$code" in
  2*) exit 0 ;;
  *)  echo "[ERROR] Non-2xx response. See $HDRS and $BODY"; exit 2 ;;
esac

# ==== Pause (like Windows "pause") ====
read -rp "Press Enter to continue . . ."
