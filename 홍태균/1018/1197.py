'''
최소 스패닝 트리

'''
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
INF = 30000000000
Nodes = [[] for _ in range(V+1)]


for _ in range(E):
    n1, n2, w = map(int,input().split())
    Nodes[n1].append((n2,w))
    Nodes[n2].append((n1,w))


W = [INF] * (V+1)
visit = [0] * (V+1)

W[0] = 0
W[1] = 0

for _ in range(V):
    min_v = INF
    for i in range(1,V+1):
        if min_v > W[i] and visit[i] == 0:
            u = i
            min_v = W[i]

    visit[u] = 1

    for i,w in Nodes[u]:
        if  visit[i] == 0 and W[i] > w:
            W[i] = w


print(sum(W))

