import turtle
tina = turtle.Turtle()
tina.hideturtle()


def draw_circle(x, y, color, size):
    tina.up()
    tina.goto(x,y)
    tina.down()
    tina.begin_fill()
    tina.fillcolor(color)
    tina.circle(size)
    tina.end_fill()


draw_circle(0, -100, "black", 100)
draw_circle(100, 50, "lime", 50)
draw_circle(-100, 50, "lime", 50)

turtle.done()
