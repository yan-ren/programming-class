import pygame
import sys
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# color: R G B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 255)
LIGHT_BLUE = (100, 160, 255)
RED = (255, 60, 60)
GREEN = (60, 200, 100)

button_font = pygame.font.SysFont(None, 50)
hud_font = pygame.font.SysFont(None, 50)
big_font = pygame.font.SysFont(None, 90)

clock = pygame.time.Clock()
button_width, button_height = 240, 80
button_rect = pygame.Rect(
    (WIDTH - button_width) // 2,
    (HEIGHT - button_height) // 2 + 60,
    button_width,
    button_height
)

GAME_DURATION = 60

playing = False
game_over = False
score = 0
time_left = GAME_DURATION
last_tick = 0

target_radius = 30
target_x = WIDTH // 2
target_y = HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            # Click on START / PLAY AGAIN button
            if not playing and button_rect.collidepoint(event.pos):
                playing = True
                game_over = False
                score = 0
                time_left = GAME_DURATION
                last_tick = pygame.time.get_ticks()
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius + 70, HEIGHT - target_radius)
            elif playing:
                dx = mx - target_x
                dy = my - target_y
                if dx * dx + dy * dy <= target_radius * target_radius:
                    score += 1
                    target_x = random.randint(target_radius, WIDTH - target_radius)
                    target_y = random.randint(target_radius + 70, HEIGHT - target_radius)

    if playing:
        now = pygame.time.get_ticks()
        if now - last_tick >= 1000:
            time_left -= 1
            last_tick = now
            if time_left <= 0:
                playing = False
                game_over = True


    screen.fill(WHITE)

    if playing:
        # show score on the left, show time on the right
        score_label = hud_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_label, (20, 20))
        time_label = hud_font.render(f"Time: {time_left}", True, RED)
        screen.blit(time_label, (WIDTH - time_label.get_width() - 20, 20))

        # draw target dot
        pygame.draw.circle(screen, RED, (target_x, target_y), target_radius)
        pygame.draw.circle(screen, BLACK, (target_x, target_y), target_radius, 3)
    else:
        if game_over:
            title = big_font.render(f"Score: {score}", True, GREEN)
            button_text = "PLAY AGAIN"
        else:
            title = big_font.render("Click the Dot!", True, BLUE)
            button_text = "START"

        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        screen.blit(title, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        color = LIGHT_BLUE if button_rect.collidepoint(mouse_pos) else BLUE
        pygame.draw.rect(screen, color, button_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, button_rect, 3, border_radius=10)

        label = button_font.render(button_text, True, WHITE)
        rect = label.get_rect(center=button_rect.center)
        screen.blit(label, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
