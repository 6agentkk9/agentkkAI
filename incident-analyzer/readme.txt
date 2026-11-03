Read payment incidents from a SQLite database.


Retrieve additional payment information through a REST API.


Analyze incidents using an AI model.


Generate structured JSON incident reports.


Log processing activity and failures.


Write automated tests using pytest.

Run the demo from the incident-analyzer directory with either command:

    python -m app.model_demo
    python app\model_demo.py

The module form is recommended; the direct-file form is also supported for IDEs
that launch the current file.

Run the service demo from the incident-analyzer directory with either command:

    python -m app.service_demo
    python app\service_demo.py

The module form is recommended.

Run the mock payment API from the incident-analyzer directory:

    python -m app.mock_payment_api

With the API running, use a second terminal in the same directory to run the
JSON integration demo with either command:

    python -m app.json_integration_demo
    python app\json_integration_demo.py

Both launch forms are supported.

Phase	What we'll build
1	Project setup and folder structure
2	Payment incident data model
3	SQLite database and repository
4	Payment REST API integration
5	AI incident analysis
6	JSON report generation
7	Logging and error handling
8	Unit testing
9	End-to-end integration
10	Production-quality improvements

incident-analyzer/
│
├── .venv/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── repositories/
│   │   └── __init__.py
│   │
│   └── services/
│       └── __init__.py
│
├── tests/
│   └── __init__.py
│
├── data/
├── reports/
│
├── requirements.txt
├── .gitignore
└── README.md