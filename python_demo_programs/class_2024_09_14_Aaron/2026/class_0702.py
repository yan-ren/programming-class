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

# wall barrier settings
WALL_SEGMENTS = 3
WALL_MIN_LEN = 5
WALL_MAX_LEN = 7
WALL_SAFE_RADIUS = 4
WALL_CHANGE_INTERVAL = 10000 # ms


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

    def hit_walls(self):
        x, y = self.head()
        return not (0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT)

    def hit_self(self):
        return self.head() in self.body[1:]

    def hit_barrier(self, wall_cells):
        return self.head() in wall_cells

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

class Wall:
    def __init__(self, blocked):
        self.cells = set()
        self.respawn(blocked)

    def respawn(self, blocked):
        self.cells = set()
        for _ in range(WALL_SEGMENTS):
            self.cells |= self._random_segment(blocked | self.cells)

    def _random_segment(self, blocked):
        """A straight horizontal or vertical run of cells that avoids blocked"""
        for _ in range(100): # repeat until a free spot is found
            length = random.randint(WALL_MIN_LEN, WALL_MAX_LEN)
            if random.random() < 0.5: # horizontal
                col = random.randint(0, GRID_WIDTH - length)
                row = random.randint(0, GRID_HEIGHT - 1)
                segment = {(col + i, row) for i in range(length)}
            else: # vertical
                col = random.randint(0, GRID_WIDTH - 1)
                row = random.randint(0, GRID_HEIGHT - length)
                segment = {(col, row + i) for i in range(length)}
            if not (segment & blocked):
                return segment

        return set()

    def draw(self, surface):
        for cell in self.cells:
            draw_cell(surface, cell, STEEL_BLUE)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('consolas', 24)
        self.running = True
        self.high_score = 0
        self.reset()

    def reset(self):
        start = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.snake = Snake(start)
        self.walls = Wall(set(self.snake.body) | self._head_safety_zone())
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False
        self.last_wall_change = pygame.time.get_ticks()
        self.run_start = pygame.time.get_ticks()
        self.elapsed_ms = 0

    def _head_safety_zone(self):
        cx, cy = self.snake.head()
        r = WALL_SAFE_RADIUS
        return {(cx + dx, cy + dy) for dx in range(-r, r + 1) for dy in range(-r, r + 1) if abs(dx) + abs(dy) <= r}

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

    def draw(self):
        self.screen.fill(BLACK)
        draw_grid(self.screen)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.walls.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        best_text = self.font.render(f"Best: {self.high_score}", True, WHITE)
        self.screen.blit(best_text, (WINDOW_WIDTH - best_text.get_width() - 10, 10))

        seconds = self.elapsed_ms // 1000
        time_text = self.font.render(f'Time: {seconds // 60:02d}:{seconds % 60:02d}', True, WHITE)
        self.screen.blit(time_text, (WINDOW_WIDTH // 2 - time_text.get_width() // 2, 10))

        if self.game_over:
            line1 = self.font.render('Game Over!', True, WHITE)
            line2 = self.font.render('Press SPACE to play again', True, WHITE)
            self.screen.blit(line1, (WINDOW_WIDTH // 2 - line1.get_width() // 2, WINDOW_HEIGHT // 2 - 30))
            self.screen.blit(line2, (WINDOW_WIDTH // 2 - line2.get_width() // 2, WINDOW_HEIGHT // 2 + 5))

        pygame.display.flip()

    def update(self):
        if self.game_over:
            return

        now = pygame.time.get_ticks()
        self.elapsed_ms = now - self.run_start

        if now - self.last_wall_change >= WALL_CHANGE_INTERVAL:
            blocked = (set(self.snake.body) | self._head_safety_zone() | {self.food.position})
            self.walls.respawn(blocked)
            self.last_wall_change = now

        will_eat = self.snake.upcoming_head() == self.food.position
        self.snake.move(grow=will_eat)

        if will_eat:
            self.score += 1
            self.high_score = max(self.high_score, self.score)
            self.food.respawn(self.snake.body)
        if self.snake.hit_walls() or self.snake.hit_self() or self.snake.hit_barrier(self.walls.cells):
            self.game_over = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

Game().run()

'''
complete snake game
- wall
- snake runs into itself
- barrier
- high score
- timer
'''
