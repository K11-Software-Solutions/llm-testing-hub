# LLM Testing Hub

This repository provides a comprehensive suite for evaluating, red teaming, and assuring Large Language Models (LLMs) using a variety of open-source tools and custom harnesses.

## Features
- **Promptfoo**: Prompt evaluation and assertion framework
- **DeepEval**: Automated LLM evaluation harness
- **LangTest**: Language model testing and benchmarking
- **Red Teaming**: Configurations and scripts for adversarial testing
- **Assurance Harnesses**: For AI safety, compliance, and robustness

## Structure
- `llm-testing-tools-eval/` — Main evaluation harnesses, configs, and scripts
- `llm_eval_agent/` — Custom LLM evaluation framework (API, dashboard, harness)
- `Session 1-6/` — Example sessions, challenge prompts, and test results
- `documents/` — Tool-specific documentation and usage guides
- `requirements.txt` — Python dependencies for evaluation harnesses
- `.env.example` — Example environment variables for API keys

## Quick Start
1. Clone the repository
2. Copy `.env.example` to `.env` and add your API keys
3. Install dependencies: `pip install -r requirements.txt`
4. Run evaluation scripts or harnesses as needed

## Security
- **Never commit secrets**: Use `.env` files for API keys and sensitive info
- **Red teaming**: Includes adversarial prompt configs and reporting

## License
MIT License

## Maintainers
K11 Software Solutions

For more details, see the documentation in the `documents/` folder.

## llm_eval_agent Framework

The `llm_eval_agent` is a custom Python framework for orchestrating, automating, and visualizing LLM evaluation workflows. It provides:

- **API Server (FastAPI):** Run, track, and manage LLM test jobs via REST endpoints.
- **Streamlit Dashboard:** Upload data, launch tests, monitor status, and visualize results in a user-friendly UI.
- **Flexible Test Harness:** Supports multiple evaluation tools (LangTest, Promptfoo, DeepEval) and custom agents.
- **Live Status Tracking:** See all test runs, their status, and download or visualize results instantly.
- **Visualization:** Generate bar charts and summary plots from test results (JSON/HTML).
- **Documentation:** See `llm_eval_agent/README_llm_eval_agent.md` for setup, API usage, and dashboard instructions.

This framework enables robust, reproducible, and extensible LLM evaluation pipelines for research and production.

- [llm_eval_agent Usage Guide](documents/README_llm_eval_agent.md)

## 📬 Contact

For consulting, training, or implementation support:  
🔗 [softwaretestautomation.org](https://www.softwaretestautomation.org)  
🔗 [k11softwaresolutions.com](https://www.k11softwaresolutions.com)  
📧 k11softwaresolutions@outlook.com