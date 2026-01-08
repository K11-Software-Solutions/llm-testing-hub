from __future__ import annotations
from langtest import Harness

def main():
    # Example: sentiment analysis using a local CSV file
    h = Harness(
        task="text-classification",
        model={"model":"distilbert-base-uncased-finetuned-sst-2-english", "hub":"huggingface"},
        data={"data_source": "llm-testing-tools-eval/data/sample_sentiment.jsonl"}
    )
    # Generate tests (robustness/bias/etc.), run them, then print a brief report.
    report = h.generate().run().report()
    print(report)
    with open("llm-testing-tools-eval/langtest_results.txt", "w", encoding="utf-8") as f:
        f.write(str(report))
    print("Results saved to llm-testing-tools-eval/langtest_results.txt")

if __name__ == "__main__":
    main()
