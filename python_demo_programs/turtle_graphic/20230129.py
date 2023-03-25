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

turtle.onkeypress(lambda: snake.setheading(90), "Up")
turtle.onkeypress(lambda: snake.setheading(-90), "Down")
turtle.onkeypress(lambda: snake.setheading(180), "Left")
turtle.onkeypress(lambda: snake.setheading(0), "Right")
turtle.listen()


def get_random_value():
    return random.randint(-SCREEN_SIZE/4, SCREEN_SIZE/4)


# one turtle object to draw food
food = turtle.Turtle(shape="circle")
food.penup()
food.speed(0)
food.color("green")
food.goto(get_random_value(), get_random_value())


while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)

    # when snake gets the food
    if snake.distance(food) < 20:
        food.goto(get_random_value(), get_random_value())
        snake.stamp()

    # add boarder condition
    if snake.xcor() >= SCREEN_SIZE/2 or snake.xcor() <= -SCREEN_SIZE/2 or snake.ycor() >= SCREEN_SIZE/2 or snake.ycor() <= -SCREEN_SIZE/2:
        break

    snake.xcor()
    snake.ycor()
    snake.pos()

    time.sleep(0.01)


snake.penup()
snake.goto(0, SCREEN_SIZE/4)
snake.color("black")
snake.write("Game Over!", align="center", font=("Verdana", 24, "normal"))
turtle.exitonclick()
