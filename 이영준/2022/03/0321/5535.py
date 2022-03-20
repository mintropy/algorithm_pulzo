"""
Title : 패셔니스타
Link : https://www.acmicpc.net/problem/5535
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    D, N = MIIS()
    temperatures = [int(input()) for _ in range(D)]
    clothes = [tuple(MIIS()) for _ in range(N)]
    dp = [[-1] * N for _ in range(D)]
    for idx1, (a1, b1, c1) in enumerate(clothes):
        if temperatures[0] < a1 or temperatures[0] > b1:
            continue
        for idx2, (a2, b2, c2) in enumerate(clothes):
            if temperatures[1] < a2 or temperatures[1] > b2:
                continue
            diff = abs(c1 - c2)
            if dp[1][idx2] < diff:
                dp[1][idx2] = diff
    for day, tmeperature in enumerate(temperatures[2:]):
        for idx1, (a1, b1, c1) in enumerate(clothes):
            if temperatures[day + 1] < a1 or temperatures[day + 1] > b1 or dp[day + 1][idx1] == -1:
                continue
            for idx2, (a2, b2, c2) in enumerate(clothes):
                if temperatures[day + 2] < a2 or temperatures[day + 2] > b2:
                    continue
                diff = abs(c1 - c2) + dp[day + 1][idx1]
                if dp[day + 2][idx2] < diff:
                    dp[day + 2][idx2] = diff
    print(max(dp[-1]))
