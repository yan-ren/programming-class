
import pygame
import sys
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Platformer")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 64)

ASSET_DIR = Path(__file__).parent / "assets"

background = pygame.image.load(ASSET_DIR / "background.png").convert()
player_img = pygame.image.load(ASSET_DIR / "player.png").convert_alpha()
platform_img = pygame.image.load(ASSET_DIR / "platform.png").convert_alpha()
coin_img = pygame.image.load(ASSET_DIR / "coin.png").convert_alpha()
flag_img = pygame.image.load(ASSET_DIR / "flag.png").convert_alpha()

GRAVITY = 0.7
MOVE_SPEED = 5
JUMP_SPEED = -14


class Player:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

    def update(self, platforms):
        dx = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= MOVE_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += MOVE_SPEED

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_SPEED
            self.on_ground = False

        # Horizontal movement
        self.rect.x += dx

        # Keep player inside screen horizontally
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)

        # Gravity
        self.vel_y += GRAVITY
        if self.vel_y > 16:
            self.vel_y = 16

        dy = self.vel_y

        # Vertical collision
        self.on_ground = False

        for platform in platforms:
            if self.rect.move(0, dy).colliderect(platform.rect):
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


player, platforms, coins, goal_rect = reset_game()
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
                player, platforms, coins, goal_rect = reset_game()
                won = False
                game_over = False

    if not won and not game_over:
        player.update(platforms)

        # Coin collection
        for coin in coins:
            if not coin.collected and player.rect.colliderect(coin.rect):
                coin.collected = True
                player.score += 1

        # Goal
        if player.rect.colliderect(goal_rect):
            won = True

        # Falling off the map
        if player.rect.top > HEIGHT:
            game_over = True

    # Draw
    screen.blit(background, (0, 0))

    for platform in platforms:
        platform.draw()

    for coin in coins:
        coin.draw()

    screen.blit(flag_img, goal_rect)
    player.draw()

    score_text = font.render(f"Coins: {player.score}/{len(coins)}", True, (20, 20, 20))
    screen.blit(score_text, (20, 20))

    help_text = font.render("Move: A/D or arrows   Jump: SPACE   Restart: R", True, (20, 20, 20))
    screen.blit(help_text, (20, 55))

    if won:
        text = big_font.render("You Win!", True, (20, 100, 20))
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))

        sub = font.render("Press R to play again", True, (20, 20, 20))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    if game_over:
        text = big_font.render("Game Over", True, (180, 30, 30))
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))

        sub = font.render("Press R to restart", True, (20, 20, 20))
        screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))

    pygame.display.flip()

pygame.quit()
sys.exit()
