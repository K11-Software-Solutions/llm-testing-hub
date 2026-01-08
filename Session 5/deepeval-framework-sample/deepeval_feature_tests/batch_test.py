
# Batch Testing Example for DeepEval
import os
import openai
import csv
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from deepeval import assert_test

prompts = [
    ("What is the capital of Italy?", "Rome"),
    ("What is the largest planet?", "Jupiter"),
    ("Who wrote Hamlet?", "Shakespeare")
]

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)
metric = FaithfulnessMetric()

os.makedirs("session5_deepeval_testresults", exist_ok=True)
with open("session5_deepeval_testresults/batch_test_results.csv", "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Prompt", "Expected", "Output", "Faithfulness Test Result"])
    for prompt, expected in prompts:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=30
        )
        output = response.choices[0].message.content.strip()
        tc = LLMTestCase(input=prompt, expected_output=expected, actual_output=output)
        try:
            assert_test(tc, [metric])
            result = "PASS"
        except AssertionError as e:
            result = f"FAIL: {e}"
        writer.writerow([prompt, expected, output, result])
print("Batch test results written to session5_deepeval_testresults/batch_test_results.csv")
