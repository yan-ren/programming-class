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
    drawer.penup()
    drawer.goto(x + 20, y - 35)
    drawer.write(value, align='center', font=('Arial', 20, 'bold'))

draw_die(10, 60, 3)
turtle.done()

'''
write a function that takes a list of numbers as input, and return a new list with only positive values

e.g.

input: [1, -2, 3, -1]
output: [1, 3]
'''
def filter_positive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)

    return result

print(filter_positive([1, 2, -1, -2]))