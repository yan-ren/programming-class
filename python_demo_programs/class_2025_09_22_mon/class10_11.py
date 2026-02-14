import turtle
import time
import random

screen_size = 800
wn = turtle.Screen()
wn.setup(screen_size, screen_size)

turtle.delay(0)
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

food = turtle.Turtle()
food.shape('circle')
food.color('green')
food.speed(0)
food.penup()
food.goto(random.randint(-screen_size//4, screen_size//4), random.randint(-screen_size//4, screen_size//4))

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

score = 0

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-screen_size//4, screen_size//4), random.randint(-screen_size//4, screen_size//4))
        snake.stamp()
        score = score + 1
        pen.goto(350, 350)
        pen.write(score)

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        pen.write('Game Over!', align='center', font=('Verdana', 24, 'normal'))
        break

    time.sleep(0.01)

turtle.done()

'''
after class: try to show the score on the screen
'''