'''
loop
- while
- for
'''
# i = 0
# while i < 10: # loop header
#     print(i)
#     i += 1

# i = 0
# while i < 4:
#     j = 0
#     while j < 3:
#         print(j)
#         j += 1
#     i += 1

# j = 0
# while j < 4:
#     i = 0
#     while i < 4:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1

'''
*
**
***
****
'''
# j = 0
# while j < 4:
#     i = 0
#     while i <= j:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1

first = 1
while first <= 9:
    second = 1
    while second <= 9:
        print(first, 'x', second, '=', first * second)
        second += 1
    first += 1

'''
homework:
- turn above multiple table program into a turtle programming
- show the table on a turtle screen
'''