'''
주간 미팅

'''
from sys import stdin
input = stdin.readline

N, V, E = map(int,input().split())
A, B = map(int,input().split())
H = list(map(int,input().split()))

INF = 987654321

maps = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, l = map(int,input().split())

    maps[a][b] = l
    maps[b][a] = l

# 다익스트라
def dij(st):
    global total
    D = [INF] * (V+1)
    D[st] = 0
    visit = [0] * (V+1)

    for i in range(1,V+1):
        if visit[A] and visit[B]:
            break
        min_v = INF
        for j in range(1,V+1):
            if visit[j] == 0 and min_v > D[j]:
                u = j
                min_v = D[j]

        visit[u] = 1

        for v in range(1,V+1):
            if D[v] > D[u] + maps[u][v] and maps[u][v] and visit[v] == 0:
                D[v] = D[u] + maps[u][v]
    # 거리 구하기
    if D[A] == INF:
        D[A] = -1
    if D[B] == INF:
        D[B] = -1

    total += D[A] + D[B]

total = 0

for i in H:
    dij(i)

print(total)