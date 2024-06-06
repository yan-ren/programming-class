import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setup(800, 600)

score = 0

# turtle for writing the text
pen = turtle.Turtle()
pen.penup()
pen.color('black')
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: " + str(score), align='center', font=('Courier', 24, 'normal'))

targets = []

# populate targets list
for _ in range(5):
    t = turtle.Turtle()
    t.shape('circle')
    t.color('red')
    t.penup()
    t.speed(0)
    targets.append(t)


def move_target(target):
    target.goto(random.randint(-380, 380), random.randint(-280, 280))
    wn.ontimer(lambda: move_target(target), 3000)

def click_target(target):
    global score
    score += 1
    pen.clear()
    pen.write("Score: " + str(score), align='center', font=('Courier', 24, 'normal'))
    move_target(target)


def click_event(target):
    target.onclick(lambda x, y: click_target(target))


def main():
    for target in targets:
        # move randomly
        move_target(target)
        # response to mouse clicking
        click_event(target)


main()
wn.mainloop()
