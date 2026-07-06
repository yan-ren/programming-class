"""Tic Tac Toe vs the computer -- endless version, someone always wins.

You are X; click a square to play, and the computer answers with O.
Twist: each player can only have three marks on the board. Placing a
fourth removes your oldest mark, so there are no draws -- the game keeps
going until somebody gets three in a row. Press R to restart.

The computer follows three simple rules:
    1. If it can win right now, it does.
    2. Else, if the player could win next move, it blocks that square.
    3. Otherwise it picks a random empty square.
"""

import random
import sys

import pygame

# --- Settings -----------------------------------------------------------------
BOARD_SIZE = 600                # the board is a square
BAR_HEIGHT = 90                 # message bar below the board
CELL = BOARD_SIZE // 3          # size of one square
PADDING = 45                    # how far marks stay from the cell edges

HUMAN, COMPUTER = "X", "O"
MAX_MARKS = 3                   # marks each player may have on the board

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
BAR_COLOR = (18, 122, 111)
X_COLOR = (66, 66, 66)
O_COLOR = (242, 235, 211)
TEXT_COLOR = (250, 250, 250)

WIN_LINES = [
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # rows
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # columns
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],                            # diagonals
]


# --- Game logic -----------------------------------------------------------------
def empty_cells(board):
    """All (row, col) squares that are still free."""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]


def winner(board):
    """Return 'X' or 'O' if someone has three in a row, else None."""
    for line in WIN_LINES:
        values = [board[r][c] for r, c in line]
        if values[0] is not None and values[0] == values[1] == values[2]:
            return values[0]
    return None


def place_mark(board, moves, mark, cell):
    """Put `mark` on `cell`. A player may only have MAX_MARKS marks, so
    placing a new one first removes that player's oldest mark."""
    if len(moves) == MAX_MARKS:
        old_r, old_c = moves.pop(0)     # forget the oldest move...
        board[old_r][old_c] = None      # ...and clear it from the board
    moves.append(cell)
    board[cell[0]][cell[1]] = mark


def find_winning_move(board, moves, mark):
    """Return a square where `mark` would win right now, or None.

    Tries every empty square on a copy of the board, exactly like a real
    move (the oldest mark disappears too), and checks for three in a row.
    """
    for r, c in empty_cells(board):
        test = [row[:] for row in board]      # a copy we can scribble on
        if len(moves) == MAX_MARKS:
            old_r, old_c = moves[0]
            test[old_r][old_c] = None         # the oldest mark would vanish
        test[r][c] = mark
        if winner(test) == mark:
            return (r, c)
    return None


def computer_move(board, computer_moves, human_moves):
    """Three simple rules: win if you can, block if you must, else random."""
    move = find_winning_move(board, computer_moves, COMPUTER)   # 1. win
    if move:
        return move
    move = find_winning_move(board, human_moves, HUMAN)         # 2. block
    if move:
        return move
    return random.choice(empty_cells(board))                    # 3. random


# --- Pygame setup -----------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE + BAR_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font(None, 52)
clock = pygame.time.Clock()


def draw_screen(board, status):
    """Draw the grid, all the marks, and the message bar."""
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, BAR_COLOR, (0, BOARD_SIZE, BOARD_SIZE, BAR_HEIGHT))
    for i in (1, 2):    # the four grid lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL), (BOARD_SIZE, i * CELL), 10)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL, 0), (i * CELL, BOARD_SIZE), 10)

    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                x1, y1 = c * CELL + PADDING, r * CELL + PADDING
                x2, y2 = (c + 1) * CELL - PADDING, (r + 1) * CELL - PADDING
                pygame.draw.line(screen, X_COLOR, (x1, y1), (x2, y2), 14)
                pygame.draw.line(screen, X_COLOR, (x1, y2), (x2, y1), 14)
            elif board[r][c] == "O":
                center = (c * CELL + CELL // 2, r * CELL + CELL // 2)
                pygame.draw.circle(screen, O_COLOR, center, CELL // 2 - PADDING, 14)

    label = font.render(status, True, TEXT_COLOR)
    rect = label.get_rect(center=(BOARD_SIZE // 2, BOARD_SIZE + BAR_HEIGHT // 2))
    screen.blit(label, rect)
    pygame.display.flip()


# --- Main game loop -----------------------------------------------------------------
def main():
    board = [[None] * 3 for _ in range(3)]   # 3x3 grid, None means empty
    human_moves = []                         # each player's moves, oldest first
    computer_moves = []
    game_over = False
    status = "Your turn (you are X)"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:  # restart
                board = [[None] * 3 for _ in range(3)]
                human_moves, computer_moves = [], []
                game_over = False
                status = "Your turn (you are X)"

            if (event.type == pygame.MOUSEBUTTONDOWN and not game_over
                    and event.pos[1] < BOARD_SIZE):
                row, col = event.pos[1] // CELL, event.pos[0] // CELL
                if board[row][col] is None:
                    # the player's move
                    place_mark(board, human_moves, HUMAN, (row, col))
                    if winner(board) == HUMAN:
                        status = "You win!  Press R to play again"
                        game_over = True
                    else:
                        # show it briefly, then the computer answers
                        draw_screen(board, "Computer is thinking...")
                        pygame.time.wait(400)
                        cell = computer_move(board, computer_moves, human_moves)
                        place_mark(board, computer_moves, COMPUTER, cell)
                        if winner(board) == COMPUTER:
                            status = "Computer wins.  Press R to play again"
                            game_over = True

        draw_screen(board, status)
        clock.tick(60)


if __name__ == "__main__":
    main()