import turtle
import random


wn = turtle.Screen()
wn.setup(600, 600)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

pen.write('Guess the number!', align='center', font=('Arial', 24, "bold"))

correct_number = random.randint(1, 10)
times = 3
while times > 0:
    user_guess = int(wn.textinput('Enter your guess', 'Enter your guess'))
    pen.clear()

    pen.goto(0, 50)
    pen.color('blue')
    pen.write('Your guess: ' + str(user_guess), align='center', font=('Arial', 24, 'bold'))

    pen.goto(0, 0)

    if user_guess == correct_number:
        pen.color('green')
        pen.write('You win!', align='center', font=('Arial', 24, 'bold'))
    else:
        pen.color("red")
        pen.write("You Lose! Correct number is " + str(correct_number), align="center", font=("Arial", 24, "bold"))

    times = times - 1

turtle.done()
