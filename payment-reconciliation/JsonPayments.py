# Function	Input
# json.dumps()	Python object → JSON string
# json.loads()	JSON string → Python object
# json.dump()	Python object → JSON file
# json.load()	JSON file → Python object

# Convert Python dictionary to JSON
import json

payment = {
    "paymentId": 1001,
    "amount": 250.50,
    "status": "SUCCESS"
}

json_data = json.dumps(payment)

print(json_data)
print(type(json_data))


# Convert JSON to Python dictionary
import json

json_data = """
{
    "paymentId": 1001,
    "amount": 250.50,
    "status": "SUCCESS"
}
"""

payment = json.loads(json_data)

print(payment["paymentId"])
print(payment["amount"])
print(payment["status"])


#Handle nested JSON
payment = {
    "paymentId": 1001,
    "amount": 250.50,
    "customer": {
        "customerId": 501,
        "name": "John"
    },
    "transactions": [
        {
            "transactionId": "TX100",
            "status": "SUCCESS"
        },
        {
            "transactionId": "TX101",
            "status": "FAILED"
        }
    ]
}

print(payment["customer"]["name"])

for transaction in payment["transactions"]:
    print(
        transaction["transactionId"],
        transaction["status"]
    )



# 1. Parse the JSON string.
# 2. Print the batch ID.
# 3. Print only failed transaction IDs.
# 4. Calculate the total amount of failed transactions.
import json

json_data = """
{
    "batchId": "BATCH100",
    "transactions": [
        {"id": 1001, "amount": 250.50, "status": "SUCCESS"},
        {"id": 1002, "amount": 175.00, "status": "FAILED"},
        {"id": 1003, "amount": 300.00, "status": "FAILED"}
    ]
}
"""

batch = json.loads(json_data)

print("Batch ID:", batch["batchId"])

failed_total = 0

for transaction in batch["transactions"]:

    if transaction["status"] == "FAILED":

       print("Failed transaction:", transaction["id"], "Amount:", transaction["amount"])
       print(f"Failed transaction: {transaction['id']} Amount: {transaction['amount']}")
       failed_total += transaction["amount"]

print("Total failed amount:", failed_total)