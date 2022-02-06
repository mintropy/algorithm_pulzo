"""
Title : 안정된 집단
Link : https://www.acmicpc.net/problem/2653
"""

import sys
input = sys.stdin.readline


N = int(input())
relations = [list(map(int, input().split())) for _ in  range(N)]

subgroups = []
check = [False] * N

possible = True
for i in range(N):
    if not possible:
        break
    if not check[i]:
        prob_subgroup = [i]
        for j in range(i + 1, N):
            if not relations[i][j]:
                prob_subgroup.append(j)
        if len(prob_subgroup) == 1:
            possible = False
            break
        for j in prob_subgroup[1:]:
            tmp = []
            for k in range(i, N):
                if not relations[j][k]:
                    tmp.append(k)
            if tmp != prob_subgroup:
                possible = False
                break
        else:
            for j in prob_subgroup:
                check[j] = True
            subgroups.append([j + 1 for j in prob_subgroup])

if possible:
    print(len(subgroups))
    for line in subgroups:
        print(*line)
else:
    print(0)
