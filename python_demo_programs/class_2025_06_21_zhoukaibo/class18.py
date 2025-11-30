# D = int(input())
#
# E = int(input())
#
# for _ in range(E):
#     sign = input()
#     amount = int(input())
#
#     if sign == '+':
#         D += amount
#     else:
#         D -= amount
#
# print(D)

total = int(input())

start = int(input())
current = start
multiplier = int(input())

day = 0
while start < total:
    current = current * 5
    start += current
    day += 1

print(day)