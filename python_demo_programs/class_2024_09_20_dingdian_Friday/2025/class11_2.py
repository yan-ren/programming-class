import turtle

# Setup screen
screen = turtle.Screen()
screen.title("RGB Trail - Follow the Mouse")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
turtle.colormode(1.0)  # Enable RGB colors from 0.0 to 1.0

# Follower turtle
follower = turtle.Turtle()
follower.shape("circle")
follower.color((0.0, 1.0, 1.0))  # Cyan in RGB
follower.penup()
follower.speed(0)

# Mouse position tracking
mouse_x, mouse_y = 0, 0

def mouse_move(x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, y

screen.onscreenclick(mouse_move)
screen.getcanvas().bind("<Motion>", lambda evt: mouse_move(evt.x - screen.window_width()//2, screen.window_height()//2 - evt.y))
screen.listen()

# Store trail dots
trail = []

def leave_rgb_trail():
    dot = turtle.Turtle()
    dot.shape("circle")
    dot.shapesize(0.4)
    dot.penup()
    dot.goto(follower.position())
    dot.speed(0)
    dot.color((0.0, 1.0, 1.0))  # Start with bright cyan
    dot.rgb = [0.0, 1.0, 1.0]   # Custom attribute for fading
    trail.append(dot)

def update_trail():
    for dot in trail[:]:
        # Fade the RGB values
        dot.rgb = [max(0.0, c - 0.02) for c in dot.rgb]
        dot.color(tuple(dot.rgb))
        dot.fillcolor(tuple(dot.rgb))
        if sum(dot.rgb) <= 0.05:
            dot.hideturtle()
            trail.remove(dot)

def game_loop():
    x, y = follower.position()
    dx = mouse_x - x
    dy = mouse_y - y
    distance = (dx**2 + dy**2)**0.5

    if distance > 1:
        follower.setheading(follower.towards(mouse_x, mouse_y))
        follower.forward(min(distance / 10, 10))
        leave_rgb_trail()

    update_trail()
    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()
