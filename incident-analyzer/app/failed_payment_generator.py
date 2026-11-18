# payments = [
#     {"payment_id": "PAY-1001", "status": "SUCCESS"},
#     {"payment_id": "PAY-1002", "status": "FAILED"},
#     {"payment_id": "PAY-1003", "status": "FAILED"},
#     {"payment_id": "PAY-1004", "status": "SUCCESS"},
# ]

payments = [
        {"payment_id": "PAY-1001", "status": "SUCCESS", "amount": 100},
        {"payment_id": "PAY-1002", "status": "FAILED", "amount": 250},
        {"payment_id": "PAY-1003", "status": "FAILED", "amount": 150},
        {"payment_id": "PAY-1004", "status": "SUCCESS", "amount": 300},
        {"payment_id": "PAY-1005", "status": "FAILED", "amount": 50},
    ]

def iter_failed_payments(payments):
    # Your implementation here
    for payment in payments:
        if payment["status"] == "FAILED":
            yield payment

    for payment in iter_failed_payments(payments):
        print(payment["payment_id"])

    # Task 1
    print("Task 1, List comprehension: Failed Payment IDs")
    failed_payment_ids = [
        p["payment_id"]
        for p in payments
        if p["status"] == "FAILED"
    ]
    print(failed_payment_ids)

    # Task 2
    print("Task 2, Dictionary comprehension: Payment Amounts")
    payment_amounts = {
        p["payment_id"]: p["amount"]
        for p in payments
    }
    print(payment_amounts)

    # Task 3
    print("Task 3, Set comprehension: Unique Statuses")
    unique_statuses = {
        p["status"]
        for p in payments
    }
    print(unique_statuses)