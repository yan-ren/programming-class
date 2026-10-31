import turtle

wn = turtle.Screen()
wn.bgcolor('light yellow')
tess = turtle.Turtle()
tess.speed(10)
tess.color('blue')
tess.shape('turtle')

# range(5, 60, 2)
# [5, 7, 9, 11, 13, ..., 59]
tess.up()
tess.color('red')
for size in range(5, 300, 2):
    tess.stamp()
    tess.forward(size)
    tess.right(42)

tess.color('green')
for size in range(300, 5, -2):
    tess.stamp()
    tess.forward(size)
    tess.right(36)

wn.exitonclick()