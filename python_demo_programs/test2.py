def check_winner(player):
    # check rows and columns
    for i in range(6):
        if all(board[i][j] == player for j in range(6)) or all(board[j][i] == player
                                                               for j in range(6)):
            return True

    # check diagonals
    if all(board[i][i] == player for i in range(6)) or all(board[i][5-i] == player
                                                           for i in range(6)):
        return True

    return False


board = [[0 for _ in range(6)] for _ in range(6)]

# given a 6x6 matrix, check if there is 5 consecutive
def check_victory(board, turn, rot):
    rows, cols = len(board), len(board[0])
    player1 = 1
    player2 = 2

    # check rows and columns
    for i in range(rows):
        for j in range(cols):
            # check rows
            if j + 5 <= cols and all(board[i][j+k] == player1 for k in range(5)):
                return player1
            elif j + 5 <= cols and all(board[i][j+k] == player2 for k in range(5)):
                return player2

            # check column
            if i + 5 <= rows and all(board[i+k][j] == player1 for k in range(5)):
                return player1
            elif i + 5 <= rows and all(board[i+k][j] == player2 for k in range(5)):
                return player2

    # check diagonals
    for i in range(rows):
        for j in range(cols):
            # check diagonal (top-left to bottom-right)
            if i + 5 <= rows and j + 5 <= cols and all(board[i + k][j + k] == player1 for k in range(5)):
                return player1
            elif i + 5 <= rows and j + 5 <= cols and all(board[i + k][j + k] == player2 for k in range(5)):
                return player2
            # check diagonal (top-right to bottom-left)
            if i + 5 <= rows and j - 5 + 1 >= 0 and all(board[i + k][j - k] == player1 for k in range(5)):
                return player1
            elif i + 5 <= rows and j - 5 + 1 >= 0 and all(board[i + k][j - k] == player2 for k in range(5)):
                return player2


board = [[1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0]]

print(check_victory(board, 1, 1))
