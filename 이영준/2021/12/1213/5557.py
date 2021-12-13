"""
Title : 1학년
Link : https://www.acmicpc.net/problem/5557
"""

import sys
input = sys.stdin.readline


N = int(input())
seq = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N - 1)]
dp[0][seq[0]] = 1
for i in range(N - 2):
    num = seq[i + 1]
    for j in range(21):
        if not dp[i][j]:
            continue
        if j + num <= 20:
            dp[i + 1][j + num] += dp[i][j]
        if j - num >= 0:
            dp[i + 1][j - num] += dp[i][j]

print(dp[-1][seq[-1]])
