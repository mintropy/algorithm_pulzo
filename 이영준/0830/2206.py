from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = []

for i in range(n):
    tmp = []
    s = str(stdin.readline().strip())
    for j in range(m):
        tmp.append(int(s[j]))
    graph.append(tmp)


def bfs(graph, n, m):
    # 각 칸까지 움직이는 최소 비용
    # 부순 벽의 개수가 0개, 1개인 경우로 나누어 계산
    count_wall_0 = [[1000000] * m for _ in range(n)]
    count_wall_1 = [[1000000] * m for _ in range(n)]
    count_wall_0[0][0] = 1
    # 위치, 밟은 칸의 수, 마주친 벽의 개수
    queue = deque([(0, 0, 1, 0)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y, c, w = queue.popleft()
        # 마지막 칸에 도착하면 최종 값 비교 & 갱신
        if x == n - 1 and y == m - 1:
            if w == 0:
                count_wall_0[x][y] = min(count_wall_0[x][y], c)
            elif w == 1:
                count_wall_1[x][y] = min(count_wall_1[x][y], c)
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 종료조건 확인
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= m:
                continue
            # 다음 칸이 벽인지 아닌지
            c0 = graph[nx][ny]
            # 값을 갱신 가능한 경우 갱신
            # 이동한 칸이 벽인 경우
            if c0 == 0:
                c1 = count_wall_0[nx][ny]
                c2 = count_wall_1[nx][ny]
                if w == 0:
                    if c1 <= c + 1:
                        continue
                    else:
                        count_wall_0[nx][ny] = c + 1
                        queue.append((nx, ny, c + 1, w))
                elif w == 1:
                    if c2 <= c + 1:
                        continue
                    else:
                        count_wall_1[nx][ny] = c + 1
                        queue.append((nx, ny, c + 1, w))      
            elif c0 == 1:
                if w == 1:
                    continue
                c1 = count_wall_0[nx][ny]
                if c1 <= c + 1:
                    continue
                else:
                    count_wall_0[nx][ny] = c + 1
                    queue.append((nx, ny, c + 1, w + 1))      
    return min(count_wall_0[-1][-1], count_wall_1[-1][-1])

ans = bfs(graph, n, m)
if ans == 1000000:
    print(-1)
else:
    print(ans)

    