N = int(input())

def convert(s):
    upper = ''
    number = 0

    for i in range(len(s)):
        # if s[i].isupper()
        if 'A' <= s[i] <= 'Z':
            upper += s[i]
            i += 1
        elif s[i].isdigit() or s[i] == '-':
        # elif '0' <= s[i] <= '9'
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            number += int(s[i:j])
            i = j
        else:
            i += 1

    return upper + str(number)


for _ in range(N):
    print(convert(input()))