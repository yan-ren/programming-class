import sys


def main():
    global ans
    n = int(sys.stdin.readline().strip())
    dp = [[0] * 402 for _ in range(402)]
    prefix_sum = [0] * 402
    ans = 0

    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        dp[i][i] = arr[i]
        ans = max(ans, dp[i][i])
        prefix_sum[i] = arr[i] + (prefix_sum[i - 1] if i > 0 else 0)

    for length in range(1, n):
        for l in range(n - length):
            r = l + length
            j, k = l + 1, r
            while j <= k:
                if (dp[l][j - 1] and dp[l][j - 1] == dp[k][r] and (j == k or dp[j][k - 1])):
                    dp[l][r] = max(dp[l][r], dp[l][j - 1] + dp[j][k - 1] + dp[k][r])
                    ans = max(ans, dp[l][r])
                    break
                if prefix_sum[j - 1] - (prefix_sum[l - 1] if l > 0 else 0) < prefix_sum[r] - prefix_sum[k - 1]:
                    j += 1
                else:
                    k -= 1

    print(ans)


if __name__ == "__main__":
    main()