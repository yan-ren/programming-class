# def function_a():
#     print("Function A is calling Function B")
#     function_b()
#
# def function_b():
#     print("Function B is calling Function C")
#     function_c()
#
# def function_c():
#     print("Function C is calling Function D")
#     function_d()
#     print('Function C is done')
#
# def function_d():
#     print("Function D has been reached!")
#
# # Start the function chain
# function_a()

'''
Turtle Catch

Game Concept:
- The player controls a turtle using arrow keys
- A target moves randomly around the screen
- The player must catch the target by moving the turtle
- Whe caught, the target moves to a new random position, and the score increases
'''
import turtle
import random

screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.setup(800, 800)

player = turtle.Turtle()
player.shape('turtle')
player.color('green')
player.penup()

target = turtle.Turtle()
target.shape('circle')
target.color('red')
target.penup()
target.goto(random.randint(-250, 250), random.randint(-250, 250))

def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Keyboard controls
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, 260)

game_running = True
time_left = 30
score = 0

def check_collision():
    global score
    if player.distance(target) < 20:
        score += 1
        print(f'Score: {score}')
        target.goto(random.randint(-250, 250), random.randint(-250, 250))

    if game_running:
        screen.ontimer(check_collision, 100)

def countdown():
    global time_left, game_running
    if time_left > 0:
        time_left -= 1
        timer_display.clear()
        timer_display.write(f"Time Left: {time_left}  Score: {score}", align="center", font=("Arial", 16, "bold"))
        screen.ontimer(countdown, 1000)
    else:
        game_running = False
        timer_display.clear()
        timer_display.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 16, "bold"))


check_collision()
countdown()
turtle.done()








