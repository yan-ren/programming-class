import turtle

# Screen setup
win = turtle.Screen()
win.title("Tic Tac Toe")
win.bgcolor("white")
win.setup(width=600, height=600)
win.tracer(0)

# Draw the grid
grid = turtle.Turtle()
grid.color("black")
grid.pensize(3)
grid.penup()
grid.goto(-100, 300)
grid.pendown()
grid.goto(-100, -300)
grid.penup()
grid.goto(100, 300)
grid.pendown()
grid.goto(100, -300)
grid.penup()
grid.goto(-300, 100)
grid.pendown()
grid.goto(300, 100)
grid.penup()
grid.goto(-300, -100)
grid.pendown()
grid.goto(300, -100)
grid.hideturtle()

# Create X and O turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Create a turtle for displaying the winner
winner_turtle = turtle.Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()

# Game state variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_x(x, y):
    t.penup()
    t.goto(x - 50, y - 50)
    t.pendown()
    t.goto(x + 50, y + 50)
    t.penup()
    t.goto(x - 50, y + 50)
    t.pendown()
    t.goto(x + 50, y - 50)

def draw_o(x, y):
    t.penup()
    t.goto(x, y - 50)
    t.pendown()
    t.circle(50)

def draw_move(row, col):
    x, y = col * 200 - 200, 200 - row * 200
    if board[row][col] == "X":
        draw_x(x, y)
    elif board[row][col] == "O":
        draw_o(x, y)

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def check_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def display_winner(winner):
    winner_turtle.goto(0, 0)
    winner_turtle.write(f"{winner} wins!", align="center", font=("Arial", 24, "normal"))

def click_handler(x, y):
    global current_player, game_over

    if game_over:
        return

    # Convert (x, y) to row and column
    col = int((x + 300) // 200)
    row = int((300 - y) // 200)

    if col > 2 or row > 2 or col < 0 or row < 0:
        return

    if board[row][col] == "":
        board[row][col] = current_player
        draw_move(row, col)
        winner = check_winner()
        if winner:
            display_winner(winner)
            game_over = True
        elif check_draw():
            winner_turtle.goto(0, 0)
            winner_turtle.write("It's a draw!", align="center", font=("Arial", 24, "normal"))
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

# Click event listener
win.listen()
win.onclick(click_handler)

# Main game loop
while True:
    win.update()
