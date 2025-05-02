import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('lightblue')
screen.title('Fun Math with Turtle!')

# Create a turtle for writing
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Create a turtle for animations
anim = turtle.Turtle()
anim.shape('turtle')
anim.color('green')
anim.speed(2)

# Get username
name = screen.textinput('Input', "What's your name?")
pen.goto(0, 200)
pen.color('purple')
pen.write(f'Welcome, {name}!', align='center', font=('Comic Sans MS', 28, 'bold'))

# Move animation turtle in a circle
for _ in range(36):
    anim.forward(10)
    anim.right(10)

pen.clear()

problems = int(screen.numinput('Input', 'How many math problems? (1-5)', minval=1, maxval=5))

operations = ['+', '-', '*', '/']

for _ in range(problems):
    operation = random.choice(operations)

turtle.done()