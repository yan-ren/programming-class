# import turtle
#
# screen = turtle.Screen()
# pen = turtle.Turtle()
#
# for i in range(4):
#     pen.forward(100)
#     pen.left(90)
#
# pen.left(90)
#
# for i in range(4):
#     pen.forward(100)
#     pen.left(90)
#
# pen.left(90)
#
# for i in range(4):
#     pen.forward(100)
#     pen.left(90)
#
# pen.left(90)
#
# for i in range(4):
#     pen.forward(100)
#     pen.left(90)
#
# turtle.done()

import turtle

screen = turtle.Screen()
screen.title("Mother's Day Card")
screen.bgcolor("white")

heart = turtle.Turtle()
heart.color("red")
heart.fillcolor("red")
heart.speed(1)

heart.begin_fill()
heart.left(50)
heart.forward(133)
heart.circle(50, 200)
heart.right(140)
heart.circle(50, 200)
heart.forward(133)
heart.end_fill()

heart.penup()
heart.goto(0, -20)
heart.pendown()

heart.write("Happy Mother's Day!", align="center", font=("Arial", 18, "normal"))
heart.hideturtle()

turtle.done()

'''
t1.distance(t2) < 20:
    t2.goto(random.randint(-280, -280), random.randint(-280, -280))
'''








