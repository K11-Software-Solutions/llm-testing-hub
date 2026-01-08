# Session 6: LangTest for LLM Robustness

This session covers LangTest, a framework for evaluating LLM robustness, bias, and fairness. You will:

- Use LangTest to run robustness, bias, and fairness tests
- Analyze results in HTML and JSON reports
- Compare LangTest with Promptfoo and DeepEval

## Structure
- `langtest/` — LangTest configs and test cases
- `session6_langtest_testresults/` — Output folder for LangTest results

## Getting Started
1. Review the LangTest configs and test folders.
2. Install dependencies:
   ```sh
   pip install langtest openai
   ```
3. Set your API key as an environment variable:
   ```sh
   export OPENAI_API_KEY=your-key-here
   ```
4. Run LangTest tests or use provided scripts for batch evaluation.

---
This session builds skills in LLM robustness and fairness evaluation using LangTest.
