from fastapi import FastAPI
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RESULTS_ROOT = BASE_DIR / "llm_eval_agent" / "results"
LOGS_DIR = BASE_DIR / "logs"
CONFIG_PATH = BASE_DIR / "config.yaml"
LATEST_DATA_PTR = DATA_DIR / "_latest.txt"
DATA_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_ROOT.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()

from fastapi import Body
from fastapi.responses import JSONResponse
import json
import datetime
import logging

# In-memory status tracking (for demo; use DB/Redis for production)
RUN_STATUS = {}
# List all runs and their status
@app.get("/runs")
def list_runs():
    runs = []
    for run_dir in RESULTS_ROOT.iterdir():
        if run_dir.is_dir():
            run_id = run_dir.name
            status = RUN_STATUS.get(run_id, {}).get("status", "unknown")
            runs.append({"run_id": run_id, "status": status})
    return {"runs": runs}

# Get status of a specific run
@app.get("/status/{run_id}")
def get_status(run_id: str):
    return RUN_STATUS.get(run_id, {"status": "unknown"})

# Config endpoints
@app.get("/config")
def get_config():
    if not CONFIG_PATH.exists():
        raise HTTPException(status_code=404, detail="Config not found")
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return JSONResponse(content=json.load(f))

@app.post("/config")
def update_config(config: dict = Body(...)):
    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    return {"status": "Config updated"}

# Models endpoint
@app.get("/models")
def get_models():
    if not CONFIG_PATH.exists():
        raise HTTPException(status_code=404, detail="Config not found")
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = json.load(f)
    return {"models": config.get("models", [])}

# Categories endpoint
@app.get("/categories")
def get_categories():
    if not CONFIG_PATH.exists():
        raise HTTPException(status_code=404, detail="Config not found")
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = json.load(f)
    return {"categories": config.get("categories", [])}

# Delete run endpoint
@app.delete("/delete-run/{run_id}")
def delete_run(run_id: str):
    run_dir = RESULTS_ROOT / run_id
    if not run_dir.exists():
        raise HTTPException(status_code=404, detail="Run not found")
    shutil.rmtree(run_dir)
    RUN_STATUS.pop(run_id, None)
    return {"status": "deleted", "run_id": run_id}

# Logs endpoint (demo: just lists log files for a run)
@app.get("/logs/{run_id}")
def get_logs(run_id: str):
    log_file = LOGS_DIR / f"{run_id}.log"
    if not log_file.exists():
        return {"run_id": run_id, "log": "No log file found."}
    with log_file.open("r", encoding="utf-8") as f:
        return {"run_id": run_id, "log": f.read()}
from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse

from pathlib import Path
import shutil
import uuid

BASE_DIR = Path(__file__).resolve().parent
from .agent import LLMEvalAgent  # requires package execution


DATA_DIR = BASE_DIR / "data"
RESULTS_ROOT = BASE_DIR / "llm_eval_agent" / "results"
LOGS_DIR = BASE_DIR / "logs"
CONFIG_PATH = BASE_DIR / "config.yaml"
LATEST_DATA_PTR = DATA_DIR / "_latest.txt"

DATA_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_ROOT.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

def _safe_resolve(base: Path, relative_path: str) -> Path:
    p = (base / relative_path).resolve()
    if not str(p).startswith(str(base.resolve())):
        raise HTTPException(status_code=400, detail="Invalid path")
    return p

def run_agent(run_id: str, data_file: str | None = None):
    run_dir = RESULTS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    # Set status to running
    RUN_STATUS[run_id] = {"status": "running"}
    try:
        agent = LLMEvalAgent(
            config_path=str(CONFIG_PATH),
            results_dir=str(run_dir),
            data_file_override=data_file,
        )
        agent.run_tests()
        RUN_STATUS[run_id]["status"] = "completed"
    except Exception as e:
        RUN_STATUS[run_id]["status"] = "failed"
        # Optionally, log the error or store it in RUN_STATUS
        RUN_STATUS[run_id]["error"] = str(e)

@app.post("/run-tests")
def run_tests(background_tasks: BackgroundTasks):
    run_id = uuid.uuid4().hex[:12]

    data_file = None
    if LATEST_DATA_PTR.exists():
        data_file = LATEST_DATA_PTR.read_text(encoding="utf-8").strip() or None

    background_tasks.add_task(run_agent, run_id, data_file)
    return {"status": "Test run started.", "run_id": run_id, "data_file": data_file}

@app.get("/results")
def list_results():
    runs = sorted([p.name for p in RESULTS_ROOT.iterdir() if p.is_dir()])
    return {"results_root": str(RESULTS_ROOT), "runs": runs}

@app.get("/results/{run_id}")
def list_results_for_run(run_id: str):
    run_dir = _safe_resolve(RESULTS_ROOT, run_id)
    if not run_dir.exists() or not run_dir.is_dir():
        raise HTTPException(status_code=404, detail="Run not found")

    files = [str(p.relative_to(run_dir)) for p in run_dir.rglob("*") if p.is_file()]
    return {"run_id": run_id, "files": files}

@app.get("/results/{run_id}/{filepath:path}")
def get_results(run_id: str, filepath: str):
    run_dir = _safe_resolve(RESULTS_ROOT, run_id)
    requested = _safe_resolve(run_dir, filepath)

    if not requested.exists() or not requested.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=str(requested), filename=requested.name)

@app.post("/upload-data")
def upload_data(file: UploadFile = File(...)):
    dest = _safe_resolve(DATA_DIR, file.filename)

    with dest.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    LATEST_DATA_PTR.write_text(str(dest), encoding="utf-8")

    return {
        "status": "Uploaded",
        "filename": file.filename,
        "saved_to": str(dest),
        "latest_pointer": str(LATEST_DATA_PTR),
    }
