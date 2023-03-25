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
# add keyboard control
turtle.onkeypress(lambda: snake.setheading(90), "Up")
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()

def get_random_value():
    return random.randint(-SCREEN_SIZE / 4, SCREEN_SIZE / 4)


# turtle object to draw food
food = turtle.Turtle(shape="circle")
food.penup()
food.speed(0)
food.color("green")
food.goto(get_random_value(), get_random_value())

def main_game_loop():
    while True:
        snake.forward(5)
        snake.stamp()
        snake.clearstamps(1)

        # when snake gets food
        if snake.distance(food) < 20:
            food.goto(get_random_value(), get_random_value())
            # make additional stamp mark, so snake is longer when gets the food
            snake.stamp()
            snake.stamp()

        time.sleep(0.01)


turtle.onkeypress(main_game_loop, "space")
turtle.exitonclick()
