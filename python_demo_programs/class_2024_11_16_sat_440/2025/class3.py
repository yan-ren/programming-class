import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

def draw_sun():
    arcade.draw_circle_filled(100, 500, 20, arcade.color.YELLOW)

def draw_house():
    arcade.draw_lbwh_rectangle_filled(400, 150, 200, 200, arcade.color.BRICK_RED)
    arcade.draw_triangle_filled(500, 500, 400, 350, 600, 350, arcade.color.DARK_BROWN)

def draw_clouds():
    arcade.draw_ellipse_filled(300, 500, 120, 80, arcade.color.WHITE)
    arcade.draw_ellipse_filled(260, 500, 120, 80, arcade.color.WHITE)
    arcade.draw_ellipse_filled(340, 500, 120, 80, arcade.color.WHITE)
    arcade.draw_ellipse_filled(300, 530, 120, 80, arcade.color.WHITE)
    arcade.draw_ellipse_filled(300, 470, 120, 80, arcade.color.WHITE)

def draw_text():
    arcade.draw_text('Welcome', 300, 500, arcade.color.BRICK_RED, 20)
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    draw_sun()
    draw_house()
    draw_clouds()
    draw_text()
    arcade.draw_arc_filled(200, 300, 100, 100, start_angle=0, end_angle=180, color=arcade.color.RED)
    arcade.draw_line(200, 300, 200, 200, arcade.color.BLUE, 3)
    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()
