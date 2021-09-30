import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
a, b = 1, 1
for _ in range(N-1):
    a, b = b, (a+b) % 10007
print(b)