#!/bin/bash
# Run all promptfoo tests in Session 2

SESSION_DIR="$(dirname "$0")/Session 2/prompts-and-asserts-testing-challanges"
RESULTS_DIR="$(dirname "$0")/session2_promptfoo_testresults"
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