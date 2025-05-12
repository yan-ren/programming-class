import turtle
import random
import time

screen = turtle.Screen()
screen.title('Catch the Falling Object')
screen.bgcolor('white')
screen.setup(600, 800)
screen.tracer(0)

screen.addshape('basket.gif')
screen.addshape('butterfly.gif')

basket = turtle.Turtle()
basket.shape('basket.gif')
basket.penup()
basket.goto(0, -300)

drop = turtle.Turtle()
drop.shape('butterfly.gif')
drop.penup()
drop.goto(random.randint(-280, 280), 380)

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-280, 260)
pen.write(f"Score: {score}", font=("Arial", 16, "normal"))

# movement
def go_left():
    x = basket.xcor()
    x -= 30
    if x < -280:
        x = -280
    basket.setx(x)

def go_right():
    x = basket.xcor()
    x += 30
    if x > 280:
        x = 280
    basket.setx(x)

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

fall_speed = 5
fall_speed2 = 1

while True:
    screen.update()
    time.sleep(0.03)















'''
Exercise:
write a program ask user for two numbers, num1 and num2
where num1 < num2
calculate the sum from num1, num1 + 1, num1 + 2, ..., num2

e.g.
num1 = 20
num2 = 30
result = 20 + 21 + 22 + ... + 30
'''
