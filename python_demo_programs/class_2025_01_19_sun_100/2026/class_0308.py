import turtle


screen = turtle.Screen()
screen.setup(600, 800)

button = turtle.Turtle()
button.hideturtle()
button.penup()
button.speed(0)

message = turtle.Turtle()
message.hideturtle()
message.penup()

button_x = -60
button_y = -20
button_width = 120
button_height = 40

# hover effect
current_color = 'lightblue'
hovering = False

def draw_button(color):
    button.clear()
    button.goto(button_x, button_y)
    button.fillcolor(color)
    button.begin_fill()

    button.pendown()
    for _ in range(2):
        button.forward(button_width)
        button.left(90)
        button.forward(button_height)
        button.left(90)

    button.end_fill()
    button.penup()
    button.goto(button_x + button_width / 2, button_y + 10)
    button.write("CLICK", align="center", font=("Arial", 16, "bold"))

def is_inside(x, y):
    return button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height

def mouse_move(event):
    global hovering

    canvas = screen.getcanvas()
    x = event.x - canvas.winfo_width() / 2
    y = canvas.winfo_height() / 2 - event.y

    inside = is_inside(x, y)
    if inside and not hovering:
        hovering = True
        draw_button('orange')
    elif not inside and hovering:
        hovering = False
        draw_button('lightblue')

def button_click(x, y):
    if is_inside(x, y):
        button.clear()
        message.goto(0, 100)
        message.write("Button Clicked!", align="center", font=("Arial", 24, "bold"))

draw_button(current_color)
screen.onclick(button_click)
screen.getcanvas().bind("<Motion>", mouse_move)

turtle.done()