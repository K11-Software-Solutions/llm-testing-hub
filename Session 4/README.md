# Session 4: AI Conversation Prompt Evaluation

This session focuses on evaluating multi-turn and single-turn AI conversation prompts for robustness, safety, and context retention. You will:

- Test multi-turn conversation flows
- Use Promptfoo to automate evaluation and assertions
- Analyze results in HTML reports

## Structure
- `ai-conversation-prompts/` — Prompt files, configs, and tests
- `session4_promptfoo_testresults/` — Output folder for HTML results

## Getting Started
1. Review the prompt and config files in `ai-conversation-prompts/`.
2. Install dependencies:
   ```sh
   pip install promptfoo openai
   ```
3. Set your API key as an environment variable:
   ```sh
   export OPENAI_API_KEY=your-key-here
   ```
4. Run Promptfoo tests or use provided scripts for batch evaluation.

---
This session builds skills in conversational LLM evaluation and prompt design.
