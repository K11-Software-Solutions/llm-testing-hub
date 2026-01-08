# LLM Eval Agent Usage Guide

This document explains how to use the `llm_eval_agent` for automated, scheduled, API-driven, and dashboard-based LLM evaluation, as well as result visualization. It covers:
- Batch and scheduled test runs
- FastAPI server with status tracking
- Streamlit dashboard for uploads, runs, and results
- Table view of all test runs (past and present) with clickable links

---

## 1. Run Evaluation Agent (Batch Testing)

```
cd llm_eval_agent
python agent.py
```
- Reads config from `config.yaml`
- Loads data and models, runs all selected tests, saves reports in `results/`

---


## 2. Schedule Automated Test Runs

```
python scheduler.py
```
- Runs tests automatically every day at midnight (customize in `scheduler.py`)

---


## 3. Start API Server (FastAPI)

```
uvicorn llm_eval_agent.api_server:app --reload
```
- POST `/run-tests` to trigger a test run (returns run_id)
- GET `/runs` to list all test runs (including past runs)
- GET `/status/{run_id}` to get the current status (running, completed, failed, unknown)
- GET `/results/{run_id}` to list result files for a run
- GET `/results/{run_id}/{filename}` to download a specific result file
- POST `/upload-data` to upload new test data
- GET `/logs/{run_id}` to fetch logs for a run

Status is tracked in memory for current runs, and shown as "unknown" for past runs if the server was restarted.

---


## 4. Streamlit Dashboard (Recommended)

```
streamlit run llm_eval_agent/llm_dashboard.py
```
- Upload test data (CSV)
- Start new test runs
- See all test runs in a table (run ID is a clickable link to results, status is always current)
- Download result files

---

## 5. Visualize Results

```
python visualize.py results/<your_report>.json
```
- Plots a bar chart of scores by category (requires matplotlib)

---


## 6. Configuration

- Edit `config.yaml` to set models, data, categories, thresholds, and report formats.
- All test runs are saved in `llm_eval_agent/results/` by run ID.

---


## Example API Calls

- Trigger test run:
  ```bash
  curl -X POST http://localhost:8000/run-tests
  ```
- List all runs:
  ```bash
  curl http://localhost:8000/runs
  ```
- Fetch results:
  ```bash
  curl http://localhost:8000/results/distilbert-base-uncased-finetuned-sst-2-english_report.json
  ```
- Upload data:
  ```bash
  curl -F "file=@data/test_data.jsonl" http://localhost:8000/upload-data
  ```

---

For more customization, edit the agent code or config as needed. The dashboard and API are designed for extensibility.
