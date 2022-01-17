"""
Title : 스티커 정리 1
Link : https://www.acmicpc.net/problem/1101
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
ans = 10 ** 9

boxes = [list(MIIS()) for _ in range(N)]

for joker_box in range(N):
    # box # of color 
    color_box = [0] * M
    move_count = 0
    for box_num in range(N):
        if box_num == joker_box:
            continue
        color_idx = -1
        for i in range(M):
            if boxes[box_num][i]:
                if color_idx == -1:
                    color_idx = i
                else:
                    color_idx = -1
                    move_count += 1
                    break
        if color_idx >= 0:
            color_box[color_idx] += 1
    for i in range(M):
        if color_box[i] > 1:
            move_count += color_box[i] - 1
    if ans > move_count:
        ans = move_count
print(ans)
