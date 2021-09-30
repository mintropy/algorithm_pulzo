import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def tsp(start, pos, ac, n):
    global ans
    if n != 0 and n != N and pos == start:
        return
    if ac > ans:
        return
    if n == N and pos == start:
        ans = min(ans, ac)
    for to in range(N):
        if graph[pos][to] != 0:
            if visit[to] == 0:
                visit[to] = 1
                tsp(start, to, ac+graph[pos][to], n+1)
                visit[to] = 0
    return


ans = 987654321
for i in range(N):
    visit = [0] * N
    tsp(i, i, 0, 0)
print(ans)
