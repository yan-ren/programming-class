'''
today:
1. break
2. continue
3. double loop
'''
# i = 0
# while i < 5:
#     if i == 2:
#         i += 1
#         continue
#
#     print(i)
#     i += 1

# i = 0
# while i < 4:
#     j = i
#     while j < 3:
#         print(j)
#         j += 1
#     i += 1


# row = 0
# while row < 3:
#     col = 0
#     while col <= row:
#         print('*', end='')
#         col += 1
#     print()
#     row += 1


'''
*
**
***
****
'''

# import turtle
#
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
#
# num_start = 60
# angle_offset = 15
#
# i = 0
# while i < num_start:
#     t.penup()
#     t.goto(-i * 10, -i * 10)
#     t.pendown()
#
#     j = 0
#     while j < 5:
#         t.forward(100)
#         t.right(144)
#         j += 1
#
#     t.right(angle_offset)
#     i += 1
#
# turtle.done()



'''
Simple snake
'''
import turtle
import random
import time


wn = turtle.Screen()
wn.setup(800, 800)
turtle.delay(0)

# create a snake on the screen
snake = turtle.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()

color = ['red', 'green', 'blue']
food = turtle.Turtle()
food.shape('circle')
food.color(random.choice(color))
food.speed(0)
food.penup()
food.goto(random.randint(-350, 350), random.randint(-350, 350))

# turtle object for writing
score = 0
writing = turtle.Turtle()
writing.hideturtle()
writing.penup()
writing.goto(-380, 380)
writing.write('Score: ' + str(score), font=('Arial', 12, 'normal'))

turtle.onkeypress(lambda: snake.setheading(0), 'Right')
turtle.onkeypress(lambda: snake.setheading(90), 'Up')
turtle.onkeypress(lambda: snake.setheading(180), 'Left')
turtle.onkeypress(lambda: snake.setheading(270), 'Down')
turtle.listen()

while True:
    snake.forward(5)
    snake.stamp()
    snake.clearstamps(1)
    time.sleep(0.01)

    if snake.distance(food) < 20:
        food.goto(random.randint(-350, 350), random.randint(-350, 350))
        snake.stamp()
        snake.stamp()
        food.color(random.choice(color))
        score += 1
        snake.color(random.choice(color))
        writing.clear()
        writing.write('Score: ' + str(score), font=('Arial', 12, 'normal'))

    if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
        writing.goto(-200, 0)
        writing.write('Game Over', font=('Arial', 12, 'normal'))
        writing.goto(-200, -50)
        writing.write('Your score:' + str(score), font=('Arial', 12, 'normal'))
        break

turtle.done()

'''
more features:
1. add border checking
2. score
3. add multiple food, giving different score
'''
