'''2017 J3'''
distance = list(map(int, input().split(' ')))
# print(value)

first = [0]
for d in distance:
    first.append(first[len(first) - 1] + d)

result = []
# result.append(first)

for i in range(5):
    row = []
    for j in range(5):
        row.append(abs(first[i] - first[j]))
    result.append(row)

# print(result)
for row in result:
    for value in row:
        print(value, end=' ')
    print()
