import turtle
import random
import time


SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

turtle.delay(0)
# one turtle object to draw snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

food = turtle.Turtle(shape='circle')
food.penup()
food.speed(0)
food.color('green')
food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4), random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    if snake.distance(food) < 20:
        food.goto(random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4),
                  random.randint(-SCREEN_SIZE // 4, SCREEN_SIZE // 4))
        snake.stamp()
        snake.stamp()

    time.sleep(0.01)