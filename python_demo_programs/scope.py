import turtle
import random

'''
SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

# create turtle object to draw snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()

def get_random_value():
    return random.randint(-SCREEN_SIZE/4, SCREEN_SIZE/4)


# create turtle object to draw food
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("red")
food.penup()
food.goto(get_random_value(), get_random_value())


def up():
    snake.setheading(90)

def down():
    snake.setheading(-90)

def left():
    snake.setheading(180)

def right():
    snake.setheading(0)


# add keyboard control to snake object
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()

# turtle object for showing score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-350, 350)
score = 0

# main game loop,
while True:
    snake.forward(5)
    snake.stamp()           # draw the snake body
    snake.clearstamps(1)    # remove the last of snake

    # when snake gets food
    if snake.distance(food) < 20:
        score += 1
        pen.clear()
        food.goto(get_random_value(), get_random_value())
        # make addition stamp mark, so snake is longer when gets the food
        snake.stamp()

    # how to exit when snake touches the edge, hard-code
    if snake.xcor() >= SCREEN_SIZE/2 or snake.xcor() <= -SCREEN_SIZE/2 or snake.ycor() >= 400 or snake.ycor() <= -400:
        break

    pen.write("Score:" + str(score), font=("Verdana", 24, "normal"))


turtle.exitonclick()
'''
'''
More ideas:

add second snake to make this as 2 players game
add more food, or add obstacle
'''

'''
two scopes:
1. scope inside function == local
2. scope outside of the function == global

but overall Python can have 4 scopes
'''




# def foo1(y):
#     a = 1
#     x = 2
#     foo2(1)
#     print(x)
#
# def foo2(y):
#     x = 5
#
#
# x = 2
# foo1(x)
#
#
#
#
# if x > 2:
#     y = 1
#
# print(y)


# def foo():
#     global s
#     print(s)
#     x = 41
#     z = 5
#     s = "not true"
#     print(x, z)
#
#
# s = "Python is great"
# foo()
# print(s)
'''
Interpreted language: Python
Compiled language: Java
'''

# def add(x, y):
#     add(x, y)
#     print(x+y)
#
#
# add(1, 2)

'''
function calls itself - recursion/recursive function

recursive function:
1. base case
write condition when program stops calling itself

2. recursive case
function calls itself
'''
# def count(k):
#     print(k)
#     if k == 0:
#         return
#
#     count(k-1)
#
#
# count(10)

def add(n):
    if n == 0:
        return n

    return n + add(n-1)


print(add(5))


