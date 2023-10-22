# Initialize the Pentago board (6x6 grid)
board = [[' ' for _ in range(6)] for _ in range(6)]

# Check if a player has won
def check_winner(player):
    # Check rows
    for row in range(6):
        if all(board[row][col] == player for col in range(6)):
            return True

    # Check columns
    for col in range(6):
        if all(board[row][col] == player for row in range(6)):
            return True

    # Check diagonals (top-left to bottom-right)
    if all(board[i][i] == player for i in range(6)):
        return True

    # Check diagonals (top-right to bottom-left)
    if all(board[i][5 - i] == player for i in range(6)):
        return True

    return False

# Main game loop
current_player = 'X'