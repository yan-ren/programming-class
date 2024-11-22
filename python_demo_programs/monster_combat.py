import random

# Initial player stats
health_level = 20
victories = 0
defeats = 0
consecutive_victories = 0
combat_count = 0


def show_rules():
    print("""
    Game Rules:
    - You face a monster with random strength (1 to 5).
    - To win, your dice roll must be higher than the monster's strength.
    - If you win, you gain health points equal to the monster's strength.
    - If you lose, you lose health points equal to the monster's strength.
    - You may avoid a monster with a 1-point health penalty.
    - The game ends when your health falls below 0.
    """)


while health_level > 0:
    monster_strength = random.randint(1, 5)
    print(f"\nYou face a monster with difficulty: {monster_strength}")

    print("What would you like to do?")
    print("1 - Fight this monster")
    print("2 - Avoid this monster and open another door")
    print("3 - Show game rules")
    print("4 - Quit the game")
    choice = input("Enter your choice: ")

    if choice == '1':  # Fight
        player_roll = random.randint(1, 6)
        combat_count += 1
        print(f"\nYour roll: {player_roll}")

        if player_roll > monster_strength:
            victories += 1
            consecutive_victories += 1
            health_level += monster_strength
            print(f"Victory! Your health level increases to {health_level}")
            print(f"Total victories: {victories}, Total defeats: {defeats}")
        else:
            defeats += 1
            consecutive_victories = 0
            health_level -= monster_strength
            print(f"Defeat! Your health level decreases to {health_level}")
            print(f"Total victories: {victories}, Total defeats: {defeats}")
    elif choice == '2':
        health_level -= 1
        print(f"\nYou avoided the monster and lost 1 health point. Health level is now {health_level}.")
    elif choice == '3':
        show_rules()
    elif choice == '4':
        print("Thank you for playing. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    if health_level <= 0:
        print("\nGame over! You have no health left.")
        print(f"Total victories: {victories}")
        break
