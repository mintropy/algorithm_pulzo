"""
Title: 은하철도
Link : https://www.acmicpc.net/problem/17250
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def find_parents(x: int, parents: list) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parents(x: int, y: int, parents: list) -> list:
    if x > y:
        x, y = y, x
    parents[y] = x
    return parents


def clac_travle(x: int, y: int, travle: list) -> list:
    if x > y:
        x, y = y, x
    travle[x] += travle[y]
    return travle


if __name__ == "__main__":
    N, M = MIIS()
    planets = [0] + [int(input()) for _ in range(N)]
    travle = planets[::]
    parents = list(range(N + 1))
    for _ in range(M):
        x, y = MIIS()
        x, y = find_parents(x, parents), find_parents(y, parents)
        if x != y:
            parents = union_parents(x, y, parents)
            travle = clac_travle(x, y, travle)
        print(travle[min(x, y)])
