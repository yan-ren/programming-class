"""
04_full_demo.py
----------------
Puts everything together into a tiny playable game:
  - pygame.sprite.Sprite / pygame.sprite.Group  (the "real" way to manage many images)
  - Blitting a sub-region of a sprite sheet (image animation)
  - Collision detection between blitted images (spritecollide)
  - A simple text HUD blitted on top of everything

Controls: LEFT / RIGHT to move, avoid the red enemies falling from the top.
Colliding with an enemy triggers an explosion animation and ends the game.

CORE IDEA:
    pygame.sprite.Sprite is a class that bundles an image + a rect together.
    A pygame.sprite.Group holds many sprites and can update() and draw() them
    all in one call -- group.draw(screen) is just a loop that blits every
    sprite's .image at its .rect, exactly like we did by hand in step 3.
"""

import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("04 - Full Demo")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

background = pygame.image.load("assets/background.png").convert()


class Player(pygame.sprite.Sprite):
    """A Sprite just needs self.image (a Surface) and self.rect (a Rect)."""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60))
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(
            topleft=(random.randint(0, SCREEN_WIDTH - 50), random.randint(-300, -40))
        )
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-300, -40)
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)


class Explosion(pygame.sprite.Sprite):
    """
    Demonstrates blitting a single frame OUT of a larger sprite sheet image,
    using Surface.subsurface(). explosion_sheet.png contains 4 frames laid
    out left-to-right, each FRAME_SIZE x FRAME_SIZE pixels.
    """

    FRAME_SIZE = 64
    FRAME_DURATION = 6  # game-loop frames to show each animation frame

    def __init__(self, center):
        super().__init__()
        self.sheet = pygame.image.load("assets/explosion_sheet.png").convert_alpha()
        self.frame_index = 0
        self.timer = 0
        self.image = self._get_frame(0)
        self.rect = self.image.get_rect(center=center)

    def _get_frame(self, index):
        x = index * self.FRAME_SIZE
        # subsurface() carves a rectangular piece OUT of an existing Surface
        # without copying pixel data -- great for sprite sheets.
        frame_rect = pygame.Rect(x, 0, self.FRAME_SIZE, self.FRAME_SIZE)
        return self.sheet.subsurface(frame_rect)

    def update(self):
        self.timer += 1
        if self.timer >= self.FRAME_DURATION:
            self.timer = 0
            self.frame_index += 1
            if self.frame_index >= 4:  # 4 frames in the sheet
                self.kill()  # removes this sprite from all Groups
                return
            self.image = self._get_frame(self.frame_index)


player = Player()
player_group = pygame.sprite.GroupSingle(player)

enemy_group = pygame.sprite.Group()
for _ in range(5):
    enemy_group.add(Enemy())

explosion_group = pygame.sprite.Group()

score = 0
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        player_group.update()
        enemy_group.update()
        score += 1

        # spritecollide checks player's rect against every enemy's rect.
        # `False` means "don't remove the enemy on collision" (we handle that ourselves).
        hit_enemies = pygame.sprite.spritecollide(player, enemy_group, False)
        if hit_enemies:
            explosion_group.add(Explosion(player.rect.center))
            player.kill()  # remove the player sprite/image from the screen
            game_over = True

    explosion_group.update()

    # --- draw order: background -> enemies -> player -> explosion -> HUD ---
    screen.blit(background, (0, 0))
    enemy_group.draw(screen)      # Group.draw() blits every sprite's image at its rect
    player_group.draw(screen)
    explosion_group.draw(screen)

    score_text = font.render(f"Score: {score // 10}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        msg = font.render("GAME OVER - close window to exit", True, (255, 80, 80))
        screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
