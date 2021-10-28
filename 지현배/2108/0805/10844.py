N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] % 1_000_000_000
    dp[i][9] = dp[i - 1][8]
print(sum(dp[-1]) % 1_000_000_000)