"""
Title : 욱제는 정치쟁이야!!
Link : https://www.acmicpc.net/problem/15925
"""

import sys
input = sys.stdin.readline


def search():
    global n, computer_room, computer_on_count
    # 컴퓨터를 하나라도 끈 것이 있는지
    computer_status_change = False
    # 각 가로줄 / 세로줄 별로 탐색
    # 가로부터 탐색
    for i in range(n):
        computer_on = 0
        computer_off = 0
        for j in range(n):
            if computer_room[i][j]:
                computer_on += 1
            else:
                computer_off += 1
        # 해당 줄을 끌 수 있을 때
        if computer_off > computer_on:
            for j in range(n):
                if computer_room[i][j] == 1:
                    computer_status_change = True
                    computer_room[i][j] = 0
                    computer_on_count -= 1
    # 세로 탐색
    for i in range(n):
        computer_on = 0
        computer_off = 0
        for j in range(n):
            if computer_room[j][i]:
                computer_on += 1
            else:
                computer_off += 1
        # 해당 줄을 끌 수 있을 때
        if computer_off > computer_on:
            for j in range(n):
                if computer_room[j][i] == 1:
                    computer_status_change = True
                    computer_room[j][i] = 0
                    computer_on_count -= 1
    
    if computer_status_change:
        return True
    else:
        return False


n, next = map(int, input().split())

# 다음 시간에 따라 바꿔서 처리하는 대신
# 모두 끄는 문제로 설정하여 해결
if next == 1:
    def change(s):
        if s == '0':
            return 1
        else:
            return 0
    computer_room = [list(map(change, input().split())) for _ in range(n)]
else:
    computer_room = [list(map(int, input().split())) for _ in range(n)]

# 켜져있는 컴퓨터
computer_on_count = 0
for i in range(n):
    for j in range(n):
        if computer_room[i][j]:
            computer_on_count += 1

# 각 대각선을 탐색하며, 꺼진 컴퓨터가 더 많은 줄을 모두 조작
while True:
    if not computer_on_count:
        print(1)
        break
    if not search():
        print(0)
        break
