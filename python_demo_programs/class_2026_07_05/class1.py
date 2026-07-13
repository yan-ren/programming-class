import sys

import pygame

BOARD_SIZE = 600
BAR_HEIGHT = 90
WIDTH, HEIGHT = BOARD_SIZE, BOARD_SIZE + BAR_HEIGHT
CELL = BOARD_SIZE // 3
LINE_W = 19
MARK_W = 14
PADDING = 45

HUMAN, COMPUTER = "X", "O"
MAX_MARKS = 3

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
BAR_COLOR = (18, 122, 111)
X_COLOR = (66, 66, 66)
O_COLOR = (242, 235, 211)
TEXT_COLOR = (250, 250, 250)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font(None, 52)
clock = pygame.time.Clock()

WIN_LINES = [
    # ROWS
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
    # COLUMNS
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
    # DIAGONALS
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],
]

def empty_cells(board):
    result = []
    for c in range(3):
        for r in range(3):
            if board[r][c] is None:
               result.append((r, c))

    return result


def winner(board):
    for line in WIN_LINES:
        values = []
        for r, c in line:
            values.append(board[r][c])
        if values[0] is not None and values[0] == values[1] == values[2]:
            return values[0]
    return None


def place_mark(board, moves, mark, cell):
    if len(moves) == MAX_MARKS:
        old_r, old_c = moves.pop(0)
        board[old_r][old_c] = None
    moves.append(cell)
    board[cell[0]][cell[1]] = mark


def find_winning_move(board, moves, mark):
    for r, c in empty_cells(board):
        test = [row[:] for row in board]
        if len(moves) == MAX_MARKS:
            old_r, old_c = moves[0]
            test[old_r][old_c] = None
        test[r][c] = mark
        if winner(test) == mark:
            return (r, c)
    return None

def draw_grid():
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, BAR_COLOR, (0, BOARD_SIZE, WIDTH, BAR_HEIGHT))
    for i in (1, 2):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL), (BOARD_SIZE, i * CELL), LINE_W)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL, 0), (i * CELL, BOARD_SIZE), LINE_W)

def main():
    board = new_board()
    player = 'X'
    game_over = False
    status = "X's turn"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board, turn = new_board(), 'X'
                game_over, ai_move_at = False, None
                status = "Your turn (you are X)"
                
        draw_grid()
        pygame.display.flip()
        clock.tick(60)

main()