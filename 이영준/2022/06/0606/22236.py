"""
Title : 가희와 비행기
Link : https://www.acmicpc.net/problem/22236
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    D, M = map(int, input().split())
    dp = [[0] * (D + 1) for _ in range(D + 1)]
    dp[0][0] = 1
    for j in range(1, D):
        for i in range(1, D):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i + 1][j - 1]) % M
    print(dp[1][D - 1] % M)
