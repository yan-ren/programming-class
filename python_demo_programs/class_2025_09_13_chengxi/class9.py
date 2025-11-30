j = 0
while j < 4:
    i = 0
    while i < 4:
        print('*', end='')
        i += 1
    print()
    j += 1

'''
*
**
***
****
'''
j = 0
while j < 4:
    i = 0
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1

'''
****
***
**
*
'''

first = 1
while first <= 9:
    second = 1
    while second <= 9:
        print(first, 'x', second, '=', first * second)
        second += 1
    first += 1
