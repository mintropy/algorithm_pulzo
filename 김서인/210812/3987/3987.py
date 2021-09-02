# https://www.acmicpc.net/problem/3987
# 보이저 1호

import sys
from typing import NoReturn
input = sys.stdin.readline

N, M = map(int, input().split())
universe = list(list(input().strip()) for _ in range(N))
# print(universe)
PR, PC = map(int,input().split())

# 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
mode_name = ['U', 'R', 'D', 'L']


def sol():
    max_voyage = 0
    max_voyage_mode = -1

    for m in range(4):
        universe_ch = list([0] * M for _ in range(N))  # 방문했는지 체크
        mode = m
        cnt = 1  # 그 방향으로 갔을 때 시그널 보내는 시간
        i = PR - 1
        j = PC - 1

        while True:
            i = i + di[mode]
            j = j + dj[mode]
            if 0 <= i < N and 0 <= j < M:
                if universe_ch[i][j] > 1: # 이미 방문한 행성을 만나면(계속 돌고 있다는 뜻이니까) - 처음 두번은 계속 돌지 않아도 다른 방향으로 튕겨주느라고 방문할 수도 있음.
                    return m, 'Voyager'

                if universe[i][j] == 'C':  # 블랙홀 만났을 때
                    break

                elif universe[i][j] == "/":  # 행성
                    universe_ch[i][j] += 1
                    # 방향 바꾸기  우<-> 상, 좌<->하
                    if mode == 0:
                        mode = 1
                    elif mode == 1:
                        mode = 0
                    elif mode == 2:
                        mode = 3
                    elif mode == 3:
                        mode = 2

                elif universe[i][j] == "\\":  # 행성
                    universe_ch[i][j] += 1
                    # 방향 바꾸기  하<->우  상<->좌
                    if mode == 0:
                        mode = 3
                    elif mode == 1:
                        mode = 2
                    elif mode == 2:
                        mode = 1
                    elif mode == 3:
                        mode = 0

                elif universe[i][j] == ".":  # 빈 공간
                    universe_ch[i][j] = 1

                cnt += 1

            else:  # 행성계를 벗어나면
                break

        if cnt > max_voyage:
            max_voyage = cnt
            max_voyage_mode = m

    return max_voyage_mode, max_voyage


max_voyage_mode2, max_voyage2 = sol()
print(mode_name[max_voyage_mode2])
print(max_voyage2)