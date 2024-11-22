import random

def choose_bounds():
    print("\nSet the bounds for the random number.")
    min_bound = int(input("Enter the minimum bound (default 0): ") or 0)
    max_bound = int(input("Enter the maximum bound (default 100): ") or 100)
    return min_bound, max_bound


while True:
    min_bound, max_bound = choose_bounds()
    random_number = random.randint(min_bound, max_bound)
    attempts = 0

    print(f"\nI have chosen a random number between {min_bound} and {max_bound}.")
    print("Try to guess it...")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < random_number:
            print(f"Wrong choice, the number is greater than {guess}")
        elif guess > random_number:
            print(f"Wrong answer, the number is smaller than {guess}")
        else:
            print("Congratulations! Correct answer")
            print(f"You guessed it in: {attempts} attempt(s).")
            break

    play_again = input("Would you like to play another game (y/n)? ").lower()
    if play_again != 'y':
        print("\nThank you and goodbye...")
        break

