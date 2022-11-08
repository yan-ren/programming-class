import pygame

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.update()
game_over = False

# rgb: Red Green Blue
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
x = 200
y = 150

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10

    display.fill(WHITE)
    pygame.draw.rect(display, BLUE, [x, y, 10, 10])
    pygame.display.update()
pygame.quit()
quit()