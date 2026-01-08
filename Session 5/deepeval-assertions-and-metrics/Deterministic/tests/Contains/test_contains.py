
import os
import openai

prompt = "Greet the user in French."
expected_substring = "Bonjour"

def get_openai_response(prompt, model="gpt-4o-mini"):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment.")
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

def test_greet_in_french():
    response = get_openai_response(prompt)
    assert expected_substring in response, f"Expected '{expected_substring}' in response, got: {response}"

if __name__ == "__main__":
    test_greet_in_french()
    print("Test passed if no assertion error is shown.")
