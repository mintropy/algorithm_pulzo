import sys

input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

n, k = MIISS()
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 간선 정보 바탕으로 초기 연결
for _ in range(k):
    before, after = MIISS()
    graph[before][after] = -1  # 전 -> 후
    graph[after][before] = 1  # 후 -> 전

# 플로이드 워샬
for k in range(1, n + 1):  # 거쳐가는 노드
    for i in range(1, n + 1):  # 출발 노드
        for j in range(1, n + 1):  # 도착 노드
            if graph[i][k] < 0 and graph[k][j] < 0:  # i -> k -> j
                graph[i][j] = -1
                graph[j][i] = 1

# 물음에 답하기
s = int(input())
for _ in range(s):
    a, b = MIISS()
    print(graph[a][b])
