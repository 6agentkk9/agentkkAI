from decimal import Decimal


class PaymentError(Exception):
    pass


class RefundValidationError(PaymentError):
    # Implement here
    pass


# def validate_refund(payment_id, refund_amount):

#     if refund_amount <= Decimal("0"):
#         raise RefundValidationError(
#             payment_id=payment_id,
#             refund_amount=refund_amount,
#             message="Refund amount must be positive"
#         )

def validate_refund(
    payment_id: str | None,
    amount: Decimal
) -> bool:
    if not payment_id:
        raise ValueError("Payment ID is required")

    if amount <= Decimal("0"):
        raise ValueError("Amount must be positive")

    if amount > Decimal("10000"):
        raise ValueError("Refund exceeds maximum limit")

    return True
