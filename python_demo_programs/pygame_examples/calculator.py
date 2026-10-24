"""A beginner-friendly Pygame calculator.

Install: python -m pip install pygame
Run:     python pygame_calculator.py

Click the buttons or use the keyboard. Enter means =, Escape means C.
This version accepts whole-number input and calculates one operation at a time.
For example: 12 + 3 =. Results can be negative or decimal.
Teaching order: draw buttons, detect clicks, store input, calculate, add keyboard.
"""

import pygame


def calculate(first, second, operator):
    """Keep the arithmetic separate from the Pygame drawing code."""
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
    # 1. Set up the window, fonts, and colors.
    pygame.init()
    screen = pygame.display.set_mode((360, 490))
    pygame.display.set_caption("My Calculator")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    background = (25, 30, 42)
    number_color = (61, 71, 90)
    operator_color = (45, 111, 180)
    clear_color = (165, 65, 75)
    white = (245, 247, 250)

    # 2. Each button is a label paired with a Rect.
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
            rect = pygame.Rect(x, y, 74, 68)
            buttons.append((layout[row][column], rect))

    # 3. These variables remember what the user has entered.
    display = "0"
    first_number = None
    operator = ""
    new_number = True  # Next digit replaces the display instead of appending.

    running = True
    while running:
        # 4. Handle events. Mouse and keyboard produce the same button label.
        for event in pygame.event.get():
            pressed = ""
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for label, rect in buttons:
                    if rect.collidepoint(event.pos):
                        pressed = label
                        break
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    pressed = "="
                elif event.key == pygame.K_ESCAPE:
                    pressed = "C"
                elif event.unicode in "0123456789+-*/=cC":
                    pressed = event.unicode.upper()

            # 5. Update the calculator's state.
            if pressed.isdigit():
                if new_number or display == "0":
                    display = pressed
                    new_number = False
                elif len(display) < 12:
                    display += pressed

            elif pressed == "C":
                display = "0"
                first_number = None
                operator = ""
                new_number = True

            elif pressed in ("+", "-", "*", "/"):
                if display != "Error":
                    # Before the second number, another operator replaces it.
                    # After the second number, press = before a new operation.
                    if operator == "" or new_number:
                        first_number = float(display)
                        operator = pressed
                        new_number = True

            elif pressed == "=":
                if operator != "" and not new_number:
                    result = calculate(first_number, float(display), operator)
                    if result == "Error":
                        display = "Error"
                    else:
                        display = format(result, ".10g")
                    first_number = None
                    operator = ""
                    new_number = True

        # 6. Draw everything again on each frame.
        screen.fill(background)
        title = small_font.render("MY CALCULATOR", True, white)
        screen.blit(title, (20, 15))

        pygame.draw.rect(screen, (235, 240, 245), (20, 45, 320, 90))
        if operator != "":
            pending = format(first_number, ".10g") + " " + operator
            text = small_font.render(pending, True, number_color)
            screen.blit(text, (30, 53))
        text = font.render(display, True, background)
        screen.blit(text, text.get_rect(midright=(330, 104)))

        for label, rect in buttons:
            color = number_color
            if label in ("+", "-", "*", "/", "="):
                color = operator_color
            elif label == "C":
                color = clear_color
            pygame.draw.rect(screen, color, rect, border_radius=8)
            text = font.render(label, True, white)
            screen.blit(text, text.get_rect(center=rect.center))

        hint = small_font.render("Enter = result    Esc = clear", True, white)
        screen.blit(hint, (20, 466))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
