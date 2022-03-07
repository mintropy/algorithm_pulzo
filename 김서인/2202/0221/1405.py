import sys

input = sys.stdin.readline

N, dong, seo, nam, buk = map(int, input().split())
direct_percent = [dong * 0.01, seo * 0.01, nam * 0.01, buk * 0.01]
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

simple = 0
visited = [[False] * 29 for _ in range(29)]
visited[14][14] = True  # 출발지도 방문한 곳!


def dfs(cnt, i, j, now_percent):
    global simple
    if cnt == N:
        simple += now_percent
        return

    for k in range(4):
        ni, nj = i + direct[k][0], j + direct[k][1]
        # 방문했던 곳에 다시 방문하면 단순하지 않음
        if visited[ni][nj] == True:
            continue
        visited[ni][nj] = True
        dfs(cnt + 1, ni, nj, now_percent * direct_percent[k])
        visited[ni][nj] = False


dfs(0, 14,14, 1)

print(simple)