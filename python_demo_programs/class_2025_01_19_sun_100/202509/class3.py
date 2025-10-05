# def message():
#     print('Hello')
#     print('Welcome to the class')

# message()
# message()

# def message(name):
#     print('Hello', name)
#     print('Welcome to the class')
#
# message('Alice')
# message('Bob')

# def calculation(a, b):
#     # print((a-b) / (a+b))
#     result = (a - b) / (a + b)
#     return result
#
# r = calculation(2, 3)
# print(r)

'''
Write a function which takes two numbers as input, return the larger number
'''

# def compare(num1, num2):
#     if num1 > num2:
#         return num1
#         print(num1)
#     else:
#         return num2

'''
Write a function that takes a list of numbers as input, calculate the sum and return the sum
'''
# def total(numbers):
#     s = 0
#     for num in numbers:
#         s += num
#
#     return s
#
# print(total([1, 2, 3, 1, 4]))

import turtle
import time
import random


screen = turtle.Screen()
screen.setup(600, 800)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

def draw_die(x, y, value):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    # draw square
    for i in range(4):
        drawer.forward(50)
        drawer.right(90)

    # write number in the centre
    # drawer.penup()
    drawer.goto(x + 20, y - 35)
    drawer.write(value, align='center', font=('Arial', 20, 'bold'))

draw_die(10, 60, 3)
turtle.done()