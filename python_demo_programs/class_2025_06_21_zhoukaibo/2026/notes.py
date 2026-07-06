"""
Pygame Lesson 2 (simple version): Two Bouncing Balls
----------------------------------------------------
The easiest collision that works and never sticks.

Two ideas only:
  1. The balls touch when the gap between their centers is smaller
     than their two radii combined.
  2. Bounce ONLY if they are getting closer. After a bounce they are
     moving apart, so the bounce can't fire twice in a row and glue
     the balls together. This check is the whole anti-stick fix.

The bounce itself: the balls simply trade speeds, like a Newton's
cradle. That's not perfect physics for off-center hits (see
two_balls.py for the realistic version), but it always looks
believable and the code stays tiny.

Run it with:  python two_balls_simple.py
"""

import pygame

# 1. Initialize pygame
pygame.init()

# 2. Create the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Bouncing Balls (simple)")

# 3. Set up variables
clock = pygame.time.Clock()
BALL_RADIUS = 30

ball1_x = WIDTH // 4
ball1_y = HEIGHT // 2
speed1_x = 4
speed1_y = 3

ball2_x = WIDTH * 3 // 4
ball2_y = HEIGHT // 3
speed2_x = -3
speed2_y = 4

BACKGROUND = (20, 20, 40)            # dark blue
BALL1_COLOR = (255, 100, 100)        # soft red
BALL2_COLOR = (100, 200, 255)        # sky blue

# 4. The GAME LOOP
running = True
while running:

    # --- A. Handle events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- B. Update the game state ---
    ball1_x += speed1_x
    ball1_y += speed1_y
    ball2_x += speed2_x
    ball2_y += speed2_y

    # Walls: abs() forces the ball back toward the inside, so a ball
    # can never get trapped flipping its speed every frame.
    if ball1_x - BALL_RADIUS <= 0:
        speed1_x = abs(speed1_x)
    elif ball1_x + BALL_RADIUS >= WIDTH:
        speed1_x = -abs(speed1_x)
    if ball1_y - BALL_RADIUS <= 0:
        speed1_y = abs(speed1_y)
    elif ball1_y + BALL_RADIUS >= HEIGHT:
        speed1_y = -abs(speed1_y)

    if ball2_x - BALL_RADIUS <= 0:
        speed2_x = abs(speed2_x)
    elif ball2_x + BALL_RADIUS >= WIDTH:
        speed2_x = -abs(speed2_x)
    if ball2_y - BALL_RADIUS <= 0:
        speed2_y = abs(speed2_y)
    elif ball2_y + BALL_RADIUS >= HEIGHT:
        speed2_y = -abs(speed2_y)

    # --- Ball vs ball collision (the simple way) ---

    # The gap between the centers now...
    dx = ball2_x - ball1_x
    dy = ball2_y - ball1_y
    # ...and what the gap will be one frame from now
    next_dx = dx + speed2_x - speed1_x
    next_dy = dy + speed2_y - speed1_y

    # Comparing SQUARED distances gives the same answer with no
    # square root needed (if a*a < b*b then a < b, for positives).
    touching = dx * dx + dy * dy <= (2 * BALL_RADIUS) ** 2
    getting_closer = next_dx * next_dx + next_dy * next_dy < dx * dx + dy * dy

    if touching and getting_closer:
        # Trade speeds, like a Newton's cradle.
        speed1_x, speed2_x = speed2_x, speed1_x
        speed1_y, speed2_y = speed2_y, speed1_y

    # --- C. Draw everything ---
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, BALL1_COLOR, (ball1_x, ball1_y), BALL_RADIUS)
    pygame.draw.circle(screen, BALL2_COLOR, (ball2_x, ball2_y), BALL_RADIUS)
    pygame.display.flip()

    # --- D. 60 frames per second ---
    clock.tick(60)

# 5. Quit cleanly
pygame.quit()