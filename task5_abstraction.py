class Payment:

    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print("Credit Card payment of", amount)


class UPIPayment(Payment):

    def process_payment(self, amount):
        print("UPI payment of", amount)


p1 = CreditCardPayment()
p2 = UPIPayment()

p1.process_payment(1000)
p2.process_payment(500)