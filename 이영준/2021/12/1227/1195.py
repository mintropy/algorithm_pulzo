"""
Title : 킥다운
Link : https://www.acmicpc.net/problem/1195
"""

import sys
input = sys.stdin.readline


up = list(input().strip())
down = list(input().strip())
if len(up) > len(down):
    up, down = down, up

len_up, len_down = len(up), len(down)
min_len = len_up + len_down

for i in range(len_up - 1, -1, -1):
    for j in range(len_up - i):
        if up[i + j] == down[j] and up[i + j] == '2':
            break
    else:
        if min_len > len_up + len_down - (len_up - i):
            min_len = len_up + len_down - (len_up - i)

for i in range(1, len_down - len_up + 1):
    for j in range(len_up):
        if up[j] == down[i + j] and up[j] == '2':
            break
    else:
        if min_len > len_down:
            min_len = len_down
            break

for i in range(len_down - len_up + 1, len_down):
    for j in range(len_down - i):
        if up[j] == down[i + j] and up[j] == '2':
            break
    else:
        if min_len > len_up + len_down - (len_down - i):
            min_len = len_up + len_down - (len_down - i)
        break

print(min_len)
