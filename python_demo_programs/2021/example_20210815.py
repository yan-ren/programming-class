# class Person:
#     def __init__(self, name):
#         self.name = name

#     def method1(self):
#         return 'hello'


# p1 = Person('jerry')
# print(p1.name)
# Person.method1()

# class = variables + methods
# variable: static variable vs instance variable
# method: static method vs instance method
# class is customized data structure
# class is the blueprint of object, we use class to create object

class Person:
    # constructor
    def __init__(self, name, age):
        # instance variable is created in the constructor
        self.name = name
        self.age = age

    # instance method
    def say_hi(self):
        return 'hi'


p1 = Person('jerry', 10)
p2 = Person('tom', 20)
print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)

p1.say_hi()
p2.say_hi()


class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id

    def get_info(self):
        return self.student_name + ":" + str(self.student_id)

    def __str__(self):
        return self.student_name


peter = Student('peter', 1)
print(peter.get_info())
print(peter)


class Grade:
    def __init__(self):
        self.grades = []


'''
Give two dictionaries, create thrid dictionary with the unique key and value from both dictionaries

d1 = {'a': 1, 'b': 3, 'c': 2}
d2 = {'a': 2, 'b': 2, 'd': 3}

d3 = {'c': 2, 'd': 3}
'''
d1 = {'a': 1, 'b': 3, 'c': 2}
d2 = {'a': 2, 'b': 2, 'd': 3}

d3 = {}

for key1, value1 in d1.items():
    if key1 not in d2:
        d3[key1] = value1

for key2, value2 in d2.items():
    if key2 not in d1:
        d3[key2] = value2

print(d3)
