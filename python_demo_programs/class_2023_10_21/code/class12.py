import turtle
import time
import random


wn = turtle.Screen()
wn.setup(800, 800)
turtle.delay(0)

# create snake on the screen
snake = turtle.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()

# add keyboard control
turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(270), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

def get_random_value():
    return random.randint(-300, 300)

# create food on the screen
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape('circle')
food.color('green')
food.goto(get_random_value(), get_random_value())

score = 0

# create turtle object for writing score
writing = turtle.Turtle()
writing.penup()
writing.hideturtle()
writing.goto(-380, 380)
writing.write("score: " + str(score), font=('Arial', 12, 'normal'))


while True:
    time.sleep(0.01)

    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    # when snake gets the food
    if snake.distance(food) < 20:
        score += 1
        food.goto(get_random_value(), get_random_value())
        snake.stamp()
        snake.stamp()
        writing.clear()
        writing.write("score: " + str(score), font=('Arial', 12, 'normal'))

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        writing.goto(-200, 0)
        writing.write("Game Over", font=('Arial', 12, 'normal'))
        writing.goto(-200, -50)
        writing.write("Your score:" + str(score), font=('Arial', 12, 'normal'))
        break


turtle.done()
