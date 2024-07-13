'''
loop:
while loop
for loop
'''
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# import time
#
# # count down
# i = 3600
# while i > 0:
#     print(i)
#     i = i - 1
#     time.sleep(1)

# infinite loop
# while True:
#     print(1)
#

# import turtle
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
#
# j = 0
# while j < 36:
#     i = 0
#     while i < 4:
#         if i == 0:
#             t.color('red')
#         elif i == 1:
#             t.color('green')
#         elif i == 2:
#             t.color('yellow')
#         else:
#             t.color('purple')
#         t.forward(100)
#         t.left(90)
#         i = i + 1
#     j = j + 1
#     t.left(10)

# turtle.done()

# i = 0
# while i < 3:
#     j = i
#     while j < 3:
#         print(j)
#         j = j + 1
#     i = i + 1

# row = 1
# while row <= 4:
#     col = 1
#     while col <= row:
#         print('*', end='')
#         col = col + 1
#     print()
#     row = row + 1
#
# row = 1
# while row <= 4:
#     col = 1
#     while col <= 4 - row:
#         print('*', end='')
#         col = col + 1
#     print()
#     row = row + 1

'''
exercise 1:
using loop to calculate the sum from 1 to 100, e.g. 1+2+3+...+99+100

exercise 2:
using loop to show all even numbers under 100
'''

import turtle
import random


wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

colors = ['red', 'yellow', 'blue', 'green']

i = 0
while i < 36:
    t.color(colors[i % len(colors)])
    t.forward(100)
    t.backward(100)
    t.left(10)
    i = i + 1

turtle.done()