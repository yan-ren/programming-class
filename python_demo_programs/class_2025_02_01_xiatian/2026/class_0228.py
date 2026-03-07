import time
import turtle
import random


wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setup(800, 600)

score = 0
misses = 0
MAX_MISSES = 50
GAME_OVER = False
GAME_TIME = 60
start_time = time.time()

def make_turtle(x, y):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    return t

score_turtle  = make_turtle(0, 260)
miss_turtle   = make_turtle(0, 225)
timer_turtle  = make_turtle(0, 190)
banner_turtle = make_turtle(0, 0)

def update_score():
    score_turtle.clear()
    score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

    miss_turtle.clear()
    miss_turtle.write(f'Lives: {MAX_MISSES - misses}', align='center', font=('Courier', 24, 'normal'))

def update_timer():
    if GAME_OVER:
        return
    elapsed = time.time() - start_time
    remaining = max(0, GAME_TIME - int(elapsed))
    timer_turtle.clear()
    timer_turtle.write(f'Time: {remaining}s',
                       align='center', font=('Courier', 18, 'normal'))
    if remaining == 0:
        end_game("Time's up!")
    else:
        wn.ontimer(update_timer, 500)

def end_game(reason):
    global GAME_OVER
    GAME_OVER = True
    for t in targets:
        t.hideturtle()
    banner_turtle.color('darkred')
    banner_turtle.write(f'{reason} Final score: {score}, close window to exit', align='center', font=('Courier', 26, 'bold'))

TIRE_COLORS = ['red', 'orange', 'purple', 'gold', 'cyan']

def tier_color(tier):
    return TIRE_COLORS[min(tier, len(TIRE_COLORS) - 1)]

def current_tier():
    return score // 5

targets = []
def create_target():
    target = turtle.Turtle()
    target.shape('circle')
    target.penup()
    target.speed(0)
    targets.append(target)
    return target

def move_target(target):
    if GAME_OVER:
        return

    global misses
    if target.pencolor() != 'white':
        misses += 1
        update_score()
        if misses >= MAX_MISSES:
            end_game('Out of lives!')
            return

    target.color(tier_color(current_tier()))
    target.goto(random.randint(-390, 390), random.randint(-290, 290))
    wn.ontimer(lambda: move_target(target), get_move_interval())

def get_move_interval():
    # return timer interval. gets shorter as score increases
    return max(800, 3000 - score * 80)

def click_target(x, y, target):
    global score
    score += 1
    target.color('white')
    update_score()

def bind_click_event(target):
    target.onclick(lambda x, y: click_target(x, y, target))

def setup_targets():
    for _ in range(5):
        target = create_target()
        move_target(target)
        bind_click_event(target)

update_score()
update_timer()
setup_targets()
wn.mainloop()