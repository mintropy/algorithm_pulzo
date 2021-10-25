import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

if N % 2 == 0 or M % 2 == 0:
    print('A')
else:
    print('B')
