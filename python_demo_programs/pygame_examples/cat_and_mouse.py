import pygame
import sys, random

pygame.init()
# constant, a variable with fixed value
WIDTH = 800
HEIGHT = 600
display = pygame.display.set_mode((WIDTH, HEIGHT))

# frame per second
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
cat_img = pygame.image.load('cat.png')
mouse_img = pygame.image.load('mouse.png')
# global variable, a variable can be accessed at anywhere in the program
mouse_x = HEIGHT / 2
mouse_y = WIDTH / 2
cat_x = HEIGHT / 2
cat_x_change = 0
cat_y = WIDTH / 2
cat_y_change = 0
change_mouse = 0
# game loop
# game frame will refresh each time
# you need a clock to control the refresh speed,
# otherwise the refresh will happen as quickly as possible

def mouse_change_position():
    global mouse_x, mouse_y
    mouse_x = random.randint(0, WIDTH - mouse_img.get_width())
    mouse_y = random.randint(0, HEIGHT - mouse_img.get_height())

# event
# events are operations that triggers game state change, such as clicks or keyboard presses
while True:
    # event loop
    for event in pygame.event.get():
        # handle exit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # handle keyboard pressing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_x_change = -10
            elif event.key == pygame.K_RIGHT:
                cat_x_change = 10
            elif event.key == pygame.K_UP:
                cat_y_change = -10
            elif event.key == pygame.K_DOWN:
                cat_y_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                cat_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                cat_y_change = 0
    # change x, y
    cat_x += cat_x_change
    cat_y += cat_y_change
    # cat stays inside the window
    if cat_x < 0:
        cat_x = 0
    elif cat_x > WIDTH - cat_img.get_width():
        cat_x = WIDTH - cat_img.get_width()

    if cat_y < 0:
        cat_y = 0
    elif cat_y > HEIGHT - cat_img.get_height():
        cat_y = HEIGHT - cat_img.get_height()

    # loop will run 60 times per second
    # mouse_change_position() will be called every 60 times
    # => mouse will change position every second
    if change_mouse == FPS * 2:
        mouse_change_position()
        change_mouse = 0
    else:
        change_mouse += 1

    # display an image to the screen
    display.fill(WHITE)
    display.blit(cat_img, (cat_x, cat_y))
    display.blit(mouse_img, (mouse_x, mouse_y))

    pygame.display.update()
    # loop with run 60 times in one second
    clock.tick(FPS)