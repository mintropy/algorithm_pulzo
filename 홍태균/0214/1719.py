'''
택배

'''
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
INF = 987654321
# 거리 저장
maps = [[INF]*N for _ in range(N)]
# 루트의 첫 이동 집하장
route = [[0] * N for _ in range(N)]

# 초기화
for _ in range(M):
    a, b, c = map(int,input().split())
    # 거리
    maps[a-1][b-1] = c
    maps[b-1][a-1] = c
    # 처음 이동은 바로 b 이기 때문
    route[a-1][b-1] = b
    route[b-1][a-1] = a

# 플로이드 와샬
for k in range(N):
    # i 시작, j 끝
    for i in range(N):
        for j in range(N):
            # 거리가 줄어들면 갱신
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]
                # 거리가 줄어 들었다는 것은 
                # 앞의 이동에서의 첫 집하장으로 갱신
                route[i][j] = route[i][k]
                
for i in range(N):
    route[i][i] = '-'
    print(*route[i])