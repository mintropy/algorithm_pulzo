"""
Title : 이친수 찾기
Link : https://www.acmicpc.net/problem/2201
"""

import sys
input = sys.stdin.readline


K = int(input())
dp = [0] * 100
dp[1] = 1
dp[2] = 2
for i in range(3, 100):
    dp[i] = dp[i - 1] + dp[i - 2]
for i in range(1, 100):
    if dp[i] > K:
        idx = i - 1
        break
ans = ''
while idx:
    if dp[idx] <= K:
        ans += '1'
        K -= dp[idx]
    else:
        ans += '0'
    idx -= 1
print(ans)
