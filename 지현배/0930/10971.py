import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [True] * N
ans = 1000000 * N
def DFS(n, cnt, cost):
    if n == 0 and cnt != 0:
        if cnt == N:
            global ans
            ans = min(ans, cost)
        return
    for i in range(N):
        if arr[n][i] != 0 and visited[i] and cost + arr[n][i] < ans:
            visited[i] = False
            DFS(i, cnt + 1, cost + arr[n][i])
            visited[i] = True
DFS(0, 0, 0)
print(ans)