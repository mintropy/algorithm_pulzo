'''
녹색 옷 입은 애가 젤다지?

'''
import sys
input = sys.stdin.readline
import heapq

# 방향
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
# 테스트 케이스 번호
tc = 0
while 1:
    # 테스트 번호 증가
    tc += 1
    N = int(input().strip())
    # 0이면 종료
    if N == 0:
        break
    INF = 987654321
    # 맵, 거리, 방문 리스트
    maps = [list(map(int,input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    # 처음 시작은 0,0 이기때문에 
    dist[0][0] = maps[0][0]
    q = []
    # heap으로 우선순위 큐 제작
    # 우선 순위를 거리로 두기위해서
    heapq.heappush(q, (maps[0][0],0,0))

    # 최대 N*N개가 나올 수 있기 때문
    for _ in range(N*N):
        # pop하면 가장 작은 거리의 node 빼내기
        node = heapq.heappop(q)

        # 현재 최소 거리
        now = node[0]
        # 현재 위치
        u = node[1:]
        
        # 도착지점
        if u == (N-1,N-1):
            break
        # 방문
        visit[u[0]][u[1]] = 1

        # 방향 탐색
        for dir in dirs:
            nx = u[0] + dir[0]
            ny = u[1] + dir[1]
            # 범위 안에서 방문 안했고 거리가 줄어든다면 갱신하고 큐에 넣기
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and dist[nx][ny] > dist[u[0]][u[1]] + maps[nx][ny]:
                dist[nx][ny] = dist[u[0]][u[1]] + maps[nx][ny]
                heapq.heappush(q, (dist[nx][ny],nx,ny))

    print(f"Problem {tc}: {dist[N-1][N-1]}")




# import sys
# input = sys.stdin.readline

# dirs = [(-1,0),(0,1),(1,0),(0,-1)]
# tc = 0
# while 1:
#     tc += 1
#     N = int(input().strip())
#     if N == 0:
#         break
#     INF = 987654321
#     maps = [list(map(int,input().split())) for _ in range(N)]
#     dist = [[INF] * N for _ in range(N)]
#     visit = [[0] * N for _ in range(N)]

#     dist[0][0] = maps[0][0]

#     for _ in range(N*N):
#         min_val = INF
#         for i in range(N):
#             for j in range(N):
#                 if min_val > dist[i][j] and visit[i][j] == 0:
#                     min_val = dist[i][j]
#                     u = (i,j)
        
#         if u == (N-1,N-1):
#             break
#         visit[u[0]][u[1]] = 1

#         for dir in dirs:
#             nx = u[0] + dir[0]
#             ny = u[1] + dir[1]
#             if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and dist[nx][ny] > dist[u[0]][u[1]] + maps[nx][ny]:
#                 dist[nx][ny] = dist[u[0]][u[1]] + maps[nx][ny]

#     print(f"Problem {tc}: {dist[N-1][N-1]}")