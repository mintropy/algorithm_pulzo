"""
Title : 알약
Link : https://www.acmicpc.net/problem/4811
"""

import sys
input = sys.stdin.readline

# 카탈란 수
dp = [0] * 31
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 31):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j]


while True:
    n = int(input())
    if not n:
        break
    print(dp[n])
