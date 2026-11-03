import requests


def get_payment(payment_id):

    response = requests.get(
        f"https://api.example.com/payments/{payment_id}",
        timeout=10
    )

    response.raise_for_status()

    return response.json()