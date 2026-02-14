'''
2018 J3
'''
distance = list(map(int, input().split())) # '3 10 12 5' -> ['3', '10', '12', '5'] -> [3, 10, 12, 5]

distance_a = [0, 0, 0, 0, 0]
distance_a[1] = distance[0]
distance_a[2] = distance[0] + distance[1]
distance_a[3] = distance[0] + distance[1] + distance[2]
distance_a[4] = distance[0] + distance[1] + distance[2] + distance[3]

print(' '.join(map(str, distance_a)))

for i in range(1, len(distance_a)):
    result = []
    for j in range(len(distance_a)):
        result.append(abs(distance_a[j] - distance_a[i]))
    print(' '.join(map(str, distance_a)))
    