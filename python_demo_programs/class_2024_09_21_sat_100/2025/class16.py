'''puzzle program

Create a dictionary of 5 countries and their capitals.

Ask the user 3 random questions like: “What is the capital of ___?”

If the answer is correct, say “✅ Correct!” — if not, show the right answer.

Show the final score out of 3.
'''
'''
import turtle
import random


screen = turtle.Screen()
screen.title("Country-Capital Quiz")

countries_and_capitals = {
    'Australia': 'Canberra',
    'Canada': 'Ottawa',
    'France': 'Paris',
    'Japan': 'Tokyo',
    'Brazil': 'Brasília'
}

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-200, 0)

def display_message(message, move = True):
    writer.clear()
    if move:
        writer.goto(-200, 0)
    writer.write(message, font=('Arial', 20, 'bold'))

def ask_question():
    country = random.choice(list(countries_and_capitals.keys()))
    display_message(f"What is the capital of {country}?")
    user_answer = screen.textinput("Answer", f"What is the capital of {country}?")
    if user_answer.lower() == countries_and_capitals[country].lower():
        display_message("Correct!", False)
        return True
    else:
        display_message(f"❌ Incorrect! The correct answer is {countries_and_capitals[country]}.", False)
        screen.delay(2)
        return False

score = 0
display_message("Guess the capital! You will be asked 3 questions.", False)
screen.delay(3)

for _ in range(3):
    if ask_question():
        score += 1
    screen.delay(2)

display_message(f"You final score is {score} out of 3.", False)

screen.exitonclick()
'''

'''
Object Oriented Programming - OOP
'''
class Student():
    # constructor
    def __init__(self):
        self.name = ''
        self.age = 0

s1 = Student()
s1.name = 'Tom'
s1.age = 12
