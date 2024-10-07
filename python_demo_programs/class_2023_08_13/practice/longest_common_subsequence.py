
'''
X, Y: string
i, j: index of string, where i is the index of X, j is the index of Y
'''
def lcs_recursive(X, Y, i, j):
    # base case: if i or j reaches the end of either string, LCS is 0
    if i == len(X) or j == len(Y):
        return 0
    # recursion case 1, if char at i and j matches
    if X[i] == Y[j]:
        return 1 + lcs_recursive(X, Y, i+1, j+1)
    else:
        return max(lcs_recursive(X, Y, i, j+1), lcs_recursive(X, Y, i+1, j))


print(lcs_recursive('abcde', 'ace', 0, 0))

def lcs_recursive_mem(X, Y, i, j, mem):
    # base case: if i or j reaches the end of either string, LCS is 0
    if i == len(X) or j == len(Y):
        return 0

    # check if the result is computed before
    if (i, j) in mem:
        return mem[(i, j)]

    # recursion case 1, if char at i and j matches
    if X[i] == Y[j]:
        mem[(i, j)] = 1 + lcs_recursive(X, Y, i+1, j+1)
    else:
        mem[(i, j)] = max(lcs_recursive(X, Y, i, j+1), lcs_recursive(X, Y, i+1, j))

    return mem[(i, j)]


def lcs_bottom_up(X, Y):
    dp = [[0 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

    # base case: when i or j is zero, dp[0][0..len(X)] == 0
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(X)][len(Y)]
