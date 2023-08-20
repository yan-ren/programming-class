import turtle
import os
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("deer_left.gif")
wn.register_shape("deer_right.gif")
wn.register_shape("hunter.gif")
wn.register_shape("nut.gif")

# Score
score = 0

# Health
lives = 3

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("deer_left.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Good things
good_things = []

for _ in range(3):
    good_thing = turtle.Turtle()
    good_thing.speed(1)
    good_thing.shape("nut.gif")
    good_thing.color("green")
    good_thing.penup()
    good_thing.goto(-100, 250)
    good_thing.speed = random.randint(2, 5)

    good_things.append(good_thing)

# Bad things
bad_things = []

for _ in range(3):
    bad_thing = turtle.Turtle()
    bad_thing.speed(1)
    bad_thing.shape("hunter.gif")
    bad_thing.color("red")
    bad_thing.penup()
    bad_thing.goto(100, 250)
    bad_thing.speed = random.randint(2, 5)

    bad_things.append(bad_thing)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 Lives: 3', align='center', font=('Courier', 24, 'normal'))

def go_left():
    player.direction = 'left'
    player.shape('deer_left.gif')

def go_right():
    player.direction = 'right'
    player.shape('deer_right.gif')


wn.listen()
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

while True:
    time.sleep(0.01)
    wn.update()

    # move the player
    if player.direction == 'left':
        player.setx(player.xcor() - 3)

    if player.direction == 'right':
        player.setx(player.xcor() + 3)

    if player.xcor() < -390:
        player.setx(-390)
    elif player.xcor() > 390:
        player.setx(390)

    for good_thing in good_things:
        # move the good things
        good_thing.sety(good_thing.ycor() - good_thing.speed)
        # check if good things are off the screen
        if good_thing.ycor() < -300:
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))
        # check for collisions
        if player.distance(good_thing) < 40:
            score += 10
            pen.clear()
            pen.write('Score: {} Lives: {}'.format(score, lives), align='center', font=("Courier", 24, "normal"))
            # move the good thing back to the top
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))

    for bad_thing in bad_things:
        # Move the bad things
        bad_thing.sety(bad_thing.ycor() - bad_thing.speed)

        if bad_thing.ycor() < -300:
            bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))

        if player.distance(bad_thing) < 40:
            # Score increases
            score -= 10
            lives -= 1

            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

            time.sleep(1)
            # Move the bad things back to the top
            for bad_thing in bad_things:
                bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))

    # check for game over
    if lives == 0:
        pen.clear()
        pen.write('Game over! Score {}'.format(score), align='center', font=("Courier", 24, 'normal'))
        wn.update()
        time.sleep(5)
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
