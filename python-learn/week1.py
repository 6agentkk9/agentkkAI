print("Hello KK")



class Payment:

    def process(self):
        print("Processing payment")


class CreditCardPayment(Payment):

    def validate_card(self):
        print("Validating card")


payment = CreditCardPayment()

payment.process()
payment.validate_card()


class Payment:

    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount


payment = Payment(250.00)

print(payment.get_amount())