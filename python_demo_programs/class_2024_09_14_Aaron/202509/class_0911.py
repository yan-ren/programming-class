'''
warm-up project:
1. list
2. dictionary
3. def
4. turtle

Game: Catch the Turtle
1. A turtle randomly appears at different spots on the screen.
2. The player must click on the turtle to score points.
3. After 30 seconds, the game ends and shows the final score.
'''
import turtle
import random
import time


screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=800)

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)
score_writer.write("Score: 0", align="center", font=("Arial", 16, "normal"))

timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(0, 230)
timer_writer.write("Time: 30", align="center", font=("Arial", 16, "normal"))


positions = {
    1: (-200, 200),
    2: (0, 200),
    3: (200, 200),
    4: (-200, 0),
    5: (0, 0),
    6: (200, 0),
    7: (-200, -200),
    8: (0, -200),
    9: (200, -200)
}

score = 0
game_over = False
time_left = 30

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

def update_timer():
    global time_left, game_over
    if time_left > 0 and not game_over:
        timer_writer.clear()
        timer_writer.write(f"Time: {time_left}", align="center", font=("Arial", 16, "normal"))
        time_left -= 1
        screen.ontimer(update_timer, 1000)
    else:
        end_game()

def move_turtle():
    if not game_over:
        spot = random.choice(list(positions.values()))
        player.goto(spot)
        screen.ontimer(move_turtle, 800)

def catch(x, y):
    global score
    if not game_over:
        score += 1
        update_score()

def end_game():
    global game_over
    game_over = True
    score_writer.goto(0, 0)
    score_writer.write(f"Game Over!\nFinal Score: {score}, click the screen to restart", align="center", font=("Arial", 20, "bold"))
    screen.onclick(restart_game)

def restart_game(x=None, y=None):
    global score, time_left, game_over
    score = 0
    time_left = 30
    game_over = False

    score_writer.goto(0, 260)
    update_score()
    timer_writer.goto(0, 230)
    timer_writer.clear()
    timer_writer.write(f"Time: {time_left}", align="center", font=("Arial", 16, "normal"))

    player.onclick(catch)
    screen.onclick(None)
    move_turtle()
    update_timer()

player.onclick(catch)
move_turtle()
update_timer()
screen.mainloop()

'''
after class follow-up
- show the count down timer on the screen. e.g. 30, 29, 28, ...
'''