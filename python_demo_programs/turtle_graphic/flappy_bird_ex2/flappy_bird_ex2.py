import turtle
import time


wn = turtle.Screen()
wn.title('Flappy bird')
wn.bgcolor('blue')
wn.bgpic('background.gif')
wn.setup(width=500, height=800)
wn.tracer(0)

wn.register_shape('bird.gif')

player = turtle.Turtle()
player.shape('bird.gif')
player.speed(0)
player.penup()
player.goto(-200, 0)
player.dx = 0
player.dy = 1
player.score = 0
gravity = -0.3

# pipe1
pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color('green')
pipe1_top.shape('square')
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
pipe1_top.dx = -2
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
pipe1_bottom.dx = -2

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color('white')
pen.goto(0, 250)
pen.write('0', move=False, align='left', font=('Arial', 32, 'normal'))

def go_up():
    player.dy += 8
    if player.dy > 8:
        player.dy = 8


wn.listen()
wn.onkeypress(go_up, 'space')

pipes = [(pipe1_top, pipe1_bottom)]

while True:
    wn.update()
    time.sleep(0.02)

    # move bird
    player.dy += gravity
    # player.sety(player.ycor()+player.dy)
    y = player.ycor()
    y += player.dy
    if y < wn.window_height() / 2:
        player.sety(y)

    if y < wn.window_height() / 2 * -1:
        player.dy = -gravity

    # pipes,
    for pipe_pair in pipes:
        pipe_top = pipe_pair[0]
        pipe_bottom = pipe_pair[1]

        pipe_top.setx(pipe_top.xcor() + pipe_top.dx)
        pipe_bottom.setx(pipe_bottom.xcor() + pipe_bottom.dx)

        # return pips to start
        if pipe_top.xcor() < -350:
            pipe_top.setx(600)
            pipe_bottom.setx(600)
            pipe_top.value = 1

        # score
        if pipe_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe_top.value
            pipe_top.value = 0

        # check for collisions with pipes
        if (pipe_top.xcor() - 30 < player.xcor() < pipe_top.xcor() + 30):
            if (player.ycor() > pipe_top.ycor() - 180 or player.ycor() < pipe_bottom.ycor() + 180):
                pen.clear()
                pen.write('Game Over', align='center', font=('Arial', 16, 'normal'))
                wn.update()
                time.sleep(3)

                # reset score
                player.score = 0
                # move pipes back
                pipe_top.setx(450)
                pipe_bottom.setx(450)
                # move player back
                player.goto(-200, 0)
                player.dy = 0
                # reset the pen
                pen.clear()
                pen.write('0', align='center', font=('Arial', 16, 'normal'))