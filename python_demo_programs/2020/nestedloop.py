n = 5
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

'''
*
* *
* * *
* * * *
* * * * *
'''
n = 6
for i in range(n):
    m = i
    for j in range(m):
        print('*', end='')
    print()

'''
* * * *
* * *
* *
*
'''
n = 6
m = n
for i in range(n):
    for j in range(m):
        print('*', end='')
    m -= 1
    print()