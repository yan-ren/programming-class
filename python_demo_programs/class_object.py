# import math
#
#
# class Car:
#     #
#     def __init__(self, brand, color, year, price):
#         self.brand = brand
#         self.color = color
#         self.year = year
#         self.price = price
#
#     def __str__(self):
#         return 'brand: ' + self.brand + ' year: ' + str(self.year)
#
#
#     '''
#     magic method
#
#     is a group of reserved method that has special features
#     '''
#
# class Dealer:
#     def __init__(self):
#         self.cars = []
#
#     def add_car(self, car):
#         self.cars.append(car)
#
#     def get_car_above_price(self, price):
#         return [car for car in self.cars if car.price > price]
#
#     # def get_brand_average(self, brand):
#
#
#
# '''
# write a class called Dealer
#
# Dealer class contains a list of cars
# write two functions, first function is call add_car, which add a car object to the list
# write a function called get_car_above_price(price)
#
# '''
# car1 = Car('toyota', 'black', 2022, 53000)
# car2 = Car('honda', 'red', 2021, 43000)
# print(car1)
#
# dealer = Dealer()
# dealer.add_car(car1)
# dealer.add_car(car2)
# for car in dealer.cars:
#     print(car)
#
# print([car.brand for car in dealer.cars])
# print(dealer.get_car_above_price(20000))
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return 'x: ' + str(self.x) + ", y: " + str(self.y)
#
#     def rotate_90_cc(self):
#         self.x, self.y = -self.y, self.x
#
#
# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1 + p2)
#
# '''
# write a class called Person, with first_name, last_name as non-static variables
# and write a non-static method called print_name which prints the first name and last name
# '''
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_name(self):
#         print(self.first_name, self.last_name)
#
#
# class Student(Person):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.graduation_year = 2019
#
#     def print_graduation(self):
#         print(self.graduation_year)
#
#
# student = Student('tom', 'steve')
# print(student.first_name)
# print(student.last_name)
# print(student.graduation_year)
# student.print_name()
#
#
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.no_of_sides = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def input_sides(self):
#         self.sides = [float(input('Enter side ' + str(i+1) + ' : ')) for i in range(self.no_of_sides)]
#
#     def display_sides(self):
#         for i in range(self.no_of_sides):
#             print('Side', i+1, 'is', self.sides[i])
#
#
# class Triangle(Polygon):
#     def __init__(self):
#         super().__init__(3)
#
#     def find_area(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#         return area
#
#
# polygon = Polygon(4)
# print(polygon.sides)
# polygon.input_sides()
# polygon.display_sides()
#

# from abc import abstractmethod


# class Car:
#     brand = "toyota"
#     # magic function
#     def __init__(self, year, color):
#         # non-static variable has to be in constructor
#         self.year = year
#         self.color = color

#     def print_number(self, number):
#         number += 1

#     def print_color(self):
#         print(self.color)

#     def __str__(self):
#         return str(self.color) + ":" + str(self.year)

#     def __gt__(self, car):
#         return self.year > car.year

#     def __lt__(self, car):
#         return self.year < car.year

#     def __eq__(self, car):
#         return self.year == car.year and self.color == car.color


# car1 = Car(2021, 'red')
# car2 = Car(2020, 'black')
# if car1 < car2:
#     print('car1 is old car')
# else:
#     print('car2 is old car')

# if car1 > car2:
#     print('car1 is new car')
# else:
#     print('car2 is new car')



# class Toyota(Car):

#     def __init__(self, year, color):
#         super().__init__(year, color)

#     def print(self, msg = "hello"):
#         print(msg)

#     @abstractmethod
#     def abs_method(self):
#         pass


# car = Car(1000, 'red')
# print(car.color)
# car.print_color()
# # car.print_number("123")
# print(car)
# print(Car.brand)


# toyota = Toyota('red', 123)
# toyota.print()
# # toyota._Toyota__print()
# '''
# all members in python class are public by default
# '''

# def method(number=1):
#     print(number)


# method(10)
# method()

l = [1, 2, 3, 4]
res = []

for number in l:
    # ** => number^2
    res.append(number**2)

print(res)

# list comprehension
res = [number**2 for number in l]
print(res)
res = [abs(i) for i in l]
[i if i > 0 else -i for i in l]

for i in l:
    if i > 0:
        res.append(i)
    else:
        res.append(-i)

number = [-1, -2, 0, 1, 2]
# res = [n if n > 0 for n in number]
print(res)
'''
[expression for item in list]
'''