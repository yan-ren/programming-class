from credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, rate):
        super().__init__(customer, bank, account, limit)
        self.rate = rate

   def charge(self, price) :
       success = super().charge(price)
       if not success:
           self.balance += 5
       return success

   def process_month(self):
       if self.balance > 0:
           self.balance = self.rate * self.balance + self.balance

for x, y in [(7,2), (5, 8), (6, 4)]:
    print(x, y)

a, b, c, d = range(7, 11)
print(a, b, c, d)