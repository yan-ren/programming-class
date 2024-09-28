'''
https://www.youtube.com/watch?v=HHQV3ifJopo&list=PLlEgNdBJEO-mRsbxRND_Cu805SCrXoOZB
'''
import turtle

wn = turtle.Screen()
wn.bgcolor('black')

ball = turtle.Turtle()
ball.penup()
shape = input('what is the shape that you like?')
color = input('which color do you like?')

ball.shape(shape)
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
