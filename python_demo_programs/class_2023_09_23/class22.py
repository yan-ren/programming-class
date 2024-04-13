'''
1. create a Student class that stores each student info, e.g. name, age, grade
2. create a Classroom class, which has a list to store multiple student object created in step1.
    - write a function in Classroom to return the oldest student
    - write a function in Classroom to return the youngest student
    - option: write a function to return the student name start with a given letter
'''
class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Classroom():
    def __init__(self):
        self.students = []

    def youngest_student(self):
        youngest = self.students[0].age
        for student in self.students:
            if student.age < youngest:
                youngest = student.age

        return youngest

    def oldest_student(self):
        oldest = self.students[0].age
        for student in self.students:
            if student.age > oldest:
                oldest = student.age

        return oldest

    def name_start_with(self, letter):
        for student in self.students:
            if student.name[0] == letter:
                print(student.name)


# s1 = Student('a', 12, grade=12)
# s2 = Student('b', 13, grade=13)
# classroom = Classroom()
# classroom.students.append(s1)
# classroom.students.append(s2)
# print(classroom.youngest_student())
# print(classroom.name_start_with('a'))

import math
# math.pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius**2

    def calculate_circle_perimeter(self):
        return math.pi * self.radius * 2



# circle1 = Circle(2)
# circle2 = Circle(4)
# print(circle1.calculate_circle_area())
# print(circle2.calculate_circle_area())

class Calculator:
    def __init__(self):
        self.basic_saving_interest = 0.01
        self.smart_saving_interest = 0.015
        self.premium_saving_interest = 0.02
        self.tax = 0.05

    def save_with_basic(self, amount, year):
        return self.apply_tax(amount*self.basic_saving_interest*year) + amount
        # return amount*self.basic_saving_interest*year + amount

    def save_with_smart(self, amount, year):
        return self.apply_tax(amount*self.smart_saving_interest*year) + amount

    def save_with_premium(self, amount, year):
        return self.apply_tax(amount*self.premium_saving_interest*year) + amount

    def apply_tax(self, amount):
        return amount*(1-self.tax)

'''
Create a python class called Food, include food name, price
Create another class called ShoppingCart, include method of adding,
and calculate the total food price in shopping cart
'''
class Food:
    def __init__(self, name, price):
        self.food_name = name
        self.food_price = price


class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add_food(self, food):
        self.cart.append(food)
    def checkout(self):
        total_price = 0
        for food in self.cart:
            # total_price += food.food_price
            total_price = total_price + food.food_price

        return total_price

apple = Food('apple', 10)
banana = Food('banana', 12)
cart = ShoppingCart()
cart.add_food(apple)
cart.add_food(banana)
print(cart.checkout())