"""
Title : 피자 오븐
Link : https://www.acmicpc.net/problem/19940
"""

from collections import deque
from sys import stdin

input = stdin.readline


def search_buttons_minimum_count():
    counts = [[0] * 5 for _ in range(61)]
    queue = deque([(0, 0, 0, 0, 0, 0), (60, 1, 0, 0, 0, 0)])
    while queue:
        x, addh, addt, mint, addo, mino = queue.popleft()
        if (
            sum(counts[x]) == addh + addt + mint + addo + mino
            and counts[x] < [addh, addt, mint, addo, mino]
        ) or (0 != sum(counts[x]) < addh + addt + mint + addo + mino):
            continue
        counts[x] = [addh, addt, mint, addo, mino]
        if x + 10 < 60:
            queue.append((x + 10, addh, addt + 1, mint, addo, mino))
        if x - 10 > 0:
            queue.append((x - 10, addh, addt, mint + 1, addo, mino))
        if x + 1 < 60:
            queue.append((x + 1, addh, addt, mint, addo + 1, mino))
        if x - 1 > 0:
            queue.append((x - 1, addh, addt, mint, addo, mino + 1))
    return counts


def count_buttons(N: int) -> int:
    count = 0
    count += N // 60
    N %= 60
    count += N // 10
    N %= 10


if __name__ == "__main__":
    counts = search_buttons_minimum_count()
    for _ in range(int(input())):
        N = int(input())
        ans = counts[N % 60][::]
        ans[0] += N // 60
        print(*ans)
