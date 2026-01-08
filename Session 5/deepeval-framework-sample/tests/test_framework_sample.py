
import os
import re
import openai
import yaml


PROMPT_FILES = [
    "prompt_1.txt",
    "prompt_2.txt"
]

def load_prompt_templates(prompts_folder):
    templates = []
    for fname in PROMPT_FILES:
        fpath = os.path.join(prompts_folder, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                templates.append(f.read().strip())
    return templates

def fill_prompt(template, topic):
    return template.replace("{{topic}}", topic)


def load_assertions(assertions_path):
    with open(assertions_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_models_from_providers(folder_path):
    models = []
    for fname in ["providers.yaml", "providers_1_temp.yaml"]:
        fpath = os.path.join(folder_path, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                try:
                    data = yaml.safe_load(f)
                    if isinstance(data, list):
                        for entry in data:
                            if "id" in entry:
                                # Try to extract model name from id or config
                                if "config" in entry and "model" in entry["config"]:
                                    models.append(entry["config"]["model"])
                                else:
                                    # Fallback: use id if model not in config
                                    models.append(entry["id"])
                except Exception as e:
                    print(f"Error reading {fpath}: {e}")
    return models

def get_openai_response(prompt, model):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment.")
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Only print error for model not found or access issues, skip model
        if hasattr(e, 'status_code') and e.status_code == 404:
            print(f"Skipping model '{model}': Not found or no access.")
        elif 'model_not_found' in str(e) or 'not exist' in str(e) or 'access' in str(e):
            print(f"Skipping model '{model}': {e}")
        else:
            print(f"Error with model '{model}': {e}")
        return None

def run_assertions(response, assertions):
    for typ, val in assertions:
        if typ == "contains":
            assert val in response, f"Expected '{val}' in response, got: {response}"
        elif typ == "contains-any":
            assert any(v in response for v in val), f"Expected any of {val} in response, got: {response}"
        elif typ == "not-contains":
            assert val not in response, f"Did not expect '{val}' in response, got: {response}"
        elif typ == "regex":
            assert re.search(val, response), f"Expected pattern '{val}' in response, got: {response}"

def test_framework_sample():
    base_dir = os.path.dirname(__file__)
    providers_folder = os.path.join(base_dir, "..", "providers")
    prompts_folder = os.path.join(base_dir, "..", "prompts")
    assertions_path = os.path.join(base_dir, "..", "data", "validations", "assertions.yaml")
    models = get_models_from_providers(providers_folder)
    if not models:
        raise RuntimeError("No models found in providers folder.")
    prompt_templates = load_prompt_templates(prompts_folder)
    if not prompt_templates:
        raise RuntimeError("No prompt templates found in prompts folder.")
    assertions = load_assertions(assertions_path)
    if not assertions:
        raise RuntimeError("No assertions found in data/validations folder.")
    print(f"Testing with models: {models}")
    for model in models:
        for case in assertions:
            topic = case["topic"]
            for template in prompt_templates:
                prompt = fill_prompt(template, topic)
                print(f"\nModel: {model} | Topic: {topic} | Template: {template[:30]}...")
                response = get_openai_response(prompt, model)
                if response is None:
                    print(f"Skipping assertions for model '{model}' due to previous error.")
                    break
                print(f"Prompt:\n{prompt}\n")
                print(f"Model Response:\n{response}\n{'-'*60}")
                # Use technical assertions for review prompt, general for funny story
                if "review" in template.lower():
                    run_asserts = case["asserts"]
                    run_assertions(response, run_asserts)
                elif "funny story" in template.lower():
                    # Just check topic is mentioned in response
                    assert topic.split()[0].lower() in response.lower(), f"Expected topic '{topic}' in response, got: {response}"
                else:
                    # Default: run all assertions
                    run_asserts = case["asserts"]
                    run_assertions(response, run_asserts)

if __name__ == "__main__":
    # Write all output and errors to results file
    results_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'session5_deepeval_testresults')
    os.makedirs(results_dir, exist_ok=True)
    results_path = os.path.join(results_dir, 'test_framework_sample_results.txt')
    import sys
    import traceback
    with open(results_path, 'w', encoding='utf-8') as f:
        try:
            # Redirect print to file
            class Tee:
                def __init__(self, *files):
                    self.files = files
                def write(self, obj):
                    for file in self.files:
                        file.write(obj)
                        file.flush()
                def flush(self):
                    for file in self.files:
                        file.flush()
            sys.stdout = sys.stderr = Tee(sys.stdout, f)
            test_framework_sample()
            print("All framework sample tests passed if no assertion error is shown.")
        except Exception as e:
            print("\nERROR: Test failed with exception:\n")
            traceback.print_exc(file=f)
            traceback.print_exc()
