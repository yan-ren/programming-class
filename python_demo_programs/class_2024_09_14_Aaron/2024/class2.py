'''
import turtle

wn = turtle.Screen()
wn.bgcolor('black')

ball = turtle.Turtle()
ball.penup()
ball.shape('circle')

color = input("which color do you like?")

ball.color(color)
ball.goto(0, 100)
ball.dy = 0
# step 2
gravity = 0.1
ball.dx = 2

while True:
    # step 2
    ball.dy -= gravity
    #
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -200:
        ball.dy *= -1

    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() > 200:
        ball.dx = ball.dx * -1
    if ball.xcor() < -200:
        ball.dx = ball.dx * -1

wn.mainloop()
'''

# write a program that takes three numbers as input, and print the average
# number1 = float(input("enter the first number:"))
# number2 = float(input("enter the second number:"))
# number3 = float(input("enter the third number:"))
#
# print('average is ', (number1 + number2 + number3) / 3)

# x = 10
# y = 12
#
# print(x == y)
# print(2*8 > 10)
#
# x = True
# y = False
# print(x or y)

import turtle


window = turtle.Screen()
window.setup(800,800)

t = turtle.Turtle()

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

turtle.done()