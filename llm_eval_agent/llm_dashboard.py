import streamlit as st
import requests
import os

API_URL = os.environ.get("LLM_API_URL", "http://localhost:8000")

st.title("LLM Evaluation Dashboard")

# Upload data
data_file = st.file_uploader("Upload test data (CSV)")
if st.button("Upload Data") and data_file:
    files = {"file": (data_file.name, data_file, "text/csv")}
    resp = requests.post(f"{API_URL}/upload-data", files=files)
    if resp.ok:
        st.success(f"Uploaded: {data_file.name}")
    else:
        st.error(f"Upload failed: {resp.text}")

# Start a test run
if st.button("Start Test Run"):
    resp = requests.post(f"{API_URL}/run-tests")
    if resp.ok:
        run_id = resp.json().get("run_id")
        st.success(f"Test run started: {run_id}")
    else:
        st.error(f"Run start failed: {resp.text}")

# List runs and status
st.header("Test Runs")
runs = requests.get(f"{API_URL}/runs").json().get("runs", [])

if runs:
    # Fetch current status for each run (live)
    table_rows = []
    for run in runs:
        status_resp = requests.get(f"{API_URL}/status/{run['run_id']}")
        status = status_resp.json().get("status", run.get("status", "unknown"))
        result_url = f"{API_URL}/results/{run['run_id']}"
        run_id_link = f'<a href="{result_url}" target="_blank">{run["run_id"]}</a>'
        # Try to find a JSON result file for this run
        files_resp = requests.get(f"{API_URL}/results/{run['run_id']}")
        files = files_resp.json().get("files", []) if files_resp.ok else []
        json_files = [f for f in files if f.endswith('.json')]
        if json_files:
            json_file = json_files[0]
            json_url = f"{API_URL}/results/{run['run_id']}/{json_file}"
            visualize_cmd = f"python visualize.py results/{run['run_id']}/{json_file}"
            visualize_link = f'<a href="{json_url}" download>Download JSON</a> | <code>{visualize_cmd}</code>'
        else:
            visualize_link = '<span style="color:gray">No JSON result</span>'
        table_rows.append(f"<tr><td>{run_id_link}</td><td>{status}</td><td>{visualize_link}</td></tr>")
    table_html = """
    <table>
        <thead><tr><th>Test Run ID</th><th>Status</th><th>Visualize</th></tr></thead>
        <tbody>
        {rows}
        </tbody>
    </table>
    """.format(rows="\n".join(table_rows))
    st.markdown(table_html, unsafe_allow_html=True)
else:
    st.info("No test runs found.")
