
# Turtle Dodge game
'''
controls: use arrow keys to move
player moves a turtle to doge falling enemies, gola is to avoid being hit by enemies

concepts covered:
- list
- loops
'''
import turtle
import random
import time

screen = turtle.Screen()
screen.title('Turtle Dodge')
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

LEFT_WALL = -280
RIGHT_WALL = 280
TOP_WALL = 280
BOTTOM_WALL = -280

player = turtle.Turtle()
player.shape('turtle')
player.color('cyan')
player.penup()
player.goto(0, BOTTOM_WALL + 30)
player.setheading(90)

player_speed = 15

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.color('white')
scoreboard.goto(0, TOP_WALL)

score = 0
lives = 5

def move_left():
    x = player.xcor() - player_speed
    if x > LEFT_WALL:
        player.goto(x, player.ycor())
        player.setheading(180)

def move_right():
    x = player.xcor() + player_speed
    if x < RIGHT_WALL:
        player.goto(x, player.ycor())
        player.setheading(0)

def move_up():
    y = player.ycor() + player_speed
    if y < TOP_WALL:
        player.goto(player.xcor(), y)
        player.setheading(90)

def move_down():
    y = player.ycor() - player_speed
    if y > BOTTOM_WALL:
        player.goto(player.xcor(), y)
        player.setheading(270)

screen.listen()
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')

coins = []

for i in range(5):
    coin = turtle.Turtle()
    coin.shape('square')
    coin.color('lime')
    coin.penup()
    coin.goto(random.randint(LEFT_WALL, RIGHT_WALL), random.randint(BOTTOM_WALL, TOP_WALL))
    coins.append(coin)


last_relocate = time.time()
game_running = True
ROUND_TIME = 60
RESTART_DELAY = 10
start_time = time.time()

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.color('yellow')
timer_display.goto(0, TOP_WALL - 30)

while game_running:
    screen.update()
    time.sleep(0.02)

    elapsed = time.time() - start_time
    time_left = ROUND_TIME - elapsed

    if time.time() - last_relocate >= 3:
        for coin in coins:
            coin.goto(random.randint(LEFT_WALL, RIGHT_WALL), random.randint(BOTTOM_WALL, TOP_WALL))
        last_relocate = time.time()

    # check collision with coins
    for coin in coins:
        if player.distance(coin) < 20:
            coin.goto(random.randint(LEFT_WALL, RIGHT_WALL), random.randint(BOTTOM_WALL, TOP_WALL))
            if coin.pencolor() == 'lime':
                score += 1

    # when time runs out, pause and restart
    if time_left <= 0:
        # countdown before restarting (uses a loop - same concept students just learned)
        for remaining in range(RESTART_DELAY, 0, -1):
            timer_display.clear()
            timer_display.write(
                f"Time's up! Restart in {remaining}s",
                align='center', font=('Courier', 16, 'bold')
            )
            screen.update()
            time.sleep(1)

        score = 0
        start_time = time.time()
        player.goto(0, BOTTOM_WALL + 30)
        for coin in coins:
            coin.goto(random.randint(LEFT_WALL, RIGHT_WALL), random.randint(BOTTOM_WALL, TOP_WALL))

    scoreboard.clear()
    scoreboard.write(f'Score: {score}', align='center', font=('Courier', 16, 'bold'))

    timer_display.clear()
    timer_display.write(f'Time: {int(time_left)}', align='center', font=('Courier', 16, 'bold'))

'''
1. add logic when player runs into the coins
    - coins randomly relocate to other position
    - increase the point by 1
    
2. create a timer, each round of game is 60s, show the timer on the screen and
when time is up, wait for 10s to restart the game

3. for each object, auto change its location every 3s, if not being caught

Homework/exercise:
implement the coin with different color, also when player catches the coin, add different score based on color
'''