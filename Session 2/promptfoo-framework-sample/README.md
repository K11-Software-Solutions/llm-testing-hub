
# Promptfoo Framework Sample

This sample demonstrates how to use Promptfoo with modular prompts, variables, and external file references for maintainable and reusable prompt testing.

## What’s Inside

- Modular prompt templates with variables
- Provider configurations for different LLMs
- YAML-based test cases and assertions
- Automated batch testing and HTML results

## Folder Structure

```
promptfoo-framework-sample/
├── promptfooconfig.yaml         # Main Promptfoo config
├── providers/
│   ├── providers.yaml           # Base provider config
│   └── providers_1_temp.yaml    # Additional provider config
├── prompts/
│   ├── prompt_1.txt             # Description prompt template
│   └── prompt_2.txt             # Story prompt template
├── tests/
│   └── tests.yaml               # Test cases and assertions
└── results.html                 # Generated test results
```

## Quick Start

1. **Install Promptfoo:**
   ```sh
   npm install -g promptfoo
   ```
2. **Set API Keys:**  
   Add your keys as environment variables or in a `.env` file:
   ```sh
   export OPENAI_API_KEY=your_key_here
   export ANTHROPIC_API_KEY=your_key_here
   ```
3. **Run Tests:**
   ```sh
   promptfoo eval promptfooconfig.yaml
   ```
4. **View Results:**
   ```sh
   promptfoo view
   ```

## How It Works

- **Config File:**  
  `promptfooconfig.yaml` references prompts, providers, and tests using `file://` paths.
- **Prompt Templates:**  
  Use variables like `{{topic}}` in prompt files for flexibility.
- **Test Cases:**  
  Define variables and assertions in YAML. Example:
  ```yaml
  - description: "Test description about cats"
    vars:
      topic: "cats"
    assert:
      - type: contains
        value: "cats"
      - type: llm-rubric
        value: "Check if the response is exactly 2 sentences"
  ```

## Best Practices

- Keep prompts simple and focused
- Use clear variable names
- Include specific assertions for outputs
- Test with a variety of topics
- Organize files by type (prompts, providers, tests)

---

This sample helps you build robust, maintainable prompt evaluation workflows with Promptfoo.

---