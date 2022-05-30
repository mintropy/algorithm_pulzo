"""
Title : 계산 로봇
Link : https://www.acmicpc.net/problem/22342
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    M, N = map(int, input().split())
    weights = list([int(i) for i in input().strip()] for _ in range(M))
    output_value = [[0] * (N + 2) for _ in range(M + 2)]
    saved_value = [[0] * (N + 2) for _ in range(M + 2)]
    ans = 0
    for j in range(1, N + 1):
        for i in range(1, M + 1):
            saved_value[i][j] = max(
                output_value[i - 1][j - 1],
                output_value[i][j - 1],
                output_value[i + 1][j - 1],
            )
            output_value[i][j] = saved_value[i][j] + weights[i - 1][j - 1]
            ans = max(ans, saved_value[i][j])
    print(ans)
