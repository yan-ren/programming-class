import turtle
import random
import time

SCREEN_SIZE = 800
window = turtle.Screen()
window.setup(SCREEN_SIZE, SCREEN_SIZE)

# one turtle for snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.penup()

# add keyboard control
turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

def get_random_value():
    return random.randint(-SCREEN_SIZE / 4, SCREEN_SIZE/4)


# turtle object to draw the food
food = turtle.Turtle(shape='circle')
food.penup()
food.speed(0)
food.color('green')
food.goto(get_random_value(), get_random_value())


while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    # when snake gets food
    if snake.distance(food) < 20:
        food.goto(get_random_value(), get_random_value())
        snake.stamp()

    if snake.xcor() < -SCREEN_SIZE/2 or snake.xcor() > SCREEN_SIZE/2 or snake.ycor() < -SCREEN_SIZE/2 or snake.ycor() > SCREEN_SIZE/2:
        break

    time.sleep(0.01)


turtle.done()
