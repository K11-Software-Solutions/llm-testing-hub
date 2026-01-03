#!/bin/bash
# Run all promptfoo tests in Session 1

SESSION_DIR="$(dirname "$0")/Session 1/prompt-testing-challanges"
RESULTS_DIR="$(dirname "$0")/session1_promptfoo_testresults"
mkdir -p "$RESULTS_DIR"

find "$SESSION_DIR" -type f -name 'promptfoo.yaml' | while read -r config; do
  echo "Running promptfoo test: $config"
  BASENAME="$(basename "$(dirname "$config")")"

  promptfoo eval \
    --config "$config" \
    --output "$RESULTS_DIR/${BASENAME}_results.json" \
            "$RESULTS_DIR/${BASENAME}_results.html"
done

echo "Done. Results saved in: $RESULTS_DIR"
read -p "Press enter to exit..."
