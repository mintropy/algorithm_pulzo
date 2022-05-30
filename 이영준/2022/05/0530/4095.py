"""
Title : 최대 정사각형
Link : https://www.acmicpc.net/problem/4095
"""

from sys import stdin
input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    while True:
        N, M = MIIS()
        if N == M == 0:
            break
        matrix = [list(MIIS()) for _ in range(N)]
        dp = [[0] * M for _ in range(N)]
        for i in range(N):
            if matrix[i][0]:
                dp[i][0] = 1
        for j in range(M):
            if matrix[0][j]:
                dp[0][j] = 1
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        print(max([max(line) for line in dp]))
