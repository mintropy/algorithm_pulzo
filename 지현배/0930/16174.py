import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[True for _  in range(N)] for _  in range(N)]
def DFS(y, x):
    if arr[y][x] == -1:
        return True
    ans = False
    if y + arr[y][x] < N and visited[y + arr[y][x]][x]:
        visited[y + arr[y][x]][x] = False
        ans |= DFS(y + arr[y][x], x)
    if x + arr[y][x] < N and visited[y][arr[y][x] + x]:
        visited[y][arr[y][x] + x] = False
        ans |= DFS(y, arr[y][x] + x)
    return ans
if DFS(0, 0):
    print('HaruHaru')
else:
    print('Hing')