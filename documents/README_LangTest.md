# LangTest Harness

LangTest is a framework for evaluating text classification models and LLMs for robustness, fairness, and more.

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
   pip install langtest pandas
   ```

---

## Demo: Run LangTest Harness
1. Prepare your data in JSONL format (see `data/sample_sentiment.jsonl` for examples). Each line should be a JSON object with a `text` and a `label` (as a stringified list, e.g., "['positive']").
2. Run the harness:
   ```sh
   python llm-testing-tools-eval/harness/langtest_harness.py --data data/sample_sentiment.jsonl --output results_langtest.txt
   ```
3. Results will be saved to the specified output file.

---

## Guide
- Edit the harness script to change model/provider or evaluation settings.
- Ensure your data matches the required format (see comments in the script).
- For more, see: https://github.com/IBM/langtest

---

## Troubleshooting
- Ensure all dependencies are installed in your active environment.
- Data format is critical—see sample files and script comments.
- For API-based models, set your API keys as environment variables.
