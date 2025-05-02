# print(2, end='')
# print(3)

# print(2, 3)
# nested loop
# i = 0
# while i < 5:
#     j = 0
#     while j < 5:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(i, 'x', j, '=', i*j)
#         j += 1
#     i += 1

target = 99
i = 0
while i <= target:
    j = 0
    while j <= target:
        if i * j == target:
            print(i, '*', j, '=', target)
        j += 1
    i += 1

'''
* 
** 
*** 
**** 
***** 
'''
'''
****
***
**
*
'''