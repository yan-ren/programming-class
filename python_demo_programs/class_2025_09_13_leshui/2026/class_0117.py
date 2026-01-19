# N = int(input())
# C = int(input())
# P = int(input())
#
# if C * P >= N:
#     print('yes')
# else:
#     print('no')

D = int(input())
E = int(input())

for i in range(E):
    sign = input()
    number = int(input())
    if sign == '+':
        D += number
    else:
        D -= number

print(D)

