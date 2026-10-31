import pygame

def calculate(first, second, operator):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        if second == 0:
            return "Error"
        return first / second

def main():
    pygame.init()
    screen = pygame.display.set_mode((360, 490))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    background = (25, 30, 42)
    number_color = (61, 71, 90)
    operator_color = (45, 111, 180)
    clear_color = (165, 65, 75)
    white = (245, 247, 250)

    layout = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    buttons = []
    for row in range(4):
        for column in range(4):
            x = 20 + column * 82
            y = 150 + row * 78
            rect = pygame.Rect(x, y , 74, 68)
            buttons.append((layout[row][column], rect))

    display = "0"
    first_number = None
    operator = ""
    new_number = True # next digit replaces the display instead of appending

    running = True
    while running:
        for event in pygame.event.get():
            pressed = ""
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for label, rect in buttons:
                    if rect.collidepoint(event.pos):
                        pressed = label
                        break
            
        for label, rect in buttons:
            color = number_color
            if label in ("+", "-", "*", "/", "="):
                color = operator_color
            elif label == "C":
                color = clear_color
            pygame.draw.rect(screen, color, rect, border_radius=8)
            text = font.render(label, True, white)
            screen.blit(text, text.get_rect(center=rect.center))

        pygame.display.flip()
        clock.tick(60)

main()