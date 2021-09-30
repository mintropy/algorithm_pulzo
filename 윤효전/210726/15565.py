import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

import collections

N, K = map(int, input().rstrip().split())
S = list(map(int, input().rstrip().split()))

dq = collections.deque()
i = 0
ans = float('inf')
c = 0

while i < len(S):
    dq.append(S[i])
    if S[i] == 1:
        c += 1
    while c >= K:
        ans = min(ans, len(dq))
        if dq.popleft() == 1:
            c -= 1
    i += 1

print([ans, -1][ans == float('inf')])