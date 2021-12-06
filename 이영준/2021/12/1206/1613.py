"""
Title : 역사
Link : https://www.acmicpc.net/problem/1613
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def check_historical_evens(idx):
    global history_events, prev_events, visited
    if visited[idx]:
        return
    visited[idx] = True
    for j in history_events[idx]:
        check_historical_evens(j)
        prev_events[idx] |= {j}
        prev_events[idx] |= prev_events[j]


N, K = MIIS()
history_events = [[] for _ in range(N + 1)]
for _ in range(K):
    x, y = MIIS()
    history_events[x].append(y)

prev_events = [set() for _ in range(N + 1)]
visited = [False] * (N + 1)
for i in range(1, N + 1):
    check_historical_evens(i)

for _ in range(int(input())):
    x, y = MIIS()
    if y in prev_events[x]:
        print(-1)
    elif x in prev_events[y]:
        print(1)
    else:
        print(0)


'''
# Python TLE
# Floyd Warshall
N, K = MIIS()
history_events = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    x, y = MIIS()
    history_events[x][y] = True

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if history_events[i][k] and history_events[k][j]:
                history_events[i][j] = True

for _ in range(int(input())):
    x, y = MIIS()
    if history_events[x][y]:
        print(-1)
    elif history_events[y][x]:
        print(1)
    else:
        print(0)
'''
