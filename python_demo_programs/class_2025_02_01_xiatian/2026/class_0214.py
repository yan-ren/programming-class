'''
Treasure collector game
- several turtles
- random treasures appear on the screen
- each turtle collects treasure
- keep score in a dictionary
- first turtle to reach a target score wins
'''
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightyellow")
wn.setup(800, 600)
wn.tracer(0)

player_data = {
    "red": {"color": "red", "speed": 3, "score": 0},
    "blue": {"color": "blue", "speed": 4, "score": 0},
    "green": {"color": "green", "speed": 2, "score": 0}
}

players = {}

for name, data in player_data.items():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(data['color'])
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-200, 200))
    players[name] = t

treasure_data = {
    'gold': {'color': 'gold', 'points': 5},
}

treasure = turtle.Turtle()
treasure.shape("circle")
treasure.color(treasure_data["gold"]["color"])
treasure.penup()
treasure.goto(random.randint(-350, 350), random.randint(-250, 250))

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)

def update_score():
    score_text = ""
    for name, data in player_data.items():
        score_text += f'{name}: {data['score']}'
    score_writer.clear()
    score_writer.write(score_text, align='center', font=('Arial', 16, 'bold'))

update_score()

def move_players():
    for name, t in players.items():
        t.forward(player_data[name]['speed'])
        t.right(random.randint(0, 20))

        if t.xcor() > 390 or t.xcor() < -390:
            t.right(180)
        if t.ycor() > 290 or t.ycor() < -290:
            t.right(180)

        if t.distance(treasure) < 20:
            player_data[name]['score'] += treasure_data['gold']['points']

            # move treasure
            treasure.goto(random.randint(-350, 350), random.randint(-250, 250))
            update_score()
            # check winner
            if player_data[name]['score'] > 100:
                score_writer.goto(0, 0)
                score_writer.write(name + " wins", align='center', font=('Arial', 24, 'bold'))
                return

    wn.update()
    wn.ontimer(move_players, 30)

move_players()
wn.mainloop()