"""
Title : 휴게소 세우기
Link : https://www.acmicpc.net/problem/1477
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(M: int, gaps: list) -> int:
    left, right = 1, gaps[0]
    min_length = right
    while left <= right:
        mid = (left + right) // 2
        count = calc_count(gaps, mid)
        if count <= M:
            if min_length > mid:
                min_length = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_length


def calc_count(gaps: list, dist: int) -> int:
    cnt = 0
    for gap in gaps:
        if gap <= dist:
            break
        if gap % dist:
            cnt += gap // dist
        else:
            cnt += gap // dist - 1
    return cnt


N, M, L = MIIS()
rest_area = [0] + sorted((MIIS())) + [L]
gaps = sorted([rest_area[i] - rest_area[i - 1] for i in range(1, N + 2)], reverse=True)

print(bin_search(M, gaps))
