import pygame
import sys


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

button_font = pygame.font.SysFont(None, 50)
countdown_font = pygame.font.SysFont(None, 200)

clock = pygame.time.Clock()

button_width, button_height = 200, 80
button_rect = pygame.Rect(
    (WIDTH - button_width) // 2,
    (HEIGHT - button_height) // 2,
    button_width,
    button_height
)

counting_down = False
count = 5
last_tick = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not counting_down and button_rect.collidepoint(event.pos):
                counting_down = True
                count = 10
                last_tick = pygame.time.get_ticks()

    if counting_down:
        now = pygame.time.get_ticks()
        if now - last_tick >= 1000:
            count -= 1
            last_tick = now
            if count < 0:
                counting_down = False

    screen.fill(WHITE)
    if counting_down:
        text = str(count) if count > 0 else "GO!"
        color = RED if count > 0 else BLUE
        label = countdown_font.render(text, True, color)
        rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(label, rect)
    else:
        mouse_pos = pygame.mouse.get_pos()
        color = LIGHT_BLUE if button_rect.collidepoint(mouse_pos) else BLUE
        pygame.draw.rect(screen, color, button_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, button_rect, 3, border_radius=10)

        label = button_font.render('START', True, WHITE)
        rect = label.get_rect(center=button_rect.center)
        screen.blit(label, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()








