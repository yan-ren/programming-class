# Pygame Blitting Demo

A small, progressive set of scripts for teaching `blit()` in pygame — from a
single static image to a tiny playable game. Each file builds on the last.

## Setup

```
pip install pygame
```

Run each script from inside this folder (they load images with the relative
path `assets/...`):

```
python 01_basic_blit.py
```

## What "blit" means

`blit()` copies pixels from one `Surface` onto another `Surface`. Every image
you load with `pygame.image.load()` is a `Surface`, and the window itself
(`screen`) is also a `Surface`. So "drawing an image" is really just:

```python
screen.blit(image, position)
```

Whatever you blit **last** is drawn **on top** — like stacking transparent
sheets of film.

## The files, in teaching order

| File | New concept |
|---|---|
| `01_basic_blit.py` | The minimum: load two images, blit background then a sprite, game loop, `.convert()` vs `.convert_alpha()` |
| `02_moving_sprite.py` | `image.get_rect()`, moving a `Rect` with arrow keys, `clamp_ip()` to stay on screen |
| `03_multiple_images_and_transforms.py` | Blitting many images (a list of enemy rects), `pygame.transform.scale()`, `pygame.transform.rotate()`, `set_alpha()` for transparency |
| `04_full_demo.py` | `pygame.sprite.Sprite` / `pygame.sprite.Group`, animating a sprite sheet with `subsurface()`, collision detection with `spritecollide()`, a text HUD |

## Suggested lesson flow

1. **Run `01`** and ask students to change `player_pos` to move the ship — show that blit position is just an (x, y) tuple.
2. Point out **draw order**: swap the two blit lines in `01` and show the ship disappears behind the background.
3. **Run `02`** and explain why we use a `Rect` instead of two loose numbers — it's what collision detection and `clamp_ip` need.
4. **Run `03`** and highlight that `transform.scale()` / `transform.rotate()` return brand-new surfaces — they never modify the original image.
5. **Run `04`** and connect it back to `03`: `Group.draw(screen)` is doing the exact same `screen.blit(image, rect)` loop the students wrote by hand, just packaged into a class.

## Assets

All images in `assets/` are simple placeholder art (generated procedurally),
so there are no licensing concerns — swap them for your own `.png` files any
time. Just keep the same filenames or update the `pygame.image.load()` calls.

- `background.png` – starfield, loaded with `.convert()` (no transparency needed)
- `player.png`, `enemy.png`, `coin.png` – loaded with `.convert_alpha()` (transparent corners)
- `explosion_sheet.png` – a 4-frame sprite sheet (each frame 64×64 px), used in `04_full_demo.py`

## Common gotchas to flag for students

- Forgetting `.convert_alpha()` on transparent PNGs → transparent areas render as black or magenta boxes.
- Blitting the background *after* the sprites → sprites vanish.
- Calling `pygame.transform.rotate()`/`scale()` every frame on the *same* variable and reassigning it, instead of keeping the original image around — repeated rotation of an already-rotated image causes quality loss and size drift.
- Not calling `clock.tick(60)` → the game runs as fast as the CPU allows, differently on every computer.
