#!/bin/bash
# session4.sh - Run all promptfoo tests in Session 4


# Load environment variables from .env at workspace root if present
if [ -f "$(dirname "$0")/.env" ]; then
  set -a
  . "$(dirname "$0")/.env"
  set +a
fi

# Ensure OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
  echo "Warning: OPENAI_API_KEY is not set. Please set it in your .env file at the workspace root."
else
  export OPENAI_API_KEY
  echo "OPENAI_API_KEY is set."
fi



echo "All Session 4 promptfoo tests complete."
SESSION_DIR="$(dirname "$0")/Session 4/ai-conversation-prompts/config/multi_turn_conversation"
# Create results directory if it doesn't exist
RESULTS_DIR="$(dirname "$0")/session4_promptfoo_testresults"
mkdir -p "$RESULTS_DIR"

find "$SESSION_DIR" -type f -name 'promptfooconfig.yaml' | while read -r config; do
  echo "Running promptfoo test: $config"
  BASENAME="$(basename "$(dirname "$config")")"

  npx promptfoo@latest validate -c "$config"
  promptfoo eval \
    --config "$config" \
    --output "$RESULTS_DIR/${BASENAME}_results.html"
done

echo "Done. Results saved in: $RESULTS_DIR"
read -p "Press enter to exit..."