import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
Ns = map(int, input().split())
M = int(input())
Ms = map(int, input().split())

d = {}
for v in Ns:
    d[v] = d.setdefault(v, 0) + 1

print(*[d.setdefault(v, 0) for v in Ms])