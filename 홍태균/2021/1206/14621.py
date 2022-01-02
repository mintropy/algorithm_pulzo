'''
나만 안되는 연애

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

U_list = [0] + list(input().split())

# 무한 값
INF = 987654321

# 거리 저장 리스트
dist = [INF] * (N+1)
# 방문 리스트
visit = [0] * (N+1)
# 전체 맵
maps = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, d = map(int,input().split())
    maps[u].append((v,d))
    maps[v].append((u,d))

# 처음은 1에서 시작하기 위해서 0으로 초기화
dist[1] = 0

# 총 N개의 대학이 있기 때문에
for _ in range(N):
    # 최소 값
    min_d = INF
    # 전체 dist를 확인하여 
    # 가장 작은 값을 가진 대학을 선택
    for i in range(1,N+1):
        if min_d > dist[i] and visit[i] == 0:
            min_d = dist[i]
            u = i
    # 해당 대학을 방문
    visit[u] = 1

    # dist를 재 설정
    for v, d in maps[u]:
        # 방문 하지 않았고 현재 값보다 지금 거리가 더 가깝고 남,여 대학이 다르다면
        if visit[v] == 0 and dist[v] > d and U_list[u] != U_list[v]:
            dist[v] = d

# 모든 대학을 방문했다면 
# 각 도로의 값을 합하여 출력
if sum(visit) == N:
    print(sum(dist[1:]))
# 모든 대학을 방문하지 못하면 -1
else:
    print(-1)