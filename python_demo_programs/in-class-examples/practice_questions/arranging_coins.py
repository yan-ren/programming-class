# def arranging_coins(coins):
#     if coins == 1:
#         return 1
#     else:
#         for i in range(coins+1):
#             if coins >= i:
#                 coins -= i
#             else:
#                 return i - 1
#
#
# print(arranging_coins(5))
#
#
# def coins(n):
#     coin_cost = 1
#     level = 1
#     for i in range(1, n+1):
#         if coin_cost > n:
#             return level - 1
#         if coin_cost < n:
#             level = level + 1
#             coin_cost = coin_cost + level


'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows
where the i-th row has exactly i coins. The last row of the staircase may be incomplete

Given the integer n return the number of complete rows of the staircase you will build

example:
n = 5

*
* *
* *

2
'''


def arrange_coins(n):
    stairs = 0
    while n - (stairs + 1) > 0:
        n -= (stairs + 1)
        stairs += 1

    return stairs


print(arrange_coins(5))






















