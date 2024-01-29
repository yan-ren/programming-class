import turtle
import time


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

while True:
    snake.forward(5)
    time.sleep(0.01)

turtle.done()
