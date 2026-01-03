
"""Minimal Agenta SDK example: create a variant and (pretend to) deploy.
Requires: pip install agenta openai opentelemetry-instrumentation-openai
Set env: AGENTA_API_KEY, AGENTA_HOST (if using Cloud)
Note: This is a scaffold; adjust to your Agenta version.
"""
import os
try:
    import agenta as ag
    from agenta.sdk.types import PromptTemplate, Message, ModelConfig
    from pydantic import BaseModel
except Exception as e:
    print("Agenta SDK not installed. Install with: pip install agenta")
    raise

os.environ.setdefault("AGENTA_HOST", "http://localhost")
ag.init()

APP_SLUG = "faq-bot"
VARIANT = "baseline"
ENV = "staging"

class Config(BaseModel):
    prompt: PromptTemplate

cfg = Config(
    prompt=PromptTemplate(
        messages=[
            Message(role="system", content="You are a concise support bot."),
            Message(role="user", content="Answer about {{product}}: {{question}}. Use only this reference: {{ground_truth}}"),
        ],
        llm_config=ModelConfig(model="gpt-4o-mini", temperature=0.2, max_tokens=300),
    )
)

print("Creating/Updating app + variant...")
app = ag.AppManager.create(app_slug=APP_SLUG, template_key="SERVICE:chat")
variant = ag.VariantManager.create(app_slug=APP_SLUG, variant_slug=VARIANT, parameters=cfg.model_dump())
print("Deploying to environment:", ENV)
deployment = ag.DeploymentManager.deploy(app_slug=APP_SLUG, variant_slug=VARIANT, environment_slug=ENV)
print("Done. Deployment:", deployment)
