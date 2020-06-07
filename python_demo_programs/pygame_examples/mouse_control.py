import pygame, sys

pygame.init()
width = 800
height = 600
display = pygame.display.set_mode((width, height))

# frame per second
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
cat_img = pygame.image.load('cat.png')
cat_x = 400
cat_x_change = 0
cat_y = 300
cat_y_change = 0
# game loop
# game frame will refresh each time
# you need a clock to control the refresh speed,
# otherwise the refresh will happen as quickly as possible

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
    elif cat_x > width - cat_img.get_width():
        cat_x = width - cat_img.get_width()

    if cat_y < 0:
        cat_y = 0
    elif cat_y > height - cat_img.get_height():
        cat_y = height - cat_img.get_height()

    # display an image to the screen
    display.fill(WHITE)
    display.blit(cat_img, (cat_x, cat_y))

    pygame.display.update()
    clock.tick(FPS)