"""
Title : 1루수가 누구야
Link : https://www.acmicpc.net/problem/17349
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


informations = [tuple(map(int, input().split())) for _ in range(9)]

ans = -1
for liar in range(9):
    # -1 : don't know, 0 : NO, 1: YES
    possible_first_base = [-1] * 10
    contradiction = False
    for idx, (condition, num) in enumerate(informations):
        if idx == liar:
            condition = (condition + 1) % 2
        if condition:
            if possible_first_base[num] == 0:
                contradiction = True
                break
            else:
                possible_first_base[num] = 1
        else:
            if possible_first_base[num] == 1:
                contradiction = True
                break
            else:
                possible_first_base[num] = 0
    if contradiction:
        continue
    candidate = -1
    next_candidate = []
    for i in range(1, 10):
        if possible_first_base[i] == 1:
            if candidate == -1:
                candidate = i
            else:
                contradiction = True
        elif possible_first_base[i] == -1:
            next_candidate.append(i)
    if contradiction:
        continue
    elif ans != -1:
        ans = -1
        break
    elif candidate == -1:
        if len(next_candidate) == 1:
            ans = next_candidate[0]
    else:
        ans = candidate

print(ans)
