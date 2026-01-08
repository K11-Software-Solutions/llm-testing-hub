#!/bin/bash
# Run all Session 6 LangTest scripts and store results in session6_langtest_testresults

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

LANGTEST_DIR="Session 6/langtest"
RESULTS_DIR="session6_langtest_testresults"

mkdir -p "$RESULTS_DIR"

python "$LANGTEST_DIR/langtest_bias_test.py"
python "$LANGTEST_DIR/langtest_fairness_test.py"
python "$LANGTEST_DIR/langtest_robustness_test.py"

echo "All Session 6 LangTest tests complete. Results are in $RESULTS_DIR."
read -p "Press enter to exit..."
