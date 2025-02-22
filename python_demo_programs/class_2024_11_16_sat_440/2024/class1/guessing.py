import random

while True:
    min_bound = int(input('Enter the minimum bound (default 0):') or 0)
    max_bound = int(input('Enter the maximum bound (default 100):') or 100)

    random_number = random.randint(min_bound, max_bound)
    attempts = 0
    print(f'Have chosen a random number between {min_bound} and {max_bound}')

    while True:
        guess = int(input('Enter your guess:'))
        attempts = attempts + 1

        if guess < random_number:
            print(f'Wrong choice, the number is greater than {guess}')
        elif guess > random_number:
            print(f'Wrong choice, the number is smaller than {guess}')
        else:
            print('Correct answer')
            print(f'You guessed it in: {attempts} attempts.')
            break

    play_again = input('Quit? (y/n)')
    if play_again == 'y':
        print('Thank you and goodbye...')
        break
