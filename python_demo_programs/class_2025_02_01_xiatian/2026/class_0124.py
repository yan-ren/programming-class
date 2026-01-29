'''
range(3)
'''
for i in range(3):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 5, 2):
    print(i)

s = 'abc1234'
for ch in s:
    print(ch)

index = 0
while index < len(s):
    print(s[index])
    index += 1

l = [1, 2, 3, 1]
for num in l:
    print(l)

index = 0
while index < len(s):
    print(s[index])
    index += 1

s = 'abcde'
s_reverse = ''
for ch in s:
    s_reverse = ch + s_reverse
print(s_reverse)

matrix = [
    [1, 2, 3],
    [2, 4, 1],
    [2 ,1, 2, 2, 4]
]
'''
matrix = [
    [3, 2, 1],
    [1, 4, 2],
    [4, 2, 2, 1, 2]
]
'''

sum = 0
for v in matrix:
    for num in v:
        sum += num

print(sum)

# result = [3, 4, 4]

result = []
for numbers in matrix:
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num

    result.append(max)

print(result)