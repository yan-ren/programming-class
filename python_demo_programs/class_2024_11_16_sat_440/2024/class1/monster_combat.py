import random


health_level = 20
victories = 0
defeats = 0
consecutive_victories = 0
combat_count = 0

while health_level > 0:
    monster_strength = random.randint(1, 5)
    print(f'\nYou face a monster with strength {monster_strength}')

    print('''
    Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre
porte
3- Afficher les règles du jeu
4- Quitter la partie
    ''')

    choice = input('Enter your choice: ')

    if choice == '1':
        player_roll = random.randint(1, 6)
        combat_count += 1
        print(f'Your roll: {player_roll}')

        if player_roll > monster_strength:
            victories += 1
            consecutive_victories += 1
            health_level += monster_strength

            print(f'Victory! your health level increases to {health_level}')
            print(f'Total victories {victories}, total defeats:{defeats}')
        else:
            defeats += 1
            consecutive_victories = 0
            health_level -= monster_strength

            print(f'Defeat! your health level decreases to {health_level}')
            print(f'Total victories: {victories}, total defeats: {defeats}')
    elif choice == '2':
        health_level -= 1
    elif choice == '3':
        print('''Pour réussir un combat, il faut que la valeur du dé lancé soit
supérieure à la force de l’adversaire. Dans ce cas, le niveau
de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager
est inférieure ou égale à la force de l’adversaire. Dans ce
cas, le niveau de vie de l’usager est diminué de la force de
l’adversaire.
La partie se termine lorsque les points de vie de l’usager
tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le
cas de l’évitement, il y a une pénalité de 1 p''')
    elif choice == '4':
        print('Goodbye')
        break
    else:
        print('Invalid option')

    if health_level < 0:
        print('Game Over! You have no health left')
        print(f'Total victories {victories}')
        break

