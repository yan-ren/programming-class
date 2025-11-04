import random
import time
import turtle

screen = turtle.Screen()
screen.setup(600, 800)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]

def draw_die(x, y, value):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    for _ in range(4):
        drawer.forward(50)
        drawer.right(90)

    drawer.penup()
    drawer.goto(x + 20, y - 35)
    drawer.write(value, align='center', font=("Arial", 20, "bold"))


score = 0
rounds = 0
guess = None

def roll_dice():
    global score, rounds
    v1 = random.choice(d1)
    v2 = random.choice(d2)
    total = v1 + v2

    drawer.clear()
    draw_die(-60, 60, v1)
    draw_die(10, 60, v2)

    drawer.penup()
    drawer.goto(-20, -20)
    drawer.write(f"Sum: {total}", align="center", font=("Arial", 16, "normal"))

    # check guess
    if (guess == "big" and total >= 7) or (guess == "small" and total < 7):
        score += 1
        drawer.goto(0, -60)
        drawer.write("✅ Correct!", align="center", font=("Arial", 16, "bold"))
    else:
        drawer.goto(0, -60)
        drawer.write("❌ Wrong!", align="center", font=("Arial", 16, "bold"))

    rounds += 1
    if rounds ==3:
        drawer.goto(0, -120)
        drawer.write(f"Game Over! You guessed {score}/3 correctly.",
                     align="center", font=("Arial", 18, "bold"))

def on_click(x, y):
    global guess
    if rounds > 3:
        return

    guess = screen.textinput('Your Guess', "Type 'big' >= 7 or 'small' < 7")
    if guess is None:
        return
    if guess not in ['big', 'small']:
        screen.textinput("Invalid", "Please type only 'big' or 'small'. Press OK to continue.")
        return

    roll_dice()


screen.onclick(on_click)
turtle.done()

'''
1. combine with guess a number program. Ask user for 'big' or 'small', big means >= 7, small means < 7
then throw dice, if correct, add one score, if not correct, no score. Repeat three times, show the number of times guess correctly 
'''