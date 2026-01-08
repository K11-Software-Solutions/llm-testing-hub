#!/bin/bash
# Run all DeepEval feature test scripts in Session 5
dir="$(dirname "$0")/Session 5/deepeval-framework-sample/deepeval_feature_tests"

for script in faithfulness_test.py relevance_test.py toxicity_test.py bias_test.py custom_metric_test.py regression_test.py llm_as_judge_test.py batch_test.py reporting_test.py; do
  echo "Running $script..."
  python "$dir/$script"
done

echo "All DeepEval feature tests completed."
