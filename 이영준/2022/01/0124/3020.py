"""
Title : 개똥벌레
Link : https://www.acmicpc.net/problem/3020
"""

import sys
input = sys.stdin.readline

n, height = map(int, input().split())

# 각 높이별 석순의 개수
cave_up = [0] * (height + 1)
cave_down = [0] * (height + 1)

for i in range(n):
    h = int(input())
    # 위에서 자랄 때
    if i % 2:
        cave_up[height - h + 1] += 1
    # 아래에서 자랄 때
    else:
        cave_down[h] += 1

cave = [0] * (height + 1)
cave[-1] += cave_down[-1]
cave[1] += cave_up[1]
for i in range(2, height + 1):
    cave_down[-i] += cave_down[-(i - 1)]
    cave[-i] += cave_down[-i]
    cave_up[i] += cave_up[i - 1]
    cave[i] += cave_up[i]

cave = sorted(cave[1:])

min_count = cave[0]
for i in range(1, height):
    if cave[i] == min_count:
        continue
    else:
        break

print(min_count, i)
