'''
Class Plan after Feb 19
- back to regular coding material with more concepts
- building game projects using python libraries, e.g. turtle, pygame
'''
# 2022 J2
# N = int(input())
# star_players = 0
# for _ in range(N):
#     scores = int(input())
#     fouls = int(input())
#
#     stars = scores * 5 - fouls * 3
#     if stars > 40:
#         star_players += 1
#
# if star_players == N:
#     print(str(star_players) + "+")
# else:
#     print(star_players)

# 2021 J3
line = input()
letters = ''
digits = ''
operation = ''
for ch in line:
    if ch.isalpha():
        if letters != '' and digits != '' and operation != '':
            print(letters, operation, digits)
            letters = ''
            operation = ''
            digits = ''
        letters += ch
    elif ch.isdigit():
        digits += ch
    elif ch == '+':
        operation += 'tighten'
    elif ch == '-':
        operation += 'loosen'

print(letters, operation, digits)
