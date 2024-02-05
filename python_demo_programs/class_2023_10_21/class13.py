'''
list = []
list.append(1)
print(list)
list.append(2)
print(list)

print(list[0])
list[0] = 100
print(list)

list = [1, 2, 3, 4, 5, 6]
index = len(list) - 1
while index >= 0:
    print(list[index])
    index -= 1

del list[4]
print(list)
'''
import turtle

wn = turtle.Screen()
wn.setup(800, 600)
wn.tracer(0)
wn.bgcolor('black')

# left paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(5, 1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()

while True:
    wn.update()