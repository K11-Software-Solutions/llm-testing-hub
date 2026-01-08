
# Promptfoo Basics

Learn how to quickly set up and use Promptfoo for automated LLM prompt testing.

## What You’ll Learn

- How to install and verify Promptfoo
- How to set up a project and run your first evaluation
- How to use prompts, providers, and assertions
- How to view and interpret results

## Quick Start

1. **Install Promptfoo** (choose one):
   - npm (global): `npm install -g promptfoo`
   - npx (one-shot): `npx promptfoo@latest`
   - Homebrew: `brew install promptfoo`

   Verify installation:
   ```sh
   promptfoo --version
   ```

2. **Create a Workspace Folder** and move into it:
   ```sh
   mkdir promptfoo-demo && cd promptfoo-demo
   ```

3. **Initialize Promptfoo**:
   ```sh
   promptfoo init
   ```
   This creates a minimal `promptfooconfig.yaml`.

4. **Run Your First Evaluation**:
   ```sh
   promptfoo eval
   ```
   If you see API key errors, set your OpenAI key:
   ```sh
   export OPENAI_API_KEY=your-key-here
   ```
   Then rerun:
   ```sh
   promptfoo eval
   ```

5. **View Results in Browser**:
   ```sh
   promptfoo view
   ```

---

## Prompts

- Use one-liner or multiline prompts in the config file.
- Inject variables with `${variable}`.
- Store large prompts in separate files and reference them.

---

## Providers

- Configure providers in the config or via environment variables.
- Connect to OpenAI, Anthropic, or local models (e.g., LM Studio).

---

## Assertions & Metrics

- **Deterministic Assertions:**  
  - `contains`: Output must include a keyword/phrase  
  - `regex`: Output must match a regular expression
- **Model-Graded Metrics:**  
  - `answer-relevance`, `factuality`, `llm-rubric` (custom grading)

---

For more details, see the [Promptfoo documentation](https://www.promptfoo.dev/docs/intro/).

Happy testing! 🚀

---
|-------|------|
