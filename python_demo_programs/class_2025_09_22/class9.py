# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
#
# print(s)

# nested loop
# i = 0
# while i < 4:
#     j = 0
#     while j < 4:
#         print(j)
#         j += 1
#     i += 1

# j = 0
# while j < 5:
#     i = 0
#     while i < j + 1:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1

'''
*
**
***
****
*****
'''

# first = 1
# while first <= 9:
#     second = 1
#     while second <= 9:
#         print(first, 'x', second, '=', first * second)
#         second += 1
#     first += 1

'''
homework:
- turn above multiple table program into a turtle programming
- show the table on a turtle screen
'''

i = 0
while i < 5:
    j = 0
    while j < 5:
        z = 0
        while z < 5:
            print(z)
            z += 1
        j += 1
    i += 1
