'''
int
float
boolean
string

if statement

loop:
- while loop
- for loop

list
dictionary
'''

import turtle
import random
import time

from black import sanitized_lines

size = 800
wn = turtle.Screen()
wn.setup(size, size)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

food = turtle.Turtle()
food.shape('circle')
food.penup()
food.speed(0)
food.color('green')
food.goto(random.randint(-400, 400), random.randint(-400, 400))

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)
    time.sleep(0.01)

    if snake.distance(food) < 20:
        food.goto(random.randint(-400, 400), random.randint(-400, 400))
        snake.stamp()

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        pen.write('Game Over', align='center', font=('Arial', 24, 'normal'))
        break

turtle.done()