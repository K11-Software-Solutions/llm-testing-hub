
# Session 2: Promptfoo Evaluation and Assertions

Welcome to Session 2! In this session, you’ll learn how to use Promptfoo to evaluate LLM prompts with automated assertions and metrics.

## What You’ll Learn

- How to configure Promptfoo for different prompt evaluation scenarios
- How to write and organize Promptfoo config files
- How to use assertions and metrics to validate LLM outputs
- How to run batch tests and review results in HTML format

## Folder Structure

- `prompts-and-asserts-testing-challanges/` — Example prompts and config files
- `promptfoo-framework-sample/` — Sample Promptfoo framework usage
- `promptfoo-assertions-and-metrics/` — Assertion and metric examples
- `session2_promptfoo_testresults/` — Output folder for HTML results

## Quick Start

1. **Review Examples:** Explore the folders above for ready-to-use Promptfoo configs and prompts.
2. **Install Dependencies:**
   ```sh
   pip install promptfoo openai
   ```
3. **Set Your API Key:**
   ```sh
   export OPENAI_API_KEY=your-key-here
   ```
4. **Run Tests:** Use the provided script or run Promptfoo directly:
   ```sh
   ./session2.sh
   # or manually:
   promptfoo eval --config path/to/promptfooconfig.yaml --output session2_promptfoo_testresults/results.html
   ```

## Example Command

```sh
promptfoo eval --config prompts-and-asserts-testing-challanges/promptfooconfig.yaml --output session2_promptfoo_testresults/example_results.html
```

## Tips

- Use assertions like `contains` and `llm-rubric` to check LLM outputs.
- Organize your prompts, providers, and tests in separate files for clarity.
- Review the generated HTML reports for detailed results.

---

This session will help you build practical skills for automated, assertion-based LLM prompt evaluation using Promptfoo.

---
