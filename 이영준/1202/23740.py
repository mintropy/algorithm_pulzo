"""
Title : 버스 노선 개편하기
Link : https://www.acmicpc.net/problem/23740
"""

import sys
input = sys.stdin.readline


N = int(input())
bus_lines = sorted([tuple(map(int, input().split())) for _ in range(N)])

new_bus_lines = []
last_bus_st, last_bus_end, min_price = bus_lines[0]
for s, e, c in bus_lines:
    if last_bus_end < s:
        new_bus_lines.append((last_bus_st, last_bus_end, min_price))
        last_bus_st, last_bus_end, min_price = s, e, c
    else:
        if last_bus_st > s:
            last_bus_st = s
        if last_bus_end < e:
            last_bus_end = e
        if min_price > c:
            min_price = c
else:
    new_bus_lines.append((last_bus_st, last_bus_end, min_price))

print(len(new_bus_lines))
for line in new_bus_lines:
    print(*line)
