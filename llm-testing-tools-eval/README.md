# My LLM Eval (DeepEval + LangTest)

A minimal, production-friendly template that combines **DeepEval** (metrics-rich LLM testing) and **LangTest** (bias/robustness/fairness audits) with optional CI.

## What’s inside
- `harness/deepeval_harness.py` — run faithfulness & relevance checks via DeepEval.
- `harness/langtest_harness.py` — run bias/robustness suites via LangTest.
- `data/ground_truth/faq_testset.jsonl` — tiny example dataset for Q&A tasks.
- `tests/test_deepeval/` and `tests/test_langtest/` — examples you can adapt.
- `.github/workflows/eval.yml` — CI that installs deps and runs both harnesses.
- `scripts/run_all.sh` — one-liner to execute both harnesses locally.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt

# Optional; only needed if you call OpenAI in your tests
export OPENAI_API_KEY=sk-...

# Run DeepEval harness (Q&A faithfulness/relevance)
python harness/deepeval_harness.py

# Run LangTest harness (example NER task; swap for your task/models)
python harness/langtest_harness.py

# Run both at once
bash scripts/run_all.sh
```

## CI (GitHub Actions)
On every pull request, CI will install dependencies and run both harnesses. Fail the build if assertions fail (DeepEval) or if LangTest exits non-zero.

## Customize
- Add your **domain-specific** test cases to `data/ground_truth/*.jsonl`.
- Write **LLM-as-judge** rubrics if you need subjective scoring.
- Extend `harness/deepeval_harness.py` with more metrics (toxicity, summarization, etc.).
- In `harness/langtest_harness.py`, change the task/model/dataset to match your use case.


## Running pytest
Both DeepEval and LangTest tests are **opt-in** (to avoid long/paid runs by default).

```bash
# DeepEval tests (require API access for judge metrics)
RUN_DEEPEVAL=1 pytest -q tests/test_deepeval

# LangTest tests (downloads models/datasets)
RUN_LANGTEST=1 pytest -q tests/test_langtest
```

## Promptfoo

We include `promptfoo.yaml` for quick regression tests.

```bash
npm install -g promptfoo
export OPENAI_API_KEY=sk-...
promptfoo eval -c promptfoo.yaml
```

## Agenta

Example scripts in `agenta_demo/` show prompt variant management and fetching deployed configs.

```bash
pip install agenta openai opentelemetry-instrumentation-openai
export AGENTA_API_KEY=...   # if using Agenta Cloud
export OPENAI_API_KEY=sk-...
python agenta_demo/manage_prompt.py
python agenta_demo/app_inference.py
```
