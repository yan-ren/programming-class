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
    while not valid_input:
        row = int(input(f"Player {current_player} — enter row (0-2): "))
        col = int(input(f"Player {current_player} — enter col (0-2): "))
