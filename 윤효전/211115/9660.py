import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())

if N % 7 == 0 or N % 7 == 2:
    print('CY')
else:
    print('SK')