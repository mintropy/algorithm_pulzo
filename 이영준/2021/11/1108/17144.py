"""
Title : 미세먼지 안녕!
Link : https://www.acmicpc.net/problem/17144
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dust_move(house: list, x1: int, x2: int) -> list:
    global R, C, dx, dy
    # 미세먼지 확산 초기화
    next_house = [[-1] * (C + 2)] + [[-1] + [0] * C + [-1] for _ in range(R)] + [[-1] * (C + 2)]
    next_house[x1][1] = next_house[x2][1] = -1
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if house[i][j] > 0:
                dust = house[i][j]
                dust_move_dir = 0
                if dust >= 5:
                    for d in range(4):
                        nx, ny = i + dx[d], j + dy[d]
                        if next_house[nx][ny] != -1:
                            dust_move_dir += 1
                            next_house[nx][ny] += dust // 5
                next_house[i][j] += dust - dust_move_dir * (dust // 5)
    return next_house


def air_conditioner_operate(house: list, air_conditioner_route: list) -> list:
    # 공기청정기 작동의 역방향으로 확인
    # 미세먼지 제거
    house[air_conditioner_route[0][0][0]][air_conditioner_route[0][0][1]] = 0
    house[air_conditioner_route[1][0][0]][air_conditioner_route[1][0][1]] = 0
    # 공기청정기 작동
    for i in range(1, len(air_conditioner_route[0])):
        x, y = air_conditioner_route[0][i]
        # 해당 위치가 비어있으면 확인할 필요 없음
        if house[x][y]:
            house[air_conditioner_route[0][i - 1][0]][air_conditioner_route[0][i - 1][1]] = house[x][y]
            house[x][y] = 0
    for i in range(1, len(air_conditioner_route[1])):
        x, y = air_conditioner_route[1][i]
        # 해당 위치가 비어있으면 확인할 필요 없음
        if house[x][y]:
            house[air_conditioner_route[1][i - 1][0]][air_conditioner_route[1][i - 1][1]] = house[x][y]
            house[x][y] = 0
    return house


R, C, T = MIIS()
# -1로 패딩
house = [[-1] * (C + 2)] + [[-1] + list(MIIS()) + [-1] for _ in range(R)] + [[-1] * (C + 2)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

# 공기청정기 위치 탐색
air_conditioner = []
for i in range(1, R + 1):
    if house[i][1] == -1:
        air_conditioner.append(i)
x1, x2 = air_conditioner

air_conditioner_route = [
    # 위쪽 경로
    list((i, 1) for i in range(x1 - 1, 0, -1))\
    + list((1, j) for j in range(2, C + 1))\
    + list((i, C) for i in range(2, x1 + 1))\
    + list((x1, j) for j in range(C - 1, 1, -1)),
    # 아래쪽 경로
    list((i, 1) for i in range(x2 + 1, R + 1))\
    + list((R, j) for j in range(2, C + 1))\
    + list((i, C) for i in range(R - 1, x2 - 1, - 1))\
    + list((x2, j) for j in range(C - 1, 1, -1)),
]

for _ in range(T):
    # 미세먼지 확산
    house = dust_move(house, x1, x2)
    # 공기청정기 작동
    house = air_conditioner_operate(house, air_conditioner_route)

print(sum(sum(house[1:R+1], start=[])) + R * 2 + 2)


'''
def dust_move(dust_pos: dict, air_conditioner: list) -> dict:
    global R, C, dx, dy
    next_dust_pos = {}
    for (x, y), dust_now in dust_pos.items():
        # 해당 자리에 미세먼지가 없으면 넘어가기
        if dust_now == 0:
            continue
        move_dir_count = 0
        # 미세먼지가 4이하이면 이동되는 미세먼지 없음
        if dust_now >= 5:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                # 범위 내부에 있고, 공기청정기 위치가 아닐 때
                if 0 <= nx < R and 0 <= ny < C and not (ny == 0 and (nx in air_conditioner)):
                    move_dir_count += 1
                    if (nx, ny) in next_dust_pos:
                        next_dust_pos[(nx, ny)] += dust_now // 5
                    else:
                        next_dust_pos[(nx, ny)] = dust_now // 5
        if (x, y) in next_dust_pos:
            next_dust_pos[(x, y)] += dust_now - (dust_now // 5) * move_dir_count
        else:
            next_dust_pos[(x, y)] = dust_now - (dust_now // 5) * move_dir_count
    return next_dust_pos


def air_conditioner_operate(dust_pos: dict, air_conditioner: list) -> dict:
    global air_conditioner_route
    # 바람 부는 방향 반대로 확인, 가장 앞부분은 공기청정기에 제거, 나머지는 이동
    # 가장 앞부분은 0으로 처리
    if (air_conditioner_route[0][0]) in air_conditioner:
        air_conditioner[air_conditioner_route[0][0]] = 0
    if (air_conditioner_route[1][0]) in air_conditioner:
        air_conditioner[air_conditioner_route[1][0]] = 0
    # 공기 청정기 작동
    # i번째 위치에 미세먼지 있으면 i - 1위치로 이동
    # i번째 위치의 미세먼지 0으로
    for i in range(1, len(air_conditioner_route[0])):
        # 해당 위치가 비어있으면 확인할 필요 없음
        if air_conditioner_route[0][i] in dust_pos:
            # 미세먼지 이동
            dust_pos[air_conditioner_route[0][i - 1]] = dust_pos[air_conditioner_route[0][i]]
            # 이동된 자리는 0으로
            dust_pos[air_conditioner_route[0][i]] = 0
    for i in range(1, len(air_conditioner_route[1])):
        # 해당 위치가 비어있으면 확인할 필요 없음
        if air_conditioner_route[1][i] in dust_pos:
            # 미세먼지 이동
            dust_pos[air_conditioner_route[1][i - 1]] = dust_pos[air_conditioner_route[1][i]]
            # 이동된 자리는 0으로
            dust_pos[air_conditioner_route[1][i]] = 0
    return dust_pos


R, C, T = MIIS()
house = [list(MIIS()) for _ in range(R)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

# 미세먼지 위치-양 계산
dust_pos = {}
# 공기청정기 위치
air_conditioner = []
for i in range(R):
    for j in range(C):
        if house[i][j] == -1:
            air_conditioner.append(i)
        elif house[i][j]:
            dust_pos[(i, j)] = house[i][j]

# 공기청정기 작동 경로
x1, x2 = air_conditioner
air_conditioner_route = [
    # 위쪽 경로
    list((i, 0) for i in range(x1 - 1, -1, -1))\
    + list((0, j) for j in range(1, C))\
    + list((i, C - 1) for i in range(1, x1 + 1))\
    + list((x1, j) for j in range(C - 2, 0, -1)),
    # 아래쪽 경로
    list((i, 0) for i in range(x2 + 1, R))\
    + list((R - 1, j) for j in range(1, C))\
    + list((i, C - 1) for i in range(R - 2, x2 - 1, - 1))\
    + list((x2, j) for j in range(C - 2, 0, -1)),
]

for _ in range(T):
    # 미세먼지 확산
    dust_pos = dust_move(dust_pos, air_conditioner)
    
    # dust_map = [[0] * C for _ in range(R)]
    # for (x, y), count in dust_pos.items():
    #     dust_map[x][y] = count
    # pprint(dust_map)
    # pprint('---------------------')
    
    # 공기청정기 작동
    dust_pos = air_conditioner_operate(dust_pos, air_conditioner)

    # dust_map = [[0] * C for _ in range(R)]
    # for (x, y), count in dust_pos.items():
    #     dust_map[x][y] = count
    # pprint(dust_map)
    # pprint('---------------------')

print(sum(dust_pos.values()))
'''