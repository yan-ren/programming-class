# temp = [20.5, 21.0, 19.8, 22.3]
#
# for i in temp:
#     print(i)
#
# for i in range(len(temp)):
#     print(temp[i])

# def f(x):
#     if x < 0:
#         return x**2
#     else:
#         return x+2
#
# print(f(-3))
# print(f(5))

'''
Demonstrate how to achieve mouse control in python turtle
- A turtle object follows the mouse
- The closer you are, the slower it moves to create a smooth 'chase' effect
'''
import random
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.tracer(0)
screen.bgcolor('black')
turtle.colormode(1.0)

follower = turtle.Turtle()
follower.shape('circle')
follower.color((0.0, 1.0, 1.0))
follower.penup()
follower.speed(0)

mouse_x, mouse_y = 0, 0

def mouse_move(x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, y


screen.onscreenclick(mouse_move)
screen.getcanvas().bind("<Motion>", lambda evt: mouse_move(evt.x - screen.window_width()//2, screen.window_height()//2 - evt.y))
screen.listen()

trail = []

def leave_rgb_trail():
    dot = turtle.Turtle()
    dot.shape('circle')
    dot.shapesize(0.4)
    dot.penup()
    dot.goto(follower.position())
    dot.speed(0)
    dot.color((0.0, 1.0, 1.0))
    dot.rgb = [0.0, 1.0, 1.0]
    trail.append(dot)

def update_trail():
    for dot in trail[:]:
        dot.rgb = [max(0.0, c - 0.02) for c in dot.rgb]
        dot.color(tuple(dot.rgb))
        dot.fillcolor(tuple(dot.rgb))
        if sum(dot.rgb) <= 0.05:
            dot.hideturtle()
            trail.remove(dot)


def game_loop():
    # x, y = follower.position()
    # dx = mouse_x - x
    # dy = mouse_y - y
    # distance = (dx**2 + dy**2) ** 0.5
    #
    # if distance > 1:
    #     follower.setheading(follower.towards(mouse_x, mouse_y))
    #     follower.forward(min(distance / 10, 10))
    #     leave_rgb_trail()
    #
    # update_trail()
    # screen.update()
    # screen.ontimer(game_loop, 10)

    if random.random() < 0.05:
        follower.setheading(random.randint(0, 360))

    follower.forward(5)
    x, y = follower.position()
    if x < -390 or x > 390:
        follower.setheading(180 - follower.heading())
    if y < -290 or y > 290:
        follower.setheading(-follower.heading())

    leave_rgb_trail()
    update_trail()
    screen.update()
    screen.ontimer(game_loop, 30)

game_loop()
screen.mainloop()


'''
Write a Turtle program that:

Asks the user how many sides the polygon should have.

Draws that polygon repeatedly in a circular pattern.

Uses random colors for each repetition.
'''