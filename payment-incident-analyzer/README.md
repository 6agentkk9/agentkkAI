# Payment Incident Analyzer

A small, layered Python application for storing payment incidents, retrieving gateway details, and producing JSON reports.

## Requirements

- Python 3.11 or newer
- Windows PowerShell, Command Prompt, macOS, or Linux

## Setup (Windows PowerShell)

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

If PowerShell blocks activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

## Run

Initialize the SQLite database and insert sample incidents:

```powershell
python -m payment_analyzer.main --init-db --seed
```

List stored incidents:

```powershell
python -m payment_analyzer.main --list
```

Generate a report for all incidents:

```powershell
python -m payment_analyzer.main --report
```

Run the mock gateway API (in a second terminal):

```powershell
python -m payment_analyzer.mock_api
```

Then check a payment through the mock API:

```powershell
python -m payment_analyzer.main --check-gateway PAY-10001
```

## Run tests

```powershell
pytest -v
pytest --cov=payment_analyzer --cov-report=term-missing
```

## Project layout

```text
src/payment_analyzer/
  config/         Environment-based settings
  models/         Pydantic/domain data models
  repositories/   SQLite persistence
  services/       Business logic and gateway client
  utils/          Logging setup
  main.py         CLI entry point
  mock_api.py     Local mock gateway API
tests/            Automated tests
data/             SQLite database (created at runtime)
logs/             Application logs (created at runtime)
reports/          JSON reports (created at runtime)
```

## Design notes

- Services receive repositories through constructor injection.
- SQLite access is managed with a context manager that commits or rolls back and always closes the connection.
- Monetary values use `Decimal`.
- The gateway client uses synchronous `requests`; a thread pool or async client can be introduced later if profiling justifies it.
- AI integration is intentionally optional. No API key or model name is assumed. Add and configure an AI provider only when needed.
- Never log card numbers, security codes, credentials, authorization tokens, or other sensitive payment data.

## Configuration

Copy `.env.example` to `.env`. The default database is `data/payment_incidents.db`, and the mock API listens on `http://localhost:8000`.

Do not commit `.env`.
