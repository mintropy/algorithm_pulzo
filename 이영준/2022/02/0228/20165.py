"""
Title : 인내의 도미노 장인 호석
Link : https://www.acmicpc.net/problem/20165
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)


def solution() -> None:
    N, M, R  = MIIS()
    dominos = [list(MIIS()) for _ in range(N)]

    total_point = 0
    directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    for i in range(R * 2):
        if i % 2:
            x, y = MIIS()
            x, y = x - 1, y - 1
            if dominos[x][y] < 0:
                dominos[x][y] *= -1
        else:
            x, y, d = input().strip().split()
            x, y = int(x) - 1, int(y) - 1,
            if dominos[x][y] < 0:
                continue
            dominos, point = simulate(N, M, x, y, directions[d], dominos)
            total_point += point

    print(total_point)
    ans = ''
    for i in range(N):
        for j in range(M):
            if dominos[i][j] > 0:
                ans += 'S '
            else:
                ans += 'F '
        ans += '\n'
    print(ans)
    return None


def simulate(N, M, x, y, d, dominos):
    global dx, dy
    count = dominos[x][y]
    point = 0
    while count:
        if 0 <= x < N and 0 <= y < M:
            if dominos[x][y] > 0:
                if count < dominos[x][y]:
                    count = dominos[x][y]
                dominos[x][y] *= -1
                point += 1
            count -= 1
            x, y = x + dx[d], y + dy[d]
        else:
            break
    return dominos, point


solution()


'''
Counter Example
3 3 3
3 3 3
3 3 3
3 3 3
1 1 E
1 1
1 2 S
1 2
1 3 S
1 3
ANS
3
S S S
S S S
S S S

2 2 1
1 1
1 1
1 1 E
1 1
'''
