'''
2018 J3
'''
given = input().split(' ')
for i in range(len(given)):
    given[i] = int(given[i])

first = [0]
start = 0
for value in given:
    start += value
    first.append(start)

print(*first)
for index in range(1, len(first)):
    res = []
    for j in range(len(first)):
        res.append(abs(first[index] - first[j]))

    print(*res)
