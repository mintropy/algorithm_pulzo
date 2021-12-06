"""
Title : 화학 실험
Link : https://www.acmicpc.net/problem/20311
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
colors = list(MIIS())


if max(colors) > (N + 1) // 2:
    print(-1)
else:
    seq = [0] * N
    colors_list = []
    for i in range(K):
        colors_list += [(colors[i], i + 1) for _ in range(colors[i])]
    colors_list.sort(key=lambda x:x[0])
    
    for i in range(0, N, 2):
        _, idx = colors_list.pop()
        seq[i] = idx
    for i in range(1, N, 2):
        _, idx = colors_list.pop()
        seq[i] = idx
    
    print(*seq)
