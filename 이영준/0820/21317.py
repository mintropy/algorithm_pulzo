"""
Title : 징검다리 건너기
Link : https://www.acmicpc.net/problem/21317
"""

import sys
input = sys.stdin.readline


n = int(input())
jumps = [tuple(map(int, input().split())) for _ in range(n - 1)]
k = int(input())


if n == 1:
    print(0)
elif n == 2:
    print(jumps[0][0])
elif n == 3:
    print(min(jumps[0][0] + jumps[1][0], jumps[0][1]))
else:
    # 큰 점프를 하지 않을 때
    dp = [20 * 5000] * n
    dp[0] = 0
    for i in range(n - 2):
        if dp[i + 1] > dp[i] + jumps[i][0]:
            dp[i + 1] = dp[i] + jumps[i][0]
        if dp[i + 2] > dp[i] + jumps[i][1]:
            dp[i + 2] = dp[i] + jumps[i][1]
    if dp[n - 1] > dp[n - 2] + jumps[n - 2][0]:
        dp[n - 1] = dp[n - 2] + jumps[n - 2][0]
    min_energy = dp[-1]
    # 각 특정 자리에서 큰 점프를 하는 경우
    for idx in range(n - 3):
        dp = [20 * 5000] * n
        dp[0] = 0
        for i in range(n - 2):
            if dp[i + 1] > dp[i] + jumps[i][0]:
                dp[i + 1] = dp[i] + jumps[i][0]
            if dp[i + 2] > dp[i] + jumps[i][1]:
                dp[i + 2] = dp[i] + jumps[i][1]
            if i == idx:
                dp[i + 3] = dp[i] + k
        if dp[n - 1] > dp[n - 2] + jumps[n - 2][0]:
            dp[n - 1] = dp[n - 2] + jumps[n - 2][0]
        if min_energy > dp[-1]:
            min_energy = dp[-1]
    
    print(min_energy)
