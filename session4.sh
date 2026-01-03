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

# Run multi_turn_conversation promptfoo test
cd "Session 4/ai-conversation-prompts/config/multi_turn_conversation"
promptfoo eval --config promptfooconfig.yaml
cd ../../../../..

echo "All Session 4 promptfoo tests complete."
# Create results directory if it doesn't exist
RESULTS_DIR="session4_promptfoo_testresults"
mkdir -p "$RESULTS_DIR"



# Run multi_turn_conversation promptfoo test and store results
cd "Session 4/ai-conversation-prompts/config/multi_turn_conversation" || { echo "Directory not found: Session 4/ai-conversation-prompts/config/multi_turn_conversation"; read -p "Press enter to exit..."; exit 1; }
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -l
if [ ! -f promptfooconfig.yaml ]; then
  echo "promptfooconfig.yaml not found!"
  read -p "Press enter to exit..."
  exit 1
fi
promptfoo eval --config "promptfooconfig.yaml" --output "../../../$RESULTS_DIR/multi_turn_conversation_results.json"
cd ../../../../..

echo "All Session 4 promptfoo tests complete. Results are in $RESULTS_DIR."
read -p "Press enter to exit..."
