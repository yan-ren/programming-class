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
gravity = 0.2

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

    speed_y += gravity
    speed2_y += gravity

    ball_x += speed_x
    ball_y += speed_y
    ball2_x += speed2_x
    ball2_y += speed2_y

    if ball_x - BALL_RADIUS <= 0:
        speed_x = abs(speed_x)
    elif ball_x + BALL_RADIUS >= WIDTH:
        speed_x = -abs(speed_x)
    if ball_y - BALL_RADIUS <= 0:
        speed_y = abs(speed_y)
    elif ball_y + BALL_RADIUS >= HEIGHT:
        speed_y = -abs(speed_y)

    if ball2_x - BALL_RADIUS <= 0:
        speed2_x = abs(speed2_x)
    elif ball2_x + BALL_RADIUS >= WIDTH:
        speed2_x = -abs(speed2_x)
    if ball2_y - BALL_RADIUS <= 0:
        speed2_y = abs(speed2_y)
    elif ball2_y + BALL_RADIUS >= HEIGHT:
        speed2_y = -abs(speed2_y)

    dx = ball2_x - ball_x
    dy = ball2_y - ball_y
    next_dx = dx + speed2_x - speed_x
    next_dy = dy + speed2_y - speed_y

    touching = dx * dx + dy * dy <= (2 * BALL_RADIUS) ** 2
    getting_closer = next_dx * next_dx + next_dy * next_dy < dx * dx + dy * dy

    if touching and getting_closer:
        speed_x, speed2_x = speed2_x, speed_x
        speed_y, speed2_y = speed2_y, speed_y

    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)
    pygame.draw.circle(screen, BALL_COLOR, (int(ball2_x), int(ball2_y)), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)