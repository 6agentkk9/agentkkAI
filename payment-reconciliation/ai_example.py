import os

from openai import OpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Configure it in the environment before running this script."
    )

print("Sending request...", flush=True)
client = OpenAI(timeout=30.0, max_retries=0)
response = client.responses.create(
    model="gpt-6-astra",
    input="Explain what a payment reconciliation process does."
)

print("Response received.", flush=True)
print(response.output_text)