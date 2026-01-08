# Session 1: Foundations of LLM Prompt Testing

Welcome to Session 1! This session is designed to help you understand and evaluate the behavior of Large Language Models (LLMs) through hands-on prompt testing. You’ll learn how to identify, measure, and improve key aspects of prompt design for real-world applications.

## What You'll Learn

- **Bias and Fairness:**
  - Discover how prompts can introduce or reduce bias in LLM outputs.
  - Learn to test and measure fairness in responses.

- **Context Window Limits:**
  - See how the length and complexity of prompts affect model performance.
  - Try prompts that push the boundaries of the model’s context window.

- **Hallucination & Factual Accuracy:**
  - Spot when the model generates incorrect or made-up information (hallucinations).
  - Apply techniques to encourage factual, reliable answers.

- **Human Values Alignment:**
  - Evaluate how well model outputs align with ethical and human values.

- **Performance Consistency:**
  - Check if the model gives consistent answers across repeated or varied prompts.

- **Regulatory & Policy Compliance:**
  - Test prompts for compliance with legal, regulatory, and policy standards.

- **Security & Prompt Injection:**
  - Explore how prompt injection attacks work and test the model’s resilience.

## How This Session is Organized
- Each topic above has its own folder in `prompt-testing-challanges/` with background, example prompts, and config files.
- The `prompts/` directory contains ready-to-use prompt examples.
- You’ll use Promptfoo to automate and evaluate your prompt experiments.

## Getting Started
1. Open each challenge folder to read the background and review the test cases.
2. Use the provided Promptfoo config and prompt files to run your tests.
3. Install dependencies:
   ```sh
   pip install promptfoo openai
   ```
4. Set your API key as an environment variable (e.g., `OPENAI_API_KEY`).

## Example: Running a Promptfoo Test
- Find a `promptfooconfig.yaml` in a challenge folder and run:
   ```sh
   promptfoo eval --config path/to/promptfooconfig.yaml
   ```

---
By completing this session, you’ll gain essential skills for robust LLM prompt evaluation and be ready for more advanced topics in later sessions.