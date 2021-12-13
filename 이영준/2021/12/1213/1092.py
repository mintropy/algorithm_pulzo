"""
Title : 배
Link : https://www.acmicpc.net/problem/1092
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N = int(input())
weight_limits = sorted((MIIS()), reverse=True)
M = int(input())
box_weights = sorted((MIIS()), reverse=True)

if box_weights[0] > weight_limits[0]:
    print(-1)
else:
    idx = []
    for i in range(N):
        for j in range(M):
            if weight_limits[i] >= box_weights[j]:
                idx.append(j)
                break
        else:
            idx.append(M)
    
    count = 0
    box_count = M
    while box_count:
        for i in range(N):
            box_idx = idx[i]
            while box_idx < M:
                if box_weights[box_idx]:
                    break
                box_idx += 1
            if box_idx == M:
                break
            box_weights[box_idx] = 0
            box_count -= 1
        count += 1
    print(count)
