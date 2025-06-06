'''
Collect the stars

player moves around collecting randomly appearing start

- Use class for both Player and Star
- collision detection between player and stars
- use sprite group
'''
from pycparser.ply.yacc import restart
from pygame import font

'''
1. when Player runs into star, star moves to another random place within the screen
2. add a score to track how many stars that Player has taken
3. star should change the location every 3 seconds, if not taken by Player
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
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
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
        self.last_move_time = pygame.time.get_ticks()  # Track time for movement
        self.relocate()

    def relocate(self):
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    def update(self, *args, **kwargs):
        if pygame.time.get_ticks() - self.last_move_time > 3000:  # 3 seconds
            self.relocate()
            self.last_move_time = pygame.time.get_ticks()


def reset_game():
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    stars.empty()
    for _ in range(5):
        stars.add(Star())
    return pygame.time.get_ticks(), 0, False


player = Player(WIDTH // 2, HEIGHT // 2, BLUE)
stars = pygame.sprite.Group()
running = True
score = 0
high_score = 0
clock = pygame.time.Clock()
game_duration = 60
start_ticks = pygame.time.get_ticks()
game_over = False

for _ in range(5):
    stars.add(Star())

while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    seconds = (current_time - start_ticks) // 1000
    time_left = max(0, game_duration - seconds)

    if not game_over:
        player.update(keys)
        stars.update()
        for star in stars:
            if player.rect.colliderect(star.rect):
                star.relocate()
                score += 1
        if time_left <= 0:
            game_over = True
            if score > high_score:
                high_score = score

        screen.blit(player.image, player.rect)
        stars.draw(screen)

        score_text = font.render(f"Score: {score}", True, BLUE)
        timer_text = font.render(f"Time: {time_left}", True, BLACK)
        high_text = font.render(f"High Score: {high_score}", True, BLACK)

        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (WIDTH - 130, 10))
        screen.blit(high_text, (10, 50))
    else:
        over_text = font.render("Time's up!", True, BLACK)
        restart_text = font.render('Press SPACE to Restart', True, BLUE)
        final_score_text = font.render(f'Your Score: {score}', True, BLACK)
        high_score_text = font.render(f'High Score: {high_score}', True, BLACK)

        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT
                                 // 2 - 60))
        screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT// 2 - 20))
        screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 20))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))

        if keys[pygame.K_SPACE]:
            start_ticks, score, game_over = reset_game()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
