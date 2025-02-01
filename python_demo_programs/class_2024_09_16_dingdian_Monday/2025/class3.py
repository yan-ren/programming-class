'''
2019
Problem J3: Cold Compress
'''
N = int(input())

for _ in range(N):
    line = input()

    result = []
    current = line[0]
    count = 1
    for index in range(1, len(line)):
        if line[index] == current:
            count += 1
        else:
            result.append(str(count))
            result.append(current)
            count = 1
            current = line[index]

    result.append(str(count))
    result.append(current)
    print(' '.join(result))
