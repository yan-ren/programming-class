'''
pygame + oop
python project
web development
- backend: python, java, typescript, etc
- frontend: typescript + react
'''
'''
class
object
'''
class Dog:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog('Bob', 3)
dog2 = Dog('Catty', 1)

print(dog1.name)
print(dog1.age)
print(dog2.name)
dog2.name = 'Dude'

# Student
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age


class Classroom:
    def __init__(self):
        self.students = []
        self.teachers = []

math_classroom = Classroom()
s1 = Student('Alice', 10, 11)
s2 = Student('Bob', 10, 10)

math_classroom.students.append(s1)
math_classroom.students.append(s2)

for student in math_classroom.students:
    if student.age > 10:
        print(student.name)

