import turtle

window = turtle.Screen()
window.title('Tic Tac Toe')
window.bgcolor('white')
window.setup(600, 600)
window.tracer(0)

# draw the grid
grid = turtle.Turtle()
grid.color('black')
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

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

board = [["", "", ""], ["", "", ""], ["", "", ""]]

def check_winner():
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def draw_x(x, y):
    pen.penup()
    pen.goto(x - 50, y - 50)
    pen.pendown()
    pen.goto(x + 50, y + 50)
    pen.penup()
    pen.goto(x - 50, y + 50)
    pen.pendown()
    pen.goto(x + 50, y - 50)

def draw_o(x, y):
    pen.penup()
    pen.goto(x, y - 50)
    pen.pendown()
    pen.circle(50)

current_player = 'X'

def draw_move(row, col):
    # find the center point x and y for row, col
    x, y = col * 200 - 200, 200 - row * 200
    if board[row][col] == 'X':
        draw_x(x, y)
    else:
        draw_o(x, y)

def click_handler(x, y):
    print(x, y)
    global current_player
    # x, y is the coordinate of mouse when make clicking
    # covert (x, y) to row and colum
    col = int((x + 300) // 200)
    row = int((300 - y) // 200)

    if col > 2 or row > 2 or col < 0 or row < 0:
        return

    if board[row][col] == "":
        board[row][col] = current_player
        draw_move(row, col)
        winner = check_winner()
        if winner:
            pen.penup()
            pen.goto(0, 0)
            pen.write(winner + " wins!", align='center', font=('Arial', 24, 'normal'))

        # switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


window.listen()
window.onclick(click_handler)


while True:
    window.update()