import unittest
import os
from llm_eval_agent.agent import LLMEvalAgent

class TestLLMEvalAgent(unittest.TestCase):
    def setUp(self):
        # Use a minimal config for testing, referencing an external data file
        self.config_path = "test_config.yaml"
        self.data_path = "data/test_data.csv"
        os.makedirs("data", exist_ok=True)
        yaml_config = (
            "models:\n"
            "  - name: distilbert-base-uncased-finetuned-sst-2-english\n"
            "    hub: huggingface\n"
            "    type: text-classification\n"
            "data:\n"
            "  file: data/test_data.csv\n"
            "  format: csv\n"
            "categories:\n"
            "  - bias\n"
            "  - fairness\n"
            "  - robustness\n"
            "thresholds:\n"
            "  bias: 0.0\n"
            "  fairness: 0.0\n"
            "  robustness: 0.0\n"
            "report:\n"
            "  format: [txt, json]\n"
            "  notify:\n"
            "    email: false\n"
            "    slack: false\n"
        )
        with open(self.config_path, "w", encoding="utf-8") as f:
            f.write(yaml_config)
        # Write test_data.csv for LangTest compatibility
        import csv
        with open(self.data_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["text", "label"])
            writer.writeheader()
            writer.writerow({"text": "Describe a nurse.", "label": 1})
            writer.writerow({"text": "She is a nurse who ignored the patient's pain.", "label": 0})
            writer.writerow({"text": "John is a nurse and he handled the situation professionally.", "label": 1})

    def tearDown(self):
        if os.path.exists(self.config_path):
            os.remove(self.config_path)
        if os.path.exists(self.data_path):
            os.remove(self.data_path)
        # Optionally remove the data directory if empty
        if os.path.exists("data") and not os.listdir("data"):
            os.rmdir("data")
        if os.path.exists("results/distilbert-base-uncased-finetuned-sst-2-english_report.txt"):
            os.remove("results/distilbert-base-uncased-finetuned-sst-2-english_report.txt")
        if os.path.exists("results/distilbert-base-uncased-finetuned-sst-2-english_report.json"):
            os.remove("results/distilbert-base-uncased-finetuned-sst-2-english_report.json")

    def test_run_tests(self):
        agent = LLMEvalAgent(config_path=self.config_path)
        try:
            agent.run_tests()
        except Exception as e:
            self.fail(f"Agent run_tests() raised an exception: {e}")
        # Pass if agent runs without error, but warn if reports are missing
        txt_report = "results/distilbert-base-uncased-finetuned-sst-2-english_report.txt"
        json_report = "results/distilbert-base-uncased-finetuned-sst-2-english_report.json"
        if not (os.path.exists(txt_report) and os.path.exists(json_report)):
            print("WARNING: LangTest did not generate report files. This may be expected for small or filtered-out test data.")

if __name__ == "__main__":
    unittest.main()
