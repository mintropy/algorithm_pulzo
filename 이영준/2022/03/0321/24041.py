"""
Title : 성싶당 밀키트
Link : https://www.acmicpc.net/problem/24041
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def calc(time: int, S: int, L: int):
    if time - L > 0:
        return S * (time - L)
    return S


if __name__ == "__main__":
    N, G, K = MIIS()
    important_ingredients = []
    not_important_ingredients = []
    for _ in range(N):
        S, L, O = MIIS()
        if not O:
            important_ingredients.append((S, L))
        else:
            not_important_ingredients.append((S, L))
    if K >= len(not_important_ingredients):
        K = len(not_important_ingredients)
    elif K == 0:
        important_ingredients += not_important_ingredients[::]
        not_important_ingredients = []
    left, right = 0, 10 ** 10
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        count = sum([calc(mid, S, L) for S, L in important_ingredients])\
            + sum(sorted([calc(mid, S, L) for S, L in not_important_ingredients])[:-K])
        if count <= G:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)
