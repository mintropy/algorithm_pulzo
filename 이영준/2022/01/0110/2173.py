"""
Title : 양파깡 만들기
Link : https://www.acmicpc.net/problem/2173
"""

from itertools import accumulate
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution():
    N, M = MIIS()
    snacks = [list(MIIS()) for _ in range(N)]
    horizontal_sum, vertical_sum = calc_prefix_sum(snacks)
    yangpakkangs = get_yangpakkangs(N, horizontal_sum, vertical_sum)
    M_yangpakkangs = find_M_yangpakkangs(M, yangpakkangs)
    if M_yangpakkangs:
        for taste, t, b, l, r in M_yangpakkangs:
            print(taste, t, l, b, r)
    else:
        print(0)


def calc_prefix_sum(snacks: list) -> tuple[list]:
    horizontal_sum = [list(accumulate(line)) for line in snacks]
    vertical_sum = list(zip(*[list(accumulate(line)) for line in list(zip(*snacks))]))
    return horizontal_sum, vertical_sum


def get_yangpakkangs(N: int, horizontal_sum: list, vertical_sum: list) -> list[tuple]:
    yangpakkangs = []
    for top in range(N - 2):
        for left in range(N - 2):
            for bottom in range(top + 2, N):
                for right in range(left + 2, N):
                    taste = get_yangpakkang_taste(horizontal_sum, vertical_sum, top, bottom, left, right)
                    yangpakkangs.append((taste, top + 1, bottom + 1, left + 1, right + 1))
    yangpakkangs.sort(key=lambda x:-x[0])
    return yangpakkangs


def get_yangpakkang_taste(horizontal_sum: list, vertical_sum: list, top: int, bottom: int, left: int, right: int) -> int:
    if left == 0:
        taste = horizontal_sum[top][right] + horizontal_sum[bottom][right]
    else:
        taste = (horizontal_sum[top][right] - horizontal_sum[top][left - 1])\
            + (horizontal_sum[bottom][right] - horizontal_sum[bottom][left - 1])
    taste += (vertical_sum[bottom - 1][left] - vertical_sum[top][left])\
            + (vertical_sum[bottom - 1][right] - vertical_sum[top][right])
    return taste


def find_M_yangpakkangs(M: int, yangpakkangs: list) -> list:
    M_yangpakkangs = []
    for yangpakkang in yangpakkangs:
        if len(M_yangpakkangs) == M:
            break
        if yangpakkang_check(M_yangpakkangs, yangpakkang):
            M_yangpakkangs.append(yangpakkang)
    if len(M_yangpakkangs) == M:
        return M_yangpakkangs
    else:
        return []


def yangpakkang_check(prev_yanpakkangs: list, yangpakkang: tuple) -> bool:
    _, top, bottom, left, right = yangpakkang
    for prev_yanpakkang in prev_yanpakkangs:
        _, t, b, l, r = prev_yanpakkang
        # outer
        if top > b or bottom < t or left > r or right < l:
            continue
        # inner
        if (t < top < b and t < bottom < b and l < left < r and l < right < r)\
            or (top < t < bottom and top < b < bottom and left < l <right and left < r < right):
                continue
        return False
    return True


solution()
