'''
Demonstrate how to achieve mouse control in python turtle
- A turtle object follows the mouse
- The closer you are, the slower it moves to create a smooth 'chase' effect
'''
import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.tracer(0)

follower = turtle.Turtle()
follower.shape('circle')
follower.color('cyan')
follower.penup()
follower.speed(0)

mouse_x, mouse_y = 0, 0

def mouse_move(x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, y

screen.onscreenclick(mouse_move)
screen.getcanvas().bind("<Motion>", lambda evt: mouse_move(evt.x - screen.window_width() // 2, screen.window_height() // 2 - evt.y))

trail = []
frame_count = 0
def game_loop():
    global frame_count
    x, y = follower.position()
    dx = mouse_x - x
    dy = mouse_y - y
    distance = (dx**2 + dy**2) ** 0.5
    if distance > 1:
        follower.setheading(follower.towards(mouse_x, mouse_y))
        follower.forward(min(distance / 10, 10))

        if frame_count % 5 == 0:
            frame_count = 0
            dot = turtle.Turtle()
            dot.shape('circle')
            dot.shapesize(0.5)
            dot.color('cyan')
            dot.penup()
            dot.goto(follower.position())
            dot.speed(0)
            trail.append(dot)

            if len(trail) > 5:
                old_dot = trail.pop(0)
                old_dot.hideturtle()
                old_dot.clear()

    frame_count += 1
    screen.update()
    screen.ontimer(game_loop, 10)

game_loop()
screen.mainloop()