class Student:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def print_name(self):
        print(self.name)

    def study(self):
        print('Student is studying')


class SeniorStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age, 'senior')
        self.online_classes = []

    def study(self):
        print('Senior student is studying')

class JuniorStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age, 'junior')
        self.in_person = []

s1 = SeniorStudent('Alice', 19)
j1 = JuniorStudent('Bob', 12)
s1.print_name()
j1.print_name()
s1.study()

# exercise 1, add school name

# exercise 2, count classes

# exercise add exchange student
class ExchangeStudent(Student):
    def __init__(self, name, age, country):
        super().__init__(name, age, 'exchange')
        self.country = country


class School:
    def __init__(self):
        self.students = []

    # add a function count how many senior, junior, and exchange


'''
list slicing
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:5])