'''
topic: while loop

why do we use while loop or why do we use loop
we want to repeat some code
'''
# i = 0
# while i < 10:
#     print('hello')
#     i += 1 # i = i + 1

# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 1

import turtle

wn = turtle.Screen()
wn.setup(800, 800)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(5)
pen.color('red')

# j = 0
# while j < 18:
#     i = 0
#     while i < 4:
#         if i == 0:
#             pen.color('red')
#         elif i == 1:
#             pen.color('green')
#         elif i == 2:
#             pen.color('yellow')
#         else:
#             pen.color('blue')
#         pen.forward(100)
#         pen.left(90)
#         i += 1
#     j += 1
#     pen.left(20)

i = 0
while i < 18: # outer loop
    j = 0
    while j < 6: # inner loop - draw hexagon
        pen.forward(40)
        pen.left(60)
        j += 1
    pen.left(20)
    i += 1

turtle.done()

'''
homework:
use double loops, if statement, to make drawing of your choice
'''