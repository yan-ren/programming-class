import random

target = random.randint(0, 100)
game_continue = True

while game_continue:
    guess = int(input('guess a number between 0 to 100:'))
    if guess == target:
        print('correct!')
        game_continue = False
    elif guess > target:
        print('guess too high')
    elif guess < target:
        print('guess too low')

while target >= 0:
    print(target)
    target -= 1

