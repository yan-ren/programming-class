'''
2023 J3
'''
n = int(input())
counter = [0, 0, 0, 0, 0]

for i in range(n):
    line = input() # 'YY.Y.'
    for i in range(len(line)):
        if line[i] == 'Y':
            counter[i] += 1

max_number = max(counter)
result = []
for i in range(len(counter)):
    if counter[i] == max_number:
        result.append(str(i))

print(','.join(result))
