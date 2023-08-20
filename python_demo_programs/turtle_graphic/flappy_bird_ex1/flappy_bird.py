import turtle
import time

window = turtle.Screen()
window.bgcolor('blue')
window.bgpic('background.gif')
window.setup(500, 800)
window.tracer(0)

# import image as shape
window.register_shape('bird.gif')

# create turtle object to draw the score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color('white')
pen.goto(0, 250)
pen.write("Score: 0", move=False, align='center', font=('Arial', 24, 'normal'))

# create turtle object to draw the bird
player = turtle.Turtle()
player.speed(0)
player.penup()
player.color('yellow')
player.shape('bird.gif')
player.goto(-200, 0)
player.dx = 0
player.dy = 1

# create turtle object for pipe
pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
pipe1_top.dx = -1
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
pipe1_bottom.dx = -1
pipe1_bottom.dy = 0

pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_top.goto(600, 280)
pipe2_top.dx = -1
pipe2_top.dy = 0
pipe2_top.value = 1

pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -200)
pipe2_bottom.dx = -1
pipe2_bottom.dy = 0

# define the control
def go_up():
    player.dy += 8
    # prevent player moving too fast
    if player.dy > 8:
        player.dy = 8


window.listen()
window.onkeypress(go_up, 'space')

# initialize game variables
player.score = 0
pipes = [(pipe1_top, pipe1_bottom), (pipe2_top, pipe2_bottom)]
gravity = -0.3


while True:
    time.sleep(0.02)
    window.update()

    # add gravity
    player.dy += gravity

    # move player
    player.sety(player.ycor() + player.dy)

    # bottom border
    if player.ycor() < -390:
        player.dy = 0
        player.sety(-390)

    # move pipes
    for pipe_pair in pipes:
        pipe_top = pipe_pair[0]
        pipe_bottom = pipe_pair[1]

        pipe_top.setx(pipe_top.xcor() + pipe_top.dx)
        pipe_bottom.setx(pipe_bottom.xcor() + pipe_bottom.dx)

        # pipe reaches the left border, reset the pipe to start
        if pipe_top.xcor() < -350:
            pipe_top.setx(600)
            pipe_bottom.setx(600)
            pipe_top.value = 1

        # check for collisions with pipes
        if (player.xcor() + 10 > pipe_top.xcor() - 30) and (player.xcor() - 10 < pipe_top.xcor() + 30):
            if (player.ycor() + 10 > pipe_top.ycor() - 180) or (player.ycor() - 10 < pipe_bottom.ycor() + 180):
                pen.clear()
                pen.write('Game over', move=False, align='center', font=('Arial', 16, 'normal'))
                window.update()
                time.sleep(3)

                # reset score
                player.score = 0
                # reset pipe
                pipe_top.setx(450)
                pipe_bottom.setx(450)
                # reset the player
                player.goto(-200, 0)
                player.dy = 0
                # reset pen
                pen.write("Score: 0", move=False, align='center', font=('Arial', 24, 'normal'))

        # check for score
        if pipe_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe_top.value
            pipe_top.value = 0
            pen.clear()
            pen.write(player.score, move=False, align='center', font=('Arial', 32, 'normal'))

