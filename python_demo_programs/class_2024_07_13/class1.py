import turtle

SCREEN_SIZE = 800
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)

# one turtle object to draw snakes
snake = turtle.Turtle()
wn.addshape('upmouth.gif')

snake.shape('upmouth.gif')
# snake.color('pink')
snake.penup()

turtle.onkeypress(lambda: snake.setheading(90), 'Up')

turtle.done()

