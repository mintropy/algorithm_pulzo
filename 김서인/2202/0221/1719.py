import sys

INF = 987654321
input = sys.stdin.readline
n, m = map(int, input().split())
move = list([0] * (n + 1) for _ in range(n + 1))  # 어디를 가장 먼저 방문해야 할지
dist = list([INF] * (n + 1) for _ in range(n + 1))  # 이동할 때 드는 최소 비용

for _ in range(m):
    start, end, time = map(int, input().split())
    dist[start][end] = time  # 경로가 있는 경우 초기화
    dist[end][start] = time
    move[start][end] = end
    move[end][start] = start

# 자기 자신으로 가는 것 0으로 초기화
for i in range(1, n + 1):
    move[i][i] = i
    dist[i][i] = 0

for k in range(1, n + 1):  # 거쳐가는 점
    for i in range(1, n + 1):  # 출발점
        for j in range(1, n + 1):  # 도착점
            if dist[i][j] > (dist[i][k] + dist[k][j]):  # 업데이트 되어야 한다면
                dist[i][j] = dist[i][k] + dist[k][j] # 비용 갱신
                move[i][j] = move[i][k] # 가장 먼저 방문할 지점 바꾸기

for i in range(1, n + 1):
    for j in range(1, n+1):
        if i == j:
            print('-', end=' ')
        else:
            print(move[i][j], end=' ')
    print()