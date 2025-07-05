'''
function/method

def
'''
# def message(name):
#     print("Welcome", name)
#     print("Today is Saturday")
#
#
# message('Jack')
# message('Jenny')
#
#
# def addition(a, b):
#     return a + b
#
#
# result = addition(1, 2)
# print(result)

# exercise: write a function which takes a list of numbers as input and return the max number in the list
# def max_num(l):
#     max = l[0]
#     min = l[0]
#     for value in l:
#         if value > max:
#             max = value
#         if value < min:
#             min = value
#
#     return max, min
#
# numbers = [4, 2, 1, 5]
# a, b = max_num(numbers)

import turtle
import random


screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.setup(800, 800)
player = turtle.Turtle()
player.shape('turtle')
player.speed(0)

coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.goto(random.randint(-200, 200), random.randint(-200, 200))

def go_up():
    if -400 < player.xcor() < 400 and -400 < player.ycor() < 400:
        player.setheading(90)
        player.forward(20)
    check_collision()

def go_down():
    player.setheading(270)
    player.forward(20)
    check_collision()

def go_left():
    player.setheading(180)
    player.forward(20)
    check_collision()

def go_right():
    player.setheading(0)
    player.forward(20)
    check_collision()

def check_collision():
    if player.distance(coin) < 50:
        coin.goto(random.randint(-200, 200), random.randint(-200, 200))

screen.listen()
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')

screen.mainloop()