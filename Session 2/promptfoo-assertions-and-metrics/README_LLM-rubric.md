# Key Differences Between `llm-rubric` and `model-graded-closedqa`

## llm-rubric

- **Evaluation Style:** Rubric-based approach.
- **How It Works:** The LLM evaluates responses against predefined criteria or scoring rubrics.
- **Flexibility:** Highly flexible and nuanced — can assess multiple dimensions such as accuracy, clarity, relevance, tone, etc.
- **Feedback:** Typically provides detailed feedback and scores across different criteria.
- **Best For:** Open-ended responses where quality can be measured on multiple axes.
- **Example:**  
  *"Rate this response on accuracy (1-5), clarity (1-5), and helpfulness (1-5)"*

---

## model-graded-closedqa

- **Evaluation Style:** Designed for closed-ended question answering.
- **How It Works:** Focuses on binary or categorical correctness (e.g., right/wrong, A/B/C/D).
- **Structure:** More structured and deterministic evaluation.
- **Best For:** Cases where there are clear, factual answers.
- **Speed & Consistency:** Faster and more consistent for objective assessments.
- **Example:**  
  *"Is this answer correct? Yes/No"* or *"Which option does this answer correspond to?"*

---

## When to Use Each

- **Use `llm-rubric`** for:
  - Essays, explanations, or creative content.
  - Complex responses that require multi-dimensional evaluation.

- **Use `model-graded-closedqa`** for:
  - Factual questions, multiple choice, true/false.
  - Objective assessments with a single correct answer.

---

**Summary:**  
Choose **`llm-rubric`** when evaluating *subjective quality*, tone, or multi-axis performance.  
Choose **`model-graded-closedqa`** when evaluating *objective correctness* in Q&A tasks.
