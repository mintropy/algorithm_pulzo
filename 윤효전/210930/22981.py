import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def calc_work(a, b):
    return a[0]*len(a) + b[-1]*len(b)


N, K = map(int, input().split())
a = sorted(map(int, input().split()))
b = []

ans = 0
for i in range(N-1):
    b.append(a.pop())
    ans = max(ans, calc_work(a, b))

if K % ans == 0:
    print(K//ans)
else:
    print(K//ans+1)
