
import os
import pytest

# Skip unless user opts in (needs API access for LLM-as-judge metrics)
RUN = os.getenv("RUN_DEEPEVAL", "0") == "1"
pytestmark = pytest.mark.skipif(not RUN, reason="Set RUN_DEEPEVAL=1 to run DeepEval tests (requires API keys).")

from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric
from deepeval import assert_test
from pathlib import Path
import json

DATA = Path("data/ground_truth/faq_testset.jsonl")

def iter_cases():
    with DATA.open() as f:
        for line in f:
            j = json.loads(line)
            yield LLMTestCase(
                input=f"Question about {j['product']}: {j['question']}",
                expected_output=j["ground_truth"],
                context=f"""Reference (ground truth): {j["ground_truth"]}
Only answer based on the reference; do not hallucinate."""
            )

def test_faq_faithfulness_and_relevance():
    metrics = [
        FaithfulnessMetric(minimum_score=0.80),
        AnswerRelevancyMetric(minimum_score=0.80),
    ]
    for tc in iter_cases():
        assert_test(tc, metrics)
