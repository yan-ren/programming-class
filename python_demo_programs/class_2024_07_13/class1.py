import time
import turtle
import random


SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)
turtle.delay(0)

# one turtle object to draw snakes
snake = turtle.Turtle()
wn.addshape('upmouth.gif')

snake.shape('upmouth.gif')
# snake.color('pink')
snake.penup()

def get_random_value():
    return random.randint(int(-SCREEN_SIZE/2 + 30), int(SCREEN_SIZE/2 - 30))

# / //

# turtle object to draw food
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.color('green')

# turtle object for writing
text = turtle.Turtle()
text.hideturtle()
text.penup()

turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(-90), 'Down')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.listen()

score = 0
text.goto(0, 300)
text.write('Score: ' + str(score), font=('Courier', 24, 'bold'))

def move():
    food.goto(get_random_value(), get_random_value())
    wn.ontimer(lambda: move(), 3000)

move()

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)
    time.sleep(0.01)

    if snake.distance(food) < 20:
        snake.stamp()
        food.goto(get_random_value(), get_random_value())
        score += 1
        text.clear()
        text.write('Score: ' + str(score), font=('Courier', 24, 'bold'))

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        text.write('Game Over', font=('Courier', 24, 'bold'))
        break

turtle.done()

