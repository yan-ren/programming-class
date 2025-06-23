import turtle
import random


screen = turtle.Screen()
screen.title("Turtle Dodger")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.goto(0, -250)
player.speed(0)

blocks = []
for _ in range(5):
    block = turtle.Turtle()
    block.shape("square")
    block.color("red")
    block.shapesize(stretch_wid=1, stretch_len=3)
    block.penup()
    block.goto(random.randint(-280, 280), random.randint(100, 600))
    blocks.append(block)


def go_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def go_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

game_over = False
def move_blocks():
    global game_over

    for block in blocks:
        y = block.ycor()
        block.sety(y - 20)
        if block.ycor() < -300:
            block.goto(random.randint(-280, 280), random.randint(300, 600))
        if player.distance(block) < 30:
            game_over = True

    screen.update()
    if not game_over:
        screen.ontimer(move_blocks, 100)
    else:
        end_game()


def end_game():
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.color('white')
    msg.penup()
    msg.goto(0, 0)
    msg.write("Game Over!", align="center", font=("Arial", 24, "bold"))


move_blocks()
screen.mainloop()