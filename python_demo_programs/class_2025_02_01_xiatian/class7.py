import turtle
import random

wn = turtle.Screen()
wn.setup(500, 500)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

pen.goto(0, 0)
pen.color("black")
pen.write("Guess a number!", align="center", font=("Arial", 24, "bold"))

correct_number = random.randint(1, 20)
user_guess = int(wn.textinput('Enter a number', 'Enter a number'))

pen.clear()
pen.goto(0, 50)
pen.color('blue')
pen.write('Your guess: ' + str(user_guess), align='center', font=('Arial', 24, 'bold'))

pen.goto(0, 0)
if user_guess == correct_number:
    pen.color('green')
    pen.write('You win!', align='center', font=('Arial', 24, 'bold'))
else:
    pen.color('red')
    pen.write('You loose!', align='center', font=('Arial', 24, 'bold'))
    pen.goto(0, -50)
    pen.write('Correct number: ' + str(correct_number), align='center', font=('Arial', 24, 'bold'))

turtle.done()