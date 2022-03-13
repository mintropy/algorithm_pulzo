'''
운동

'''
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
INF = 987654321
D = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    D[a][b] = c

for k in range(V):
    for j in range(V):
        for i in range(V):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

min_D = INF
for i in range(V):
    if min_D > D[i][i]:
        min_D = D[i][i]
if min_D == INF:
    print(-1)
else:
    print(min_D)


## 틀림
# def dfs(v,dist):
#     global i, min_dist
#     visit[v] = 1
#     for next, n_dist in vil[v]:
#         if visit[next]:
#             if next == i:
#                 if min_dist > dist + n_dist:
#                     min_dist = dist + n_dist
#             return
#         dfs(next,dist+n_dist)
        
# min_dist = 987654321    
# for i in range(V):
#     visit = [0] * V
#     dfs(i,0)   

# print(min_dist)