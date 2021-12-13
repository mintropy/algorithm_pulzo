"""
Title : 선분 덮기
Link : https://www.acmicpc.net/problem/2024
"""

import sys
input = sys.stdin.readline


M = int(input())

lines = []
while True:
    l, r = map(int, input().split())
    if l == 0 and r == 0:
        break
    if l < 0:
        l = 0
    if r > M:
        r = M
    if l == r or r <= 0 or l >= M:
        continue
    else:
        lines.append((max(0, l), min(M, r)))
lines.sort(key=lambda x: (x[0], -(x[1] - x[0])))

now = 0
next_prob = 0
count = 0
for l, r in lines:
    if l > now:
        now = next_prob
        count += 1
        if l > now:
            break
    if r > next_prob:
        next_prob = r
else:
    if now != M and next_prob == M:
        now = M
        count += 1

if now == M:
    print(count)
else:
    print(0)
