# import random
# import time
# import turtle
#
# wn = turtle.Screen()
# wn.setup(800, 800)
# turtle.delay(0)
#
# snake = turtle.Turtle()
# snake.shape('square')
# snake.speed(0)
# snake.penup()
#
# food = turtle.Turtle()
# food.shape('circle')
# food.color('green')
# food.speed(0)
# food.penup()
# food.goto(random.randint(-350, 350), random.randint(-350, 350))
#
# writing = turtle.Turtle()
# writing.penup()
# writing.hideturtle()
#
# turtle.onkeypress(lambda: snake.setheading(90), 'Up')
# turtle.onkeypress(lambda: snake.setheading(270), 'Down')
# turtle.onkeypress(lambda: snake.setheading(180), 'Left')
# turtle.onkeypress(lambda: snake.setheading(0), 'Right')
# turtle.listen()
#
# while True:
#     snake.forward(5)
#     time.sleep(0.01)
#
#     if snake.xcor() > 400 or snake.xcor() < -400 or snake.ycor() > 400 or snake.ycor() < -400:
#         writing.write('Game Over', font=('Arial', 12, 'normal'))
#         break
#
# turtle.done()

# r = int(input())
# g = int(input())
# b = int(input())
#
# print(r * 3 + g * 4 + b * 5)

# 2023 j1