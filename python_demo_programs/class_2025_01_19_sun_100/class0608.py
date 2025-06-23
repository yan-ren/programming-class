'''
conditional
if elif else

loop
- while
- for
'''
import random
# function
# def message():
#     print('Hello')
#     print('Welcome')
#
# message()
# message()
#
# def add(a, b):
#     return a + b
#
# print(add(1, 2))
# print(add(3, 1))

# def say_hello(name):
#     print('Hello', name)

# say_hello('Alice')
# say_hello('Bob')
#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(7))
# print(is_even(12))

# exercise: Write a function count_vowels(text) that returns the number of vowels in the string.
# count_vowels("hello")  # Expected: 2
# def count_vowels(word):
#     count = 0
#     for letter in word:
#         if letter in 'aeiou':
#             count += 1
#     return count
#
# print(count_vowels('hello'))
# print(count_vowels('hi'))

# exercise: Write a function reverse_string(s) that returns the reversed string.
# e.g. reverse_string("python")  # Expected: "nohtyp"
# def reverse_string(word):
#     # return word[::-1]
#     re = ''
#     i = len(word) - 1
#     while i >= 0:
#         re += word[i]
#         i -= 1
#
#     return re

import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_circle_in_square(size):
    draw_square(size)


def draw_pattern():
    turtle.bgcolor('black')
    turtle.pensize(2)
    turtle.speed(0)

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    for i in range(36):
        turtle.color(random.choice(colors))
        draw_circle_in_square(100)
        turtle.right(10)

    turtle.hideturtle()

draw_pattern()
turtle.done()
