import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setup(800, 600)
wn.tracer(0)

score = 0
time_left = 60
game_over = False

TARGET_TYPES = [
    ('red', 1),    # common
    ('red', 1),    # weighted to appear more often
    ('blue', 2),   # uncommon
    ('gold', 3),   # rare
]

score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color('black')
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

timer_turtle = turtle.Turtle()
timer_turtle.speed(0)
timer_turtle.color('black')
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(200, 260)

legend_turtle = turtle.Turtle()
legend_turtle.speed(0)
legend_turtle.penup()
legend_turtle.hideturtle()
legend_turtle.goto(-370, 260)

gameover_turtle = turtle.Turtle()
gameover_turtle.speed(0)
gameover_turtle.color('darkred')
gameover_turtle.penup()
gameover_turtle.hideturtle()
gameover_turtle.goto(0, 0)

def update_score():
    score_turtle.clear()
    score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

def update_timer():
    timer_turtle.clear()
    color = 'red' if time_left <= 10 else 'black'
    timer_turtle.color(color)
    timer_turtle.write(f'Time: {time_left}s', align='center', font=('Courier', 24, 'normal'))

def draw_legend():
    legend_turtle.write('● +1  ● +2  ● +3', align='left', font=('Courier', 13, 'normal'))

def show_game_over():
    gameover_turtle.write(f'GAME OVER\nFinal Score: {score}',
                          align='center', font=('Courier', 36, 'bold'))

targets = []


def create_target(color):
    target = turtle.Turtle()
    target.shape('circle')
    target.color(color)
    target.penup()
    target.speed(0)
    targets.append(target)
    return target


def move_target(target):
    if game_over:
        return
    target.goto(random.randint(-390, 390), random.randint(-290, 290))
    wn.ontimer(lambda: move_target(target), 3000)

def get_points(color):
    for target_color, points in TARGET_TYPES:
        if target_color == color:
            return points
    return 1

def click_target(x, y, target):
    global score
    score += get_points(target.pencolor())
    update_score()
    move_target(target)


def bind_click_event(target):
    target.onclick(lambda x, y: click_target(x, y, target))


def setup_targets():
    for _ in range(3):                          # 3 red targets
        t = create_target('red')
        move_target(t)
        bind_click_event(t)
    for _ in range(2):                          # 2 blue targets
        t = create_target('blue')
        move_target(t)
        bind_click_event(t)
    t = create_target('gold')                   # 1 gold target
    move_target(t)
    bind_click_event(t)

def countdown():

setup_targets()
wn.mainloop()
