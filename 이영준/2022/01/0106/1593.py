"""
Title : 문자 해독
Link : https://www.acmicpc.net/problem/1593
"""

import sys
input = sys.stdin.readline


len_w, len_s = map(int, input().split())
W = input().strip()
S = input().strip()

target = {}
for w in W:
    if w in target:
        target[w] += 1
    else:
        target[w] = 1

ans = 0
now = {}
for i in range(-1, len_w - 1):
    s = S[i]
    if s in now:
        now[s] += 1
    else:
        now[s] = 1

for i in range(len_w - 1, len_s):
    last, new = S[i - len_w], S[i]
    now[last] -= 1
    if now[last] == 0:
        now.pop(last)
    if new in now:
        now[new] += 1
    else:
        now[new] = 1
    
    if target == now:
        ans += 1

print(ans)
