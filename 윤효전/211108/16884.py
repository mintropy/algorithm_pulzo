import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2:
        print('koosaga')
    else:
        print('cubelover')
