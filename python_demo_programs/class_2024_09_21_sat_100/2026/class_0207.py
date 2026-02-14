s = input()
c = int(input())

blocks = []
i = 0
while i < len(s):
    letter = s[i]
    i += 1
    j = i
    while j < len(s) and s[j].isdigit():
        j += 1
    blocks.append((letter, int(s[i:j])))
    i = j

# print(blocks)
total = 0
for letter, count in blocks:
    total += count

c = c % total
if c == 0:
    c = total

for letter, count in blocks:
    if c <= count:
        print(letter)
        break
    c -= count