"""
Title : 도도의 음식 준비
Link : https://www.acmicpc.net/problem/22953
"""

import itertools
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def angry_boss(c, cooking_time):
    for chef in c:
        if cooking_time[chef] == 1:
            continue
        else:
            cooking_time[chef] -= 1
    return cooking_time


def bin_search(cooking_time: list, cooks: int) -> int:
    # cooks개의 요리는 하는데 걸리는 시간 탐색
    left, right = 1, max(cooking_time) * cooks
    min_time = right
    while left <= right:
        mid = (left + right) // 2
        # mid시간으로 가능한 요리 개수 탐색
        able_cook = sum([mid // i for i in cooking_time])
        if able_cook >= cooks:
            if min_time > mid:
                min_time = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_time


n, k, c = MIIS()
cooking_time = list(MIIS())

comb = list(itertools.combinations_with_replacement(range(n), c))
best_time = max(cooking_time) * k

for c in comb:
    reduced_cooking_time = angry_boss(c, cooking_time[::])
    if reduced_cooking_time == []:
        continue
    time = bin_search(reduced_cooking_time, k)
    if time < best_time:
        best_time = time

print(best_time)
