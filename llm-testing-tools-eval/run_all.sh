#!/usr/bin/env bash
set -euo pipefail
python harness/deepeval_harness.py
python harness/langtest_harness.py
