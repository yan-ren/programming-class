'''
2023 J2
'''

N = int(input())
shu = 0
for i in range(N):
    pepper = input()
    if pepper == 'Poblano':
        shu += 1500
    elif pepper == 'Mirasol':
        shu += 6000
    elif pepper == 'Serrano':
        shu += 15500
    elif pepper == 'Cayenne':
        shu += 40000
    elif pepper == 'Thai':
        shu += 75000
    elif pepper == 'Habanero':
        shu += 125000

print(shu)

'''
2022 J2
'''
N = int(input())
star_players = 0
for i in range(N):
    score = int(input())
    foul = int(input())

    if score * 5 - foul * 3 > 40:
        star_players += 1

if star_players == N:
    print(str(star_players) + '+')
else:
    print(star_players)

