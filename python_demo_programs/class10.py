# # exercise 2:
# # write a function which takes a list of numbers, return the count of positive number
#
#
# def count_positive(numbers):
#     count = 0
#     for value in numbers:
#         if value > 0:
#             count += 1
#
#     return count
#
#
# print(count_positive([1, 2, -1, 4]))
# print(count_positive([1, 2, -1, 4, -3]))
#
#
# # exercise 1:
# # write a function which takes two list of numbers, return True,
# # if there are common value between the list, otherwise return False
# def find_common(numbers1, numbers2):
#     for v1 in numbers1:
#         if v1 in numbers2:
#             return True
#
#     return False
#
#
# print(find_common([1, 2], [2, 3]))
# print(find_common([1, 2], [3, 4]))

import turtle


wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(800, 600)
wn.tracer(0)

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.penup()
paddle_left.goto(-350, 0)
paddle_left.shapesize(5, 1)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(350, 0)
paddle_right.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.dx = 0.5
ball.dy = 0.5

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

wn.listen()
wn.onkeypress(paddle_left_up, 'w')
wn.onkeypress(paddle_left_down, 's')
wn.onkeypress(paddle_right_up, 'Up')
wn.onkeypress(paddle_right_down, 'Down')

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 60 and ball.ycor() > paddle_right.ycor() - 60):
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 60 and ball.ycor() > paddle_left.ycor() - 60):
        ball.dx *= -1

