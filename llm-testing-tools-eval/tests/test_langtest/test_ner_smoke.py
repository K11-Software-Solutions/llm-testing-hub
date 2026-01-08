
import os
import pytest

# LangTest downloads models/datasets; opt-in to avoid long CI
RUN = os.getenv("RUN_LANGTEST", "0") == "1"
pytestmark = pytest.mark.skipif(not RUN, reason="Set RUN_LANGTEST=1 to run LangTest tests (downloads models).")

from langtest import Harness

def test_ner_smoke_report():
    h = Harness(
        task="ner",
        model={"model":"dslim/bert-base-NER", "hub":"huggingface"},
        data={"data_source":"conll2003", "split":"test", "sample_size": 50}
    )
    report = h.generate().run().report()
    # Basic sanity checks on report structure
    assert "summary" in report or isinstance(report, (str, dict))
