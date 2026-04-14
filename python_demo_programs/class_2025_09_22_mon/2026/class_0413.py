'''
exercise: use double loop, how to print following pattern
*
* *
* * *
* * * *
* * * * *
'''
# for i in range(5): # we want 5 rows
#     for j in range(i + 1):
#         print('*', end='')
#
#     print()

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
scoreboard.goto(0, TOP_WALL + 5)

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