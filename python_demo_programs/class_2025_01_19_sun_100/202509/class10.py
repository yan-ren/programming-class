# N = int(input())
#
# star = 0
# for _ in range(N):
#     score = int(input())
#     foul = int(input())
#
#     if score * 5 - foul * 3 > 40:
#         star += 1
#
# if star == N:
#     print(str(star)+'+')
# else:
#     print(star)


# a = 12
# b = '+'
#
# print(str(a)+b)

# N = int(input())
# highest = -1
# winner = ''
#
# for _ in range(N):
#     name = input()
#     bid = int(input())
#
#     if bid > highest:
#         highest = bid
#         winner = name
#
# print(winner)

donut = int(input())
event = int(input())

for _ in range(event):
    sign = input()
    amount = int(input())

    if sign == '+':
        donut += amount
    else:
        donut -= amount

print(donut)

'''
2023 J3
'''