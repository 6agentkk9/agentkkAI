Scenario: You're developing a payment reconciliation service that will eventually call a REST API.

Complete these tasks:
1. Create a project directory named payment-reconciliation.
2. Create and activate a virtual environment.
3. Install the requests package.
4. Save the installed dependencies to requirements.txt.
5. Explain how another developer can recreate your environment.

mkdir payment-reconciliation
cd payment-reconciliation

py -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install requests

python -m pip freeze > requirements.txt


Another developer runs:
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt


payment-reconciliation/
│
├── .venv/
├── main.py
├── requirements.txt
└── .gitignore


Final AI Use Case

Python application that sends a prompt to an AI model, receives a response, and uses that response in an enterprise support workflow.

(1) Install the OpenAI Python SDK
.\.venv\Scripts\Activate.ps1
python -m pip install openai

(2) Configure your API key securely

import os

print("API key configured:", bool(os.getenv("OPENAI_API_KEY")))

   check here https://platform.openai.com/api-keys?utm_source=chatgpt.com

On Windows, to keep using the key after closing the terminal:
1. Open "Edit environment variables for your account" from the Start menu.
2. Under User variables, choose New.
3. Set the variable name to OPENAI_API_KEY and the value to your API key.
4. Save, then completely close and reopen VS Code so it receives the updated environment.

The script reads OPENAI_API_KEY from the environment each time it runs. Do not put
the API key in the Python file or commit it to source control.
