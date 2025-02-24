import random
import time
import turtle

wn = turtle.Screen()
wn.setup(600, 600)

pen = turtle.Turtle()

for i in range(10):
    v1 = random.randint(1, 6)
    v2 = random.randint(1, 6)
    pen.clear()
    pen.write(v1, align='center', font=('Arial', 20, 'normal'))

    time.sleep(1)

turtle.done()