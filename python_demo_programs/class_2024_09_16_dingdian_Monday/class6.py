'''
2019 J2
'''
L = int(input())

for _ in range(L):
    items = input().split(' ') # '9 +' -> ['9', '+']
    print(items[1] * int(items[0]))


