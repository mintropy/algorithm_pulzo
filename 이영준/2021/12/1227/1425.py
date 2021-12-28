"""
Title : 원숭이 땅을 옮기다
Link : https://www.acmicpc.net/problem/1425
"""

import sys
input = sys.stdin.readline


def check(mid: int):
    low, high = -(10 ** 9), 10 ** 9
    for i in range(N):
        x1, y1 = monkey_positions[i]
        for j in range(i + 1, N):
            x2, y2 = monkey_positions[j]
            d = abs(x1 - x2) + abs(y1 - y2)
            if d > mid:
                return False
            d = (mid - d) // 2
            l, h = y1 - d, y2 + d
            if h < low or l > high:
                return False
            if low <= l <= high:
                low = l
            if low <= h <= high:
                high = h
    return True


N = int(input())
monkey_positions = []
for _ in range(N):
    monkey_positions.append(tuple(map(int, input().split())))
monkey_positions.sort(key=lambda x:x[1])

min_dist = 10 ** 10
left, right = 0, 10 ** 10
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        if min_dist > mid:
            min_dist = mid
        right = mid -1
    else:
        left = mid + 1

print(min_dist)
