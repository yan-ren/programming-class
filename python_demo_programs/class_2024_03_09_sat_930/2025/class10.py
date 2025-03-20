'''
Collect the stars

player moves around collecting randomly appearing start

- Use class for both Player and Star
- collision detection between player and stars
- use sprite group
'''
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
        self.rect = self.image.get_rect(
            center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        )



player = Player(WIDTH // 2, HEIGHT // 2)
stars = pygame.sprite.Group()
running = True

for _ in range(5):
    stars.add(Star())

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # draw
    screen.blit(player.image, player.rect)
    stars.draw(screen)

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()