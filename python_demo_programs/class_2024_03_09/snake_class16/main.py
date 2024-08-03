import turtle


wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor('black')
wn.bgpic('border.gif')
wn.tracer(False)

turtle.register_shape('upmouth.gif')
turtle.register_shape('food.gif')
turtle.register_shape('downmouth.gif')
turtle.register_shape('leftmouth.gif')
turtle.register_shape('rightmouth.gif')
turtle.register_shape('body.gif')

head = turtle.Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

def go_up():
    head.direction = 'up'
    head.shape('upmouth.gif')

def go_down():
    head.direction = 'down'
    head.shape('downmouth.gif')

def go_left():
    head.direction = 'left'
    head.shape('leftmouth.gif')

def go_right():
    head.direction = 'right'
    head.shape('rightmouth.gif')


wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')
wn.listen()

while True:
    wn.update()

turtle.done()
