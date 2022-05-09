"""
Title : 배열 탈출
Link : https://www.acmicpc.net/problem/11909
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    seq = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1):
        x, y = seq[0][i], seq[0][i + 1]
        if x <= y:
            dp[0][i + 1] = dp[0][i] + y - x + 1
        else:
            dp[0][i + 1] = dp[0][i]
        x, y = seq[i][0], seq[i + 1][0]
        if x <= y:
            dp[i + 1][0] = dp[i][0] + y - x + 1
        else:
            dp[i + 1][0] = dp[i][0]
    for i in range(1, n):
        for j in range(1, n):
            now, up, left = seq[i][j], seq[i - 1][j], seq[i][j - 1]
            alpha_up = 0 if up > now else now - up + 1
            alpha_left = 0 if left > now else now - left + 1
            alpha_up += dp[i - 1][j]
            alpha_left += dp[i][j - 1]
            dp[i][j] = min(alpha_up, alpha_left)
    print(dp[-1][-1])
