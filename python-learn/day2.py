
class Payment:

    def process(self):
        print("Generic payment processing")


class CreditCardPayment(Payment):

    def process(self):
        super().process()
        print("Additional credit card validation")


payment = CreditCardPayment()
payment.process()

print("Payment example 1")


class Payment:

    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def calculate_fee(self):
        return self.amount * 0.02

    def display(self):
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Amount: {self.amount}")
        print(f"Fee: {self.calculate_fee()}")


payment = Payment(7001, 500.00)

payment.display()

print("Payment example 2")

class Payment:

    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount


payment = Payment(250.00)

print(payment.amount)

print("Payment example 3")


class Payment:

    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def calculate_fee(self):
        return self.amount * 0.02

    def display(self):
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Amount: {self.amount}")
        print(f"Fee: {self.calculate_fee()}")


payment = Payment(7001, 500.00)

payment.display()


print("Payment example 4")
