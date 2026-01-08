# Run all Session 5 DeepEval framework sample tests

echo "All Session 5 tests complete."
#!/bin/bash
# Run all Deepeval tests in Session 5


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

SESSION_DIR="$(dirname "$0")/Session 5/deepeval-assertions-and-metrics"
RESULTS_DIR="$(dirname "$0")/session5_deepeval_testresults"
mkdir -p "$RESULTS_DIR"

if [ -z "$OPENAI_API_KEY" ]; then
  echo "Please set your OPENAI_API_KEY before running this script."
  echo "Example: export OPENAI_API_KEY=sk-..."
  exit 1
fi

find "$SESSION_DIR" -type f -name 'test_*.py' | while read -r testfile; do
  echo "Running Deepeval test: $testfile"
  BASENAME="$(basename "$(dirname "$testfile")")"
  python "$testfile" > "$RESULTS_DIR/${BASENAME}_results.txt" 2>&1
  echo "Result saved to $RESULTS_DIR/${BASENAME}_results.txt"
done

python "$(dirname "$0")/Session 5/deepeval-framework-sample/tests/test_framework_sample.py" > "$RESULTS_DIR/test_framework_sample_results.txt" 2>&1
echo "Result saved to $RESULTS_DIR/test_framework_sample_results.txt"

echo "Done. Results saved in: $RESULTS_DIR"
read -p "Press enter to exit..."
