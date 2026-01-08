# Comparison of Promptfoo, DeepEval, and LangTest for LLM Evaluation

This document provides a practical comparison of three popular open-source LLM evaluation frameworks: **Promptfoo**, **DeepEval**, and **LangTest**. It covers their core features, strengths, and best-use scenarios for LLM testing and assurance.

---

## 1. Overview Table

| Feature                | Promptfoo                | DeepEval                | LangTest                |
|------------------------|--------------------------|-------------------------|-------------------------|
| **Focus**              | Prompt & output testing  | Assertion-based eval    | Robustness, bias, fairness |
| **Test Types**         | Prompt, assertion, metrics| Assertions, custom metrics | Bias, fairness, robustness |
| **Config Format**      | YAML/JSON                | Python                  | YAML/JSON               |
| **Extensibility**      | High (custom providers, metrics, assertions) | High (custom assertions, metrics) | Moderate (custom categories, test configs) |
| **UI/Visualization**   | HTML, CLI, VS Code ext   | CLI, HTML, Python plots | CLI, HTML, Python plots |
| **Multi-model**        | Yes                      | Yes                     | Yes                     |
| **API/SDK**            | Node.js, CLI, REST       | Python SDK              | Python SDK, CLI         |
| **Best for**           | Prompt engineering, regression, multi-provider eval | Assertion-driven eval, custom metrics | LLM robustness, bias/fairness, compliance |

---


## 2. Promptfoo
**Strengths:**
- Simple YAML/JSON config for prompts, models, and assertions
- Supports multiple providers (OpenAI, Azure, Cohere, local, etc.)
- Custom assertions and metrics (JS or Python)
- HTML/CLI/VS Code UI for results
- Great for prompt regression, A/B, and multi-model testing
**Limitations:**
- Not focused on bias/fairness/robustness
- Limited out-of-the-box LLM-specific metrics

**Example: Minimal promptfoo.yaml**
```yaml
prompts:
  - "Translate to French: {{input}}"
providers:
  - openai:gpt-3.5-turbo
  - openai:gpt-4o
tests:
  - vars: {input: "Hello world"}
    assert:
      - type: icontains
        value: "Bonjour"
```
**Run:**
```bash
promptfoo test promptfoo.yaml --output html
```
**Custom assertion (JS):**
```yaml
assert:
  - type: javascript
    value: |
      (output) => output.length < 100
```


## 3. DeepEval
**Strengths:**
- Python-native, assertion-based evaluation
- Custom assertions and metrics (Python)
- Integrates with test frameworks (pytest, unittest)
- Good for RAG, factuality, and custom eval pipelines
**Limitations:**
- Less focus on prompt engineering workflows
- No built-in bias/fairness/robustness tests

**Example: Minimal DeepEval test**
```python
from deepeval import assert_output, assert_score

def test_french_translation():
    output = my_llm("Translate to French: Hello world")
    assert_output(output, contains="Bonjour")
    assert_score(output, metric="length", max=100)

# Custom assertion
from deepeval.metrics import BaseMetric
class MyMetric(BaseMetric):
    def score(self, output, **kwargs):
        return 1.0 if "Bonjour" in output else 0.0

def test_custom():
    output = my_llm("Translate to French: Hello world")
    assert_score(output, metric=MyMetric())
```


## 4. LangTest
**Strengths:**
- Focused on LLM robustness, bias, and fairness
- YAML/JSON config for categories and thresholds
- Built-in tests for bias, fairness, robustness (e.g., gender, typo, context)
- CLI and Python SDK
**Limitations:**
- Less flexible for custom metrics/assertions
- Not designed for prompt regression or multi-provider prompt testing

**Example: Minimal LangTest config.yaml**
```yaml
models:
  - name: openai/gpt-3.5-turbo
    hub: openai
    type: text-classification
data:
  file: data/test_data.jsonl
categories:
  - bias
  - robustness
thresholds:
  bias: 0.8
  robustness: 0.8
report:
  format: [txt, json]
```
**Run:**
```bash
python agent.py
# or via API/CLI as described in this repo
```

---

## 5. When to Use Each
- **Promptfoo:**
  - When you want to test prompts across many models/providers
  - For prompt regression, A/B, and assertion-based output checks
  - When you want a simple config and UI for prompt testing
- **DeepEval:**
  - When you need custom assertions/metrics in Python
  - For RAG, factuality, and integration with Python test suites
  - When you want to extend with your own logic
- **LangTest:**
  - When you need to evaluate LLMs for bias, fairness, and robustness
  - For compliance, safety, and assurance scenarios
  - When you want out-of-the-box tests for LLM reliability

---

## 6. Example Use Cases
- **Promptfoo:**
  - "Does my prompt work the same on GPT-4, Claude, and Gemini?"
  - "Did my prompt change break any assertions?"
- **DeepEval:**
  - "Does my RAG pipeline return factual answers?"
  - "Can I write a custom assertion for my domain?"
- **LangTest:**
  - "Is my LLM output robust to typos and context changes?"
  - "Does my model show gender or cultural bias?"

---

## 7. References
- [Promptfoo Documentation](https://promptfoo.dev/)
- [DeepEval Documentation](https://github.com/confident-ai/deepeval)
- [LangTest Documentation](https://github.com/JohnSnowLabs/langtest)

---

---

## 8. Summary
For most LLM evaluation workflows, these tools can be combined:
- Use **Promptfoo** for prompt regression and multi-model prompt testing
- Use **DeepEval** for custom assertions and Python-based metrics
- Use **LangTest** for robustness, bias, and fairness evaluation
