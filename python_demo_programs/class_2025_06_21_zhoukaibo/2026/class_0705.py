import math
import sys
import pygame


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
speed_x = 4
speed_y = 3
BALL_RADIUS = 30

ball2_x = WIDTH * 3 // 4
ball2_y = HEIGHT // 3
speed2_x = -3
speed2_y = 4

BACKGROUND = (20, 20, 40)
BALL_COLOR = (255, 100, 100)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_x += speed_x
    ball_y += speed_y
    ball2_x += speed2_x
    ball2_y += speed2_y

    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        speed_x = -speed_x
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        speed_y = -speed_y

    if ball2_x - BALL_RADIUS <= 0 or ball2_x + BALL_RADIUS >= WIDTH:
        speed2_x = -speed2_x
    if ball2_y - BALL_RADIUS <= 0 or ball2_y + BALL_RADIUS >= HEIGHT:
        speed2_y = -speed2_y

    dx = ball2_x - ball_x
    dy = ball2_y - ball_y
    distance = math.sqrt(dx * dx + dy * dy)

    if 0 < distance <= BALL_RADIUS * 2 + 5:
        speed1_x, speed2_x = speed2_x, speed_x
        speed1_y, speed2_y = speed2_y, speed_y

        nx = dx / distance  # direction from ball 1 to ball 2,
        ny = dy / distance  # scaled to length 1
        overlap = BALL_RADIUS * 2 - distance
        ball_x -= nx * overlap / 2  # each ball gives way by half
        ball_y -= ny * overlap / 2
        ball2_x += nx * overlap / 2
        ball2_y += ny * overlap / 2

    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.circle(screen, BALL_COLOR, (int(ball2_x), int(ball2_y)), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)