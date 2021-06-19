# class Pizza:
#     def __init__(self, radius, toppings, slices=8):
#         self.radius = radius
#         self.toppings = toppings
#         self.slices = slices
#
#
# # construct __init__ is special type method
# pizza = Pizza(10, 2, 6)
# pizza1 = Pizza(10, 2)
#
# class Dog:
#     kind = 'Canine'
#
#     def __init__(self, name):
#         self.name = name
#
#
# a = Dog('Astro')
# b = Dog('Buddy')
# print(a.kind)
# print(b.kind)
# print(Dog.kind)
#
# # Dog.kind = "wild"
# # print(a.kind)
# # print(b.kind)
# # print(Dog.kind)
#
# # a new instance variable in a gets created
# # a.kind = "wild"
# # a.age = 4
# # print(a.kind)
# # print(a.age)
# #
# # print(b.kind)
# # print(b.age)
# # print(Dog.kind)
#
# class Dog:
#
#     def __init__(self, name):
#         self._name = name
#         self.tricks = []
#
#     def get_name(self):
#         return self._name
#
#     def teach_trick(self, trick):
#         self.tricks.append(trick)
#
#     def __str__(self):
#         return self._name + str(self.tricks)
#
#
# a = Dog('fido')
# b = Dog('buddy')
# a.teach_trick('roll over')
# b.teach_trick('sit')
# print(a)
# print(b)

'''
write a recursive function that check if a string is palindrome
palindrome is a word that read the same no matter from left to right or right to left
example:
kayak -> True
racecar -> True
civic -> True
'''
'''
kayak -> k + aya + k
aya -> a + y + a
y -> palindrome? yes

abba -> a + bb + a
bb -> b + b
'''
# def check_panlindrome(str):
#     if len(str) == 1:
#         return True
#     elif len(str) == 2:
#         return str[0] == str[1]
#
#     return str[0] == str[len(str) - 1] and check_panlindrome(str[1:len(str)-1])
#
#
# str = 'abba'
# print(check_panlindrome(str))

'''
customized objects are allowed in Python
in order to create customized objects, you need to write class first,
all objects are created from class
'''
'''
class can contain variables(static vs non-static) and methods
static variable == class variable
non-static variable == instance variable
'''
'''
static variable belong to the class, to access static variable, use class name
non-static variable has to be created in constructor, with self
self is used to represent the instance of the class, we can access the attributes and methods of the class
'''
class Car:
    model = 'toyota'

    def __init__(self, year, color):
        self.year = year
        self.color = color

    def print_car_info(self):
        print(str(self.year) + ":" + self.color)

'''
constructor, __init__ is used when creating objects, for initializing variable
when creating objects, non-static variable is created inside __init__
to use non-static variable, need to use it by object
'''
a = Car(2021, "red")
print(a.year)
a.print_car_info()

b = Car(2020, "blue")
b.print_car_info()

'''
Write a class called Person, inside class put two non-static variables, name and age
write a method called get_person_info, which returns the name together with the age
'''


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_person_info(self):
        return self.name + ":" + str(self.age)
