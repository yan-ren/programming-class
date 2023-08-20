import turtle
tina = turtle.Turtle()

def _circle(x,y,color,size):
    tina.up()
    tina.goto(x,y)
    tina.down()
    tina.begin_fill()
    tina.fillcolor(color)
    tina.circle(size)
    tina.end_fill()


_circle(0,-100,"black",100)
_circle(100,50,"black",50)
_circle(-100,50,"black",50)

turtle.done()
