import arcade
import random
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Rock Paper Scissors'
CHOICES = ['Rock', 'Paper', 'Scissors']


class GameState(Enum):
    NOT_STARTED = 0
    ROUND_ACTIVE = 1
    ROUND_DONE = 2
    GAME_OVER = 3


class AttackType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.5
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type, x, y):
        super().__init__()
        self.attack_type = attack_type
        self.textures = self.load_textures()

        self.scale = self.ATTACK_SCALE
        self.current_texture_index = 0
        self.set_texture(self.current_texture_index)

        self.center_x = x
        self.center_y = y
        self.time_since_last_swap = 0.0
        self.animation_update_time = 1.0 / self.ANIMATION_SPEED

    def load_textures(self):
        """Load the correct textures for each attack type."""
        if self.attack_type == AttackType.ROCK:
            return [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            return [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png"),
            ]
        else:  # AttackType.SCISSORS
            return [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors-close.png"),
            ]

    def update_animation(self, delta_time: float = 1 / 60):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture_index = (self.current_texture_index + 1) % len(self.textures)
            self.set_texture(self.current_texture_index)
            self.time_since_last_swap = 0.0


class RPSGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        self.game_state = GameState.NOT_STARTED
        self.player_choice = None
        self.computer_choice = None
        self.result = "Press SPACE to start!"
        self.player_score = 0
        self.computer_score = 0

        # Initialize the sprite lists
        self.attack_animations = arcade.SpriteList()
        self.face_sprites = arcade.SpriteList()
        self.choice_sprites = arcade.SpriteList()
        
        # Create player and computer face sprites with same width
        DESIRED_WIDTH = 100
        
        # Load player face and calculate scale
        self.player_face = arcade.Sprite("assets/faceBeard.png")
        player_scale = DESIRED_WIDTH / self.player_face.width
        self.player_face.scale = player_scale
        self.player_face.center_x = 200
        self.player_face.center_y = 420
        
        # Load computer face and calculate scale
        self.computer_face = arcade.Sprite("assets/compy.png")
        computer_scale = DESIRED_WIDTH / self.computer_face.width
        self.computer_face.scale = computer_scale
        self.computer_face.center_x = 600
        self.computer_face.center_y = 420
        
        # Add faces to the face sprite list
        self.face_sprites.append(self.player_face)
        self.face_sprites.append(self.computer_face)
        
        # Create choice sprites (initially hidden)
        self.player_choice_sprite = arcade.Sprite()
        self.player_choice_sprite.center_x = 200
        self.player_choice_sprite.center_y = 320  # Positioned below the face
        
        self.computer_choice_sprite = arcade.Sprite()
        self.computer_choice_sprite.center_x = 600
        self.computer_choice_sprite.center_y = 320  # Positioned below the face
        
        # Add choice sprites to the choice sprite list
        self.choice_sprites.append(self.player_choice_sprite)
        self.choice_sprites.append(self.computer_choice_sprite)

        # Load attack animations and add them to the sprite list
        self.rock = AttackAnimation(AttackType.ROCK, 200, 200)
        self.paper = AttackAnimation(AttackType.PAPER, 400, 200)
        self.scissors = AttackAnimation(AttackType.SCISSORS, 600, 200)

        self.attack_animations.append(self.rock)
        self.attack_animations.append(self.paper)
        self.attack_animations.append(self.scissors)

    def on_draw(self):
        """Render the game visuals."""
        self.clear()
        arcade.draw_text('Rock Paper Scissors', SCREEN_WIDTH // 2,
                         SCREEN_HEIGHT - 50, arcade.color.BLACK, 18, anchor_x='center')

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(self.result, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.BLACK, 18,
                             anchor_x='center')
        else:
            # Draw faces
            self.face_sprites.draw()
            
            # Draw choices if they exist
            if self.player_choice and self.computer_choice:
                self.choice_sprites.draw()
                
            # Draw score and result
            arcade.draw_text(f'Score: {self.player_score} - {self.computer_score} Computer', SCREEN_WIDTH // 2,
                             50, arcade.color.BLACK, 16, anchor_x='center')
            arcade.draw_text(self.result, SCREEN_WIDTH // 2, 100, arcade.color.BLACK, 18, anchor_x='center')

            # Draw attack options and prompt
            if self.game_state == GameState.ROUND_ACTIVE:
                arcade.draw_text('Choose your attack!', SCREEN_WIDTH // 2,
                              350, arcade.color.BLACK, 16, anchor_x='center')
                self.attack_animations.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """Detects player clicks to choose an attack based on texture."""
        if self.game_state == GameState.ROUND_ACTIVE:
            for animation in self.attack_animations:
                # Check if the click is within the sprite's bounds
                if animation.left < x < animation.right and animation.bottom < y < animation.top:
                    # Map the AttackType to the corresponding choice string
                    if animation.attack_type == AttackType.ROCK:
                        player_choice = "Rock"
                    elif animation.attack_type == AttackType.PAPER:
                        player_choice = "Paper"
                    elif animation.attack_type == AttackType.SCISSORS:
                        player_choice = "Scissors"

                    self.play_game(player_choice)
                    break


    def on_key_press(self, key, modifiers):
        """Handles keyboard inputs for game state changes."""
        if key == arcade.key.SPACE and self.game_state in [GameState.NOT_STARTED, GameState.ROUND_DONE]:
            self.result = "Choose Rock, Paper, or Scissors!"
            self.game_state = GameState.ROUND_ACTIVE
            self.player_choice = None
            self.computer_choice = None
        elif key == arcade.key.ENTER and self.game_state == GameState.GAME_OVER:
            self.player_score = 0
            self.computer_score = 0
            self.game_state = GameState.NOT_STARTED
            self.result = "Press SPACE to start!"

    def play_game(self, player_choice):
        """Determines round result and updates game state."""
        self.player_choice = player_choice
        self.computer_choice = random.choice(CHOICES)

        # Update player choice sprite
        if self.player_choice == "Rock":
            self.player_choice_sprite.texture = arcade.load_texture("assets/srock.png")
        elif self.player_choice == "Paper":
            self.player_choice_sprite.texture = arcade.load_texture("assets/spaper.png")
        else:  # Scissors
            self.player_choice_sprite.texture = arcade.load_texture("assets/scissors.png")
            
        # Update computer choice sprite
        if self.computer_choice == "Rock":
            self.computer_choice_sprite.texture = arcade.load_texture("assets/srock.png")
        elif self.computer_choice == "Paper":
            self.computer_choice_sprite.texture = arcade.load_texture("assets/spaper.png")
        else:  # Scissors
            self.computer_choice_sprite.texture = arcade.load_texture("assets/scissors.png")

        if self.player_choice == self.computer_choice:
            self.result = "It's a tie! Press SPACE to restart."
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
                (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
                (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "You win this round! Press SPACE to restart."
            self.player_score += 1
        else:
            self.result = "You lose this round! Press SPACE to restart."
            self.computer_score += 1

        if self.player_score == 3:
            self.result = "Congratulations! You won the game! Press ENTER to restart."
            self.game_state = GameState.GAME_OVER
        elif self.computer_score == 3:
            self.result = "Game over! Computer wins! Press ENTER to restart."
            self.game_state = GameState.GAME_OVER
        else:
            self.game_state = GameState.ROUND_DONE

    def on_update(self, delta_time):
        for animation in self.attack_animations:
            animation.update_animation(delta_time)


game = RPSGame()
arcade.run()
