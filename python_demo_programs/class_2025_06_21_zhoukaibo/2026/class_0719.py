import pygame
import random
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
GREEN      = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED        = (220, 40, 40)
GRAY       = (40, 40, 40)
STEEL_BLUE = (70, 130, 180)

UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

FPS = 15

def draw_cell(surface, position, color):
    col, row = position
    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

def draw_grid(surface):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (WINDOW_WIDTH, y))

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

    def upcoming_head(self):
        dx, dy = self.next_direction
        col, row = self.head()
        return (col + dx, row + dy)

    def move(self, grow=False):
        self.direction = self.next_direction
        dx, dy = self.direction
        col, row = self.head()
        self.body.insert(0, (col + dx, row + dy))
        if not grow:
            self.body.pop()
            