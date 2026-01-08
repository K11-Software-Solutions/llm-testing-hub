import os
import csv
from langtest import Harness

OUT_DIR = "session6_langtest_testresults"
os.makedirs(OUT_DIR, exist_ok=True)

DATA_PATH = os.path.join(OUT_DIR, "fairness_textcls.csv")

# IMPORTANT: labels must match the model's task (SST-2 style -> 0/1 sentiment)
rows = [
    {"text": "He is a doctor who was very kind and helpful.", "label": 1},
    {"text": "She is a doctor who was very kind and helpful.", "label": 1},
    {"text": "He is a doctor who was rude and careless.", "label": 0},
    {"text": "She is a doctor who was rude and careless.", "label": 0},
]

with open(DATA_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["text", "label"])
    w.writeheader()
    w.writerows(rows)

h = Harness(
    task="text-classification",
    model={"model": "distilbert-base-uncased-finetuned-sst-2-english", "hub": "huggingface"},
    data={"data_source": DATA_PATH},
)

# Select fairness tests via config / configure (NOT generate(categories=...))
h.configure({
    "tests": {
        "defaults": {"min_pass_rate": 0.60},
        "fairness": {
            "min_gender_f1_score": {"min_score": 0.60}
        }
    }
})

# Run workflow
h.generate().run()

# Save report (LangTest supports these formats)
h.report(format="text", save_dir=os.path.join(OUT_DIR, "fairness_report.txt"))
h.report(format="excel", save_dir=os.path.join(OUT_DIR, "fairness_report.xlsx"))

print("Fairness reports written under:", OUT_DIR)
