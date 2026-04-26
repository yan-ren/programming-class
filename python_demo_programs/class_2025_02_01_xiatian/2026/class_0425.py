# class BankAccount:
#     # static variable
#     bank_name = 'Python Bank'
#
#     def __init__(self, owner, balance=0):
#         self.owner = owner # instance variable
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{self.owner} deposited ${amount}. Balance: ${self.balance}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print('Insufficient funds.')
#         else:
#             self.balance -= amount
#             print(f'{self.owner} withdraw ${amount}. Balance: ${self.balance}')
#
#     def __str__(self):
#         return f'{BankAccount.bank_name} {self.owner}: balance: {self.balance}'
#
#
# tom_account = BankAccount('Tom', 10)
# print(tom_account.balance)
# print(tom_account.bank_name)
#
# jerry_account = BankAccount('Jerry')
# print(jerry_account.balance)
# print(jerry_account.bank_name)
#
# print(BankAccount.bank_name)
# BankAccount.bank_name = 'Python 3 bank'
#
# print(tom_account)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f'{self.name} says: Woof!'

    def fetch(self):
        return f'{self.name} fetches the ball!'


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def purr(self):
        return f"{self.name} purrs..."

d = Dog('Rex', 3, 'Labrador')
c = Cat('Luna', 5, True)

print(d.speek())
print(c.speak())
print(d.description())
print(d.fetch())
print(c.purr())
