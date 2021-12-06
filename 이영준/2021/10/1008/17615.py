"""
Title : 볼 모으기 
Link : https://www.acmicpc.net/problem/17615
"""

import sys
input = sys.stdin.readline


def find_cont_balls(balls: list) -> tuple:
    # 연속한 공 색과 개수
    left_color = balls[0]
    left_count = 1
    for i in range(1, n):
        if balls[i] == left_color:
            left_count += 1
        else:
            break
    right_color = balls[-1]
    right_count = 1
    for i in range(n - 2, -1, -1):
        if balls[i] == right_color:
            right_count += 1
        else:
            break
    return left_color, left_count, right_color, right_count


n = int(input())
balls = input().strip()

# 4가지로 나누어 진행
# 왼쪽 >> 오른쪽, 오른쪽 >> 왼쪽으로 이동하면서
# 파랑, 빨강이 각각 왼쪽, 오른쪽에 놓을 때 이동 횟수 탐색

# 더 간단하게
# 기본적으로 이동 횟수 == 파랑 / 빨강 공 개수
# 그런데 왼쪽, 오른쪽에서 연속한 파랑, 빨강 공 갯수만큼 줄여서 세면 됨

red_balls = balls.count('R')
blue_balls = n - red_balls

left_blue = right_blue = blue_balls
left_red =  right_red = red_balls

left_color, left_count, right_color, right_count = find_cont_balls(balls)

if left_color == 'R':
    left_red -= left_count
else:
    left_blue -= left_count
if right_color == 'R':
    right_red -= right_count
else:
    right_blue -= right_count

print(min(left_blue, left_red, right_blue, right_red))
