'''
행복 유치원
https://www.acmicpc.net/problem/13164
'''

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
children = list(map(int, input().split()))
diff = [0] * (N - 1)

for i in range(N - 1):
    diff[i] = children[i + 1] - children[i]

diff.sort(reverse=True)

ans = 0

for i in range(K - 1, N - 1):
    ans += diff[i]

print(ans)
