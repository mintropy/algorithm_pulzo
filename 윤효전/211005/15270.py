import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [None]
for _ in range(N):
    graph.append([])

for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    graph[a].append(b)

visit = [None] + [0]*N


def dfs(pos, n):
    if pos > N:
        return n
    if visit[pos]:
        return dfs(pos+1, n)
    res = 0
    for v in graph[pos]:
        if not visit[v]:
            visit[v] = 1
            res = max(res, dfs(pos+1, n+1))
            visit[v] = 0
    return max(res, dfs(pos+1, n))


res = dfs(1, 0)  # 찾은 페어 수
print(res)
res *= 2  # 페어 수 * 2 = 총 인원

if res < N:  # 로봇 춤 출 사람이 남은 경우
    res += 1  # 로봇 춤 추가

print(res)
