#!/usr/bin/env bash
set -euo pipefail

# Move to repo/workspace root relative to this script
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

# Load environment variables from .env at workspace root if present
if [ -f "$ROOT_DIR/.env" ]; then
  set -a
  . "$ROOT_DIR/.env"
  set +a
fi

# Create results directory if it doesn't exist
RESULTS_DIR="$ROOT_DIR/session3_promptfoo_testresults"
mkdir -p "$RESULTS_DIR"

# Go to the config directory
cd "$ROOT_DIR/Session 3/LLM-red-teaming" || { echo "Directory not found: Session 3/LLM-red-teaming"; exit 1; }

echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -l

if [ ! -f redteam-translation.yaml ]; then
  echo "redteam-translation.yaml not found!"
  exit 1
fi


# Run eval and write output
npx --yes promptfoo@latest eval --config redteam-translation.yaml \
  --output "$RESULTS_DIR/redteam-translation_results.json"

echo "Session 3 red teaming promptfoo test complete."
echo "Results: $RESULTS_DIR/redteam-translation_results.json"
read -p "Press enter to exit..."
