
"""Fetch deployed prompt config and run a single inference.
Set env: OPENAI_API_KEY, (optional) AGENTA_API_KEY if fetching from Cloud.
"""
import os
import openai

try:
    import agenta as ag
except Exception:
    print("Agenta SDK not installed. Install with: pip install agenta")
    raise

os.environ.setdefault("AGENTA_HOST", "http://localhost")
ag.init()
openai.api_key = os.environ.get("OPENAI_API_KEY")

APP_SLUG = "faq-bot"
ENV = "staging"

cfg = ag.ConfigManager.get_from_registry(app_slug=APP_SLUG, environment_slug=ENV)

def render_messages(product: str, question: str, ground_truth: str):
    msgs = []
    for m in cfg["messages"]:
        content = m["content"]
        content = content.replace("{{product}}", product).replace("{{question}}", question).replace("{{ground_truth}}", ground_truth)
        msgs.append({"role": m["role"], "content": content})
    return msgs

def main():
    messages = render_messages(
        "AcmeCRM",
        "How do I export contacts?",
        "Go to Contacts → Export → choose CSV or XLSX."
    )
    resp = openai.ChatCompletion.create(
        model=cfg["llm_config"]["model"],
        messages=messages,
        temperature=cfg["llm_config"].get("temperature", 0.2),
        max_tokens=cfg["llm_config"].get("max_tokens", 300),
    )
    print(resp.choices[0].message["content"])

if __name__ == "__main__":
    main()
