import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    edges[p].append((q, r))
# 위상정렬
visited = [True] * (N + 1)
topology = [1]
def topology_sort(n):
    # 방문체크를 하고
    visited[n] = False
    for edge, _ in edges[n]:
        # 아직 방문하지 않은 방문 가능한 노드를 방문하고 재귀 수행
        if visited[edge]:
            topology_sort(edge)
    # 재귀를 빠져나오기 전에 리스트에 넣는다.
    topology.append(n)
topology_sort(1)
dp = [0] * (N + 1)
ans = [[] for _ in range(N + 1)]
ans[1] = [1]
# 리스트를 뒤집어서 dp 수행
for i in topology[:0:-1]:
    for next, score in edges[i]:
        # dp 값을 갱신 가능 할 때, 갱신하고 방문 노드를 누적한다.
        if dp[next] < dp[i] + score:
            dp[next] = dp[i] + score
            ans[next] = ans[i] + [next]
print(dp[1])
print(*ans[1])