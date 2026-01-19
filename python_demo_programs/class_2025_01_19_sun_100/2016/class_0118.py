distance = list(map(int, input().split()) )# '3 10 12 5' -> ['3', '10', '12', '5']

distance_A = [0,
              distance[0],
              distance[0] + distance[1],
              distance[0]+distance[1]+distance[2],
              distance[0]+distance[1]+distance[2]+distance[3]]

print(' '.join(list(map(str, distance_A))))

for i in range(1, len(distance_A)):
    result = []
    for j in range(len(distance_A)):
        result.append(abs(distance_A[j] - distance_A[i]))
    print(' '.join(list(map(str, result))))
