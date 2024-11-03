#
# running = True
# sum = 0
# count = 0
# while running:
#     text = input('Enter a number or exit: ')
#     # print(text)
#
#     if text == 'exit':
#         running = False
#     else:
#         sum += int(text)
#         count += 1
#
#
# print(sum / count)

'''
Ask user to input numbers, if user types 'exit' the program stops and print the sum of all numbers 
that user has entered so far
'''

# import turtle
#
#
# screen = turtle.Screen()
# screen.setup(600, 800)
#
# pen = turtle.Turtle()
#
# j = 0
# while j < 360 / 15:
#     i = 0
#     while i < 4:
#         if i == 0:
#             pen.color('red')
#         elif i == 1:
#             pen.color('yellow')
#         elif i == 2:
#             pen.color('green')
#         else:
#             pen.color('blue')
#         pen.forward(100)
#         pen.left(90)
#         i += 1
#     pen.left(15)
#     j += 1
#
# turtle.done()

# given a number check if it's prime or not

import math


number = 1

while number <= 100:
    i = 2
    is_prime = True

    while i <= math.sqrt(number):
        if number % i == 0:
            is_prime = False
        i += 1

    if is_prime:
        print(number)

    number += 1

'''
ask user to enter number until user types 'exit'
when user types exit, print the largest number that user has typed in
'''