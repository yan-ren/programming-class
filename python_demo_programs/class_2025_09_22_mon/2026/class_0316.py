board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

current_player = "X"
winner = None
game_over = False

while not game_over:
    # print the board
    print('\n  0   1   2')
    for i, row in enumerate(board):
        print(f'{i} ' + ' | '.join(row))
        if i < 2:
            print(" ---+---+---")
    print()

    valid_input = False
    row = ''
    col = ''
    while not valid_input:
        row = int(input(f"Player {current_player} — enter row (0-2): "))
        col = int(input(f"Player {current_player} — enter col (0-2): "))
        # check if row or column is valid
        if row not in range(3) or col not in range(3):
            print('Numbers must be between 0 and 2. Try again.')
        elif board[row][col] != ' ':
            print('That cell is already taken! Try again.')
        else:
            valid_input = True

    board[row][col] = current_player

    # check rows
    for row_check in board:
        if row_check[0] == row_check[1] == row_check[2] == current_player:
            winner = current_player

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == current_player:
            winner = current_player

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        winner = current_player
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        winner = current_player

    # check draw
    draw = True
    for row_check in board:
        for cell in row_check:
            if cell == ' ':
                draw = False

    # end game or switch player
    if winner:
        game_over = True
    elif draw:
        game_over = True
    else:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

print('\n  0   1   2')
for i, row in enumerate(board):
    print(f'{i} ' + ' | '.join(row))
    if i < 2:
        print(" ---+---+---")
print()

if winner:
    print(f'\nPlayer {winner} wins!')
else:
    print('\nIt is a draw!')
