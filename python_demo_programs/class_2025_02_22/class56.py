import time
import turtle
import random
import winsound

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

score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-380, 350)
score_display.write(f"Score: {score}", font=("Arial", 18, "bold"))

time_left = 60
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(250, 350)
timer_display.write(f"Time: {time_left}", font=("Arial", 18, "bold"))

# Keyboard controls
screen.listen()
screen.onkeypress(lambda: player.sety(player.ycor() + 20), "Up")
screen.onkeypress(lambda: player.sety(player.ycor() - 20), "Down")
screen.onkeypress(lambda: player.setx(player.xcor() - 20), "Left")
screen.onkeypress(lambda: player.setx(player.xcor() + 20), "Right")

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 18, "bold"))

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_display.clear()
        timer_display.write(f"Time: {time_left}", font=("Arial", 18, "bold"))
        screen.ontimer(countdown, 1000)
    else:
        game_over()

def game_over():
    winsound.Beep(600, 500)
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 0)
    message.write("Time's up\nGame Over", align='center', font=("Arial", 24, "bold"))
    screen.update()

def game_loop():
    global score
    if time_left > 0:
        if player.distance(target) < 20:
            score += 1
            update_score()
            target.goto(random.randint(-250, 250), random.randint(-250, 250))
        screen.update()
        screen.ontimer(game_loop, 100)

countdown()
game_loop()
turtle.done()
