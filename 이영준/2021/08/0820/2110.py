"""
Title : 공유기 설치
Link : https://www.acmicpc.net/problem/2110
"""

import sys
input = sys.stdin.readline


def bin_search(n: int, c: int, home: list) -> int:
    min_length = 0
    st, end = 0, (home[-1] - home[0]) // (c - 1) + 1
    while st <= end:
        mid = (st + end) // 2
        # mid거리로 c개가 가능한지 확인
        router = 1
        router_now = 0
        for i in range(1, len(home)):
            if home[i] - home[router_now] >= mid:
                router += 1
                router_now = i
                if router == c:
                    break
        if router == c:
            st = mid + 1
            if mid > min_length:
                min_length = mid
        else:
            end = mid - 1
    return min_length


n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])

print(bin_search(n, c, home))
