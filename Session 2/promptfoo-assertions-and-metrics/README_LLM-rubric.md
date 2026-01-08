
# Comparing `llm-rubric` vs. `model-graded-closedqa`

## `llm-rubric`

- **What it does:** Uses a scoring rubric to evaluate responses on multiple criteria (e.g., accuracy, clarity, relevance, tone).
- **How it works:** The LLM grades each response based on your custom rubric or set of instructions.
- **Best for:** Open-ended, creative, or complex answers where quality is multi-dimensional.
- **Feedback:** Provides detailed scores and feedback for each criterion.
- **Example:**
  > Rate this response on accuracy (1-5), clarity (1-5), and helpfulness (1-5).

---

## `model-graded-closedqa`

- **What it does:** Checks if an answer is correct for closed-ended questions (e.g., yes/no, multiple choice).
- **How it works:** The LLM determines if the answer matches the expected result (right/wrong, A/B/C/D, etc.).
- **Best for:** Factual, objective questions with a single correct answer.
- **Feedback:** Returns a clear, categorical result (e.g., Yes/No, Correct/Incorrect).
- **Example:**
  > Is this answer correct? Yes/No

---

## When to Use Each

- Use **`llm-rubric`** for:
  - Essays, explanations, or creative writing
  - Answers needing nuanced, multi-criteria evaluation

- Use **`model-graded-closedqa`** for:
  - Factual Q&A, multiple choice, or true/false
  - Tasks with a single, objective correct answer

---

**Summary:**
- Choose **`llm-rubric`** for subjective, multi-dimensional quality assessment.
- Choose **`model-graded-closedqa`** for objective correctness in Q&A tasks.
