import random
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


def computer_move(board, computer_moves, human_moves):
    # win
    # move = find_winning_move(board, computer_moves, COMPUTER)
    # if move:
    #     return move
    # move = find_winning_move(board, human_moves, HUMAN)
    # if move:
    #     return move
    return random.choice(empty_cells(board))


def draw_screen(board, status):
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, BAR_COLOR, (0, BOARD_SIZE, BOARD_SIZE, BAR_HEIGHT))
    # four grid lines
    for i in (1, 2):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL), (BOARD_SIZE, i * CELL), 10)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL, 0), (i * CELL, BOARD_SIZE), 10)

    for r in range(3):
        for c in range(3):
            if board[r][c] == 'X':
                x1, y1 = c * CELL + PADDING, r * CELL + PADDING
                x2, y2 = (c + 1) * CELL - PADDING, (r + 1) * CELL - PADDING
                pygame.draw.line(screen, X_COLOR, (x1, y1), (x2, y2), 14)
                pygame.draw.line(screen, X_COLOR, (x1, y2), (x2, y1), 14)
            elif board[r][c] == 'O':
                center = (c * CELL + CELL // 2, r * CELL + CELL // 2)
                pygame.draw.circle(screen, O_COLOR, center, CELL // 2 - PADDING, 14)
    label = font.render(status, True, TEXT_COLOR)
    rect = label.get_rect(center=(BOARD_SIZE // 2, BOARD_SIZE + BAR_HEIGHT // 2))
    screen.blit(label, rect)
    pygame.display.flip()


def main():
    # 3x3 grid
    board = [[None] * 3 for _ in range(3)]
    human_moves = []
    computer_moves = []
    game_over = False
    status = "Your turn (you are X)"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # restart
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = [[None] * 3 for _ in range(3)]
                human_moves = []
                computer_moves = []
                game_over = False
                status = "Your turn (you are X)"

            if (event.type == pygame.MOUSEBUTTONDOWN and not game_over and event.pos[1] < BOARD_SIZE):
                row, col = event.pos[1] // CELL, event.pos[0] // CELL
                if board[row][col] is None:
                    place_mark(board, human_moves, HUMAN, (row, col))
                    if winner(board) == HUMAN:
                        status = "You win! Press R to play again"
                        game_over = True
                    else:
                        draw_screen(board, 'Computer is thinking...')
                        pygame.time.wait(400)
                        cell = computer_move(board, computer_moves, human_moves)
                        place_mark(board, computer_moves, COMPUTER, cell)
                        if winner(board) == COMPUTER:
                            status = 'Computer wins. Press R to play again'
                            game_over = True

        draw_screen(board, status)
        clock.tick(60)

main()