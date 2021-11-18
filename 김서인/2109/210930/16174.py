import collections
import sys

input = sys.stdin.readline

directions = [(1, 0), (0, 1)]  # 아래, 오른쪽

N = int(input())

jump_map = list(list(map(int, input().split())) for _ in range(N))
visited = [[False] * N for _ in range(N)]

def bfs():
    q = collections.deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        i, j = q.popleft()
        if jump_map[i][j] == -1:
            return 'HaruHaru'

        for k in range(2):
            ni = i + directions[k][0] * jump_map[i][j]
            nj = j + directions[k][1] * jump_map[i][j]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
                visited[ni][nj] = True
                q.append((ni,nj))
    return 'Hing'

ans = bfs()
print(ans)