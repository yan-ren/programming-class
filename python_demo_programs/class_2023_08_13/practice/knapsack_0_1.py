def knapsack(values, weights, capacity):
    n = len(values)
    
    # create a 2d list to store the maxi value at each i and capacity
    dp = [[0 for x in range(capacity + 1)] for y in range(n+1)]
    
    # fill in the 2d list
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # if we can still take i item, need to choose between take or not take
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            # if we cannot take the item, there is no option
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(knapsack(values, weights, capacity))

'''
when i = 0 or w = 0 -> base case -> no items to pick or capacity is zero cannot take anything
-> value is 0
'''