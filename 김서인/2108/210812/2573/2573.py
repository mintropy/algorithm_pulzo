from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sea = []

for _ in range(N):
    sea.append(list(map(int, input().split())))

# 상우하좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 두 부분 이상으로 나뉘어졌는지 체크
def check():
    dq = deque()
    ch = list([0] * M for _ in range(N))
    ices_cnt = 0

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if ch[i][j] == 0 and sea[i][j] != 0:
                dq.append((i, j))
                ch[i][j] = 1
                ices_cnt += 1
                while dq:
                    y, x = dq.popleft()
                    for mode in range(4):
                        ii = y + di[mode]
                        jj = x + dj[mode]
                        if 1 <= ii < N - 1 and 1 <= jj < M - 1 and ch[ii][jj] == 0 and sea[ii][jj] != 0:
                            ch[ii][jj] = 1
                            dq.append((ii, jj))

    if ices_cnt <= 1:
        return False
    return True


# 1년마다 녹이기
def melt():
    melts = list([0] * M for _ in range(N))  # 빙산 얼마나 녹아야 하는지 저장하는 리스트

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if sea[i][j] != 0:
                # 얼마나 빙산 줄어들지
                melting_spots = 0
                for mode in range(4):
                    ii = i + di[mode]
                    jj = j + dj[mode]
                    if 0 <= ii < N and 0 <= jj < M and sea[ii][jj] == 0:
                        melting_spots += 1

                melts[i][j] = melting_spots

    # 그만큼씩 빼주기
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if sea[i][j] != 0:
                for _ in range(melts[i][j]):
                    if sea[i][j] > 0:
                        sea[i][j] -= 1


# 다 녹았는지 체크하는 함수
def all_melt():  # True or False를 리턴
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if sea[i][j] != 0:
                return False
    return True


year = 0
while True:
    if check():  # 빙산이 두 덩어리로 나눠졌으면
        print(year)
        break

    else:  # 빙산이 두 덩어리로 나눠지지 않았는데
        if all_melt():  # 빙산이 다 녹았으면
            print(0)
            break
        else:  # 빙산이 다 안 녹았으면 1년 더 !
            year += 1
            melt()
