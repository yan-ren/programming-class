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

colors = ['red', 'green', 'blue']

food = turtle.Turtle()
food.shape('circle')
food.color(random.choice(colors))
food.speed(0)
food.penup()
food.goto(random.randint(-350, 350), random.randint(-350, 350))

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(270), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

# if food.pencolor() == 'red':

score = 0

# Create turtle object for writing
writing = turtle.Turtle()
writing.penup()
writing.hideturtle()
writing.goto(-380, 380)
writing.write('Score: ' + str(score), font=('Arial', 12, 'normal'))

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1) # clear the oldest stamp
    time.sleep(0.01)

    if snake.distance(food) < 20:
        food.goto(random.randint(-350, 350), random.randint(-350, 350))
        snake.stamp()
        snake.stamp()
        score += 1
        writing.clear()
        writing.write('score:' + str(score), font=('Arial', 12, 'normal'))

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        break

turtle.done()

'''
challenge
1. how to add border control
2. score
3. when game over, show some text
4. create different food, for different score
5. randomized the color of the food
'''