"""
Title : 초콜릿 뺏어 먹기
Link : https://www.acmicpc.net/problem/23322
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, K = MIIS()
    chocolates = list(MIIS())
    print(sum(chocolates) - N * chocolates[0], N - chocolates.count(chocolates[0]))
