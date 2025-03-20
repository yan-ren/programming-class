import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.width < WIDTH:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Obstacle:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -self.height
            self.x = random.randint(0, WIDTH - self.width)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


player = Player(WIDTH // 2 - 25, HEIGHT - 60, 50, 20, 5, (0, 255, 255))
obstacle = Obstacle(random.randint(0, WIDTH - 50), -50, 50, 20, 5, (255, 0, 0))

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    obstacle.move()

    screen.fill((30, 30, 30))
    player.draw(screen)
    obstacle.draw(screen)
    pygame.display.update()

pygame.quit()
