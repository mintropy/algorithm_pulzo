"""
Title : 포도주 시식
Link : https://www.acmicpc.net/problem/2156
"""

import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
# 4개 값은 각각 이전 와인과 해당와인을 마시지 않을 때,
# 해당 와인를 마시지 않을 때,
# 이전 와인를 마시지 않고 해당 와인을 마실 때,
# 이전 와인과 해당 와인을 마실 때
dp = [[0] * 4 for _ in range(n)]

dp[0][2] = dp[0][3] = wine[0]
if n >= 2:
    dp[1][0] = wine[0]
    dp[1][2] = wine[1]
    dp[1][3] = wine[0] + wine[1]
if n >= 3:
    dp[2][0] = wine[0]
    dp[2][1] = wine[1]
    dp[2][2] = wine[0] + wine[2]
    dp[2][3] = wine[1] + wine[2]

for i in range(2, n):
    dp[i][0] = max(dp[i - 2])
    dp[i][1] = max(dp[i - 1])
    dp[i][2] = max(dp[i - 1][:2]) + wine[i]
    dp[i][3] = dp[i - 1][2] + wine[i]

print(max(dp[-1]))