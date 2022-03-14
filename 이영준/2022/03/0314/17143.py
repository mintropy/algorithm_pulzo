"""
Title : 낚시왕
Link : https://www.acmicpc.net/problem/17143
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def move_shark(r, c, s, d):
    global R, C, directions
    _s, _d = s, d
    while _s:
        if _d == 1:
            if _s >= r:
                _s -= r
                r = 0
                _d = directions[_d]
            else:
                r -= _s
                break
        elif _d == 2:
            if _s >= R - r - 1:
                _s -= R - r - 1
                r = R - 1
                _d = directions[_d]
            else:
                r += _s
                break
        elif _d == 3:
            if _s >= C - c - 1:
                _s -= C - c - 1
                c = C - 1
                _d = directions[_d]
            else:
                c += _s
                break
        else:
            if _s >= c:
                _s -= c
                c = 0
                _d = directions[_d]
            else:
                c -= _s
                break
    return r, c, _d


if __name__ == '__main__':
    R, C, M = MIIS()
    sharks = {}
    for _ in range(M):
        r, c, s, d, z = MIIS()
        if d <= 2:
            s %= (R - 1) * 2
        else:
            s %= (C - 1) * 2
        sharks[(r - 1, c - 1)] = (s, d, z)

    directions = {1: 2, 2: 1, 3: 4, 4: 3}
    ans = 0
    for idx in range(C):
        for j in range(R):
            if (j, idx) in sharks:
                ans += sharks[(j, idx)][2]
                sharks.pop((j, idx))
                break
        next_sharks = {}
        for (r, c), (s, d, z) in sharks.items():
            r, c, _d = move_shark(r, c, s, d)
            if (r, c) in next_sharks:
                if z > next_sharks[(r, c)][2]:
                    next_sharks[(r, c)] = (s, _d, z)
            else:
                next_sharks[(r, c)] = (s, _d, z)
        sharks = next_sharks
    print(ans)

'''
100 3 2
2 3 0 1 2
4 3 1 1 3
'''
