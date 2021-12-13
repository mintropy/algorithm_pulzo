"""
Title : X와 K
Link : https://www.acmicpc.net/problem/1322
"""

import sys
input = sys.stdin.readline


X, K = map(int, input().split())

ones = set()
idx = 0
while True:
    if X < (1 << idx):
        break
    if X & (1 << idx):
        ones.add(idx)
    idx += 1
zeros = sorted(set(range(100)) - ones)

ans = 0
while K:
    idx = 0
    while True:
        if K < (1 << (idx + 1)):
            break
        idx += 1
    ans += 1 << zeros[idx]
    K -= 1 << idx

print(ans)
