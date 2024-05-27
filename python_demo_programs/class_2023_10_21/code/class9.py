# s = 'abcdef'
#
# for i in s:
#     print(i)
#
# '''
# Print from 0 to 9, using for loop
# '''
# for i in range(10):
#     print(i)
#
# # break in for loop
# for i in range(10):
#     if i == 2:
#         break

import turtle

window = turtle.Screen()
window.setup(800, 600)

t = turtle.Turtle()
t.shape('turtle')
t.fillcolor('lawn green')
# t.pencolor('')
t.pensize(3)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.up()
t.goto(0, 100)
t.down()

for i in range(3):
    t.forward(100)
    t.left(120)

t.write("Hello", font=("Arial", 20, "normal"))
turtle.exitonclick()
turtle.done()
