import turtle

wn = turtle.Screen()
wn.setup(800, 600)
alex = turtle.Turtle()

'''
turtle color
pencolor
fillcolor
'''
# alex.pencolor('red')
# alex.fillcolor('green')

# alex.color('red') # set pencolor and fillcolor all together

# RGB R - red G - Green B - Blue

# (0, 255)
# Painting Red Yellow Blue
# wn.colormode(255)
# alex.color((20, 20, 20))
# alex.color('#34ebba')
alex.pensize(5)
alex.speed(8)
# alex.circle(40)
# 360
number_of_squares = 72
for i in range(number_of_squares):
    for color in ['yellow', 'red', 'purple']:
        alex.color(color)
        alex.forward(150)
        alex.left(120)

    alex.left(360 / number_of_squares)

wn.exitonclick()

# practice: how to draw pentagon/hexagon
