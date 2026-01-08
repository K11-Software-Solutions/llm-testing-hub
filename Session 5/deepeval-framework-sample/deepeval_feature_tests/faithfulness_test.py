
# Faithfulness/Factuality Test Example for DeepEval
import os
import openai
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from deepeval import assert_test

prompt = "What is the capital of France?"
expected = "Paris"

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=20
)
output = response.choices[0].message.content.strip()

metric = FaithfulnessMetric()
# Faithfulness metric requires retrieval_context (ground truth/context)
tc = LLMTestCase(input=prompt, expected_output=expected, actual_output=output, retrieval_context=[expected])
assert_test(tc, [metric])
os.makedirs("session5_deepeval_testresults", exist_ok=True)
with open("session5_deepeval_testresults/faithfulness_test.txt", "w", encoding="utf-8") as f:
    f.write(f"Prompt: {prompt}\nExpected: {expected}\nOutput: {output}\nFaithfulness test passed.\n")
