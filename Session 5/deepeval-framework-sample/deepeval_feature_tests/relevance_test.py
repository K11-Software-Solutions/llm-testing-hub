
# Relevance Test Example for DeepEval
import os
import openai
# from deepeval.metrics import RelevanceMetric  # Not available in all versions

# Use FaithfulnessMetric as a placeholder if RelevanceMetric is unavailable
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from deepeval import assert_test

prompt = "Tell me about the Eiffel Tower."
expected = "Eiffel Tower"

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=50
)
output = response.choices[0].message.content.strip()

metric = FaithfulnessMetric()
# Faithfulness metric used as a placeholder for relevance; requires retrieval_context
tc = LLMTestCase(input=prompt, expected_output=expected, actual_output=output, retrieval_context=[expected])
assert_test(tc, [metric])
os.makedirs("session5_deepeval_testresults", exist_ok=True)
with open("session5_deepeval_testresults/relevance_test.txt", "w", encoding="utf-8") as f:
    f.write(f"Prompt: {prompt}\nExpected: {expected}\nOutput: {output}\nRelevance (Faithfulness) test passed.\n")
