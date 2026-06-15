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

UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

FPS = 60

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
        col, row = self.head
        return (col + dx, row + dy)

    def move(self, grow=False):
        self.direction = self.next_direction
        dx, dy = self.direction
        col, row = self.head
        self.body.insert(0, (col + dx, row + dy))
        if not grow:
            self.body.pop()

    def hit_walls(self):
        x, y = self.head
        return not (0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT)

    def hit_self(self):
        return self.head in self.body[1:]

    def draw(self, surface):
        for i, cell in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            draw_cell(surface, cell, color)

class Food:
    def __init__(self, snake_body):
        self.position = (0, 0)
        self.respawn(snake_body)

    def respawn(self, snake_body):
        while True:
            position = (random.randint(0, GRID_WIDTH - 1),
                        random.randint(0, GRID_HEIGHT - 1))

            if position not in snake_body:
                self.position = position
                return

    def draw(self, surface):
        draw_cell(surface, self.position, RED)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('consolas', 24)
        self.running = True
        self.reset()

    def reset(self):
        start = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.snake = Snake(start)
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)

