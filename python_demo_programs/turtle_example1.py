import turtle

wn = turtle.Screen()
# screensize() set the area the turtle can draw
wn.screensize(1000, 1000)
# change the screen size
wn.setup(800, 600)
bob = turtle.Turtle()
# turtle.colormode(255)

answer = input("which shape do you want to draw? circle or square\n")
bob.pencolor('red')

if answer == "circle":
    bob.circle(100)
elif answer == 'square':
    for i in range(4):
        bob.forward(100)
        bob.left(90)
elif answer == 'triangle':
    for i in range(3):
        bob.forward(100)
        bob.right(120)


turtle.exitonclick()
