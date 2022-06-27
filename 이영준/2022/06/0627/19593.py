"""
Title : 다도해
Link : https://www.acmicpc.net/problem/19593
"""

from sys import stdin

input = stdin.readline


def calc_nums(N: int, E: int, A: int, B: int, first: bool = False) -> tuple:
    if not first:
        E = (E * A + B) % (N * N)
    X = E // N
    Y = E % N
    return E, X, Y


def find_parent(parents: list[int], x: int) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(parents: list[int], x: int, y: int) -> tuple:
    if x > y:
        x, y = y, x
    parents[y] = x
    counts[x] += counts[y]
    return parents, counts


if __name__ == "__main__":
    for _ in range(int(input())):
        N, seed, A, B = map(int, input().split())
        N_sq = N * N
        parents = list(range(N))
        counts = [1] * N
        comb = set()
        M = 0
        E, X, Y = calc_nums(N, seed % (N * N), A, B, True)
        while counts[0] < N:
            if (E, X, Y) in comb:
                break
            comb.add((E, X, Y))
            _X, _Y = find_parent(parents, X), find_parent(parents, Y)
            if X != Y and _X != _Y:
                parents, counts = union_parent(parents, _X, _Y)
            E, X, Y = calc_nums(N, E, A, B)
            M += 1

        if counts[0] == N:
            print(M)
        else:
            print(0)