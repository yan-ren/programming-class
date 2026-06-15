import turtle

wn = turtle.Screen()
wn.bgcolor('black')

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')

ball.dy = 0
gravity = 0.1

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -200:
        ball.dy *= -1
        
wn.mainloop()
