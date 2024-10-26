'''
Write a program that ask user for a number, check the number with the target
and reminder user if the guess is too high or too low
1. improve: only give three chances
'''
# import random
#
#
# target = random.randint(1, 20)
# chance = 3
# run = True
#
# while run:
#     if chance == 0:
#         print('game over')
#         break
#
#     guess = int(input('Guess a number between 1 to 20:'))
#     if guess == target:
#         print('correct')
#         run = False
#     elif guess > target:
#         print('your guess is bigger than correct answer')
#     else:
#         print('your guess is smaller than correct answer')
#
#     chance = chance - 1

# numbers = [-1, 2, 1, -4]
# new_numbers = []
#
# for num in numbers:
#     if num > 0:
#         new_numbers.append(num)
#
# print(new_numbers)
# # new_numbers = [num for num in numbers if num > 0]
# print(new_numbers)

import turtle

window = turtle.Screen()
window.bgcolor("black")
window.setup(800, 600)
window.tracer(0) # disable window auto update

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(5, 1)
paddle_left.penup()
paddle_left.goto(-350, 0)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.shapesize(5, 1)
paddle_right.penup()
paddle_right.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.color('green')
ball.shape('circle')
ball.penup()
ball.dx = 0.05
ball.dy = 0.05

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write('Player A: 0 Player B: 0', align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

def paddle_right_up():
    paddle_right.sety(paddle_right.ycor() + 20)

def paddle_right_down():
    paddle_right.sety(paddle_right.ycor() - 20)


window.listen()
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down,  'Down')
window.onkeypress(lambda: paddle_left.sety(paddle_left.ycor() + 20), 'w')
window.onkeypress(lambda: paddle_left.sety(paddle_left.ycor() + 20), 's')

score_left = 0
score_right = 0

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx = ball.dx * -1

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        score_left = score_left + 1
        text = 'Player A: ' + str(score_left) + ' Player B: ' + str(score_right)
        pen.clear()
        pen.write(text, align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() < -390:
        score_right = score_right + 1
        text = 'Player A: ' + str(score_left) + ' Player B: ' + str(score_right)
        pen.clear()
        pen.write(text, align='center', font=('Courier', 24, 'bold'))

    # paddle and ball collision
    # right paddle x locates at ~350,
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
        (paddle_right.ycor()-60< ball.ycor() < paddle_right.ycor() + 60):
        ball.dx = ball.dx * -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and \
            (paddle_left.ycor() - 60 < ball.ycor() < paddle_left.ycor() + 60):
        ball.dx = ball.dx * -1


'''
Homework:
1. how to show the updated score on the screen
2. Given a list of numbers, there is one number showed multiple times, find that number
list = [1, 2, 3, 4, 1]
number = 1
'''


