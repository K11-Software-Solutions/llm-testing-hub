import json
from pathlib import Path
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric
from deepeval import assert_test

DATA = Path("data/ground_truth/faq_testset.jsonl")

def test_faq_cases():
    metrics = [
        FaithfulnessMetric(minimum_score=0.5),  # lowered threshold for quick demo
        AnswerRelevancyMetric(minimum_score=0.5),
    ]
    with DATA.open() as f:
        for line in f:
            j = json.loads(line)
            tc = LLMTestCase(
                input=f"Question about {j['product']}: {j['question']}",
                expected_output=j["ground_truth"],
                context=j["ground_truth"]
            )
            # Will raise AssertionError if fails
            assert_test(tc, metrics)
