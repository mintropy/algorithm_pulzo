'''
별자리 만들기

'''
import sys
input = sys.stdin.readline

N = int(input())

stars = []
for i in range(N):
    stars.append(tuple(map(float,input().split())))

visit = [0] * N
INF = 10**5
dist = [INF] * N
dist[0] = 0

# 프림 알고리즘
for _ in range(N):
    # 최소거리인 별 찾기
    min_dist = INF
    for i in range(N):
        if visit[i] == 0 and min_dist > dist[i]:
            u = i
            min_dist = dist[i]

    visit[u] = 1

    # 거리를 구해서 더 짧은 거리를 갱신
    for v in range(N):
        # 피타고라스와 round를 통해서
        now_dist = (abs(stars[u][0] - stars[v][0])**2 + abs(stars[u][1] - stars[v][1])**2)**0.5
        now_dist = round(now_dist,2)
        if visit[v] == 0 and dist[v] > now_dist:
            dist[v] = now_dist

print(sum(dist))