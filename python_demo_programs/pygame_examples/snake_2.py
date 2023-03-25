import pygame
import random

WIDTH = 800
HEIGHT = 600

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()

game_over = False

snake_x = WIDTH / 2
snake_y = HEIGHT / 2

snake_speed_x = 0
snake_speed_y = 0

clock = pygame.time.Clock()


def draw_score(score):
    score_font = pygame.font.SysFont("comicsansms", 35)
    value = score_font.render("Your score: " + str(score), True, RED)
    display.blit(value, [0, 0])

def get_random_food():
    return random.randrange(0, WIDTH - 10) // 10 * 10, random.randrange(0, HEIGHT - 10) // 10 * 10


def draw_snake(snake_body):
    for x, y in snake_body:
        pygame.draw.rect(display, BLUE, [x, y, 10, 10])


food_x, food_y = get_random_food()
snake_body = []
snake_length = 1

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed_y = -10
                snake_speed_x = 0
            elif event.key == pygame.K_RIGHT:
                snake_speed_x = 10
                snake_speed_y = 0
            elif event.key == pygame.K_LEFT:
                snake_speed_x = -10
                snake_speed_y = 0
            elif event.key == pygame.K_DOWN:
                snake_speed_y = 10
                snake_speed_x = 0

    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True

    snake_x += snake_speed_x
    snake_y += snake_speed_y
    display.fill(WHITE)
    # pygame.draw.rect(display, BLUE, [snake_x, snake_y, 10, 10])
    pygame.draw.rect(display, RED, [food_x, food_y, 10, 10])
    # populate snake body list
    # add head
    snake_head = (snake_x, snake_y)
    snake_body.append(snake_head)
    # remove tail
    if len(snake_body) > snake_length:
        del snake_body[0]
    draw_snake(snake_body)
    draw_score(snake_length - 1)

    # when snake eats food
    if food_x - 2 < snake_x < food_x + 2 and food_y - 2 < snake_y < food_y + 2:
        food_x, food_y = get_random_food()
        snake_length += 1

    # when snake runs into itself
    for x in snake_body[0:len(snake_body) - 1]:
        if x == snake_head:
            game_over = True

    pygame.display.update()

    clock.tick(30)


pygame.quit()
quit()