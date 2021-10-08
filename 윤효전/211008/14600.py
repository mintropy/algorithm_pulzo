import sys
from pprint import pprint
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def rotate_list(l):
    l = zip(*l)
    l = list(map(lambda x: x[::-1], l))
    return l


def print_list(l):
    for v in l:
        print(*v)


N = int(input())
if N == 1:
    S = [
        [
            [1, 1],
            [-1, 1]
        ]
    ]
else:
    S = [
        [
            [2, 2, 3, 3],
            [2, 5, 5, 3],
            [1, 1, 5, 4],
            [-1, 1, 4, 4]
        ],
        [
            [2, 2, 3, 3],
            [2, 5, 5, 3],
            [1, -1, 5, 4],
            [1, 1, 4, 4]
        ],
        [
            [2, 2, 3, 3],
            [2, 5, 5, 3],
            [1, 1, 5, 4],
            [1, -1, 4, 4]
        ],
        [
            [2, 2, 3, 3],
            [2, 5, 5, 3],
            [-1, 1, 5, 4],
            [1, 1, 4, 4]
        ],
    ]

x, y = map(int, input().split())
x, y = x-1, 2**N - y
for case in S:
    for _ in range(4):
        if case[y][x] == -1:
            print_list(case)
        case = rotate_list(case)
