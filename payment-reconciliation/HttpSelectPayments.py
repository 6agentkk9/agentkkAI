#  Activate the virtual environment and service
# .\.venv\Scripts\Activate.ps1
# python -m pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)
print(response.text)


# Full test

# Use this public test API:

# https://jsonplaceholder.typicode.com/todos/1

# Write a program that:
# 1. Makes a GET request.
# 2. Uses a 10-second timeout.
# 3. Checks the HTTP status.
# 4. Parses the JSON response.
# 5. Prints the id, title, and completed fields.
# 6. Handles HTTP and connection errors.

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    todo = response.json()

    print("ID:", todo["id"])
    print("Title:", todo["title"])
    print("Completed:", todo["completed"])

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)