board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

turn = 'X'
winner = None

for move in range(9):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

    print('Player', turn, 'turn')
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != ' ':
        print('This spot is taken. Try again.')
        continue

    board[row][col] = turn

    for i in range(3):
        # row
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = turn
        # col
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = turn

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = turn
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = turn

    if winner:
        for row in board:
            print('|'.join(row))
            print('-' * 5)
        print('Player', winner, 'wins!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

if not winner:
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    print('Tie')