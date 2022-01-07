import sys
input = sys.stdin.readline

T, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(T + 1)]
for t in range(1, T + 1):
    num = int(input())

    dp[t][0] = dp[t - 1][0] + (1 if num == 1 else 0)
    for w in range(1, W + 1):
        curr = w % 2 + 1
        dp[t][w] = max(dp[t - 1][w - 1] + (1 if num == curr else 0), dp[t - 1][w] + (1 if num == curr else 0))
print(max(dp[-1]))