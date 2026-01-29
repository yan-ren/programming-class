s = input().strip()
max_len = 1

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i: j + 1]
        if sub == sub[::-1]:
            max_len = max(max_len, len(sub))

print(max_len)