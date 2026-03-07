class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return self.name + " says: woof!"

    def is_adult(self):
        if self.age >= 3:
            return True
        else:
            return False

    def feed(self, food):
        if food == 'meat':
            return True
        else:
            return False

dog = Dog('Bob', 3)
print(dog.name)
print(dog.age)
print(dog.bark())
print(dog.is_adult())
print(dog.feed('meat'))

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append(-amount)

    def get_statement(self):
        return f'Account: {self.owner}, balance: {self.balance}'

account = BankAccount('Alice', 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_statement())

# static variable / class variable vs non-static / instance variable
class Employee:
    # class variable
    company = 'TechCorp'

    def __init__(self, name, salary):
        # instance variable
        self.name = name
        self.salary = salary


employee1 = Employee('Alice', 90000)
print(employee1.salary)
print(Employee.company)

class Student:
    school_name = 'Python academy'

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


s1 = Student('Alice', 6, 12)
s2 = Student('Bob', 7, 13)
print(s1.name)
print(s2.name)
print(Student.school_name)
print(s1.school_name)
print(s2.school_name)

# write a Temperature class that takes celsius values and write a instance function that can convert celsius to fahrenheit
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    # todo