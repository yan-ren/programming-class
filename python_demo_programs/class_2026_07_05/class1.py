import sys

import pygame

BOARD_SIZE = 600
BAR_HEIGHT = 90
WIDTH, HEIGHT = BOARD_SIZE, BOARD_SIZE + BAR_HEIGHT
CELL = BOARD_SIZE // 3
LINE_W = 19
MARK_W = 14
PADDING = 45

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

def new_board():
    return [[None] * 3 for _ in range(3)]


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