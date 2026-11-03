import json

payment_json = """
{
    "payment_id": "PAY-10001",
    "amount": "250.00",
    "currency": "USD",
    "gateway": {
        "name": "MockGateway",
        "status": "DECLINED",
        "response_code": "51"
    }
}
"""

# Convert JSON string into Python dictionary
payment = json.loads(payment_json)

print(payment["payment_id"])
print(payment["amount"])
print(payment["gateway"]["name"])
print(payment["gateway"]["status"])
print(payment["gateway"]["response_code"])