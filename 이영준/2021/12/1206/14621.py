"""
Title : 나만 안되는 연애
Link : https://www.acmicpc.net/problem/14621
"""

import sys
input = sys.stdin.readline


def find_parents(x: int, parents: list) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(x_parent: int, y_parent: int, parents: list) -> list:
    if x_parent < y_parent:
        parents[y_parent] = x_parent
    else:
        parents[x_parent] = y_parent
    return parents


n, m = map(int, input().split())
schools = list(input().strip().split())
schools_by_gender = {i + 1: schools[i] for i in range(n)}

roads = [tuple(map(int, input().split())) for _ in range(m)]
roads.sort(key=lambda x:x[2])

parents = list(range(n + 1))

road_count = 0
total_dist = 0
for x, y, d in roads:
    if road_count == n - 1:
        break
    if schools_by_gender[x] == schools_by_gender[y]:
        continue
    x_parent, y_parent = find_parents(x, parents), find_parents(y, parents)
    if x_parent == y_parent:
        continue
    road_count += 1
    total_dist += d
    parents = union_parent(x_parent, y_parent, parents)
if road_count == n - 1:
    print(total_dist)
else:
    print(-1)
