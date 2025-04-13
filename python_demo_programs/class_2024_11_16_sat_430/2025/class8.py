import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Game')
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2

        self.change_x = 0
        self.change_y = 0

        arcade.set_background_color(arcade.color.DARK_SLATE_BLUE)

    def on_draw(self):
        # Clear the screen
        self.clear()
        arcade.draw_lbwh_rectangle_filled(
            self.player_x,
            self.player_y,
            width=50,
            height=50,
            color=arcade.color.BLUE
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.change_x = 0

    def on_update(self, delta_time):
        # Update player position with boundary checking
        new_x = self.player_x + self.change_x
        new_y = self.player_y + self.change_y

        # Check boundaries
        if 25 <= new_x <= SCREEN_WIDTH - 25 and 25 <= new_y <= SCREEN_HEIGHT - 25:
            self.player_x = new_x
            self.player_y = new_y

def main():
    window = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()