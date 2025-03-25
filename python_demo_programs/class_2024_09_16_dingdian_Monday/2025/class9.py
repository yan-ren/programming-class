import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 50
ITEM_SIZE = 30
OBSTACLE_SIZE = 40
PLAYER_SPEED = 5
ITEM_SPEED = 3
OBSTACLE_SPEED = 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collect & Dodge Game")
clock = pygame.time.Clock()

class Player:
    
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT - 100
        self.rect = pygame.Rect(self.x, self.y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = BLUE
        self.score = 0

    def move(self, dx, dy):
        self.x = max(0, min(self.x + dx, WINDOW_WIDTH - PLAYER_SIZE))
        self.y = max(0, min(self.y + dy, WINDOW_HEIGHT - PLAYER_SIZE))
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Item:
    def __init__(self):
        self.reset()
        self.color = YELLOW

    def reset(self):
        self.x = random.randint(0, WINDOW_WIDTH - ITEM_SIZE)
        self.y = -ITEM_SIZE
        self.rect = pygame.Rect(self.x, self.y, ITEM_SIZE, ITEM_SIZE)

    def move(self):
        self.y += ITEM_SPEED
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Obstacle:
    def __init__(self):
        self.reset()
        self.color = RED

    def reset(self):
        self.x = random.randint(0, WINDOW_WIDTH - OBSTACLE_SIZE)
        self.y = -OBSTACLE_SIZE
        self.rect = pygame.Rect(self.x, self.y, OBSTACLE_SIZE, OBSTACLE_SIZE)

    def move(self):
        self.y += OBSTACLE_SPEED
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

def main():
    player = Player()
    items = [Item() for _ in range(3)]
    obstacles = [Obstacle() for _ in range(2)]
    font = pygame.font.Font(None, 36)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            # Player movement
            keys = pygame.key.get_pressed()
            dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED
            dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_SPEED
            player.move(dx, dy)

            # Move items and check collisions
            for item in items:
                item.move()
                if item.rect.colliderect(player.rect):
                    player.score += 10
                    item.reset()
                elif item.y > WINDOW_HEIGHT:
                    item.reset()

            # Move obstacles and check collisions
            for obstacle in obstacles:
                obstacle.move()
                if obstacle.rect.colliderect(player.rect):
                    game_over = True
                if obstacle.y > WINDOW_HEIGHT:
                    obstacle.reset()

        # Draw everything
        screen.fill(BLACK)
        player.draw(screen)
        for item in items:
            item.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {player.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("Game Over! Press R to restart", True, WHITE)
            screen.blit(game_over_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2))

        pygame.display.flip()
        clock.tick(60)

        # Handle game restart
        if game_over and pygame.key.get_pressed()[pygame.K_r]:
            player = Player()
            items = [Item() for _ in range(3)]
            obstacles = [Obstacle() for _ in range(2)]
            game_over = False

if __name__ == "__main__":
    main()