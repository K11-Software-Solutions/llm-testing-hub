import os
import csv
from langtest import Harness

OUT_DIR = "session6_langtest_testresults"
os.makedirs(OUT_DIR, exist_ok=True)

DATA_PATH = os.path.join(OUT_DIR, "qa.csv")
with open(DATA_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["text", "label"])
    w.writeheader()
    w.writerow({"text": "What is the capital of France?", "label": "Paris"})

h = Harness(
    task="question-answering",
    model={"model": "google/flan-t5-small", "hub": "huggingface"},
    data={"data_source": DATA_PATH},
)

h.configure({
    "tests": {
        "defaults": {"min_pass_rate": 0.80},
        "robustness": {
            "add_typo": {"min_pass_rate": 0.80},
            "uppercase": {"min_pass_rate": 0.80},
            "add_punctuation": {"min_pass_rate": 0.80},
        }
    }
})

h.generate().run()
h.report(format="text", save_dir=os.path.join(OUT_DIR, "robustness_report.txt"))
h.report(format="excel", save_dir=os.path.join(OUT_DIR, "robustness_report.xlsx"))

print("Robustness reports written under:", OUT_DIR)
