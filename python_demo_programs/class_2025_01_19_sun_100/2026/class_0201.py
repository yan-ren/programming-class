'''
2015 J3
'''

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
    for i in range(index + 1, 26):
        if alphabet[i] not in vowels:
            return alphabet[i]

    return 'z'


text = input()
new_text = ''
for ch in text:
    if ch in vowels:
        new_text += ch
    else:
        new_text += ch
        new_text += nearest_vowel(ch)
        new_text += next_consonant(ch)

# i = 0
# while i < len(text):
#     if text[i] in vowels:
#         new_text += text[i]
#     else:
#         new_text += text[i]
#         new_text += nearest_vowel(text[i])
#         new_text += next_consonant(text[i])
#
#     i += 1


# print(new_text)
#
# s = '5 6'
# s = list(map(int, s.split())) # ['5', '6'] -> [5, 6]

n = int(input())
antonia = 100
david = 100

for _ in range(n):
    line = list(map(int, input().split()))
    if line[0] > line[1]:
        david -= line[1]
    elif line[0] < line[1]:
        antonia -= line[0]

print(antonia)
print(david)