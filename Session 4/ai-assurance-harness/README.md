# WeOptimize AI – Red Teaming Harness

Baseline **Promptfoo** evaluation for the **WeOptimize.ai B2B Multi-LLM Assistant**.
Covers **security**, **bias**, **privacy**, and **harmful content** with reproducible configs, runners, and reports.

## 📂 Repository Structure
```
weoptimize-redteam-harness/
├── configs/                   # Promptfoo suites + model profiles
│   ├── redteam-translation.yaml
│   └── model-profiles/
│       ├── openai.gpt-4o-mini.yml
│       ├── anthropic.claude-sonnet-4.yml
│       └── lmstudio.qwen3-1.7b.yml
├── prompts/                   # corpora for harmful, pii, bola, injection, templates
├── datasets/                  # synthetic datasets (no real PII)
├── scripts/                   # runners, redaction, summarizers
├── docs/                      # methodology, threat model, compliance mapping
├── reports/                   # generated artifacts (html/json/csv/png)
├── examples/                  # minimal working examples for quickstart
└── README.md
```

## 🚀 Quickstart
```bash
npm install -g promptfoo
./scripts/run_promptfoo.sh configs/redteam-translation.yaml
promptfoo view
```

## 🧪 What’s Included
- Red-team suites (PII, BOLA, harmful content, injection)
- Model-graded assertions (refusal clarity, empathy)
- Provider profiles (OpenAI, Anthropic, LM Studio)
- Evidence outputs: HTML, JSON, CSV, PNG scorecards

## 🛡️ Safety & Data Hygiene
- Use **synthetic** PII only
- Encode/store harmful prompts responsibly
- Never commit secrets; use `.env`/CI secrets
