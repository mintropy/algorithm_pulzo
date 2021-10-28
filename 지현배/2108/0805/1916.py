import sys
# 힙을 이용
import heapq
def sol():
    ipt = sys.stdin.readline
    N = int(ipt())
    M = int(ipt())
    # bus[i]에는 [i에서 갈수있는 노드, 버스비] 리스트가 포함됨
    bus = [[] for _ in range(N + 1)]
    # 모든 노드의 최소비용을 큰수로 해둠
    visited = [float('INF') for _ in range(N + 1)]
    queue = []
    for _ in range(M):
        s, e, c = map(int, ipt().split())
        bus[s].append([e, c])
    start, end = map(int, ipt().split())
    heapq.heappush(queue, (0, start))
    while queue:
        cost, loc = heapq.heappop(queue)
        # 현위치가 도착지면 총 비용 반환
        if loc == end:
            return cost
        # 최소비용이 현재 총 비용보다 작거나 같으면 다음 큐
        if visited[loc] <= cost:
            continue
        visited[loc] = cost
        # 현위치에서 갈 수 있는 노드 돌면서
        for next_loc, next_cost in bus[loc]:
            # 다음 노드의 최소비용이 현재 총 비용 + 다음 비용보다 클 때 큐에 추가
            if cost + next_cost < visited[next_loc]:
                heapq.heappush(queue, (cost + next_cost, next_loc))
print(sol())