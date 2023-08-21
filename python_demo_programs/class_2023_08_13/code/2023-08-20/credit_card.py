class CreditCard:
    '''
    By convension, _variable means protected value in python class
    __variable means private value in python class
    '''
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer
    

class PredatoryCreditCard(CreditCard):
    identity = "normal"

    def __init__(self, customer, bank, acnt, limit, interest):
        super().__init__(customer, bank, acnt, limit) # call the parent constructor
        self._interest = interest

    def get_interest(self):
        return self._interest
    

credit_card = CreditCard("A", "ABC", 123, 1000)
credit_card._customer # not encourage, since _customer is defined as protected
credit_card.get_customer()

# iterator example
class Progression:
    def __init__(self, start = 0):
        self._current = start

    def __next__(self):
        '''return the next element, or else raise Exception to tell stop looping'''
        if self._current is None:
            raise StopIteration()
        else:
            value = self._current
            self._current += 1
            return value
    
    def __iter__(self):
        '''by convention, an iterator must return itself as iterator'''
        return self


p = Progression()
for value in p:
    print(value)

