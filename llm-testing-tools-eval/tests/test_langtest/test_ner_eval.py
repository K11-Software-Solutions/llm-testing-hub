from langtest import Harness

def test_ner_task():
    # Example LangTest run; small sample size for speed
    h = Harness(
        task="ner",
        model={"model":"dslim/bert-base-NER", "hub":"huggingface"},
        data={"data_source":"conll2003", "split":"test", "sample_size":50}
    )
    report = h.generate().run().report()
    # report is dict-like; ensure keys exist
    assert "summary" in report
