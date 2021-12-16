import sys
input = sys.stdin.readline

# 3 <= N <= 100
N = int(input())
S = tuple(map(int, input().split()))

dp = [[0]*21 for _ in range(N-1)]

dp[0][S[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j+S[i] <= 20:
                dp[i][j+S[i]] += dp[i-1][j]
            if j-S[i] >= 0:
                dp[i][j-S[i]] += dp[i-1][j]

print(dp[-1][S[-1]])