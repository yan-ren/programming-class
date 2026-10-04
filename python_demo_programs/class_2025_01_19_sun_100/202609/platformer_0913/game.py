import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 64)

background = pygame.image.load("assets/background.png").convert()
player_img = pygame.image.load("assets/player.png").convert_alpha()
platform_img = pygame.image.load("assets/platform.png").convert_alpha()
coin_img = pygame.image.load("assets/coin.png").convert_alpha()
flag_img = pygame.image.load("assets/flag.png").convert_alpha()

MOVE_SPEED = 5
JUMP_SPEED = -14
GRAVITY = 0.7

class Player:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

    def update(self):
        dx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= MOVE_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += MOVE_SPEED

        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.vel_y = JUMP_SPEED
            self.on_ground = False

        self.rect.x += dx

        # keep player within the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # make gravity jump
        self.vel_y += GRAVITY
        if self.vel_y > 16:
            self.vel_y = 16

        dy = self.vel_y

        self.on_ground = False

        for platform in platforms:
            if self.rect.move(0, dy).collidedict(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    dy = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
                    dy = 0
        self.rect.y += dy

    def draw(self):
        screen.blit(self.image, self.rect)

class Platform:
    def __init__(self, x, y, width_tiles=1):
        self.image = pygame.Surface((64 * width_tiles, 32), pygame.SRCALPHA)
        for i in range(width_tiles):
            self.image.blit(platform_img, (i * 64, 0))

        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        screen.blit(self.image, self.rect)

class Coin:
    def __init__(self, x, y):
        self.image = coin_img
        self.rect = self.image.get_rect(center=(x, y))
        self.collected = False

    def draw(self):
        if not self.collected:
            screen.blit(self.image, self.rect)

def reset_game():
    player = Player(80, 420)

    platforms = [
        Platform(0, 500, 15),
        Platform(180, 410, 3),
        Platform(390, 340, 3),
        Platform(610, 275, 3),
        Platform(800, 380, 2),
    ]

    coins = [
        Coin(260, 370),
        Coin(470, 300),
        Coin(690, 235),
        Coin(850, 340),
    ]

    goal = flag_img.get_rect(bottomright=(940, 500))

    return player, platforms, coins, goal


player, platforms, coins, goal = reset_game()
won = False
game_over = False
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, platforms, coins, goal = reset_game()
                won = False
                game_over = False

    if not won and not game_over:
        player.update(platforms)

        # coin collections
        for coin in coins:
            if not coin.collected and player.rect.colliderect(coin.rect):
                coin.collected = True
                player.score += 1



pygame.quit()
sys.exit()