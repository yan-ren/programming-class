# s = 'abc'
# print(s[::-1])

text = input()
max_len = 1

for i in range(len(text)):
    for j in range(i, len(text)):
        partial = text[i:j+1]
        if partial == partial[::-1]:
            max_len = max(max_len, len(partial))
print(max_len)
