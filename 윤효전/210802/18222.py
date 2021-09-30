import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

l = []
n = 1
while n <= 1_000_000_000_000_000_000:
    l.append(n)
    n *= 2

import bisect

def solve(n, depth):
    if n == 1:
        return [0, 1][depth%2 == 1]
    return solve(n-l[bisect.bisect_left(l, n)-1], depth+1)


print(solve(N, 0))