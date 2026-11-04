# Payment Incident Analyzer

A Python-based payment production support tool that retrieves payment and gateway information, analyzes incidents using an AI model, and generates structured JSON incident reports.

## Project Overview

The application demonstrates how Python can be used to build a practical production-support solution.

### Features

- Payment incident management using SQLite.
- Repository and service-layer architecture.
- REST API integration using `requests`.
- JSON response parsing and mapping.
- AI-powered incident analysis using the OpenAI API.
- Structured analysis output using Pydantic.
- JSON incident report generation.
- Application logging and exception handling.
- Unit testing with pytest and mocking.
- Integration testing with SQLite and a mock payment API.

## Technology Stack

- Python
- SQLite
- REST APIs
- requests
- OpenAI Python SDK
- Pydantic
- JSON
- logging
- pytest

## Architecture

The application is organized into layers:

- **Models:** Payment incident and gateway response data structures.
- **Repositories:** Database access and persistence.
- **Services:** Business logic, API integration, AI analysis, and report generation.
- **Tests:** Unit and integration tests.

## Prerequisites

- Python 3.10 or later
- Visual Studio Code (recommended)
- An OpenAI API key for AI analysis

## Setup

Clone or download the project and open its root directory.

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_available_model
PAYMENT_API_BASE_URL=http://localhost:8000
```

Use a model ID available to your API account. Do not commit `.env` to Git.

## Initialize the Database

```powershell
python -m app.database
```

## Start the Mock Payment API

In a separate terminal:

```powershell
python -m app.mock_payment_api
```

Keep the server running while using the API client or running integration tests.

## Run the Application

Run the application's configured entry point:

```powershell
python -m app.main
```

If your current AI demonstration is in `app/ai_demo.py`, you can run it with:

```powershell
python -m app.ai_demo
```

The AI demonstration requires a valid API key and model configuration.

## Run Tests

Run the complete test suite:

```powershell
python -m pytest -v
```

Run only integration tests:

```powershell
python -m pytest tests/test_integration.py -v
```

## Output

Generated incident reports are saved under:

```text
reports/
```

Application logs are saved under:

```text
logs/
```

## Important Notes

- The included payment API is a local mock service, not a real payment gateway.
- AI analysis is advisory and must be reviewed by an authorized support engineer.
- AI output must not independently trigger payment retries or financial transactions.
- Use synthetic payment data for development and testing.
- Keep credentials and sensitive payment information out of source control.

## Learning Outcomes

This project demonstrates Python application development, database integration, REST API consumption, AI integration, structured data processing, logging, exception handling, and automated testing.