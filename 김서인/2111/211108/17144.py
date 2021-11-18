import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

R, C, T = MIIS()
arr = [list(MIIS()) for _ in range(R)]


# 공기 청정기 위치 찾기
def find_air_cleaner():
    for i in range(R):
        if arr[i][0] == -1:
            return i


# 미세먼지 확산
def spread():
    # 미세 먼지 있는 모든 칸, 먼지 양을 미리 구해두자
    dust_zones = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust_zones.append((i, j, arr[i][j]))

    # 그 곳에서 먼저 확산
    for i, j, origin_volume in dust_zones:
        spread_volume = origin_volume // 5  # 확산되는 양

        # 확산될 것이 없으면 컨티뉴
        if spread_volume == 0:
            continue
        spread_cnt = 0
        # 인접한 네 방향으로 확산
        for k in range(4):
            ni = i + directions[k][0]
            nj = j + directions[k][1]

            # 범위 내
            if ni < 0 or ni >= R:
                continue
            if nj < 0 or nj >= C:
                continue

            # 공기 청정기 아니고
            if ni == air_cleaner_i and nj == 0:
                continue
            if (ni == air_cleaner_i + 1) and nj == 0:
                continue

            arr[ni][nj] += spread_volume
            spread_cnt += 1
        # 남은 미세먼지 양
        arr[i][j] -= (spread_volume * spread_cnt)


# 공기청정기 작동
def air_cleaner():
    # 위쪽

    # 아래쪽으로
    for i in range(air_cleaner_i - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]

    #  <-
    for j in range(C - 1):
        arr[0][j] = arr[0][j + 1]

    # 위로
    for i in range(air_cleaner_i):
        arr[i][C - 1] = arr[i + 1][C - 1]

    # ->
    for j in range(C - 1, 0, -1):
        arr[air_cleaner_i][j] = arr[air_cleaner_i][j - 1]
    # 공기청정기에서 나온 바람
    arr[air_cleaner_i][1] = 0

    # 아래

    # 위로
    for i in range(air_cleaner_i + 2, R - 1):
        arr[i][0] = arr[i + 1][0]

    #  <-
    for j in range(C - 1):
        arr[R - 1][j] = arr[R - 1][j + 1]

    # 아래쪽으로
    for i in range(R - 1, air_cleaner_i + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]

    # ->
    for j in range(C - 1, 0, -1):
        arr[air_cleaner_i + 1][j] = arr[air_cleaner_i + 1][j - 1]
    # 공기청정기에서 나온 바람
    arr[air_cleaner_i + 1][1] = 0


air_cleaner_i = find_air_cleaner()
for _ in range(T):  # T초만큼 반복
    spread()
    air_cleaner()

# 남은 먼지 양
left_dust = 0
for i in range(R):
    left_dust += sum(arr[i])
print(left_dust + 2)  # 공기 청정기
