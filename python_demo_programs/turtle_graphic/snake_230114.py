import turtle
import random

SIZE = 800

window = turtle.Screen()
window.setup(SIZE, SIZE)
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()

food = turtle.Turtle()
food.hideturtle()
food.color("green")
food.shape("square")
food.penup()
food.setx(random.randint(-SIZE/2, SIZE/2))
food.sety(random.randint(-SIZE/2, SIZE/2))
food.showturtle()

# control the turtle to move around
def up():
    snake.sety(snake.ycor()+20)

def down():
    snake.sety(snake.ycor()-20)

def left():
    snake.setx(snake.xcor()-20)

def right():
    snake.setx(snake.xcor()+20)


window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.listen()

while True:
    window.update()
    # snake and food are attached
    if snake.distance(food) < 20:
        food.setx(random.randint(-SIZE / 2, SIZE / 2))
        food.sety(random.randint(-SIZE / 2, SIZE / 2))


turtle.done()
