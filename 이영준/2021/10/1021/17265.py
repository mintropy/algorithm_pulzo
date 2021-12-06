"""
Title : 나의 인생에는 수학과 함께
Link : https://www.acmicpc.net/problem/17265
"""

import sys
input = sys.stdin.readline


def search(x: int, y: int, value_now: int):
    global n, math_map, min_value, max_value
    if x == n - 1 and y == n - 1:
        if value_now < min_value:
            min_value = value_now
        if value_now > max_value:
            max_value = value_now
        return
    # 아래쪽으로 이동
    if x < n - 1:
        poly = str(value_now) + math_map[x + 1][y]
        # 숫자 탐색을 위해 아래쪽, 오른쪽 이동
        if x < n - 2:
            next_val = eval(poly + math_map[x + 2][y])
            search(x + 2, y, next_val)
        if y < n - 1:
            next_val = eval(poly + math_map[x + 1][y + 1])
            search(x + 1, y + 1, next_val)
    # 오른쪽으로 이동
    if y < n - 1:
        poly = str(value_now) + math_map[x][y + 1]
        # 숫자 탐색을 위해 아래쪽, 오른쪽 이동
        if x < n - 1:
            next_val = eval(poly + math_map[x + 1][y + 1])
            search(x + 1, y + 1, next_val)
        if y < n - 2:
            next_val = eval(poly + math_map[x][y + 2])
            search(x, y + 2, next_val)


n = int(input())
math_map = [list(map(str, input().strip().split())) for _ in range(n)]

min_value = 10 ** 5
max_value = -(10 ** 5)

search(0, 0, math_map[0][0])
print(max_value, min_value)
