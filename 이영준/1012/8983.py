"""
Title : 사냥꾼
Link : https://www.acmicpc.net/problem/8983
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(shooting_area: list, x: int, y: int, l: int) -> bool:
    # x, y에서 거리 l인 사격대가 있는지
    if y > l:
        return False
    left, right = 0, len(shooting_area) - 1
    while left <= right:
        mid = (left + right) // 2
        x0 = shooting_area[mid]
        if abs(x0 - x) + y <= l:
            return True
        elif x0 < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


m, n, l = MIIS()
shooting_area = sorted(list(MIIS()))
animal_count = 0
for _ in range(n):
    if bin_search(shooting_area, *MIIS(), l):
        animal_count += 1

print(animal_count)
