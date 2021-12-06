'''
돌 게임 6

'''
import sys
input = sys.stdin.readline

N = int(input())

if N % 7 == 2 or N % 7 == 0:
    print('CY')
else:
    print('SK')