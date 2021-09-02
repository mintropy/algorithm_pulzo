import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())  # 노드 개수, 간선 개수
start = int(input())  # 시작점
INF = 10*20000+1  # 무한

arr = [[] for _ in range(V + 1)]  # 연결된 노드 있으면, 그 노드와 가는 데 드는 비용을 저장한 리스트

for _ in range(E):  # 간선 정보 입력받기
    u, v, w = map(int, input().split())
    arr[u].append([w, v])  # u에서 v로 갈 때 비용 w

distance = [INF] * (V + 1)  # start에서 각각 노드로 갈 때 최단 비용을 저장한 리스트
# 다익스트라
Q = []
heapq.heappush(Q, (0, start))  # start에서 start로 가는 비용(0). 인덱스를 큐에 넣고 시작
distance[start] = 0

while Q:
    now_cost, now_idx = heapq.heappop(Q)  # 가장 최단 거리인 노드 정보 꺼냄 (인덱스, 비용)
    if distance[now_idx] < now_cost:  # 최단 거리가 아니라면 그만 두기
        continue

    for info in arr[now_idx]:  # 현재 노드와 연결된 다른 노드
        now_next_cost, next_idx = info  # 연결된 다른 노드 인덱스, 현재 노드-> 그 노드 가는 데 드는 비용
        next_idx_cost = now_cost + now_next_cost  # 출발점 -> 현재 노드 -> next_idx로 이동하는 데 드는 비용
        if next_idx_cost < distance[next_idx]:  # 거쳐서 가는 것이, 안 거쳐 가는 것보다 비용이 적게 들면
            distance[next_idx] = next_idx_cost  # 출발점 -> next_idx 가는 비용을 업데이트
            heapq.heappush(Q, (next_idx_cost, next_idx))

# 출력
for i in range(1, V+1):
    ans = distance[i]
    if ans == INF:
        ans = 'INF'
    print(ans)
