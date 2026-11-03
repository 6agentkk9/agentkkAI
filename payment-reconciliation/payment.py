def calculate_fee(amount):

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return amount * 0.02