import os
import re
import openai

prompt = "In which year was the Java language first released? Respond with the year only."
expected_pattern = r"\b1995\b"

def get_openai_response(prompt, model="gpt-4o-mini"):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment.")
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10
    )
    return response.choices[0].message.content.strip()

def test_java_year_regex():
    response = get_openai_response(prompt)
    resp = response.strip()
    if not re.search(expected_pattern, resp):
        print(f"DEBUG: repr(response)={repr(response)} | expected_pattern={expected_pattern}")
        print(f"DEBUG: regex={expected_pattern}, response={resp}")
    assert re.search(expected_pattern, resp), f"Expected pattern '{expected_pattern}' in response, got: {response}"

if __name__ == "__main__":
    results_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'session5_deepeval_testresults')
    os.makedirs(results_dir, exist_ok=True)
    results_path = os.path.join(results_dir, 'Regex_results.txt')
    try:
        test_java_year_regex()
        with open(results_path, 'w', encoding='utf-8') as f:
            f.write("Test passed if no assertion error is shown.\n")
        print(f"Test passed. Result saved to {results_path}")
    except Exception as e:
        with open(results_path, 'w', encoding='utf-8') as f:
            import traceback
            traceback.print_exc(file=f)
        print(f"Test failed. Error written to {results_path}")
