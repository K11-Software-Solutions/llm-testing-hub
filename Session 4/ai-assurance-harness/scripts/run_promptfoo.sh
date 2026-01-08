#!/usr/bin/env bash
set -euo pipefail
CFG=${1:-configs/baseline/promptfooconfig.BaseLine.yaml}
echo "[*] Running Promptfoo suite: $CFG"
promptfoo eval -c "$CFG" --max-concurrency 4 --output ./reports/html --json ./reports/json/results.json || true
echo "[*] View with: promptfoo view"
