"""
Title : 맥주 마시면서 걸어가기
Link : https://www.acmicpc.net/problem/9205
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    home = tuple(map(int, input().split()))
    conv = set(tuple(map(int, input().split())) for _ in range(n))
    festival = tuple(map(int, input().split()))
    conv.add(festival)
    
    st = set()
    st.add(home)
    arrival = False
    while st:
        near = set()
        # 주변에 가능한지
        for x in st:
            for y in conv:
                if abs(x[0] - y[0]) + abs(x[1] - y[1]) <= 1000:
                    near.add(y)
        # 주변을 시작으로
        conv -= near
        st = near
        if festival in near:
            arrival = True
            break
    
    if arrival:
        print('happy')
    else:
        print('sad')


'''
import sys, collections
# bfs
for _ in range(int(input())):
    n = int(input())
    home = tuple(map(int, input().split()))
    conv = list(tuple(map(int, input().split())) for _ in range(n))
    festival = tuple(map(int, input().split()))
    points = [home] + conv + [festival]
    
    # 1 불가능, 0 가능
    dist = [[0] * (n + 2) for _ in range (n + 2)]
    for i in range(n + 2):
        for j in range(i):
            x1, y1 = points[i]
            x2, y2 = points[j]
            d = abs(x1 - x2) + abs(y1 - y2)
            if d > 1000:
                continue
            dist[i][j] = 1
            dist[j][i] = 1
    
    queue = collections.deque([0])
    visited = [False] * (n + 2)
    arrival = False
    while queue:
        p = queue.popleft()
        if p == n + 1:
            arrival = True
            break
        visited[p] = True
        for q in range(n + 2):
            if dist[p][q] and not visited[q]:
                queue.append(q)
    
    if arrival:
        print('happy')
    else:
        print('sad')
'''


'''
# slow Floyd_Warshall
for _ in range(int(input())):
    n = int(input())
    home = tuple(map(int, input().split()))
    conv = list(tuple(map(int, input().split())) for _ in range(n))
    festival = tuple(map(int, input().split()))
    points = [home] + conv + [festival]
    
    # 1 불가능, 0 가능
    dist = [[0] * (n + 2) for _ in range (n + 2)]
    for i in range(n + 2):
        for j in range(i + 1):
            x1, y1 = points[i]
            x2, y2 = points[j]
            d = abs(x1 - x2) + abs(y1 - y2)
            if d > 1000:
                continue
            dist[i][j] = 1
            dist[j][i] = 1
    
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                # i에서 j까지
                dist_ij = dist[i][j]
                # i에서 j까지 k거쳐서
                dist_ik = dist[i][k]
                dist_kj = dist[k][j]
                if dist_ik and dist_kj and not dist_ij:
                    dist[i][j] = 1
    
    if dist[0][-1]:
        print('happy')
    else:
        print('sad')
'''
