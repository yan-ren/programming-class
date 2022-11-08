'''
variable
conditional
loop
- for loop - list
- while loop

python basic coding syntax
java

learn English:
- learn English letters
- words/gramme
- sentence
- reading books/writing essay

summer + turtle -> graphical drawing program

hundreds of computer languages
'''
# import turtle

# wn = turtle.Screen()
# bob = turtle.Turtle()

# i = 0
# while i < 4:
#     bob.forward(100)
#     bob.right(90)
#     i += 1

# range(4) -> [0, 1, 2, 3]
# for i in range(4):
#     bob.forward(100)
#     bob.right(90)

# range(3) -> [0, 1, 2]
# nested loop
# for j in range(6):
#     bob.right(60)
#     for i in range(3):
#         bob.forward(100)
#         bob.right(120)
# wn.bgcolor('lightgreen')
# bob.pencolor('red')
# for i in range(50):
#     bob.forward(200)
#     bob.right(123)

# turtle.exitonclick()

'''
draw a hexagon in color
'''
# import turtle
# wn = turtle.Screen()
# tracy = turtle.Turtle()

# tracy.pencolor("blue")
# for i in range(6):
#     tracy.forward(100)
#     tracy.right(60)

# turtle.exitonclick()







import turtle

wn = turtle.Screen()
# screensize() set the area the turtle can draw
wn.screensize(1000, 1000)
# change the screen size
wn.setup(800, 600)
bob = turtle.Turtle()
print(turtle.screensize())
# bob.forward(100)
# bob.goto(400, 300)
# bob.forward(100)
# bob.fd(100)
'''
forward()
backward()
left()
right()
'''
bob.shape("turtle")
# bob.fillcolor('black')
# bob.begin_fill()
# bob.circle(100)
# bob.end_fill()
# bob.goto(100, 135)
# bob.begin_fill()
# bob.circle(40)
# bob.end_fill()
# bob.goto(-100, 135)
# bob.begin_fill()
# bob.circle(40)
# bob.end_fill()
turtle.colormode(255)
# bob.pencolor((100, 150, 80))

# bob.pensize(10)
# bob.speed(1)
# bob.forward(100)
# bob.speed(10)
# bob.forward(100)
# bob.penup()
# bob.goto(100, 100)
# bob.pendown()
# bob.clear()
# bob.stamp()
# bob.forward(100)
# bob.stamp()
# rgb: red green blue, (0, 255)

# n = 10
# while n <= 200:
#     bob.circle(n)
#     n = n + 10

'''
use if statement and input to create a program asking user 
if they want to draw a shap
'''

answer = input("which shape do you want to draw? circle or square\n")
if answer == "circle":
    bob.circle(100)
else:
    for i in range(4):
        bob.forward(100)
        bob.left(90)

turtle.exitonclick()
