N = int(input())

def process(s):
    letters = ''
    number = 0

    i = 0
    while i < len(s):
        if 'A' <= s[i] <= 'Z':
            letters += s[i]
            i += 1
        elif s[i] == '-' or s[i].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            number += int(s[i:j])
            i = j
        else:
            i += 1

    return letters + str(number)

for _ in range(N):
    print(process(input()))