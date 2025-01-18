# a = 0
#
# while a == 0:
#     print(a)

# i = 0
#
# while i < 10:
#     print(i)
#     i = i + 1 # i += 1

i = 0

# while i < 20:
#     print(i)
#     i += 2

# while i < 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

import turtle

screen = turtle.Screen()
screen.setup(600, 800)

pen = turtle.Turtle()

i = 0
while i < 5:
    pen.forward(100)
    pen.right(144)
    i += 1

# j = 0
# while j < 360/15:
#     i = 0
#     while i < 4:
#         if i == 0:
#             pen.color('red')
#         elif i == 1:
#             pen.color('yellow')
#         elif i == 2:
#             pen.color('blue')
#         else:
#             pen.color('green')
#         pen.forward(100)
#         pen.left(90)
#         i += 1
#     pen.left(15)
#     j += 1

turtle.done()


