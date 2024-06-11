import turtle
import random

SCREEN_SIZE = 800

wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_firework(t):
    # let pen go to random place
    x = random.randint(-SCREEN_SIZE // 3, SCREEN_SIZE // 3)
    y = random.randint(-SCREEN_SIZE // 3, SCREEN_SIZE // 3)

    colors = ['blue', 'red', 'yellow', 'purple']
    t.color(random.choice(colors))
    t.penup()
    t.goto(x, y)
    t.pendown()

    # draw shape
    # for i in range(36):
    #     t.forward(100)
    #     t.backward(100)
    #     t.left(10)

    size = random.randint(40, 80)
    # how to put the shape that we draw before
    for i in range(18):
        for j in range(4):
            t.forward(size)
            t.left(90)
        t.left(20)


for i in range(10):
    draw_firework(pen)


pen.penup()
pen.goto(0, 300)
pen.color('white')
pen.write('Happy New Year!', align='center', font=('Verdana', 24, 'normal'))

turtle.done()

'''exercise
write a function which takes a list of string as input, return the longest string

'''