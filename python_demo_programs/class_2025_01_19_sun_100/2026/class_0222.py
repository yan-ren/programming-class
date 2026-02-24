'''
OOP: object oriented programming
'''
from python_demo_programs.class_2024_04_27.class6 import names
from python_demo_programs.class_2025_09_13_leshui.class7 import grades


# import pygame.examples.aliens as game
#
# game.main()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog = Dog('Bob', 12)
print(dog.name)
print(dog.age)

dog2 = Dog('Charlie', 9)
print(dog2.name)
print(dog2.age)
dog2.name = 'Tom'

# create a class about student
class Student:
    def __init__(self, name, grade, iq):
        self.name = name
        self.grade = grade
        self.iq = iq

s1 = Student('Bob', 9, 100)
s2 = Student('Alice', 10, 89)
class Classroom:
    def __init__(self):
        self.students = []

classroom1 = Classroom()
classroom1.students.append(s1)
classroom1.students.append(s2)

# find the student with highest iq, hint: loop through students list in classroom and check each student's iq