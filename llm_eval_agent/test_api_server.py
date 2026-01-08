import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from fastapi.testclient import TestClient
from llm_eval_agent.api_server import app

client = TestClient(app)

def test_run_tests_returns_run_id():
    resp = client.post("/run-tests")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "Test run started."
    assert "run_id" in body

def test_list_results_returns_runs():
    resp = client.get("/results")
    assert resp.status_code == 200
    body = resp.json()
    assert "runs" in body
    assert isinstance(body["runs"], list)

def test_upload_data_sets_latest_pointer():
    file_content = b"text,label\nhello,1\n"
    resp = client.post(
        "/upload-data",
        files={"file": ("test.csv", file_content, "text/csv")},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "Uploaded"
    assert body["filename"] == "test.csv"
    assert "latest_pointer" in body
