# Promptfoo Harness

Promptfoo is a framework for regression testing and prompt evaluation for LLMs, supporting multiple providers and custom assertions.

---

## Installation
1. Install Node.js (if not already installed):
   https://nodejs.org/
2. Install promptfoo globally:
   ```sh
   npm install -g promptfoo
   ```

---

## Demo: Run Promptfoo
1. Ensure you have a promptfoo.yaml config file (see the workspace root for an example).
2. Set your OpenAI API key (if using OpenAI):
   ```sh
   set OPENAI_API_KEY=sk-...   # Windows
   export OPENAI_API_KEY=sk-... # Linux/Mac
   ```
3. Run promptfoo evaluation:
   ```sh
   promptfoo eval -c promptfoo.yaml
   ```
   Or, for a specific config:
   ```sh
   promptfoo eval --config llm-testing-tools-eval/promptfoo.yaml --output llm-testing-tools-eval/promptfoo_results.html
   ```

---

## Guide
- Edit promptfoo.yaml to define your prompts, providers, and assertions.
- Supports multiple LLM providers and custom metrics.
- For more, see: https://github.com/promptfoo/promptfoo

---

## Troubleshooting
- Ensure Node.js and promptfoo are installed and in your PATH.
- API keys must be set for cloud LLM providers.
- Review promptfoo.yaml for correct syntax and provider IDs.
