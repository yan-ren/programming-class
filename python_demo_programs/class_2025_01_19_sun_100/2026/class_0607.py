import pygame
import random
import sys


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 40, 40)
GRAY = (40, 40, 40)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

FPS = 15

def draw_cell(surface, position, color):
    col, row = position
    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

def draw_grid(surface):
    """Draw faint grid lines so the cells are visible (optional)."""
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (WINDOW_WIDTH, y))

class Food:
    def __init__(self, snake_body):
        self.position = (0, 0)
        self.respawn(snake_body)

    def respawn(self, snake_body):
        while True:
            position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT -1))
            if position not in snake_body:
                self.position = position
                return

    def draw(self, surface):
        draw_cell(surface, self.position, RED)

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

    def hits_wall(self):
        col, row = self.head()
        return not (0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT)

    def hit_self(self):
        return self.head in self.body[1:]

    def draw(self, surface):
        for i, cell in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            draw_cell(surface, cell, color)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('consolas', 24)
        self.running = True
        self.snake = Snake((GRID_WIDTH // 2, GRID_HEIGHT // 2))
        self.food = Food(self.snake.body)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)

    def update(self):
        will_eat = self.snake.upcoming_head() == self.food.position
        self.snake.move(grow=will_eat)
        if will_eat:
            self.food.respawn(self.snake.body)
        if self.snake.hits_wall() or self.snake.hit_self():
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        draw_grid(self.screen)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

Game().run()