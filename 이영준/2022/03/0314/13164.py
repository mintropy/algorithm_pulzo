"""
Title : 행복 유치원
Link : https://www.acmicpc.net/problem/13164
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution() -> None:
    N, K = MIIS()
    heights = tuple(MIIS())

    if N == K:
        print(0)
        return None

    heights_diff = sorted([heights[i] - heights[i - 1] for i in range(1, N)])
    print(sum(heights_diff[:N-K]))
    return None


solution()
