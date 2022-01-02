'''
특정한 최단 경로

'''
import sys
input = sys.stdin.readline

N, E = map(int,input().split())
# map은 인접 리스트로
maps = [[] for _ in range(N+1)]

# 맵 만들기
for _ in range(E):
    a, b, c = map(int,input().split())
    maps[a].append((b,c))
    maps[b].append((a,c))

INF = 987654321
# 다익스트라 st -> ed
def dij(st,ed):
    dist = [INF] * (N+1)
    visit = [0] * (N+1)
    dist[st] = 0

    for _ in range(N):
        min_d = INF
        for i in range(1,N+1):
            if min_d > dist[i] and visit[i] == 0:
                u = i
                min_d = dist[i]
    
        visit[u] = 1
        if u == ed:
            return dist[u]

        for b, c in maps[u]:
            if dist[b] > dist[u] + c:
                dist[b] = dist[u] + c
    # 못가면 -1
    return -1


v1, v2 = map(int,input().split())
# 통과 못하면 -1을 출력하기 위해
route = -1

# 각 경로가 가지 못하면 안되기 때문에 0 이상 이면 된다
# 거리가 0일수도 있기 때문
if dij(1,v1) >= 0 and dij(v1,v2) >= 0 and dij(v2,N) >= 0 and dij(1,v2) >= 0 and dij(v1,N) >= 0:
    # 두개의 경로중 가장 짧은 것 - 경로는 v1으로 먼저 오는 것과 v2로 먼저 오는 경우를 나누어서
    route1 = dij(1,v1) + dij(v1,v2) + dij(v2,N)
    route2 = dij(1,v2) + dij(v1,v2) + dij(v1,N)
    route = min(route1,route2)
print(route)
'''
4 4
1 2 1
2 3 4
2 4 5
3 4 100
2 3
출력 : 14

4 5
1 2 100
2 3 4
2 4 5
3 4 100
1 3 1
2 3
출력 : 10

7 7
1 2 3
3 2 5
1 3 1
6 5 3
7 5 8
5 4 2
6 4 3
2 6
출력 : -1

4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
1 4
출력 : 4

3 3
1 3 20 
1 2 15
2 3 6 
1 3
출력 : 20
'''