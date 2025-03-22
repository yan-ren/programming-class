# import turtle
# import random
# import time
#
#
# screen = turtle.Screen()
# screen.setup(800, 800)
#
# counter = turtle.Turtle()
# counter.hideturtle()
# counter.penup()
# counter.goto(0, 0)
# screen.tracer(0)
#
# def countdown(start):
#     # show countdown from start to 0 and show the number on the turtle
#     # hint: using loop
#     while start >= 0:
#         screen.clear()
#         screen.bgcolor(random.choice(["white", "lightblue", "lightgreen", "yellow", "pink"]))
#
#         font_size = 48 + (start % 2) * 10  # Alternates between 48 and 58
#         counter.write(start, align="center", font=("Arial", font_size, "bold"))
#         start -= 1
#         screen.update()
#         time.sleep(1)
#
# def finish():
#     # show time's up words on the screen with animation, e.g. change screen backgroud every 1s
#     for _ in range(6):
#         screen.bgcolor(random.choice(["red", "orange", "purple", "blue"]))
#         counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))
#         screen.update()
#         time.sleep(0.5)
#         screen.clear()
#         time.sleep(0.5)
#
#     counter.write("Time's up!", align="center", font=("Arial", 48, "bold"))
#     screen.update()
#
#
# countdown(10)
# finish()
# turtle.done()

def f2():
    print('In f2')

def f1():
    f2()
    print('In f1')

f1()

'''
Exercise:

write a function, which takes a list of numbers, and return another list with each number is the square
of the input list
input: [1, 2, 3, 4]
output: [1, 4, 9, 16]
'''