"""
Title : 가장 긴 증가하는 부분 수열
Link : https://www.acmicpc.net/problem/11053
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

dp = [1] * (n)

for i in range(n):
    for j in range(i + 1):
        if dp[i] < dp[j] + 1 and seq[i] > seq[j]:
            dp[i] = dp[j] + 1

print(max(dp))