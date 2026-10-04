'''
snake game
'''
import pygame
import random
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

BALCK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
RED = (255, 0, 0)
GRAY = (40, 40, 40)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_cell(surface, position, color):
    col, row = position
    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

class Snake:
    def __init__(self, start):
        self.body = [start]
        self.direction = RIGHT
        self.next_direction = RIGHT

    def head(self):
        return self.body[0]

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.next_direction = new_direction

    def move(self, grow = False):
        self.direction = self.next_direction
        dx, dy = self.direction
        col, row = self.head()
        self.body.insert(0, (col + dx, row + dy))
        if not grow:
            self.body.pop()

    def draw(self, surface):
        for i, cell in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            draw_cell(surface, cell, color)

    def hit_walls(self):
        x, y = self.head()
        if 0 <= x < GRID_WIDTH or 0 <= y < GRID_HEIGHT:
            return True
        return False

    def hit_self(self):
        return self.head in self.body[1:]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        self.running = True
        self.reset()

    def reset(self):
        start = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.snake = Snake(start)
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False