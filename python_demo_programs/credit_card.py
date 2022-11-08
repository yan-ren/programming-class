class CreditCard:

    def __init__(self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed. false if charge was denied
        """
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        self.balance -= amount



