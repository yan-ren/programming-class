# line = '5 6'
# line = list(map(int, line.split())) # ['5', '6'] -> [5, 6]

'''
2014 J3
'''
antonia = 100
david = 100

n = int(input())

for i in range(n):
    points = list(map(int, input().split()))
    if points[0] > points[1]:
        david -= points[0]
    elif points[1] > points[0]:
        antonia -= points[1]

print(antonia)
print(david)