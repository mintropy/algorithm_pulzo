import collections
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

N, M, T = MIIS()
miro = tuple(tuple(MIIS()) for _ in range(N))

visited = [[0] * M for _ in range(N)]
visited_with_sword = [[0] * M for _ in range(N)]


def bfs():
    q = collections.deque()
    flag = 0  # 명검 획득 여부

    if miro[0][0] == 2:  # 혹시 출발점에 명검 있으면
        flag = 1

    q.append((0, 0, flag))
    visited[0][0] = 1

    while q:
        i, j, flag = q.popleft()

        if i == (N - 1) and j == (M - 1):  # 도착
            return flag

        if miro[i][j] == 2:  # 명검 획득
            flag = 1

        for k in range(4):
            ni = i + directions[k][0]
            nj = j + directions[k][1]

            if 0 <= ni < N and 0 <= nj < M:  # 범위
                if flag == 1:  # 검 주웠으면
                    if visited_with_sword[ni][nj]==0:  # 방문 안했으면
                        # 어떤 경우에든(벽이어도) 갈 수 있음
                        visited_with_sword[ni][nj] = visited_with_sword[i][j] + 1
                        q.append((ni, nj, flag))

                else:  # 검 없으면
                    if visited[ni][nj]==0:  # 방문 안했으면

                        if miro[ni][nj] == 0:  # 길
                            visited[ni][nj] = visited[i][j] + 1
                            q.append((ni, nj, flag))

                        elif miro[ni][nj] == 2:  # 명검
                            visited_with_sword[ni][nj] = visited[i][j] + 1
                            q.append((ni, nj, 1))

                        # 벽은 못감
    return -1

flag = bfs()

if flag == 1:
    ans = visited_with_sword[N-1][M-1] -1
    if ans > T:
        print('Fail')
    else:
        print(ans)

elif flag == -1:
    print('Fail')

else:
    ans = visited[N - 1][M - 1] - 1  # 출발점 1로 해서
    if ans > T:
        print('Fail')
    else:
        print(ans)
