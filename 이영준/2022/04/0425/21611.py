"""
Title : 마법사 상어와 블리자드
Link : https://www.acmicpc.net/problem/21611
"""

import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def square_to_linear(n: int, magical_map: int) -> list:
    # 기본 지도를 선형으로 저장
    magical_linear_map = [0] * (n ** 2)
    # 탐색 방향, 길이
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    search = [i // 2 for i in range(2, n * 2 + 1)]
    search[-1] -= 1
    # 선형 지도에 넣을 위치
    idx = 1
    # 정 사각형 지도에서 지금 위치, 방향
    d = 0
    x = y = n // 2
    for s in search:
        # s칸만큼 앞으로 진행
        for _ in range(s):
            # 한 칸 앞으로
            x, y = x + dx[d], y + dy[d]
            # 해당 칸의 숫자 저장
            magical_linear_map[idx] = magical_map[x][y]
            idx += 1
        # 방향 회전
        d = (d + 1) % 4
    return magical_linear_map


def freeze_balls(magical_linear_map: list, d: int, s: int, linear_idx: list) -> list:
    # 마법을 사용해서 구슬 파괴
    for i in range(s):
        magical_linear_map[linear_idx[d][i]] = 0
    return magical_linear_map


def ball_front_explode(n: int, magical_linear_map: list) -> int:
    # 구슬이 폭발할때마다 점수를 저장해서 리턴
    score = 0
    while True:
        # 폭발이 있었는지
        is_explode = False
        # 연속된 구슬의 위치
        # 구슬을 계속 당기지 말고, 4개 이상이면 0으로 바꾸기만 하자
        balls_idx = []
        # 지금 확인 하는 숫자, 연속 개수
        ball_num_now = 0
        for i in range(1, n ** 2):
            # 빈공간이면 넘어가기
            if magical_linear_map[i] == 0:
                continue
            # 기존에 공을 보고 있지 않았거나, 기존과 같은 공일때
            elif len(balls_idx) == 0:
                ball_num_now = magical_linear_map[i]
                balls_idx = [i]
            elif ball_num_now == magical_linear_map[i]:
                balls_idx.append(i)
            # 새로운 공이 시작되고, 이전 공 정보 있을때 폭발
            # 구슬을 당기지 않으면, 폭발이 아닐 때 작업 필요 ㄴㄴ
            else:
                if len(balls_idx) >= 4:
                    score += ball_num_now * len(balls_idx)
                    is_explode = True
                    # 폭발할 구슬 위치 모두 0으로
                    for j in balls_idx:
                        magical_linear_map[j] = 0
                # 지금 위치에서 다시 공 개수 세는 카운트하기
                # 빈 공간인지에 따라
                ball_num_now = magical_linear_map[i]
                if ball_num_now != 0:
                    balls_idx = [i]
                else:
                    balls_idx = []
        # 마지막 부분 입력 or 폭발
        if len(balls_idx) >= 4:
            score += ball_num_now * len(balls_idx)
            is_explode = True
            for j in balls_idx:
                magical_linear_map[j] = 0
        # 변화가 없을 때
        if not is_explode:
            return score, magical_linear_map


def new_balls(n: int, magical_linear_map: list) -> list:
    new_magical_linear_map = [0] * (n ** 2)
    # 새로 변하는 구슬 입력위치 인덱스
    idx_input = 1
    ball_num_now = 0
    ball_continuous = 0
    for i in range(1, n ** 2):
        # 빈공간이면 넘어가기
        if magical_linear_map[i] == 0:
            continue
        # 새로운 리스트에 추가하지 못할 때
        if idx_input == n ** 2:
            break
        # 같은 공이 연속될 때
        if ball_num_now == magical_linear_map[i]:
            ball_continuous += 1
        # 다른 공이 나오면 정보 입력
        else:
            if ball_num_now != 0:
                # 이전 공에 대한 정보 처리
                new_magical_linear_map[idx_input] = ball_continuous
                new_magical_linear_map[idx_input + 1] = ball_num_now
                idx_input += 2
            # 새로운 공 정보 입력
            ball_num_now = magical_linear_map[i]
            if ball_num_now != 0:
                ball_continuous = 1
            else:
                ball_continuous = 0
    # 입력하지 못한 공 정보가 있는지
    if idx_input < n ** 2 and ball_continuous > 0:
        new_magical_linear_map[idx_input] = ball_continuous
        new_magical_linear_map[idx_input + 1] = ball_num_now
    return new_magical_linear_map


n, m = MIIS()
magical_map = [list(MIIS()) for _ in range(n)]

# 지도를 선형으로 바꾸어 탐색
magical_linear_map = square_to_linear(n, magical_map)
# 각 방향이 주어졌을 때 확인해야하는 인덱스
linear_idx = [[], [7, 22], [3, 14], [1, 10], [5, 18]]
# 인덱스 추가적 생성
for _ in range(7, n + 1, 2):
    for i in range(1, 4 + 1):
        l1, l2 = linear_idx[i][-1], linear_idx[i][-2]
        linear_idx[i].append(l1 + (l1 - l2 + 8))

totla_score = 0
# 블리자드 실행
for _ in range(m):
    d, s = map(int, input().split())
    # d방향 s칸에 구슬 파괴
    magical_linear_map = freeze_balls(magical_linear_map, d, s, linear_idx)
    # 구슬 앞으로 & 폭발
    # 구슬을 앞으로 당기지는 않음
    score, magical_linear_map = ball_front_explode(n, magical_linear_map)
    totla_score += score
    # 구슬 변화 / 중간에 빈 공간도 확인하며 채워넣기
    magical_linear_map = new_balls(n, magical_linear_map)

print(totla_score)
