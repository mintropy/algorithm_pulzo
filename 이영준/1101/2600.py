"""
Title : 구슬게임
Link : https://www.acmicpc.net/problem/2600
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def winable(i: int, j: int) -> bool:
    if i >= b1 and not dp[i - b1][j]:
        return True
    if i >= b2 and not dp[i - b2][j]:
        return True
    if i >= b3 and not dp[i - b3][j]:
        return True
    if j >= b1 and not dp[i][j - b1]:
        return True
    if j >= b2 and not dp[i][j - b2]:
        return True
    if j >= b3 and not dp[i][j - b3]:
        return True
    return False


b1, b2, b3 = MIIS()

dp = [[False] * (501) for _ in range(501)]
for i in range(501):
    for j in range(501):
        # 조건에 따라 구슬을 빼지 못할 때
        if i < b1 and j < b1:
            continue
        # 한번에 끝낼 수 있는 조건일 때
        if (i == 0 and (j == b1 or j == b2 or j == b3)) or (j == 0 and (i == b1 or i == b2 or i == b3)):
            dp[i][j] = True
        # 아니라면 탐색
        else:
            dp[i][j] = winable(i, j)

for _ in range(5):
    k1, k2 = MIIS()
    if dp[k1][k2]:
        print('A')
    else:
        print('B')
