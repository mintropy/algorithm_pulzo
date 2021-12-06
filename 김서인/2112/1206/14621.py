import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
university_type = [0] + input().split()
visited = [False] * (N + 1)
distance = [9999999999] * (N + 1)

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    adj[u].append((v, d))
    adj[v].append((u, d))


def prim():
    Q = []
    ans = 0
    cnt = 0  # 연결한 학교 수
    # 출발점 초기화
    heapq.heappush(Q, (0, 1, 'no', university_type[1]))  # 거리, 위치, 연결된 노드의 타입, 타입

    while Q:
        curr_dis, curr_idx, adj_idx_type, type = heapq.heappop(Q) # 가장 가까운 거리 대학
        if visited[curr_idx]:
            continue

        if adj_idx_type == type: # 남초, 여초 체크
            continue

        now_type = type
        visited[curr_idx] = True
        ans += curr_dis
        cnt += 1
        if cnt == N: # 다 방문 했는지 체크
            return ans

        for node, weight in adj[curr_idx]:
            if not visited[node]:  # 인접, 방문 체크
                if university_type[node] != now_type: # 남초, 여초 대학 다르면
                    heapq.heappush(Q, (weight, node, university_type[curr_idx], university_type[node]))

    return -1


print(prim())

# 남초와 여초를 연결해야 함!!