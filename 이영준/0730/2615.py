"""
Title : 오목
Link : https://www.acmicpc.net/problem/2615
"""

import sys
input = sys.stdin.readline


def is_omok(omok, color):
    # 각 색을 기준으로 네 방향으로 탐색
    # 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선
    # 동시에 각각에 해당하는 반대방향 탐색
    for i in range(19):
        for j in range(19):
            # 해당하는 색을 만나면
            if omok[i][j] == color:
                for d in range(4):
                    tf, left_most = search(omok, color, i, j, d)
                    if tf:
                        return True, left_most
    return False, [0, 0]

def search(omok, color, i, j, d):
    # 양방향으로 확인하기
    dx, dy = [0, 1, 1, 1], [1, 1, 0, -1]
    # 해당 방향 d와 반대 방향
    dx1, dy1 = [0, -1, -1, -1], [-1, -1, 0, 1]
    # 해당 color의 돌이 몇 개인지
    # 해당 칸을 제외, 양쪽으로 각각 +5칸씩 확인
    count = 1
    # 가장 왼쪽 돌 확인
    left_most = [i, j]
    # 양 방향 따로 확인
    for k in range(1, 6):
        x1, y1 = i + dx[d] * k, j + dy[d] * k
        # 범위를 벗어나지 않는지
        if x1 < 0 or x1 >= 19:
            break
        if y1 < 0 or y1 >= 19:
            break
        # 범위 안이고, 해당 색인지
        if omok[x1][y1] == color:
            count += 1
            if y1 < left_most[1]:
                left_most = [x1, y1]
            elif y1 == left_most[1] and x1 < left_most[0]:
                left_most = [x1, y1]
        else:
            break
    for k in range(1, 6):
        x2, y2 = i + dx1[d] * k, j + dy1[d] * k
        # 범위를 벗어나지 않는지
        if x2 < 0 or x2 >= 19:
            break
        if y2 < 0 or y2 >= 19:
            break
        # 범위 안이고, 해당 색인지
        if omok[x2][y2] == color:
            count += 1
            if y2 < left_most[1]:
                left_most = [x2, y2]
            elif y2 == left_most[1] and x2 < left_most[0]:
                left_most = [x2, y2]
        else:
            break
    # 정확히 오목인지 확인
    if count == 5:
        return True, left_most
    else:
        return False, [0, 0]


omok = [list(map(int, input().split())) for _ in range(19)]
tf1, left_most1 = is_omok(omok, 1)
tf2, left_most2 = is_omok(omok, 2)
# 0,0 기준으로 계산하였기에, 좌표는 각각 +1 해줌
if tf1:
    print(1)
    print(left_most1[0] + 1, left_most1[1] + 1)
elif tf2:
    print(2)
    print(left_most2[0] + 1, left_most2[1] + 1)
else:
    print(0)