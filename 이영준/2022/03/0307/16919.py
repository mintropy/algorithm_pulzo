"""
Title : 봄버맨 2
Link : https://www.acmicpc.net/problem/16919
"""

import sys
input = sys.stdin.readline


def check_bomb(i: int, j: int) -> bool:
    global R, C, my_map, dx, dy
    for d in range(4):
        x, y = i + dx[d], j + dy[d]
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if my_map[x][y] == 'O':
            return True
    return False


if __name__ == '__main__':
    R, C, N = map(int, input().split())
    my_map = [input().strip() for _ in range(R)]

    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    if not N % 2:
        print(('O' * C + '\n') * R)
    elif N == 1:
        print('\n'.join(my_map))
    else:
        next_map = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if my_map[i][j] == 'O' or check_bomb(i, j):
                    next_map[i][j] = '.'
        if N % 4 == 1:
            my_map = next_map
            next_map = [['O'] * C for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    if my_map[i][j] == 'O' or check_bomb(i, j):
                        next_map[i][j] = '.'
        ans = '\n'.join(list(''.join(line) for line in next_map))
        print(ans)

'''
6 7 5
.......
...O...
....O..
.......
OO.....
OO.....

2 2 5
O.
.O

2 2 3
O.
.O
'''
