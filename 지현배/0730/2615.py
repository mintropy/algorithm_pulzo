import sys

# 바둑판 세팅
go = []
for _ in range(19):
    go.append(list(map(int, sys.stdin.readline().split())))
# 각각 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선 방향
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]
# 반복문 중간에 return하기 위해 함수를 사용
def func():
    for i in range(19):
        for j in range(19):
            # 바둑판을 순회하며
            target = go[i][j]
            # 그 좌표의 바둑돌이 비어있지 않다면
            if target != 0:
                # 4 방향을 확인함
                for n in range(4):
                    # 탐색할 돌들이 유효한 좌표 내에 있는지 확인
                    # 왼쪽 아래 대각선 방향 탐색때문에
                    # target과 그 반대에 있는 돌 중 어느 돌이 가장 왼쪽 혹은 오른쪽, 아래 혹은 위에
                    # 있는지 모르기 때문에 min, max로 가장 사이드에 있는 돌이 좌표 내에 있는지 확인
                    if min(i, i + 4 * di[n]) < 0 or max(i, i + 4 * di[n]) > 18:
                        continue
                    if min(j, j + 4 * dj[n]) < 0 or max(j, j + 4 * dj[n]) > 18:
                        continue
                    # 탐색할 돌들을 오목 배열에 넣음
                    omok = [
                        target, 
                        go[i + di[n]][j + dj[n]], 
                        go[i + 2 * di[n]][j + 2 * dj[n]], 
                        go[i + 3 * di[n]][j + 3 * dj[n]], 
                        go[i + 4 * di[n]][j + 4 * dj[n]]
                        ]
                    # 배열 내 요소 들의 max와 min이 같다면 배열 내에 같은 수만 있다
                    if max(omok) == min(omok):
                        # 육목 이상인지 확인
                        # 육목 가능한 범위에 있는 돌이 유효한 좌표내에 있고 target과 같은 수라면
                        # continue
                        if 0 <= i - di[n] <= 18 and 0 <= j - dj[n] <= 18 and\
                            go[i - di[n]][j - dj[n]] == target:
                            continue
                        if 0 <= i + 5 * di[n] <= 18 and 0 <= j + 5 * dj[n] <= 18 and\
                            go[i + 5 * di[n]][j + 5 * dj[n]] == target:
                            continue
                        # 왼쪽 아래 대각선 방향 탐색이 아니라면 가장 왼쪽 위 좌표가 i, j이다.
                        if n != 3:
                            return target, i, j
                        # 왼쪽 아래 대각선 방향 탐색이라면 target에서 가장 먼 돌 좌표를 반환한다.
                        else:
                            return target, i + 4 * di[n], j + 4 * dj[n]
    # 오목이 없으면 0을 반환
    return 0
res = func()
# 승부 안 났을 때
if res == 0:
    print(0)
# 승부 났을 때
else:
    print(res[0])
    print(res[1] + 1, res[2] + 1)

# import sys

# go = []
# for _ in range(19):
#     go.append(list(map(int, sys.stdin.readline().split())))

# def func():
#     for i in range(19):
#         for j in range(19):
#             target = go[i][j]
#             if target != 0:
#                 if j < 15:
#                     omok = go[i][j:j + 5]
#                     if max(omok) == min(omok):
#                         for _ in range(1):
#                             if j > 0 and go[i][j - 1] == target:
#                                 break
#                             if j < 14 and go[i][j + 5] == target:
#                                 break
#                             return target, i, j
#                     if i < 15:
#                         omok = [target, go[i + 1][j + 1], go[i + 2][j + 2], go[i + 3][j + 3], go[i + 4][j + 4]]
#                         if max(omok) == min(omok):
#                             for _ in range(1):
#                                 if j > 0 and i > 0 and go[i - 1][j - 1] == target:
#                                     break
#                                 if j < 14 and i < 14 and go[i + 5][j + 5] == target:
#                                     break
#                                 return target, i, j
#                 if i < 15:
#                     omok = [target, go[i + 1][j], go[i + 2][j], go[i + 3][j], go[i + 4][j]]
#                     if max(omok) == min(omok):
#                         for _ in range(1):
#                             if i > 0 and go[i - 1][j] == target:
#                                 break
#                             if i < 14 and go[i + 5][j] == target:
#                                 break 
#                             return target, i, j
#                     if j > 3:
#                         omok = [target, go[i + 1][j - 1], go[i + 2][j - 2], go[i + 3][j - 3], go[i + 4][j - 4]]
#                         if max(omok) == min(omok):
#                             for _ in range(1):
#                                 if i > 0 and j < 14 and go[i - 1][j + 1]:
#                                     break
#                                 if i < 14 and j > 0 and go[i + 5][j - 5]:
#                                     break
#                                 return target, i + 4, j - 4
#     return 0
# res = func()
# if res == 0:
#     print(0)
# else:
#     print(res[0])
#     print(res[1] + 1, res[2] + 1)