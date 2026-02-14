# time = input() # format HH:MM
# hour = int(time[0:2])
# minute = int(time[3:])
#
# travel = 120 # minutes of travel needed
#
# while travel > 0:
#     if 7 <= hour < 10 or 15 <= hour < 19:
#         travel -= 0.5
#     else:
#         travel -= 1
#
#     minute += 1
#     if minute == 60:
#         hour += 1
#         minute = 0
#     if hour == 24:
#         hour = 0
#
# print(f'{hour:02d}:{minute:02d}')
# import math
#
# name = 'Tom'
# print(f'my name is {name}')
#
# pi = 3.14159
# print(f'{pi:.4f}')
#
# print(math.trunc(pi * 10000) / 10000)
#
# n = 7
# print(f'{n:03}')
# print(f'{n:3}')

vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def nearest_vowel(c):
    best = vowels[0]
    best_dist = abs(ord(c) - ord(best))

    for v in vowels:
        dist = abs(ord(c) - ord(v))
        if dist < best_dist:
            best_dist = dist
            best = v
    return best

def next_consonant(c):
    index = alphabet.index(c)
    for i in range(index+1, 26):
        if alphabet[i] not in vowels:
            return alphabet[i]
    return 'z'

