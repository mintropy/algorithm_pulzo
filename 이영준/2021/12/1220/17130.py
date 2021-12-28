"""
Title : 토끼가 정보섬에 올라간 이유
Link : https://www.acmicpc.net/problem/17130
"""

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
island = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if island[i][j] == 'R':
            rabbit = (i, j)

max_carrot = -1
dp = [[-1] * M for _ in range(N)]
dp[rabbit[0]][rabbit[1]] = 0

for j in range(M - 1):
    for i in range(N):
        if dp[i][j] == -1:
            continue
        if island[i][j] == 'O':
            if max_carrot < dp[i][j]:
                max_carrot = dp[i][j]
        is_carrot = 1 if island[i][j] == 'C' else 0
        if i > 0 and island[i - 1][j + 1] != '#' and dp[i - 1][j + 1] < dp[i][j] + is_carrot:
            dp[i - 1][j + 1] = dp[i][j] + is_carrot
        if island[i][j + 1] != '#' and dp[i][j + 1] < dp[i][j] + is_carrot:
            dp[i][j + 1] = dp[i][j] + is_carrot
        if i < N - 1 and island[i + 1][j + 1] != '#' and dp[i + 1][j + 1] < dp[i][j] + is_carrot:
            dp[i + 1][j + 1] = dp[i][j] + is_carrot
else:
    for i in range(N):
        if island[i][M - 1] == 'O':
            if max_carrot < dp[i][M - 1]:
                max_carrot = dp[i][M - 1]

print(max_carrot)
