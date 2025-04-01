import turtle
import random
import time
import winsound

SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

turtle.delay(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()

food = turtle.Turtle(shape='circle')
food.penup()
food.speed(0)
food.goto(random.randint(-200, 200), random.randint(-200, 200))


turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

running = True
while running:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)
    if snake.distance(food) < 20:
        winsound.Beep(600, 500)
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        snake.stamp()
        snake.stamp()

    time.sleep(0.01)