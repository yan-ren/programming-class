'''
OOP: Object Oriented Programming
'''
class Car:
    # constructor
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = 2020
        self.color = 'red'

    def start(self):
        print('car starts')

    @staticmethod
    def test():
        print('test function')





c1 = Car('toyota')
print(c1.brand)

c2 = Car('mazda')

c3 = Car('honda')
print(c3.brand)
c3.start() # nonstatic/instance method
Car.test() # static method