import collections
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    cnt = 0
    steps = 0
    q = collections.deque()
    q.append((P, 0))
    while q:
        pos, step = q.popleft()
        if visit[pos] == 1:
            continue
        else:
            if pos <= S:
                cnt += 1
                steps += step
            if cnt == 2:
                return steps
            visit[pos] = 1

        for v in graph[pos]:
            q.append((v, step+1))


N, S, P = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

ans = N - bfs() - 1
print(ans)
