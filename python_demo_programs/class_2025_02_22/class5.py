import time
import turtle
import random


screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.setup(800, 800)

player = turtle.Turtle()
player.shape('turtle')
player.color('green')
player.penup()

target = turtle.Turtle()
target.shape('circle')
target.color('red')
target.penup()
target.goto(random.randint(-250, 250), random.randint(-250, 250))

# Keyboard controls
screen.listen()
screen.onkeypress(lambda: player.sety(player.ycor() + 20), "Up")
screen.onkeypress(lambda: player.sety(player.ycor() - 20), "Down")
screen.onkeypress(lambda: player.setx(player.xcor() - 20), "Left")
screen.onkeypress(lambda: player.setx(player.xcor() + 20), "Right")

def game_loop():
    while True:
        if player.distance(target) < 20:
            target.goto(random.randint(-250, 250), random.randint(-250, 250))

        time.sleep(0.1)
        screen.update()

screen.ontimer(game_loop, 100)
turtle.done()