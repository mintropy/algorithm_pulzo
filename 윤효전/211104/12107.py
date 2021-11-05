import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
if N == 1:
    print('B')
else:
    print('A')
