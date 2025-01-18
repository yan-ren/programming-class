'''2021 j2'''
# N = int(input())
# winner = ''
# highest_bid = 0
#
# for _ in range(N):
#     name = input()
#     bid = int(input())
#
#     if bid > highest_bid:
#         highest_bid = bid
#         winner = name
#
# print(winner)

'''2020 j2'''
P = int(input())
N = int(input())
R = int(input())

day = 1
current = N
total = N
while True:
    current = current * R
    total += current

    if total > P:
        print(day)
        break
    day += 1
