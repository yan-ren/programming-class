X = int(input())

same = []
for _ in range(X):
    data = input().split()
    same.append(data)

Y = int(input())
diff = []
for _ in range(Y):
    data = input().split()
    diff.append(data)

# print(same)
# print(diff)
G = int(input())
groups = {}

for _ in range(G):
    group_name = input() # 'A C G'
    numbers = group_name.split() # ['A', 'C', 'G']
    groups[numbers[0]] = group_name
    groups[numbers[1]] = group_name
    groups[numbers[2]] = group_name

count = 0
for pair in same:
    if groups[pair[0]] != groups[pair[1]]:
        count += 1

for pair in diff:
    if groups[pair[0]] == groups[pair[1]]:
        count += 1

print(count)