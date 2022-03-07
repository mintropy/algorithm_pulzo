"""
Title : 도둑
Link : https://www.acmicpc.net/problem/13422
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution() -> None:
    for _ in range(int(input())):
        N, M, K = MIIS()
        houses = list(MIIS())
        houses += houses
        prefix_sum = sum(houses[:M])

        if N == M:
            if prefix_sum < K:
                print(1)
            else:
                print(0)
            continue

        ans = 0
        for i in range(N):
            if prefix_sum < K:
                ans += 1
            prefix_sum += houses[i + M] - houses[i]
        print(ans)
    return None


solution()

# 468 ms
# ------------------------------
# 480 ms
from itertools import accumulate
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution() -> None:
    for _ in range(int(input())):
        N, M, K = MIIS()
        houses = list(MIIS())
        if N == M:
            if sum(houses) < K:
                print(1)
            else:
                print(0)
            continue

        houses = list(accumulate(houses + houses))
        ans = 0
        for i in range(N):
            prefix_sum = houses[i + M] - houses[i]
            if prefix_sum < K:
                ans += 1
        print(ans)
    return None


solution()
