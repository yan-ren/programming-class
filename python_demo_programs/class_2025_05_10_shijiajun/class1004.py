'''
nested loop: one loop inside another
'''
# i = 0
# while i < 4:
#     j = 0
#     while j < 4:
#         print(j)
#         j += 1
#     i += 1

j = 0
while j < 5:
    i = 0
    while i < 5:
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

# row = 1
# while row <= 4:
#     star = 0
#     while star < row:
#         print('*', end='')
#         star += 1
#     print()
#     row += 1


'''

'''

# first = 1
# while first <= 9:
#     second = 1
#     while second <= 9:
#         print(first, 'x', second, '=', first * second)
#         second += 1
#     first += 1

# prime number: only can be divided by 1 and itself
n = 31
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count += 1

if count > 2:
    print('Not prime')
else:
    print('Prime')

# follow up: find all prime number under 50, hint: using nested loop

number = 1
while number <= 50:
    count = 0
    divisor = 1
    while divisor <= number:
        if number % divisor == 0:
            count += 1

    if count <= 2:
        print(number)

    number += 1

'''
3. Write a loop that calculates the total of the following series of numbers:
(1 / 50) + (2 / 49) + (3 / 48) + (4 / 47) + ...+ (48 / 3) + (49 / 2) + (50 / 1)
'''