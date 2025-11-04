# s = 'abc'
#
# for ch in s:
#     print(ch)
#
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# s = 'A'

# use function
# print(s.isupper())
# print(s.islower())
# print(s.isdigit())

# compare
# if 'A' <= s <= 'Z':

# if 'a' <= s <= 'z'

# if '0' <= s <= '9'

# s = 'abcdef'
# print(s[0:3])

N = int(input())

def process(s):
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
            number = number + int(s[i:j])
            i = j
        else:
            i += 1

    return letter + str(number)

for _ in range(N):
    print(process(input()))