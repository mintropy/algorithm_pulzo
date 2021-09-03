'''
Title : 킹
Link : https://www.acmicpc.net/problem/1063
'''

import sys

input = sys.stdin.readline

def move(d: str):
    global king, stone
    # 움직이기 전 기초 작업
    k1, k2 = king[0], int(king[1])
    s1, s2 = stone[0], int(stone[1])
    # 각 방향을 숫자로 변환, 변화량을 빠르게 호출
    dirc_to_num = {'T': 0, 'RT': 1, 'R': 2, 'RB': 3, 'B': 4, 'LB': 5, 'L': 6, 'LT': 7}
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    dirc_num = dirc_to_num[d]
    # 왕이 움직일 좌표
    l1, l2 = chr(ord(k1) + dy[dirc_num]), k2 + dx[dirc_num]
    # 가능한 경우의 수
    # 1. 킹의 이동에 문제가 없는 경우
    # 2. 이동했을 때, 보드를 넘는 경우
    # 3. 이동했을 때, 돌을 만나는 경우
    # 3-1. 만난 돌의 이동이 문제가 없는 경우
    # 3-2. 만난 돌이 이동하면 보드를 벗어나는 경우
    if l1 == '@' or l1 == 'I':
        # 체스판을 벗어나면 아무 행동도 하지 않음
        return
    if l2 == 0 or l2 == 9:
        # 체스판을 벗어나면 아무것도 하지 않음
        return
    if l1 != s1 or l2 != s2:
        # 이동 후 체스판 안에 있고, 돌과 만나지 않는 경우
        king = l1 + str(l2)
        return
    if l1 == s1 and l2 == s2:
        # 이동 후 체스판 안에 있고, 돌과 만나는 경우
        t1, t2 = chr(ord(s1) + dy[dirc_num]), s2 + dx[dirc_num]
        if t1 == '@' or t1 == 'I':
            # 돌이 이동할 때, 체스판을 벗어나는 경우
            return
        elif t2 == 0 or t2 == 9:
            # 돌이 이동할 때, 체스판을 벗어나는 경우
            return
        else:
            # 킹과 돌 모두 이동할 수 있을 때
            king = l1 + str(l2)
            stone = t1 + str(t2)
        return

king, stone, n = map(str, input().strip().split())
command = [str(input().strip()) for _ in range(int(n))]
for cmd in command:
    move(cmd)
print(king)
print(stone)