"""
Title : 유성
Link : https://www.acmicpc.net/problem/10703
"""

import sys
input = sys.stdin.readline


def find_meteor(r: int, s: int, picture: list) -> tuple:
    # 유성 전체
    meteor = []
    # 유성에서 확인하면 되는 부분
    # 모든 열에서 가장 밑부분만 확인하면 됨
    meteor_check = [-1] * s
    for i in range(r):
        for j in range(s):
            if picture[i][j] == 'X':
                meteor.append([i,j])
                if meteor_check[j] < i:
                    meteor_check[j] = i
    
    return meteor, meteor_check


def check(picture: list, meteor_check: list) ->bool:
    global s
    # 확인할 유성이 한 칸 내려가서 땅과 만나면 False
    # 아니라면 True 반환
    for j in range(s):
        if picture[meteor_check[j] + 1][j] == '#':
            return False    
    return True


r, s = map(int, input().split())

picture = [list(str(input().strip())) for _ in range(r)]

meteor, meteor_check = find_meteor(r, s, picture)
meteor_down = 0

# 하나하나씩 내리지 말고, 몇 칸 내려가는지 확인 & 마지막에 적용하기
while True:
    # 유성이 더 내려가지 못하는 경우 종료
    if not check(picture, meteor_check):
        # 종료되기 전 내려가야되는 정보를 바탕으로 picture 수정하기
        for i, j in meteor[::-1]:
            picture[i][j] = '.'
            picture[i + meteor_down][j] = 'X'
        break
    meteor_down += 1
    # 확인하면 되는 meteor_check의 유성만 한칸씩 내리기
    for k in range(s):
        if meteor_check[k] != -1:
            meteor_check[k] += 1

for pic in picture:
    print(''.join(pic))