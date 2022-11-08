import pygame
import random

pygame.init()
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

game_over = False

# snake variables
x = 200
y = 150
x_change = 0
y_change = 0
snake_block = 10
snake_speed = 5
snake_length = 1
snake_list = []

# food variables
food_width = snake_block
#         food_x = round(random.randrange(0, display_width - snake_block))
'''
[0, 800-10) 
e.g. 450 / 10 -> 45.0
'''
food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
print(food_x, food_y)
clock = pygame.time.Clock()

score_font = pygame.font.SysFont('comicsansms', 35)


def display_score(d: pygame.display, score: int):
    text = score_font.render('Your Score:'+str(score), True, BLUE)
    d.blit(text, [0, 0])


while not game_over: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= snake_speed
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_speed
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_speed
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_speed
                x_change = 0

    if x >= display_width or x < 0 or y >= display_height or y < 0:
        game_over = True

    # update food position
    if food_x <= x <= food_x + food_width and food_y <= y <= food_y + food_width:
        food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
        snake_length += 1
        print('snake length:', snake_length)

    # update snake position
    # [[1, 1], [1, 2]] -> [[1,2], [1, 3]]
    x += x_change
    y += y_change
    snake_head = [x, y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # stop snake run into itself
    for position in snake_list[:-1]:
        if snake_head == position:
            game_over = True

    display.fill(WHITE)
    # draw food
    pygame.draw.rect(display, BLUE, [food_x, food_y, food_width, food_width])
    # draw snake
    for position in snake_list:
        pygame.draw.rect(display, RED, [position[0], position[1], snake_block, snake_block])
    # display score
    display_score(display, len(snake_list) - 1)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
