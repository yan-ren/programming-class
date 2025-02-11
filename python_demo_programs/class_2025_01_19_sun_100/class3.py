# import turtle
#
#
# wn = turtle.Screen()
# wn.setup(800, 600)
# wn.bgcolor('cyan')
#
# pen = turtle.Turtle()
# color = wn.textinput('Select color', 'Choose a color for drawing (red, yellow, blue)')
# pen.color(color)
#
# shape = wn.textinput('Select shape', 'Choose a shape to draw (circle, square, triangle)')
#
# if shape == 'circle':
#     pen.begin_fill()
#     pen.circle(50)
#     pen.end_fill()
#
# if shape == 'square':
#
#
# turtle.done()
import time
import turtle
import random

game_window = turtle.Screen()
game_window.setup(800, 600)
game_window.tracer(0)

red_ball = turtle.Turtle()
red_ball.shape('circle')
red_ball.color('red')
red_ball.penup()
red_ball.goto(random.randint(-300, 300), random.randint(-250, 250))

blue_ball = turtle.Turtle()
blue_ball.shape('circle')
blue_ball.color('blue')
blue_ball.penup()
blue_ball.goto(random.randint(-300, 300), random.randint(-250, 250))

while True:
    red_ball.setx(red_ball.xcor() + random.randint(-50, 50))
    red_ball.sety(red_ball.ycor() + random.randint(-50, 50))

    # make sure red ball stays inside the screen
    if red_ball.xcor() > 380 or red_ball.xcor() < -380:
        red_ball.goto(random.randint(-300, 300), random.randint(-250, 250))

    if red_ball.ycor() > 280 or red_ball.ycor() < -280:
        red_ball.goto(random.randint(-300, 300), random.randint(-250, 250))


    game_window.update()
    time.sleep(0.05)

turtle.done()