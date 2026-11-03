from openai import (
    OpenAI,
    APIConnectionError,
    APIStatusError,
    RateLimitError
)

client = OpenAI(timeout=30.0, max_retries=2)

incident = """
Payment ID: 1001
Amount: 250 USD
Status: FAILED
Error Code: TIMEOUT

Description:
Payment gateway did not respond
within the configured timeout.
"""

prompt = f"""
You are an experienced payment production support analyst.

Analyze the following incident.

{incident}

Provide:
1. Possible causes.
2. Recommended investigation steps.
3. Suggested application logs to review.
4. Possible corrective actions.

Do not claim that a suspected cause is confirmed.
Clearly distinguish facts from hypotheses.
"""

try:
    response = client.responses.create(
        model="gpt-6-astra",
        input=prompt
    )

    print("AI Incident Analysis:")
    print(response.output_text)

except RateLimitError:
    print("AI API rate limit exceeded")

except APIConnectionError:
    print("Unable to connect to AI API")

except APIStatusError as error:
    print("AI API returned an error:", error.status_code)