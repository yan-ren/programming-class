'''
https://www.youtube.com/watch?v=HHQV3ifJopo&list=PLlEgNdBJEO-mRsbxRND_Cu805SCrXoOZB
'''
import turtle

wn = turtle.Screen()
wn.bgcolor('black')

ball = turtle.Turtle()
ball.penup()
ball.shape('circle')
ball.color('green')
ball.goto(0, 200)
ball.dy = 0
# step 2
gravity = 0.1

while True:
    # step 2
    ball.dy -= gravity
    #
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -300:
        ball.dy *= -1

wn.mainloop()
