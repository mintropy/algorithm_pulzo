"""
Title : 내일 할거야
Link : https://www.acmicpc.net/problem/7983
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    homeworks = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:-x[1])
    now = homeworks[0][1]
    for d, t in homeworks:
        if now > t:
            now = t
        now -= d
    print(now)
