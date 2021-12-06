"""
Title : 사이클 게임
Link : https://www.acmicpc.net/problem/20040
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_parent(x: int, parents: list) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(x_p: int, y_p: int, parents: list) -> list:
    if x_p < y_p:
        parents[y_p] = x_p
    else:
        parents[x_p] = y_p
    return parents


n, m = MIIS()
parents = list(range(n))
for i in range(1, m + 1):
    u, v = MIIS()
    u_p, v_p = find_parent(u, parents), find_parent(v, parents)
    # 사이클 가능한지
    if u_p == v_p:
        print(i)
        break
    parents = union_parent(u_p, v_p, parents)
# 끝까지 종료되지 않는 경우
else:
    print(0)