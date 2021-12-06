"""
Title : 나이트 게임
Link : https://www.acmicpc.net/problem/16884
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    if int(input()) % 2:
        print('koosaga')
    else:
        print('cubelover')

'''
# short coding
for _ in range(int(input())):
    print(['cubelover','koosaga'][int(input())%2])
'''

'''
모든 경우 0 ~ 8칸에 영향(놓을 수 없게 됨)을 줌
    >> (거의 모든 경우의 수에서) 놓여진 말 위치에 따라 1 ~ 8칸 덜 영향을 줄 수 있음

n이 짝수 일 때 : 선 플레이어가 짐
    >> 전체 짝수 개
    >> 선 플레이어가 이기려면 홀수개 칸을 남겨서 넘겨줘야 함
    >> 후 플레이어가 항상 짝수개 칸을 남기도록 나이트 배치할 수 있음

n이 홀수 일 때 : 선 플레이어가 이김
    >> 전체 홀수 개
    >> 선플레이어가 항상 놓을 수 있는 칸을 홀수개로 유지할 수 있음
'''
