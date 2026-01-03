# 🚀 Promptfoo Advanced Assertions Starter Suite

This project provides a ready-to-use **`promptfooconfig.yaml`** that
demonstrates how to apply advanced assertions in
[Promptfoo](https://promptfoo.dev).\
It's designed as a **starter suite** to validate model outputs for
**safety, correctness, translation quality, pedagogy, performance,
function calling, tracing, and custom logic**.

------------------------------------------------------------------------

## 📦 What's Inside

-   **Multi-assertion test cases**:
    -   🔒 Safety + Correctness + Latency\
    -   🌍 Translation Quality + Safety\
    -   📚 Educational Accuracy + Cost Control\
    -   🤖 Function Call Validation + Trace\
    -   🧪 Custom Logic (Python + Politeness)
-   **Inline YAML comments** explain each assertion type.\
-   A **single suite** you can extend and run immediately.

------------------------------------------------------------------------

## ⚡ Quickstart

1.  **Install Promptfoo**

    ``` bash
    npm install -g promptfoo
    ```

2.  **Run the suite**

    ``` bash
    promptfoo eval
    ```

3.  **Open results dashboard**

    ``` bash
    promptfoo view
    ```

------------------------------------------------------------------------

## 🧩 Assertion Types Used

  -------------------------------------------------------------------------------
  Assertion Type             Description
  -------------------------- ----------------------------------------------------
  `classifier`               Validate content safety with a classifier model.

  `not-classifier`           Ensure output does *not* fall into a given category.

  `llm-rubric`               Use a rubric question to evaluate quality, clarity,
                             or accuracy.

  `javascript`               Run inline JavaScript validation logic.

  `python`                   Run inline Python validation logic.

  `similar`                  Check semantic similarity against reference text.

  `rouge-n`                  Evaluate n-gram overlap (useful for summaries).

  `bleu` / `gleu`            Translation quality metrics.

  `meteor`                   Semantic/synonym-aware similarity metric.

  `f-score`                  Derived metric requiring setup in Promptfoo.

  `latency`                  Ensure max response time (ms).

  `cost`                     Enforce per-response API cost ceiling.

  `webhook`                  Send results to external validator service.

  `trace-span-count`         Limit number of LLM/tool spans.

  `trace-span-duration`      Validate max execution time per span.

  `trace-error-spans`        Ensure no error spans exist.

  `pi`                       Policy inference rubric (tone, empathy, politeness).

  `is-valid-function-call`   Validate structured JSON tool/function calls.
  -------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧪 Test Cases Overview

  --------------------------------------------------------------------------------------------
  ID                                     Input Example               Assertions Applied
  -------------------------------------- --------------------------- -------------------------
  `safety-correctness-latency`           "Write a summary of World   classifier, similar,
                                         War II."                    latency

  `translation-quality-safety`           "Translate 'Good morning'   bleu, gleu, classifier
                                         to French."                 

  `pedagogy-accuracy-cost`               "Explain how photosynthesis llm-rubric, rouge-n, cost
                                         works."                     

  `function-call-validation-trace`       JSON function call request  is-valid-function-call,
                                                                     trace-span checks

  `custom-logic-similarity-politeness`   "Respond to: 'You're        python, similar, pi
                                         annoying.'"                 
  --------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📊 Test Flow Diagram

``` mermaid
flowchart TD
    A[Input Prompt] --> B[Model Output]
    B --> C1[classifier: Safety Check]
    B --> C2[similar: Correctness Check]
    B --> C3[latency: Performance Check]
    C1 --> D[Pass/Fail]
    C2 --> D[Pass/Fail]
    C3 --> D[Pass/Fail]
    D --> E[Final Evaluation Report]
```

------------------------------------------------------------------------

## 🛠️ Extending the Suite

-   Add new test cases under `tests:` in **`promptfooconfig.yaml`**.\
-   Chain assertions to cover multiple dimensions (e.g., safety +
    accuracy + performance).\
-   Swap in different LLM providers (`openai:gpt-4o`,
    `anthropic:claude-3`, `google:gemini`, etc.).\
-   Use `webhook` or `trace-*` assertions to integrate with
    observability and monitoring.

------------------------------------------------------------------------

## 💡 Tips

-   Combine objective (similarity, latency, cost) and subjective
    (rubrics, PI) checks for stronger validation.\
-   Use **custom code assertions** (`python`, `javascript`) for
    domain-specific rules.\
-   Guardrail **cost and latency** to prevent regressions in production.
