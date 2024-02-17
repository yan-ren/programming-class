'''
Given an array of integers that represet coins and an integer called amount., find the minimum amount of coins it
requires to make complete change for amount

coins = [1, 2, 3]
amount = 10

output: 4, can use 2 coins with value 3 and 2 coins with value 2 to make amount 10:
3 + 3 + 2 + 2 = 10
'''
import sys

coins = [1, 2, 3]
amount = 10

mem = [0] * (amount + 1)

# top-down
def coin_change(coins, remainig):
    min = sys.maxsize
    if remainig < 0:
        return -1

    if remainig == 0:
        return 0

    if mem[remainig] != 0:
        return mem[remainig]

    for coin in coins:
        result = coin_change(coins, remainig - coin)

        if result >= 0 and result < min:
            min = 1 + result

    if min == sys.maxsize:
        mem[remainig] = -1
    else:
        mem[remainig] = min

    return min


print(coin_change(coins, amount))

# bottom-up
def change_coin(coins, amount):
    dp = [sys.maxsize] * (amount + 1)

    # base case: amount = 0
    dp[0] = 0

    # find solution for each amount
    for current_amount in range(1, amount + 1):
        # try each coin
        for coin in coins:
            if coin < current_amount:
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

    if dp[amount] == sys.maxsize:
        return -1

    return dp[amount]
