import time
import turtle
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = turtle.Screen()
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.bgcolor('black')
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()

class Cannon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 45
        self.shape = 'triangle'
        self.power = 10

    def rotate_left(self):
        self.angle += 10

    def rotate_right(self):
        self.angle -= 10

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.5, 1)
        pen.setheading(self.angle)
        pen.stamp()


class CannonBall():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.shape = 'circle'
        self.state = 'ready'

    def update(self, GRAVITY):
        if self.state == 'fire':
            self.x += self.dx
            self.y += self.dy
            self.dy += GRAVITY

            if self.y < -300:
                self.state = 'ready'

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.5, 0.5)
        pen.stamp()

    def fire(self):
        if self.state == 'ready':
            self.x = cannon.x
            self.y = cannon.y
            self.dx = math.cos(math.radians(cannon.angle)) * cannon.power
            self.dy = math.sin(math.radians(cannon.angle)) * cannon.power
            self.state = 'fire'


cannon = Cannon(-250, -200)
cannon.render(pen)
cannonball = CannonBall(-250, -200)
cannonball.render(pen)

# keyboard control
window.listen()
window.onkeypress(cannonball.fire, 'space')
window.onkeypress(cannon.rotate_left, 'Left')
window.onkeypress(cannon.rotate_right, 'Right')

GRAVITY = -0.1

while True:
    time.sleep(0.01)
    pen.clear()
    cannonball.update(GRAVITY)
    cannon.render(pen)
    cannonball.render(pen)

    window.update()