"""
Title : 마리오 파티
Link : https://www.acmicpc.net/problem/14550
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


while True:
    try:
        N, S, T = MIIS()
        positions = []
        while len(positions) != N:
            positions += list(MIIS())
        positions += [0]

        dp = [None] * (N + 1)
        for i in range(S):
            dp[i] = positions[i]
        for _ in range(T - 1):
            next_dp = [None] * (N + 1)
            for i in range(N + 1):
                if dp[i] is None:
                    continue
                for j in range(1, S + 1):
                    if i + j > N:
                        break
                    if next_dp[i + j] is None or next_dp[i + j] < dp[i] + positions[i + j]:
                        next_dp[i + j] = dp[i] + positions[i + j]
            dp = next_dp[::]
        print(dp[-1])
    except:
        break
