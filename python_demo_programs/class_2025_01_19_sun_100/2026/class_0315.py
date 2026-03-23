class Circle:
    # constructor: initialize instance variable
    def __init__(self, radius):
        self.radius = radius

    # instance method
    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * self.radius * 3.14

c1 = Circle(10)
c2 = Circle(20)
print(c1.area())
print(c2.area())

class MathHelper:
    # static variable
    PI = 3.1415

    def __init__(self, name):
        # instance variable
        self.name = name

    # instance method
    def circle_area(self, radius):
        return MathHelper.PI * radius ** 2

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

helper1 = MathHelper('help1')
print(helper1.name)
print(helper1.circle_area(10))

print(MathHelper.is_even(10))
print(MathHelper.PI)

class BankAccount:
    bank_name = "PyBank"
    interest_rate = 0.03

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. Balance: ${self.balance}")