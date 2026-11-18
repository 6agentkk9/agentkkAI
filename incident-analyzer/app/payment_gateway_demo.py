from os import name
from typing import Protocol
from decimal import Decimal

# 1. Define the contract
class PaymentGateway(Protocol):

    def authorize(self, payment_id: str, amount: Decimal) -> str:
        ...

    def refund(self, payment_id: str, amount: Decimal) -> str:
        ...

# 2. Implement the contract without inheritance
class MockPaymentGateway:

    def authorize(self, payment_id: str, amount: Decimal) -> str:
        print(f"Authorizing {payment_id}: {amount}")
        return "MOCK_APPROVED"


    def refund(self, payment_id: str, amount: Decimal) -> str:
        print(f"Refunding {payment_id}: {amount}")
        return "MOCK_REFUNDED"

# 3. Implement declining gateway
class DecliningGateway:

    def authorize(self, payment_id: str, amount: Decimal) -> str:
        print(f"Declining {payment_id}: {amount}")
        return "DECLINED"


# 4. Dependency injection
class PaymentService:

    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def process_payment(
        self,
        payment_id: str,
        amount: Decimal
    ) -> str:

        return self.gateway.authorize(payment_id, amount)


# 5. Factory pattern
class GatewayFactory:

    @staticmethod
    def create_gateway(name: str) -> PaymentGateway:

        if name == "mock":
            return MockPaymentGateway()

        if name == "declining":
            return DecliningGateway()

        raise ValueError(f"Unknown gateway: {name}")


# 6. Execute
mock_gateway = GatewayFactory.create_gateway("mock")
declining_gateway = GatewayFactory.create_gateway("declining")

mock_service = PaymentService(mock_gateway)
declining_service = PaymentService(declining_gateway)

amount = Decimal("125.50")

print(
    mock_service.process_payment("PAY-20001", amount)
)

print(
    declining_service.process_payment("PAY-20001", amount)
)
