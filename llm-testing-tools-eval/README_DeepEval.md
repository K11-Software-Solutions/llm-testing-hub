# DeepEval Harness

DeepEval is a framework for regression and assertion-based evaluation of LLMs.

---

## Installation
1. (Recommended) Create a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```
2. Install dependencies:
   ```sh
   pip install deepeval openai
   ```

---

## Demo: Run DeepEval Harness
1. Prepare your prompts and expected outputs in a CSV or JSONL file (see `data/ground_truth/` for examples).
2. Run the harness:
   ```sh
   python llm-testing-tools-eval/harness/deepeval_harness.py --data data/ground_truth/faq_testset.jsonl --output results_deepeval.txt
   ```
3. Results will be saved to the specified output file.

---

## Guide
- Edit the harness script to change model/provider or evaluation settings.
- Set your OpenAI API key as an environment variable: `set OPENAI_API_KEY=sk-...`
- For more, see: https://github.com/confident-ai/deepeval

---

## Troubleshooting
- Ensure all dependencies are installed in your active environment.
- Data format is critical—see sample files and script comments.
- For API-based models, set your API keys as environment variables.
