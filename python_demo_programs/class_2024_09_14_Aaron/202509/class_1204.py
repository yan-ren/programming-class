# s = 'A'

# if s.isupper():
#     print('Upper letter')
#
# if 'A' <= s <= 'Z':

# s.islower()
# 'a' <= s <= 'z'

# s.isdigit()
# '0' <= s <= '9'

# 2025 J3

N = int(input())

def convert(s):
    letter = ''
    number = 0
    i = 0
    while i < len(s):
        if 'A' <= s[i] <= 'Z':
            letter += s[i]
            i += 1
        elif s[i] == '-' or s[i].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            number += int(s[i:j])
            i = j
        else:
            i += 1

    return letter + str(number)

# print(convert('Ahkiy-6ebvXCV1'))
for _ in range(N):
    text = input()
    print(convert(text))