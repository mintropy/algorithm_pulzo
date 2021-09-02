import sys
from collections import deque
input = sys.stdin.readline
def sol():
    N, M = map(int, input().split())
    ocean = [list(map(int, input().split())) for _ in range(N)]
    di = (-1, 0, 1, 0)
    dj = (0, 1, 0, -1)
    # 두 덩어리로 갈라지는데 걸리는 시간
    res = 0
    # 빙하의 좌표를 담는 배열
    iceberg = []
    # 바다와 인접한 빙하의 좌표와 인접면 개수를 담는 배열
    melting_ice = []
    # 첫 행,열과 마지막 행,열은 바다이므로 1 ~ N - 1
    # 줄여보려는 시도를 했으나 오히려 시간이 더 걸리길래 포기함
    # Phase 1. iceberg와 melting_ice를 수집함
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if ocean[i][j] != 0:
                iceberg.append([i, j])
                cnt = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ocean[ni][nj] == 0:
                        cnt += 1
                if cnt > 0:
                    melting_ice.append([i, j, cnt])
    # Phase 2. 두 덩어리로 갈라질 때까지 무한 반복
    while True:
        # Phase 2-1. 빙하가 녹는다.
        while melting_ice:
            y, x, cnt = melting_ice.pop()
            ocean[y][x] -= cnt
            if ocean[y][x] <= 0:
                ocean[y][x] = 0
        # 빙하가 몇 덩어리인지 판단할 변수
        berg_part = 0
        chk = [[True for _ in range(M)] for _ in range(N)]
        # Phase 2-2. 빙하가 몇 덩어리인지 판단
        for i, j in iceberg:
            if ocean[i][j] != 0 and chk[i][j]:
                chk[i][j] = False
                berg_part += 1
                queue = deque([[i, j]])
                while queue:
                    y, x = queue.popleft()
                    for k in range(4):
                        ny = y + di[k]
                        nx = x + dj[k]
                        if ocean[ny][nx] != 0 and chk[ny][nx]:
                            chk[ny][nx] = False
                            queue.append([ny, nx])
        # 날짜 카운트
        res += 1
        # 빙하가 0개이면 2개로 갈라지지 않고 다 녹았다는 것
        if berg_part == 0:
            return 0
        # 빙하가 2개 이상이면 결과 반환
        if berg_part > 1:
            return res
        # Phase 2-3. 녹을 빙하를 다시 카운트
        for i, j in iceberg:
            if ocean[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ocean[ni][nj] == 0:
                        cnt += 1
                if cnt > 0:
                    melting_ice.append([i, j, cnt])
        # Phase 2-2와 2-3을 합칠 수가 있음
print(sol())





# import sys
# from collections import deque
# input = sys.stdin.readline
# def sol():
#     N, M = map(int, input().split())
#     iceberg = [list(map(int, input().split())) for _ in range(N)]
#     di = (-1, 0, 1, 0)
#     dj = (0, 1, 0, -1)
#     res = 0
#     while True:
#         arr = []
#         part = 0
#         chk = [[0 for _ in range(M)] for _ in range(N)]
#         for i in range(1, N - 1):
#             for j in range(1, M - 1):
#                 if iceberg[i][j] != 0:
#                     if chk[i][j] == 0:
#                         chk[i][j] = 1
#                         part += 1
#                         q = deque([[i, j]])
#                         while q:
#                             y, x = q.popleft()
#                             for k in range(4):
#                                 ni = y + di[k]
#                                 nj = x + dj[k]
#                                 if iceberg[ni][nj] != 0 and chk[ni][nj] == 0:
#                                     chk[ni][nj] = 1
#                                     q.append([ni, nj])
#                     cnt = 0
#                     for k in range(4):
#                         ni = i + di[k]
#                         nj = j + dj[k]
#                         if iceberg[ni][nj] == 0:
#                             cnt += 1
#                     if cnt > 0:
#                         arr.append([i, j, cnt])
#         if part == 0:
#             return 0
#         if part > 1:
#             return res
#         res += 1
#         for y, x, melt in arr:
#             iceberg[y][x] -= melt
#             if iceberg[y][x] < 0:
#                 iceberg[y][x] = 0
# print(sol())