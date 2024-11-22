'''

'''
# delivery = int(input())
# collision = int(input())

# points = delivery * 50 - collision * 10

# if delivery > collision:
#     points = points + 500
    
# print(points)

import turtle
import time
import random

wn = turtle.Screen()
wn.setup(800, 800)
turtle.delay(0)

snake = turtle.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()

food = turtle.Turtle()
food.shape('circle')
food.color('green')
food.speed(0)
food.penup()
food.goto(random.randint(-350, 350), random.randint(-350, 350))

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(270), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

while True:
    snake.forward(5)
    time.sleep(0.01)

turtle.done()