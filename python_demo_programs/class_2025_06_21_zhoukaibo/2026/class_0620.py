'''class & object

object oriented programming

In computer science, OOP is a popular programming style that organizes code around 'objects' rather that logic or functions
'''
dog_name = "Rex"
dog_age = 3
dog_breed = "Labrador"

dog2_name = "Buddy"
dog2_age = 5

# class bundles related data together with the functions that operate on it
# A class is a blueprint; an object is a thing built from that blueprint.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# dog1 = Dog()
# dog1.name = 'Rex'
# dog1.age = 2

dog1 = Dog('Rex', 2)

# dog2 = Dog()
# dog2.name = 'Buddy'
# dog2.age = 5
print(dog1.name)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grade = []

s1 = Student('Bob', 'abc')
s1.grade.append(12)
s1.grade.append(39)
